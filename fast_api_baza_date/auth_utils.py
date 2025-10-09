from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.db_conectare import get_db
from db.models.utilizatori_model import UtilizatoriModel

def get_current_user(db: Session = Depends(get_db)) -> UtilizatoriModel:
    """
    Aceasta funcție trebuie să returneze utilizatorul logat.
    Pentru început, poți folosi un user dummy sau primul user din DB.
    În aplicația reală, aici decodezi JWT sau verifici sesiunea.
    """
    user = db.query(UtilizatoriModel).first()  # exemplu simplu
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
    return user
