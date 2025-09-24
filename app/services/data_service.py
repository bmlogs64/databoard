import pandas as pd
import requests
from io import StringIO
from app.config import URL_PLANILHA

def buscar_planilha():
    resp = requests.get(URL_PLANILHA)
    resp.raise_for_status()
    df = pd.read_csv(StringIO(resp.text))
    return df

def tratar_dados(df: pd.DataFrame) -> pd.DataFrame:
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["timestamp"] = df["timestamp"].dt.tz_convert("America/Sao_Paulo")
    
    df["cpf"] = df["cpf"].astype(str).str.zfill(11)
    df["cpf"] = df["cpf"].apply(lambda x: f"{x[:3]}.{x[3:6]}.{x[6:9]}-{x[9:]}")
    
    def formatar_telefone(numero: str) -> str:
        numero = str(numero).replace(" ", "")
        if numero.startswith("+55"):
            ddd = numero[3:5]
            resto = numero[5:]
            if len(resto) == 9:
                return f"+55 ({ddd}) {resto[:5]}-{resto[5:]}"
            elif len(resto) == 8:
                return f"+55 ({ddd}) {resto[:4]}-{resto[4:]}"
        return numero

    df["numero"] = df["numero"].apply(formatar_telefone)
    df["data_formatada"] = df["timestamp"].dt.strftime("%d/%m/%Y %H:%M:%S")
    return df

def buscar_e_tratar_dados():
    df = buscar_planilha()
    df_tratado = tratar_dados(df)
    return df_tratado.to_dict(orient="records")
