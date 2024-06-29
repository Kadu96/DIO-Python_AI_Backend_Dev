from typing import Annotated
from pydantic import UUID4, Field
from Projeto_API.contrib.schemas import BaseSchema


class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[str, Field(description="Nome do Centro de treinamento", examples=["Centro SUl"], max_length=20)]
    endereco: Annotated[str, Field(description="Endereço do Centro de treinamento", examples=["Sul"], max_length=60)]
    proprietario: Annotated[
        str, Field(description="Proprietario do Centro de treinamento", examples=[""], max_length=30)
    ]


class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[str, Field(description="Nome do Centro de treinamento", examples=["Centro SUl"], max_length=20)]


class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description="Identificador do Centro de Treinamento")]
