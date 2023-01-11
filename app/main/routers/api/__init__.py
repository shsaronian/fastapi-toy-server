from fastapi import APIRouter

from app.main.routers.api import endpoints

api_router = APIRouter()
api_router.include_router(endpoints.router, prefix="/endpoints", tags=["Endpoints"])