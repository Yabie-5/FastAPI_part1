from fastapi import APIRouter
from app.api.routes import ma_companyController

router = APIRouter()

router.include_router(ma_companyController.router,prefix="/companys",tags=["macompany"])