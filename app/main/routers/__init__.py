from fastapi import APIRouter

from app.main.routers import api

api_router = APIRouter()
api_router.include_router(api.api_router, prefix="/api")
