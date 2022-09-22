from fastapi import APIRouter
from app.api.routes.ma_companyController import router as company_router

router = APIRouter()

router.include_router(company_router,prefix="/companys",tags=["macompany"])