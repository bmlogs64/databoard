import pandas as pd

def tratar_dados(df: pd.DataFrame) -> pd.DataFrame:

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["timestamp"] = df["timestamp"].dt.tz_convert("America/Sao_Paulo")

    df["cpf"] = df["cpf"].astype(str).str.zfill(11)

    def formatar_cpf(cpf: str) -> str:
        
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    df["cpf"] = df["cpf"].apply(formatar_cpf)

    def formatar_telefone(numero: str) -> str:

        numero = numero.replace(" ", "")

        if numero.startswith("+55"):

            ddd = numero[3:5]

            resto = numero[5:]

            if len(resto) == 9:

                return f"+55 ({ddd}) {resto[:5]}-{resto[5:]}"
            
            elif len(resto) == 8:

                return f"+55 ({ddd}) {resto[:4]}-{resto[4:]}"
            
        return numero
    
    df["numero"] = df["numero"].astype(str).apply(formatar_telefone)

    df["data_formatada"] = df["timestamp"].dt.strftime("%d/%m/%Y %H:%M:%S")

    return df


if __name__ == "__main__":

    print("🔎 Testando tratamento de dados...")

    dados = {
        "id": ["b09c49f4", "fe670f4a"],
        "nome": ["Sra. Isabelly Lopes", "Gael Melo"],
        "numero": ["+5563915618197", "+5522928481748"],
        "email": ["sra.isabelly.lopes.2558@email.com", "gael.melo.5353@example.com"],
        "cpf": [83494893241, 20300243332],
        "timestamp": ["2025-09-24T13:07:09.518288Z", "2025-09-24T13:08:09.822167Z"]
    }

    df = pd.DataFrame(dados)

    df_tratado = tratar_dados(df)

    print("✅ Dados tratados com sucesso!\n")
    print(df_tratado)
