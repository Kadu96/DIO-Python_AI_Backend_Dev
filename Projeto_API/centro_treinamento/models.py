from datetime import datetime
from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from Projeto_API.atleta.models import AtletaModel
from Projeto_API.contrib.models import BaseModel


class CentroTreinamentoModel(BaseModel):
    __tablename__ = "centro_treinamentos"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    endereco: Mapped[str] = mapped_column(String(60), nullable=False)
    proprietario: Mapped[str] = mapped_column(String(30), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    atleta: Mapped["AtletaModel"] = relationship(back_populates="centro_treinamento")
