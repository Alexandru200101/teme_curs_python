import uuid
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String
from .base import Base


class AutoriModel(Base):
    __tablename__ = "autori"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nume: Mapped[str] = mapped_column(String(100), nullable=False)

    # Relația către cărți
    carti = relationship("CartiModel", back_populates="autor")

from db.models.carti_model import CartiModel


