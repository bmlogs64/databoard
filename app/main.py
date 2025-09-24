from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
from app.services.data_service import buscar_e_tratar_dados

app = FastAPI()

origins = ["*"]

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
        return JSONResponse(
            content={"status": "sucesso", "dados": dados},
            media_type="application/json; charset=utf-8"
        )
    except Exception as e:
        return JSONResponse(
            content={"status": "erro", "mensagem": str(e)},
            media_type="application/json; charset=utf-8"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000)),
        reload=True
    )
