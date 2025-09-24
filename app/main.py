from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from app.data_service import buscar_e_tratar_dados

app = FastAPI()

origins = [
    "https://bmlogs64.github.io/databoard",
    "*" 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/dados")
def dados():
    try:
        dados = buscar_e_tratar_dados()
        return dados
    except Exception as e:
        return {"status": "erro", "mensagem": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000)),
        reload=True
    )
