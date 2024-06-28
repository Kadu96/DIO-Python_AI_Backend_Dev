from typing import Annotated
from pydantic import Field
from Projeto_API.contrib.schemas import BaseModel


class CentroTreinamneto(BaseModel):
    nome: Annotated[str, Field(description="Nome do Centro de treinamento", examples=[""], max_length=20)]
    endereco: Annotated[str, Field(description="Endereço do Centro de treinamento", examples=[""], max_length=60)]
    proprietario: Annotated[
        str, Field(description="Proprietario do Centro de treinamento", examples=[""], max_length=30)
    ]
