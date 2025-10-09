import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(dotenv_path)

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

required_vars = ["DB_USER", "DB_PASSWORD", "DB_HOST", "DB_PORT", "DB_NAME"]
for var in required_vars:
    if not globals().get(var):
        raise ValueError(f"Variabila de mediu lipsă: {var}. Verifică fișierul .env!")

def verifica_sau_creeaza_baza_date():
    engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/")
    with engine.connect() as conn:
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"))
        conn.commit()
        print(f"Baza de date '{DB_NAME}' a fost verificată sau creată.")

def conectare_baza_date():
    db_url = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_engine(db_url, echo=False)
    return engine

def get_session():
    engine = conectare_baza_date()
    SessionLocal = sessionmaker(bind=engine)
    return SessionLocal()

def get_db():
    db = get_session()
    try:
        yield db
    finally:
        db.close()