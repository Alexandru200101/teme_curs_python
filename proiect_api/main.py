from fastapi import FastAPI, HTTPException, Header, Query, Depends
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, field_validator
import os, csv, secrets, io, uuid
import matplotlib.pyplot as plt
from rapidfuzz import fuzz
from typing import List, Optional
from datetime import datetime
import logging
import re

# Configurare logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Car Rental API", version="1.0.0")

# =========================
# CONFIGURARE
# =========================
USERS_FILE = "users.csv"
CARS_FILE = "cars.csv"
ACTIVE_TOKENS = {}

# =========================
# MODELE DE DATE
# =========================
class UserModel(BaseModel):
    name: str
    email: str
    password: str

    @field_validator("email")
    def email_valid(cls, v):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, v):
            raise ValueError("Email invalid")
        return v

    @field_validator("password")
    def password_valid(cls, v):
        if len(v) < 6:
            raise ValueError("Parola trebuie să aibă minim 6 caractere")
        return v

    @field_validator("name")
    def name_valid(cls, v):
        if len(v.strip()) < 2:
            raise ValueError("Numele trebuie să aibă minim 2 caractere")
        return v.strip()

class LoginModel(BaseModel):
    email: str
    password: str

    @field_validator("email")
    def email_valid(cls, v):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, v):
            raise ValueError("Email invalid")
        return v

class CarModel(BaseModel):
    brand: str
    model: str
    year: int
    engine: str
    hp: int
    fuel: str
    consumption: str
    price: str
    rent: str

    @field_validator("year")
    def year_valid(cls, v):
        current_year = datetime.now().year
        if v < 1886 or v > current_year + 1:
            raise ValueError(f"An invalid. Trebuie să fie între 1886 și {current_year + 1}")
        return v

    @field_validator("hp")
    def hp_valid(cls, v):
        if v <= 0:
            raise ValueError("HP trebuie sa fie > 0")
        return v

    @field_validator("price", "rent")
    def price_valid(cls, v):
        try:
            v_clean = v.replace('$', '').replace(',', '')
            price_val = float(v_clean)
            if price_val <= 0:
                raise ValueError("Prețul trebuie să fie mai mare decât 0")
        except ValueError:
            raise ValueError("Preț invalid")
        return v

    @field_validator("brand", "model", "engine", "fuel")
    def not_empty_validator(cls, v):
        if not v or not v.strip():
            raise ValueError("Câmpul nu poate fi gol")
        return v.strip()

class CarSearchModel(BaseModel):
    query: Optional[str] = None
    brand: Optional[str] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None
    min_year: Optional[int] = None
    max_year: Optional[int] = None
    fuel_type: Optional[str] = None

# =========================
# UTILITARE
# =========================
def generate_unique_id():
    return str(uuid.uuid4())

def get_current_user(token: str = Header(...)):
    if token not in ACTIVE_TOKENS:
        raise HTTPException(status_code=401, detail="Token invalid sau expirat")
    return ACTIVE_TOKENS[token]

