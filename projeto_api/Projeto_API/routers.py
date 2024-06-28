from fastapi import APIRouter
from Projeto_API.centro_treinamento.controller import router as centro_treinamento
from Projeto_API.atleta.controller import router as atleta
from Projeto_API.categorias.controller import router as categoria


api_router = APIRouter()
api_router.include_router(atleta, prefix="/atletas", tags=["atletas"])
api_router.include_router(categoria, prefix="/categorias", tags=["categorias"])
api_router.include_router(centro_treinamento, prefix="/centros_treinamento", tags=["centros_treinamento"])
