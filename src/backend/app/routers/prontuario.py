from fastapi import APIRouter
from fastapi.responses import JSONResponse
from ..services.prontuario_service import build_prontuario

router = APIRouter()

@router.post("/criar")
def criar_prontuario(payload: dict):
    pront = build_prontuario(payload.get("user_id","unknown"))
    return JSONResponse({"status":"ok","prontuario":pront})
