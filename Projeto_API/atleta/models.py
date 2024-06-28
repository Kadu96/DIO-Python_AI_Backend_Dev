from datetime import datetime
from sqlalchemy import DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from Projeto_API.categorias.models import CategoriaModel
from Projeto_API.centro_treinamento.models import CentroTreinamentoModel
from Projeto_API.contrib.models import BaseModel


class AtletaModel(BaseModel):
    __tablename__ = "atletas"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), nullable=False, unique=True)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    peso: Mapped[float] = mapped_column(Float, nullable=False)
    altura: Mapped[float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    categoria: Mapped["CategoriaModel"] = relationship(back_populates="atleta")
    categoria_id: Mapped[int] = mapped_column(ForeignKey("categorias.pk_id"))
    centro_treinamento: Mapped["CentroTreinamentoModel"] = relationship(back_populates="atleta")
    centro_treinamento_id: Mapped[int] = mapped_column(ForeignKey("centro_treinamentos.pk_id"))
