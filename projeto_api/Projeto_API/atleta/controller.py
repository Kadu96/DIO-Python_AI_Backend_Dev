from datetime import datetime
from sqlalchemy.future import select
from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status

from Projeto_API.contrib.dependencies import DatabaseDependency
from Projeto_API.atleta.schemas import AtletaIn, AtletaOut
from Projeto_API.atleta.models import AtletaModel
from Projeto_API.categorias.models import CategoriaModel
from Projeto_API.centro_treinamento.models import CentroTreinamentoModel

router = APIRouter()


@router.post("/", summary="Criar novo atleta", status_code=status.HTTP_201_CREATED, response_model=AtletaOut)
async def post(db_session: DatabaseDependency, atleta_in: AtletaIn = Body(...)):
    categoria_nome = atleta_in.categoria.nome
    centro_treinamento_nome = atleta_in.centro_treinamento.nome
    categoria = (await db_session.execute(select(CategoriaModel).filter_by(nome=categoria_nome))).scalars().first()
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"Categoria {categoria_nome} não encotrada!!"
        )
    centro_treinamento = (
        (await db_session.execute(select(CentroTreinamentoModel).filter_by(nome=centro_treinamento_nome)))
        .scalars()
        .first()
    )
    if not centro_treinamento:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Centro de Treinamento {centro_treinamento_nome} não encotrado!!",
        )
    atleta_out = AtletaOut(id=uuid4(), created_at=datetime.utcnow(), **atleta_in.model_dump())
    atleta_model = AtletaModel(**atleta_in.model_dump(exclude={"categoria", "centro_treinamento"}))
    atleta_model.categoria_id = categoria.pk_id
    atleta_model.centro_treinamento_id = centro_treinamento.pk_id

    db_session.add(atleta_model)
    await db_session.commit()

    return atleta_out
