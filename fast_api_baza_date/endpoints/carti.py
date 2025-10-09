from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.db_conectare import get_db
from db.models.carti_model import CartiModel

router = APIRouter(prefix="/carti", tags=["Carti"])

@router.get("/")
def get_carti(db: Session = Depends(get_db)):
    carti = db.query(CartiModel).all()
    rezultate = []
    for carte in carti:
        rezultate.append({
            "id": carte.id,
            "titlu": carte.titlu,
            "gen": carte.gen,
            "an_publicare": carte.an_publicare,
            "autor": {
                "id": carte.autor.id,
                "nume": carte.autor.nume
            }
        })
    return rezultate