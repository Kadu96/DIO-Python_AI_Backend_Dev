from fastapi import APIRouter, Body, status

from Projeto_API.contrib.dependencies import DatabaseDependency
from Projeto_API.atleta.schemas import AtletaIn, AtletaOut

router = APIRouter()


@router.post("/", summary="Criar novo atleta", status_code=status.HTTP_201_CREATED, response_model=AtletaOut)
async def post(db_session: DatabaseDependency, atleta_in: AtletaIn = Body(...)):
    pass
