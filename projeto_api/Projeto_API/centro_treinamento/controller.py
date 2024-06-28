from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy.future import select

from Projeto_API.contrib.dependencies import DatabaseDependency
from Projeto_API.centro_treinamento.schemas import CentroTreinamentoIn, CentroTreinamentoOut
from Projeto_API.centro_treinamento.models import CentroTreinamentoModel

router = APIRouter()


@router.post(
    "/",
    summary="Criar nova Centro de Treinamento",
    status_code=status.HTTP_201_CREATED,
    response_model=CentroTreinamentoOut,
)
async def post(
    db_session: DatabaseDependency, centrotreina_in: CentroTreinamentoIn = Body(...)
) -> CentroTreinamentoOut:
    centro_treinamento_out = CentroTreinamentoOut(id=uuid4(), **centrotreina_in.model_dump())
    centro_treinamento_model = CentroTreinamentoModel(**centrotreina_in.model_dump())

    db_session.add(centro_treinamento_model)
    await db_session.commit()

    return centro_treinamento_out


@router.get(
    "/",
    summary="Consultar os Centro de Treinamento",
    status_code=status.HTTP_200_OK,
    response_model=list[CentroTreinamentoOut],
)
async def query(db_session: DatabaseDependency) -> list[CentroTreinamentoOut]:
    centro_treinamento: list[CentroTreinamentoOut] = (
        (await db_session.execute(select(CentroTreinamentoModel))).scalars().all()
    )

    return centro_treinamento


@router.get(
    "/{id}",
    summary="Consultar Centro de Treinamento por ID",
    status_code=status.HTTP_200_OK,
    response_model=CentroTreinamentoOut,
)
async def queryID(id: UUID4, db_session: DatabaseDependency) -> CentroTreinamentoOut:
    centro_treinamento: CentroTreinamentoOut = (
        (await db_session.execute(select(CentroTreinamentoModel).filter_by(id=id))).scalars().first()
    )

    if not centro_treinamento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Centro de Treinamento não encontrado no ID {id}"
        )

    return centro_treinamento
