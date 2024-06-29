from typing import Annotated
from pydantic import Field, PositiveFloat

from Projeto_API.contrib.schemas import BaseSchema, OutMixin
from Projeto_API.categorias.schemas import CategoriaIn
from Projeto_API.centro_treinamento.schemas import CentroTreinamentoAtleta


class Atleta(BaseSchema):
    nome: Annotated[str, Field(description="Nome do Atleta", examples=["Joao"], max_length=50)]
    cpf: Annotated[str, Field(description="CPF do Atleta", examples=["11111111111"], max_length=11)]
    idade: Annotated[int, Field(description="Idade do Atleta", examples=[28])]
    peso: Annotated[PositiveFloat, Field(description="Peso do Atleta", examples=[75.5])]
    altura: Annotated[PositiveFloat, Field(description="Altura do Atleta", examples=[1.70])]
    sexo: Annotated[str, Field(description="Sexo do Atleta", examples=["M"], max_length=1)]
    categoria: Annotated[CategoriaIn, Field(description="Categoria")]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description="Centro Treinamento")]


class AtletaIn(Atleta):
    pass


class AtletaOut(AtletaIn, OutMixin):
    pass
