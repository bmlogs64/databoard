from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json
from app.services.data_service import buscar_e_tratar_dados

app = FastAPI()

origins = [
    "https://bmlogs64.github.io",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/dados")
def get_dados():
    try:
        dados = buscar_e_tratar_dados()
        return JSONResponse(
        content=json.loads(json.dumps({"status": "sucesso", "dados": dados}, ensure_ascii=False)),
        status_code=200
        )
    except Exception as e:
        return JSONResponse(
        content=json.loads(json.dumps({"status": "erro", "mensagem": str(e)}, ensure_ascii=False)),
        status_code=500
        )


@app.get("/")
def root():
    return {"mensagem": "API funcionando! 🚀"}
