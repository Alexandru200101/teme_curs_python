from pydantic import BaseModel, field_validator, Field
from typing import Annotated

class UtilizatorCreate(BaseModel):
    nume: Annotated[str, Field(min_length=2, max_length=100)]
    email: Annotated[str, Field(pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")]
    parola: Annotated[str, Field(min_length=6)]

    @field_validator("parola")
    def parola_complexa(cls, v):
        if not any(c.isupper() for c in v):
            raise ValueError("Parola trebuie să conțină cel puțin o literă mare")
        if not any(c.isdigit() for c in v):
            raise ValueError("Parola trebuie să conțină cel puțin o cifră")
        return v

class UtilizatorLogin(BaseModel):
    email: Annotated[str, Field(pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")]
    parola: str

class CarteCreate(BaseModel):
    titlu: Annotated[str, Field(min_length=1, max_length=200)]
    descriere: Annotated[str, Field(max_length=1000)] | None = None
    gen : Annotated[str, Field(max_length=100)] | None = None
    an_publicare: Annotated[int, Field(ge=0)] | None = None

class ImprumutCreate(BaseModel):
    utilizator_id: str
    carte_id: str