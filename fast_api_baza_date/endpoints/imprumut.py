from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.db_conectare import get_db
from db.models.imprumut_model import Imprumut
from db.models.carti_model import CartiModel
from db.models.utilizatori_model import UtilizatoriModel
from auth_utils import get_current_user
from validari.modele import ImprumutCreate
from datetime import datetime
import uuid

router = APIRouter(prefix="/imprumuturi", tags=["Imprumuturi"])

@router.post("/")
def creeaza_imprumut(imprumut: ImprumutCreate, db: Session = Depends(get_db)):
    carte = db.query(CartiModel).filter(CartiModel.id == imprumut.carte_id).first()
    if not carte:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cartea nu a fost găsită"
        )

    utilizator = db.query(UtilizatoriModel).filter(UtilizatoriModel.id == imprumut.utilizator_id).first()
    if not utilizator:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Utilizatorul nu a fost găsit"
        )

    imprumut_existent = db.query(Imprumut).filter(
        Imprumut.carte_id == imprumut.carte_id,
        Imprumut.data_returnare == None
    ).first()
    
    if imprumut_existent:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cartea este deja împrumutată"
        )

    imprumut_nou = Imprumut(
        id=str(uuid.uuid4()),
        user_id=imprumut.utilizator_id,
        carte_id=imprumut.carte_id,
        data_inceput=datetime.utcnow(),
        data_returnare=None
    )

    db.add(imprumut_nou)
    db.commit()
    db.refresh(imprumut_nou)

    return {
        "message": "Cartea a fost împrumutată cu succes",
        "imprumut_id": imprumut_nou.id,
        "carte_titlu": carte.titlu
    }

@router.get("/utilizator/{user_id}")
def get_imprumuturi_utilizator(user_id: str, db: Session = Depends(get_db)):
    imprumuturi = db.query(Imprumut).filter(Imprumut.user_id == user_id).all()
    
    rezultate = []
    for imprumut in imprumuturi:
        carte = db.query(CartiModel).filter(CartiModel.id == imprumut.carte_id).first()
        rezultate.append({
            "imprumut_id": imprumut.id,
            "carte_titlu": carte.titlu if carte else "Necunoscut",
            "data_inceput": imprumut.data_inceput,
            "data_returnare": imprumut.data_returnare,
            "este_activ": imprumut.data_returnare is None
        })
    
    return rezultate

@router.get("/active")
def get_imprumuturi_active(db: Session = Depends(get_db)):
    imprumuturi = db.query(Imprumut).filter(Imprumut.data_returnare == None).all()
    
    rezultate = []
    for imprumut in imprumuturi:
        carte = db.query(CartiModel).filter(CartiModel.id == imprumut.carte_id).first()
        utilizator = db.query(UtilizatoriModel).filter(UtilizatoriModel.id == imprumut.user_id).first()
        
        rezultate.append({
            "imprumut_id": imprumut.id,
            "carte_titlu": carte.titlu if carte else "Necunoscut",
            "utilizator_nume": utilizator.nume if utilizator else "Necunoscut",
            "utilizator_email": utilizator.email if utilizator else "Necunoscut",
            "data_inceput": imprumut.data_inceput,
            "zile_scurse": (datetime.utcnow() - imprumut.data_inceput).days
        })
    
    return rezultate

@router.post("/returnare/{imprumut_id}")
def returneaza_carte(
    imprumut_id: str,
    db: Session = Depends(get_db),
    user: UtilizatoriModel = Depends(get_current_user)
):
    imprumut = db.query(Imprumut).filter(Imprumut.id == imprumut_id).first()

    if not imprumut:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Împrumutul nu a fost găsit"
        )

    # ❗ Verificăm dacă utilizatorul logat e același care a împrumutat cartea
    if imprumut.user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Nu poți returna o carte împrumutată de alt utilizator."
        )

    if imprumut.data_returnare:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cartea a fost deja returnată"
        )

    imprumut.data_returnare = datetime.utcnow()
    db.commit()

    return {"message": "Cartea a fost returnată cu succes"}