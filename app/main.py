from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.services.data_service import buscar_e_tratar_dados

app = FastAPI(title="Dashboard de Dados")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"], 
)

@app.get("/dados")
def get_dados():
    try:
        dados = buscar_e_tratar_dados()
        return {"status": "sucesso", "total": len(dados), "dados": dados}
    except Exception as e:
        return {"status": "erro", "mensagem": str(e)}
