from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
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
            content={"status": "sucesso", "dados": dados},
            status_code=200,
            media_type="application/json",
            ensure_ascii=False,  # mantém ç, ~, á, etc.
        )
    except Exception as e:
        return JSONResponse(
            content={"status": "erro", "mensagem": str(e)},
            status_code=500,
            ensure_ascii=False,
        )

@app.get("/")
def root():
    return {"mensagem": "API funcionando! 🚀"}
