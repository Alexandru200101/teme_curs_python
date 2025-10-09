from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, Depends, HTTPException, status, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
import jwt
from datetime import datetime, timedelta
from db.db_conectare import get_db, verifica_sau_creeaza_baza_date
from db.db_init import init_db, adauga_autori_si_carti
from endpoints import utilizatori, carti, autori, imprumut

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("🚀 Inițializare aplicație...")
    
    print("🔍 Verific baza de date...")
    verifica_sau_creeaza_baza_date()
    print("✅ Baza de date verificată/creată")
    
    print("🔧 Inițializez tabelele...")
    init_db()
    print("✅ Tabelele au fost inițializate")
    
    # Adaugă date de test
    try:
        print("📚 Adaug datele inițiale...")
        adauga_autori_si_carti()
        print("✅ Datele inițiale au fost adăugate în baza de date")
    except Exception as e:
        print(f"⚠️ Eroare la adăugarea datelor inițiale: {e}")
    
    yield
    
    # Shutdown
    print("👋 Închidere aplicație...")

app = FastAPI(
    title="API Biblioteca",
    description="API modern pentru gestionarea unei biblioteci digitale",
    version="1.0.0",
    lifespan=lifespan
)

# Mount pentru fișiere statice
app.mount("/static", StaticFiles(directory="static"), name="static")

# Template-uri
templates = Jinja2Templates(directory="templates")

# Funcție pentru a verifica token-ul JWT din cookie
def get_current_user(request: Request):
    token = request.cookies.get("access_token")
    if token:
        try:
            from validari.auth import verifica_token
            payload = verifica_token(token)
            return payload
        except:
            return None
    return None

# Funcție pentru a verifica dacă utilizatorul este admin
def is_admin(user: dict) -> bool:
    # Listă de email-uri care au acces de admin
    admin_emails = ["admin@biblioteca.ro", "administrator@biblioteca.ro"]
    return user.get("sub") in admin_emails

# Rute pentru pagini
@app.get("/")
def index(request: Request):
    user = get_current_user(request)
    return templates.TemplateResponse("index.html", {"request": request, "user": user})

@app.get("/catalog")
def catalog(request: Request, db: Session = Depends(get_db)):
    user = get_current_user(request)
    
    # Încarcă cărțile din baza de date
    from db.models.carti_model import CartiModel
    from db.models.imprumut_model import Imprumut
    
    carti = db.query(CartiModel).all()
    
    # Obține împrumuturile active pentru fiecare carte
    carti_afisare = []
    for carte in carti:
        # Verifică dacă cartea este împrumutată
        imprumut_activ = db.query(Imprumut).filter(
            Imprumut.carte_id == carte.id,
            Imprumut.data_returnare == None
        ).first()
        
        este_imprumutata = imprumut_activ is not None
        
        carti_afisare.append({
            "id": carte.id,
            "titlu": carte.titlu,
            "autor": carte.autor.nume if carte.autor else "Necunoscut",
            "gen": carte.gen,
            "an_publicare": carte.an_publicare,
            "este_imprumutata": este_imprumutata,
            "imprumut_id": imprumut_activ.id if este_imprumutata else None
        })
    
    return templates.TemplateResponse("catalog.html", {
        "request": request, 
        "user": user,
        "carti": carti_afisare
    })

@app.get("/admin")
def admin_panel(request: Request, db: Session = Depends(get_db)):
    user = get_current_user(request)
    if not user or not is_admin(user):
        return templates.TemplateResponse("index.html", {
            "request": request, 
            "error": "Nu ai acces la panoul de administrare"
        })
    
    # Statistici pentru admin
    from db.models.carti_model import CartiModel
    from db.models.utilizatori_model import UtilizatoriModel
    from db.models.imprumut_model import Imprumut
    from sqlalchemy import func
    
    total_carti = db.query(CartiModel).count()
    total_utilizatori = db.query(UtilizatoriModel).count()
    total_imprumuturi = db.query(Imprumut).count()
    imprumuturi_active = db.query(Imprumut).filter(Imprumut.data_returnare == None).count()
    
    # Împrumuturi active pentru afișare
    imprumuturi_active_list = db.query(Imprumut).filter(Imprumut.data_returnare == None).all()
    imprumuturi_afisare = []
    
    for imprumut in imprumuturi_active_list:
        carte = db.query(CartiModel).filter(CartiModel.id == imprumut.carte_id).first()
        utilizator = db.query(UtilizatoriModel).filter(UtilizatoriModel.id == imprumut.user_id).first()
        
        imprumuturi_afisare.append({
            "id": imprumut.id,
            "carte_titlu": carte.titlu if carte else "Necunoscut",
            "utilizator_nume": utilizator.nume if utilizator else "Necunoscut",
            "data_inceput": imprumut.data_inceput
        })
    
    return templates.TemplateResponse("admin.html", {
        "request": request, 
        "user": user,
        "is_admin": True,
        "total_carti": total_carti,
        "total_utilizatori": total_utilizatori,
        "total_imprumuturi": total_imprumuturi,
        "imprumuturi_active": imprumuturi_active,
        "imprumuturi_list": imprumuturi_afisare
    })

