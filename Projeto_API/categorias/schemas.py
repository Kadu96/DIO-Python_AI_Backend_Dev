from typing import Annotated
from pydantic import Field
from Projeto_API.contrib.schemas import BaseModel


class Categoria(BaseModel):
    nome: Annotated[str, Field(description="Nome da Categoria", examples=["Scale"], max_length=10)]
