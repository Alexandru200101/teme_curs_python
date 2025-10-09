from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy import or_
from db.db_conectare import get_db
from db.models.carti_model import CartiModel
from db.models.autori_model import AutoriModel

router = APIRouter(prefix="/carti", tags=["Carti"])

templates = Jinja2Templates(directory="templates")

# ✅ Endpoint JSON (rămâne pentru API)
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


# ✅ Endpoint HTML pentru catalog (cu filtrare după gen + căutare)
@router.get("/catalog")
def catalog(request: Request, db: Session = Depends(get_db)):
    gen = request.query_params.get("gen")
    search = request.query_params.get("search")

    query = db.query(CartiModel)

    # Filtrare după gen (dacă nu e 'all' sau None)
    if gen and gen.lower() != "all":
        query = query.filter(CartiModel.gen == gen)

    # Căutare după titlu, gen sau autor
    if search:
        query = query.join(CartiModel.autor).filter(
            or_(
                CartiModel.titlu.ilike(f"%{search}%"),
                CartiModel.gen.ilike(f"%{search}%"),
                AutoriModel.nume.ilike(f"%{search}%")
            )
        )

    carti = query.all()

    # Toate genurile distincte
    genuri = [g[0] for g in db.query(CartiModel.gen).distinct().all() if g[0]]

    # Prelucrare pentru template
    carti_data = []
    for c in carti:
        carti_data.append({
            "id": c.id,
            "titlu": c.titlu,
            "gen": c.gen,
            "an_publicare": c.an_publicare,
            "autor": c.autor.nume if c.autor else "Necunoscut",
            "este_imprumutata": False,  # poți lega ulterior cu Imprumut
            "imprumut_id": None
        })

    return templates.TemplateResponse(
        "catalog.html",
        {
            "request": request,
            "carti": carti_data,
            "gen_selectat": gen,
            "genuri": genuri,
            "user": None  # poți adăuga autentificarea aici
        }
    )