# Rute pentru autentificare
@app.post("/login")
def login(
    request: Request,
    email: str = Form(...),
    parola: str = Form(...),
    db: Session = Depends(get_db)
):
    from validari.auth import creare_token
    from validari.criptare import verifica_parola
    from db.models.utilizatori_model import UtilizatoriModel

    user = db.query(UtilizatoriModel).filter(UtilizatoriModel.email == email).first()
    if not user or not verifica_parola(parola, user.parola):
        return templates.TemplateResponse("index.html", {
            "request": request, 
            "error": "Email sau parolă incorectă"
        })

    token_data = {
        "sub": user.email,
        "user_id": user.id,
        "nume": user.nume
    }
    access_token = creare_token(data=token_data)

    response = RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)
    response.set_cookie(key="access_token", value=access_token, httponly=True, max_age=3600)
    return response

@app.post("/register")
def register(
    request: Request,
    nume: str = Form(...),
    email: str = Form(...),
    parola: str = Form(...),
    confirm_parola: str = Form(...),
    db: Session = Depends(get_db)
):
    from validari.criptare import hash_parola
    from db.models.utilizatori_model import UtilizatoriModel
    import uuid

    if parola != confirm_parola:
        return templates.TemplateResponse("index.html", {
            "request": request, 
            "error": "Parolele nu coincid"
        })

    existing_user = db.query(UtilizatoriModel).filter(UtilizatoriModel.email == email).first()
    if existing_user:
        return templates.TemplateResponse("index.html", {
            "request": request, 
            "error": "Email-ul este deja înregistrat"
        })

    new_user = UtilizatoriModel(
        id=str(uuid.uuid4()),
        nume=nume,
        email=email,
        parola=hash_parola(parola)
    )

    db.add(new_user)
    db.commit()

    # Autentifică automat după înregistrare
    token_data = {
        "sub": new_user.email,
        "user_id": new_user.id,
        "nume": new_user.nume
    }
    from validari.auth import creare_token
    access_token = creare_token(data=token_data)

    response = RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)
    response.set_cookie(key="access_token", value=access_token, httponly=True, max_age=3600)
    return response

@app.get("/logout")
def logout():
    response = RedirectResponse(url="/")
    response.delete_cookie("access_token")
    return response

# Rute pentru împrumuturi
@app.post("/imprumuta/{carte_id}")
def imprumuta_carte(
    carte_id: str,
    request: Request,
    db: Session = Depends(get_db)
):
    user = get_current_user(request)
    if not user:
        return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)
    
    from db.models.carti_model import CartiModel
    from db.models.imprumut_model import Imprumut
    import uuid
    from datetime import datetime

    # Verifică dacă cartea există
    carte = db.query(CartiModel).filter(CartiModel.id == carte_id).first()
    if not carte:
        return RedirectResponse(url="/catalog?error=Cartea nu a fost găsită", status_code=status.HTTP_302_FOUND)

    # Verifică dacă cartea este deja împrumutată
    imprumut_existent = db.query(Imprumut).filter(
        Imprumut.carte_id == carte_id,
        Imprumut.data_returnare == None
    ).first()
    
    if imprumut_existent:
        return RedirectResponse(url="/catalog?error=Cartea este deja împrumutată", status_code=status.HTTP_302_FOUND)

    # Creează împrumutul
    imprumut_nou = Imprumut(
        id=str(uuid.uuid4()),
        user_id=user["user_id"],
        carte_id=carte_id,
        data_inceput=datetime.utcnow(),
        data_returnare=None
    )

    db.add(imprumut_nou)
    db.commit()

    return RedirectResponse(url="/catalog?success=Cartea a fost împrumutată cu succes", status_code=status.HTTP_302_FOUND)

@app.post("/returnare/{imprumut_id}")
def returnare_carte(
    imprumut_id: str,
    request: Request,
    db: Session = Depends(get_db)
):
    user = get_current_user(request)
    if not user:
        return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)
    
    from db.models.imprumut_model import Imprumut
    from datetime import datetime

    imprumut = db.query(Imprumut).filter(Imprumut.id == imprumut_id).first()
    
    if not imprumut:
        return RedirectResponse(url="/catalog?error=Împrumutul nu a fost găsit", status_code=status.HTTP_302_FOUND)
    
    if imprumut.data_returnare:
        return RedirectResponse(url="/catalog?error=Cartea a fost deja returnată", status_code=status.HTTP_302_FOUND)
    
    # Marchează cartea ca returnată
    imprumut.data_returnare = datetime.utcnow()
    db.commit()

    return RedirectResponse(url="/catalog?success=Cartea a fost returnată cu succes", status_code=status.HTTP_302_FOUND)

# Include router-ele pentru endpoint-uri API
app.include_router(utilizatori.router)
app.include_router(carti.router)

app.include_router(imprumut.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)