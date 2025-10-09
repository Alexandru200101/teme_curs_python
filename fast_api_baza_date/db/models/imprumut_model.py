import uuid
import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, DateTime
from .base import Base



class Imprumut(Base):
    __tablename__ = "imprumuturi"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("utilizatori.id"), nullable=False)
    carte_id: Mapped[str] = mapped_column(String(36), ForeignKey("carti.id"), nullable=False)
    data_inceput: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    data_returnare: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=True)

    # Relațiile inverse
    utilizatori = relationship("UtilizatoriModel", back_populates="imprumuturi")
    carte = relationship("CartiModel", back_populates="imprumuturi")

from db.models.utilizatori_model import UtilizatoriModel
from db.models.carti_model import CartiModel



