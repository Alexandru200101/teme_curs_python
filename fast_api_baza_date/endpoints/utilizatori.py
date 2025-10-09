from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.db_conectare import get_db
from db.models.utilizatori_model import UtilizatoriModel
from validari.modele import UtilizatorCreate, UtilizatorLogin
from validari.criptare import hash_parola, verifica_parola
from validari.auth import creare_token
import uuid

router = APIRouter(prefix="/utilizatori", tags=["Utilizatori"])

@router.post("/register")
def register(utilizator: UtilizatorCreate, db: Session = Depends(get_db)):
    existing_user = db.query(UtilizatoriModel).filter(UtilizatoriModel.email == utilizator.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email-ul este deja înregistrat"
        )
    
    new_user = UtilizatoriModel(
        id=str(uuid.uuid4()),
        nume=utilizator.nume,
        email=utilizator.email,
        parola=hash_parola(utilizator.parola)
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"message": "Utilizator creat cu succes", "user_id": new_user.id}

@router.post("/login")
def login(utilizator: UtilizatorLogin, db: Session = Depends(get_db)):
    user = db.query(UtilizatoriModel).filter(UtilizatoriModel.email == utilizator.email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email sau parolă incorectă"
        )
    
    if not verifica_parola(utilizator.parola, user.parola):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email sau parolă incorectă"
        )
    
    token_data = {
        "sub": user.email,
        "user_id": user.id,
        "nume": user.nume
    }
    access_token = creare_token(data=token_data)
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "nume": user.nume,
            "email": user.email
        }
    }