def read_csv_file(filename: str) -> List[dict]:
    if not os.path.exists(filename) or os.stat(filename).st_size == 0:
        return []
    
    try:
        with open(filename, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return list(reader)
    except Exception as e:
        logger.error(f"Eroare la citirea fișierului {filename}: {e}")
        return []

def write_csv_file(filename: str, fieldnames: List[str], data: List[dict]):
    try:
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        logger.error(f"Eroare la scrierea fișierului {filename}: {e}")
        raise HTTPException(status_code=500, detail="Eroare la salvarea datelor")

def convert_car_numeric_fields(car: dict) -> dict:
    """Converteste campurile numerice ale masinii cu gestionarea erorilor"""
    try:
        car["year"] = int(car.get("year", 0))
        car["hp"] = int(car.get("hp", 0))
        car["rent_count"] = int(car.get("rent_count", 0))
    except (ValueError, TypeError) as e:
        logger.warning(f"Eroare la conversia campurilor numerice pentru masina {car.get('id')}: {e}")
        # Setam valori default in caz de eroare
        car["year"] = 0
        car["hp"] = 0
        car["rent_count"] = 0
    return car

def search_cars_in_memory(cars: List[dict], search_params: dict) -> List[dict]:
    """Cauta masini in lista data conform parametrilor"""
    results = cars.copy()
    
    # Filtrare dupa disponibilitate
    if search_params.get("available_only"):
        results = [car for car in results if car.get("rented") == "no"]
    
    # Filtrare dupa query (cautare text)
    if search_params.get("query"):
        query = search_params["query"].lower().strip()
        filtered = []
        for car in results:
            brand = car.get("brand", "").lower()
            model = car.get("model", "").lower()
            year = str(car.get("year", "")).lower()
            
            if (query in brand or query in model or query in year or
                fuzz.partial_ratio(query, brand) >= 70 or
                fuzz.partial_ratio(query, model) >= 70):
                filtered.append(car)
        results = filtered
    
    # Filtrare dupa brand
    if search_params.get("brand"):
        brand_filter = search_params["brand"].lower()
        results = [car for car in results if car.get("brand", "").lower() == brand_filter]
    
    # Filtrare dupa an
    if search_params.get("min_year"):
        results = [car for car in results if int(car.get("year", 0)) >= search_params["min_year"]]
    
    if search_params.get("max_year"):
        results = [car for car in results if int(car.get("year", 0)) <= search_params["max_year"]]
    
    # Filtrare dupa pret
    if search_params.get("min_price"):
        results = [car for car in results if 
                  float(car.get("price", "0").replace('$', '').replace(',', '')) >= search_params["min_price"]]
    
    if search_params.get("max_price"):
        results = [car for car in results if 
                  float(car.get("price", "0").replace('$', '').replace(',', '')) <= search_params["max_price"]]
    
    # Filtrare dupa tip combustibil
    if search_params.get("fuel_type"):
        fuel_filter = search_params["fuel_type"].lower()
        results = [car for car in results if car.get("fuel", "").lower() == fuel_filter]
    
    return results

def initialize_files():
    """Initializeaza fisierele CSV daca nu exista"""
    # Users file
    if not os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["id", "name", "email", "password"])
            logger.info("Fișierul users.csv a fost creat")
        except Exception as e:
            logger.error(f"Eroare la crearea users.csv: {e}")
    
    # Cars file
    if not os.path.exists(CARS_FILE):
        try:
            with open(CARS_FILE, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["id", "brand", "model", "year", "engine", "hp", 
                               "fuel", "consumption", "price", "rent", "rented", "rent_count"])
            
            # Masini de exemplu
            sample_cars = [
                ["a1b2c3d4-e5f6-7890-abcd-ef1234567890", "Porsche", "911 Carrera", "2025", "3.0L twin-turbo flat-6", "379", "Benzină", "18/25 mpg", "132300", "2000", "no", "0"],
                ["a2b3c4d5-e6f7-8901-bcde-f12345678901", "Porsche", "911 Carrera S", "2024", "3.0L twin-turbo flat-6", "443", "Benzină", "18/24 mpg", "172960", "2500", "no", "0"],
                ["b1c2d3e4-f5g6-7890-cdef-123456789012", "Porsche", "911 Carrera T", "2025", "3.0L twin-turbo flat-6", "388", "Benzină", "18/25 mpg", "143700", "2200", "no", "0"],
                ["c2d3e4f5-g6h7-8901-defg-234567890123", "Porsche", "911 Carrera GTS", "2024", "3.0L twin-turbo flat-6", "473", "Benzină", "17/23 mpg", "201505", "3000", "no", "0"],
                ["d3e4f5g6-h7i8-9012-efgh-345678901234", "Porsche", "911 Turbo S", "2024", "3.8L twin-turbo flat-6", "640", "Benzină", "15/20 mpg", "207000", "3200", "no", "0"],
            ]
            
            with open(CARS_FILE, "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                for car in sample_cars:
                    writer.writerow(car)
            logger.info("Masini de exemplu au fost adaugate")
            
        except Exception as e:
            logger.error(f"Eroare la crearea cars.csv: {e}")

# =========================
# ENDPOINT-URI UTILIZATORI
# =========================
@app.post("/users/register", response_model=dict)
def register(user: UserModel):
    """Inregistrare utilizator nou"""
    initialize_files()
    
    users = read_csv_file(USERS_FILE)
    
    if any(u.get("email") == user.email for u in users):
        raise HTTPException(status_code=400, detail="Email deja folosit")
    
    user_id = generate_unique_id()
    new_user = {
        "id": user_id,
        "name": user.name,
        "email": user.email,
        "password": user.password
    }
    
    users.append(new_user)
    write_csv_file(USERS_FILE, ["id", "name", "email", "password"], users)
    
    logger.info(f"Utilizator nou înregistrat: {user.email}")
    return {"message": "Utilizator creat cu succes", "user_id": user_id}

@app.post("/users/login", response_model=dict)
def login(data: LoginModel):
    """Autentificare utilizator"""
    users = read_csv_file(USERS_FILE)
    
    if not users:
        raise HTTPException(status_code=400, detail="Nu există utilizatori înregistrați")
    
    for user in users:
        if user.get("email") == data.email and user.get("password") == data.password:
            token = secrets.token_hex(32)
            ACTIVE_TOKENS[token] = {
                "email": data.email,
                "user_id": user.get("id"),
                "login_time": datetime.now().isoformat()
            }
            logger.info(f"Utilizator autentificat: {data.email}")
            return {"message": "Login reușit", "token": token}
    
    raise HTTPException(status_code=400, detail="Email sau parola incorectă")

@app.post("/users/logout", response_model=dict)
def logout(token: str = Header(...)):
    """Deconectare utilizator"""
    if token in ACTIVE_TOKENS:
        email = ACTIVE_TOKENS[token]["email"]
        del ACTIVE_TOKENS[token]
        logger.info(f"Utilizator deconectat: {email}")
        return {"message": "Logout reușit"}
    
    raise HTTPException(status_code=400, detail="Token invalid")

# =========================
# ENDPOINT-URI MASINI (PUBLICE)
# =========================
@app.get("/cars", response_model=dict)
def get_all_cars(
    available_only: bool = Query(False, description="Afiseaza doar masinile disponibile")
):
    """Obține toate mașinile sau doar pe cele disponibile"""
    cars = read_csv_file(CARS_FILE)
    
    if not cars:
        return {"message": "Nu există mașini în sistem", "count": 0, "cars": []}
    
    search_params = {"available_only": available_only}
    filtered_cars = search_cars_in_memory(cars, search_params)
    
    # Converteste campurile numerice
    for car in filtered_cars:
        convert_car_numeric_fields(car)
    
    return {"count": len(filtered_cars), "cars": filtered_cars}

@app.get("/cars/search", response_model=dict)
def search_cars(
    query: Optional[str] = Query(None, description="Cautare dupa brand, model sau an"),
    brand: Optional[str] = Query(None, description="Filtrare dupa brand"),
    min_price: Optional[float] = Query(None, description="Pret minim"),
    max_price: Optional[float] = Query(None, description="Pret maxim"),
    min_year: Optional[int] = Query(None, description="An minim"),
    max_year: Optional[int] = Query(None, description="An maxim"),
    fuel_type: Optional[str] = Query(None, description="Tip combustibil"),
    available_only: bool = Query(False, description="Doar masini disponibile")
):
    """Căutare avansată a mașinilor"""
    cars = read_csv_file(CARS_FILE)
    
    if not cars:
        return {"message": "Nu există mașini în sistem", "count": 0, "cars": []}
    
    search_params = {
        "query": query,
        "brand": brand,
        "min_price": min_price,
        "max_price": max_price,
        "min_year": min_year,
        "max_year": max_year,
        "fuel_type": fuel_type,
        "available_only": available_only
    }
    
    filtered_cars = search_cars_in_memory(cars, search_params)
    
    # Converteste campurile numerice
    for car in filtered_cars:
        convert_car_numeric_fields(car)
    
    return {"count": len(filtered_cars), "cars": filtered_cars}

@app.get("/cars/{car_id}", response_model=dict)
def get_car_details(car_id: str):
    """Obține detalii despre o mașină specifică"""
    cars = read_csv_file(CARS_FILE)
    
    for car in cars:
        if car.get("id") == car_id:
            convert_car_numeric_fields(car)
            return {"car": car}
    
    raise HTTPException(status_code=404, detail="Mașina nu a fost găsită")

# =========================
# ENDPOINT-URI MASINI (PROTECTATE - necesită autentificare)
# =========================
# @app.get("/cars/available", response_model=dict)
# def get_available_cars(current_user: dict = Depends(get_current_user)):
#     """Obține toate mașinile disponibile pentru închiriere (necesită autentificare)"""
#     try:
#         cars = read_csv_file(CARS_FILE)
#         logger.info(f"Utilizator {current_user['email']} solicită mașini disponibile")
#         logger.info(f"Număr total mașini în sistem: {len(cars)}")
        
#         if not cars:
#             logger.info("Nu există mașini în sistem")
#             return {"message": "Nu există mașini în sistem", "count": 0, "cars": []}
        
#         # Filtrare mașini disponibile
#         available_cars = []
#         for car in cars:
#             rented_status = car.get("rented", "no").lower().strip()
#             if rented_status == "no":
#                 available_cars.append(car)
        
#         logger.info(f"Mașini disponibile găsite: {len(available_cars)}")
        
#         if not available_cars:
#             return {"message": "Nu există mașini disponibile momentan", "count": 0, "cars": []}
        
#         # Converteste câmpurile numerice
#         for car in available_cars:
#             try:
#                 car["year"] = int(car.get("year", 0))
#                 car["hp"] = int(car.get("hp", 0))
#                 car["rent_count"] = int(car.get("rent_count", 0))
#             except (ValueError, TypeError) as e:
#                 logger.warning(f"Eroare conversie câmpuri numerice pentru mașina {car.get('id')}: {e}")
#                 car["year"] = 0
#                 car["hp"] = 0
#                 car["rent_count"] = 0
        
#         return {
#             "count": len(available_cars), 
#             "cars": available_cars,
#             "message": f"Găsite {len(available_cars)} mașini disponibile"
#         }
        
#     except Exception as e:
#         logger.error(f"Eroare la obținerea mașinilor disponibile: {e}")
#         raise HTTPException(status_code=500, detail="Eroare internă la obținerea mașinilor disponibile")

@app.post("/cars/add", response_model=dict)
def add_car(car: CarModel, current_user: dict = Depends(get_current_user)):
    """Adaugă o mașină nouă (necesită autentificare)"""
    initialize_files()
    
    cars = read_csv_file(CARS_FILE)
    car_id = generate_unique_id()
    
    new_car = {
        "id": car_id,
        "brand": car.brand,
        "model": car.model,
        "year": car.year,
        "engine": car.engine,
        "hp": car.hp,
        "fuel": car.fuel,
        "consumption": car.consumption,
        "price": car.price,
        "rent": car.rent,
        "rented": "no",
        "rent_count": 0
    }
    
    cars.append(new_car)
    write_csv_file(CARS_FILE, 
                  ["id", "brand", "model", "year", "engine", "hp", "fuel", 
                   "consumption", "price", "rent", "rented", "rent_count"], 
                  cars)
    
    logger.info(f"Mașină adăugată: {car.brand} {car.model} de către {current_user['email']}")
    return {"message": "Mașină adăugată cu succes", "car_id": car_id}

@app.delete("/cars/{car_id}", response_model=dict)
def delete_car(car_id: str, current_user: dict = Depends(get_current_user)):
    """Șterge o mașină (necesită autentificare)"""
    cars = read_csv_file(CARS_FILE)
    
    initial_count = len(cars)
    cars = [car for car in cars if car.get("id") != car_id]
    
    if len(cars) == initial_count:
        raise HTTPException(status_code=404, detail="Mașina nu a fost găsită")
    
    write_csv_file(CARS_FILE, 
                  ["id", "brand", "model", "year", "engine", "hp", "fuel", 
                   "consumption", "price", "rent", "rented", "rent_count"], 
                  cars)
    
    logger.info(f"Mașină ștearsă (ID: {car_id}) de către {current_user['email']}")
    return {"message": "Mașină ștearsă cu succes"}

@app.post("/rent/{car_id}", response_model=dict)
def rent_car(car_id: str, current_user: dict = Depends(get_current_user)):
    """Închiriere mașină (necesită autentificare)"""
    cars = read_csv_file(CARS_FILE)
    
    car_found = False
    car_name = ""
    for car in cars:
        if car.get("id") == car_id:
            car_found = True
            car_name = f"{car.get('brand', '')} {car.get('model', '')}"
            if car.get("rented") == "yes":
                raise HTTPException(status_code=400, detail=f"Mașina {car_name} este deja închiriată")
            
            car["rented"] = "yes"
            car["rent_count"] = str(int(car.get("rent_count", 0)) + 1)
            break
    
    if not car_found:
        raise HTTPException(status_code=404, detail="Mașina nu există")
    
    write_csv_file(CARS_FILE, 
                  ["id", "brand", "model", "year", "engine", "hp", "fuel", 
                   "consumption", "price", "rent", "rented", "rent_count"], 
                  cars)
    
    logger.info(f"Mașină {car_name} închiriată de {current_user['email']}")
    return {"message": f"Mașina {car_name} a fost închiriată cu succes"}

@app.post("/return/{car_id}", response_model=dict)
def return_car(car_id: str, current_user: dict = Depends(get_current_user)):
    """Returnare mașină (necesită autentificare)"""
    cars = read_csv_file(CARS_FILE)
    
    car_found = False
    car_name = ""
    for car in cars:
        if car.get("id") == car_id:
            car_found = True
            car_name = f"{car.get('brand', '')} {car.get('model', '')}"
            if car.get("rented") == "no":
                raise HTTPException(status_code=400, detail=f"Mașina {car_name} nu este închiriată")
            
            car["rented"] = "no"
            break
    
    if not car_found:
        raise HTTPException(status_code=404, detail="Mașina nu există")
    
    write_csv_file(CARS_FILE, 
                  ["id", "brand", "model", "year", "engine", "hp", "fuel", 
                   "consumption", "price", "rent", "rented", "rent_count"], 
                  cars)
    
    logger.info(f"Mașină {car_name} returnată de {current_user['email']}")
    return {"message": f"Mașina {car_name} a fost returnată cu succes"}

# =========================
# STATISTICI
# =========================
@app.get("/stats/top-cars", response_model=dict)
def top_rented_cars():
    """Top 5 mașini cele mai închiriate"""
    cars = read_csv_file(CARS_FILE)
    
    if not cars:
        return {"message": "Nu există mașini în sistem", "top_cars": []}
    
    for car in cars:
        convert_car_numeric_fields(car)
    
    sorted_cars = sorted(cars, key=lambda x: x["rent_count"], reverse=True)
    top_cars = sorted_cars[:5]
    
    return {"top_cars": top_cars}

@app.get("/stats/overview", response_model=dict)
def stats_overview():
    """Statistici generale despre mașini"""
    cars = read_csv_file(CARS_FILE)
    
    if not cars:
        return {
            "total_cars": 0,
            "available_cars": 0,
            "rented_cars": 0,
            "total_rents": 0,
            "avg_rents_per_car": 0
        }
    
    total_cars = len(cars)
    available_cars = sum(1 for car in cars if car.get("rented") == "no")
    rented_cars = total_cars - available_cars
    total_rents = sum(int(car.get("rent_count", 0)) for car in cars)
    avg_rents = total_rents / total_cars if total_cars > 0 else 0
    
    return {
        "total_cars": total_cars,
        "available_cars": available_cars,
        "rented_cars": rented_cars,
        "total_rents": total_rents,
        "avg_rents_per_car": round(avg_rents, 2)
    }

@app.get("/stats/top-cars-graph")
def top_cars_graph():
    """Grafic cu top mașini închiriate"""
    cars = read_csv_file(CARS_FILE)
    
    if not cars:
        raise HTTPException(status_code=400, detail="Nu există mașini în sistem")
    
    for car in cars:
        car["rent_count"] = int(car.get("rent_count", 0))
    
    sorted_cars = sorted(cars, key=lambda x: x["rent_count"], reverse=True)
    top5 = sorted_cars[:5]
    
    if not top5:
        raise HTTPException(status_code=400, detail="Nu există date pentru grafic")
    
    labels = [f"{car.get('brand', '')} {car.get('model', '')}" for car in top5]
    values = [car.get('rent_count', 0) for car in top5]
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, values, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57'])
    plt.title("Top mașini închiriate")
    plt.ylabel("Număr închirieri")
    plt.xticks(rotation=45)
    
    for bar, value in zip(bars, values):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, 
                str(value), ha='center', va='bottom')
    
    plt.tight_layout()
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=150, bbox_inches='tight')
    buf.seek(0)
    plt.close()
    
    return StreamingResponse(buf, media_type="image/png")

# =========================
# UTILITARE GENERALA
# =========================
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "active_users": len(ACTIVE_TOKENS),
        "users_file": os.path.exists(USERS_FILE),
        "cars_file": os.path.exists(CARS_FILE)
    }

@app.get("/")
def root():
    return {
        "message": "Bun venit la Car Rental API",
        "version": "1.0.0",
        "endpoints": {
            "users": "/users/register, /users/login, /users/logout",
            "cars_public": "/cars, /cars/search, /cars/{id}",
            "cars_protected": "/cars/available, /cars/add, /rent/{id}, /return/{id}",
            "stats": "/stats/top-cars, /stats/overview, /stats/top-cars-graph"
        }
    }

# Initializeaza la pornire
initialize_files()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



    




