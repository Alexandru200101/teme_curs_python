import uuid
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from .base import Base



class CartiModel(Base):
    __tablename__ = "carti"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    titlu: Mapped[str] = mapped_column(String(200), nullable=False)
    autor_id: Mapped[str] = mapped_column(String(36), ForeignKey("autori.id"), nullable=False)
    gen: Mapped[str] = mapped_column(String(100), nullable=True)
    an_publicare: Mapped[int] = mapped_column(nullable=True)


    # Relațiile
    autor = relationship("AutoriModel", back_populates="carti")
    imprumuturi = relationship("Imprumut", back_populates="carte")

from db.models.autori_model import AutoriModel
from db.models.imprumut_model import Imprumut

