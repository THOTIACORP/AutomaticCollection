from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import captura, prontuario

app = FastAPI(title="Escudo Orofacial API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(captura.router, prefix="/captura", tags=["captura"])
app.include_router(prontuario.router, prefix="/prontuario", tags=["prontuario"])

@app.get("/")
def root():
    return {"project":"escudo-orofacial", "status":"ok"}
