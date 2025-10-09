# FastAPI
from django.db import router
from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# SQLAlchemy
from sqlalchemy.orm import Session
from sqlalchemy import or_

# Database
from db.db_conectare import get_db

# Modele
from db.models.carti_model import CartiModel
from db.models.autori_model import AutoriModel
from db.models.imprumut_model import ImprumutModel
from db.models.utilizatori_model import UtilizatoriModel  # dacă ai un model User

# Autentificare
from validari.auth import get_current_user  # funcție care returnează userul curent

# Alte utilități
from datetime import datetime
templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get("/catalog")
def catalog(request: Request, db: Session = Depends(get_db), user=Depends(get_current_user)):
    gen = request.query_params.get("gen")
    search = request.query_params.get("search")

    query = db.query(CartiModel)

    if gen and gen.lower() != "all":
        query = query.filter(CartiModel.gen == gen)

    if search:
        query = query.join(CartiModel.autor).filter(
            or_(
                CartiModel.titlu.ilike(f"%{search}%"),
                CartiModel.gen.ilike(f"%{search}%"),
                AutoriModel.nume.ilike(f"%{search}%")
            )
        )

    carti = query.all()

    carti_data = []
    for c in carti:
        # Verificăm dacă cartea este împrumutată și cine a împrumutat-o
        imprumut = db.query(ImprumutModel).filter(
            ImprumutModel.carte_id == c.id,
            ImprumutModel.data_returnare == None
        ).first()

        este_imprumutata = False
        imprumut_id = None

        if imprumut:
            este_imprumutata = True
            # Doar cel care a împrumutat vede butonul de returnare activ
            if imprumut.user_id == user.id:
                imprumut_id = imprumut.id
            else:
                imprumut_id = None  # altcineva nu poate returna

        carti_data.append({
            "id": c.id,
            "titlu": c.titlu,
            "gen": c.gen,
            "an_publicare": c.an_publicare,
            "autor": c.autor.nume if c.autor else "Necunoscut",
            "este_imprumutata": este_imprumutata,
            "imprumut_id": imprumut_id
        })

    return templates.TemplateResponse(
        "catalog.html",
        {"request": request, "carti": carti_data, "user": user}
    )
