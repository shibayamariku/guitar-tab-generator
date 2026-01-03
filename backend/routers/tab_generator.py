# routers/tab_generator.py

from fastapi import APIRouter
from services import tab_service  # ← さっきのファイルを呼び出す

router = APIRouter(prefix="/tabs", tags=["tabs"])

@router.get("/")
def list_tabs():
    return {"tabs": ["A", "B", "C"]}

@router.post("/generate")
def generate_tab():
    result = tab_service.generate()
    return {"message": result}
