from datetime import datetime
from pydantic import UUID4
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, Query, status
from fastapi_pagination import Page, add_pagination, paginate

from Projeto_API.contrib.dependencies import DatabaseDependency
from Projeto_API.atleta.schemas import AtletaIn, AtletaListOut, AtletaOut, AtletaUpdate
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
    try:
        atleta_out = AtletaOut(id=uuid4(), created_at=datetime.utcnow(), **atleta_in.model_dump())
        atleta_model = AtletaModel(**atleta_out.model_dump(exclude={"categoria", "centro_treinamento"}))
        atleta_model.categoria_id = categoria.pk_id
        atleta_model.centro_treinamento_id = centro_treinamento.pk_id

        db_session.add(atleta_model)
        await db_session.commit()
    except IntegrityError:
        await db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_303_SEE_OTHER,
            detail=f"Já existe um atleta cadastrado com o cpf: {atleta_in.cpf}",
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ocorreu um erro ao inserir dados no banco"
        )
    return atleta_out


@router.get(
    "/",
    summary="Consultar Atletas",
    status_code=status.HTTP_200_OK,
    response_model=Page[AtletaListOut],
)
async def getAll(
    db_session: DatabaseDependency,
    nome: str = Query(None, description="Nome do Atleta"),
    cpf: str = Query(None, description="CPF do Atleta"),
) -> Page[AtletaListOut]:
    query = select(AtletaModel).join(CentroTreinamentoModel).join(CategoriaModel)

    if nome:
        query = query.filter(AtletaModel.nome.ilike(f"%{nome}%"))
    if cpf:
        query = query.filter(AtletaModel.cpf == cpf)

    result = await db_session.execute(query)
    atletas = result.scalars().all()

    atletas_out = [
        AtletaListOut(
            nome=atleta.nome,
            centro_treinamento=atleta.centro_treinamento.nome,
            categoria=atleta.categoria.nome,
        )
        for atleta in atletas
    ]

    return paginate(atletas_out)


@router.get(
    "/{id}",
    summary="Consultar Atletas por ID",
    status_code=status.HTTP_200_OK,
    response_model=AtletaOut,
)
async def queryID(id: UUID4, db_session: DatabaseDependency) -> AtletaOut:
    query_atleta = (await db_session.execute(select(AtletaModel).filter_by(id=id))).scalars().first()
    atleta: AtletaOut = query_atleta  # type: ignore

    if not atleta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Categoria não encotarda no ID {id}")

    return atleta


@router.patch(
    "/{id}",
    summary="Editar Atletas por ID",
    status_code=status.HTTP_200_OK,
    response_model=AtletaOut,
)
async def edit(id: UUID4, db_session: DatabaseDependency, atleta_up: AtletaUpdate = Body(...)) -> AtletaOut:
    query_atleta = (await db_session.execute(select(AtletaModel).filter_by(id=id))).scalars().first()
    atleta: AtletaOut = query_atleta  # type: ignore

    if not atleta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Atleta não encotardo no ID {id}")

    atleta_update = atleta_up.model_dump(exclude_unset=True)
    for key, value in atleta_update.items():
        setattr(atleta, key, value)

    await db_session.commit()
    await db_session.refresh(atleta)

    return atleta


@router.delete("/{id}", summary="Deletar Atletas por ID", status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: UUID4, db_session: DatabaseDependency) -> None:
    query_atleta = (await db_session.execute(select(AtletaModel).filter_by(id=id))).scalars().first()
    atleta: AtletaOut = query_atleta  # type: ignore

    if not atleta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Atleta não encotardo no ID {id}")

    await db_session.delete(atleta)
    await db_session.commit()


add_pagination(router)
