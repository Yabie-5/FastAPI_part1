from typing import List
from fastapi import APIRouter

router = APIRouter()

@router.get("/all")
async def get_all_company():
    allcompanydata = [
        {"id":1,"company_cd":"0001","company_nm":"CompanyA"},
        {"id":2,"company_cd":"0002","company_nm":"CompanyB"}
    ]

    return allcompanydata