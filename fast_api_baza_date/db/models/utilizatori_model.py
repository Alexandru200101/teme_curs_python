from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String
import uuid
from .base import Base


class UtilizatoriModel(Base):
    __tablename__ = "utilizatori"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nume: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    parola: Mapped[str] = mapped_column(String(100), nullable=False)

    # RELAȚIE: forward reference ca string
    imprumuturi = relationship("Imprumut", back_populates="utilizatori")
    
from db.models.imprumut_model import Imprumut


