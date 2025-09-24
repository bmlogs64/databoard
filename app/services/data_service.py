import pandas as pd
import requests
from io import StringIO
from app.config import URL_PLANILHA

def buscar_planilha():
    if not URL_PLANILHA:
        raise ValueError("A URL da planilha não está definida no .env")

    try:
        resp = requests.get(URL_PLANILHA, timeout=10)
        resp.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Erro ao acessar a planilha: {e}")

    df = pd.read_csv(StringIO(resp.text), encoding="utf-8")
    return df

def tratar_dados(df: pd.DataFrame) -> pd.DataFrame:

    df["timestamp"] = pd.to_datetime(df["timestamp"], errors='coerce')

    if df["timestamp"].dt.tz is None:
        df["timestamp"] = df["timestamp"].dt.tz_localize("UTC").dt.tz_convert("America/Sao_Paulo")
    else:
        df["timestamp"] = df["timestamp"].dt.tz_convert("America/Sao_Paulo")
    
    df["cpf"] = df["cpf"].astype(str).str.zfill(11)
    df["cpf"] = df["cpf"].apply(lambda x: f"{x[:3]}.{x[3:6]}.{x[6:9]}-{x[9:]}")

    def formatar_telefone(numero: str) -> str:
        numero = str(numero).replace(" ", "").replace("+", "")
        if numero.startswith("55"):
            numero = numero[2:]
        ddd = numero[:2]
        restante = numero[2:]
        if len(restante) == 9:
            return f"+55 ({ddd}) {restante[:5]}-{restante[5:]}"
        elif len(restante) == 8:
            return f"+55 ({ddd}) {restante[:4]}-{restante[4:]}"
        else:
            return f"+55 ({ddd}) {restante}"

    df["numero"] = df["numero"].apply(formatar_telefone)

    df["data_formatada"] = df["timestamp"].dt.strftime("%d/%m/%Y %H:%M:%S")

    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype(str)

    return df

def buscar_e_tratar_dados():
    df = buscar_planilha()
    df_tratado = tratar_dados(df)
    return {"status": "sucesso", "dados": df_tratado.to_dict(orient="records")}
