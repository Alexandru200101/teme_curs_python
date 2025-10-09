from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_parola(parola: str) -> str:
    return pwd_context.hash(parola)

def verifica_parola(parola: str, hash_parola_db: str) -> bool:
    return pwd_context.verify(parola, hash_parola_db)
