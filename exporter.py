import pandas as pd

def save_as_csv(dados: list[dict[str, str]], filename: str = "noticias_ia.csv")-> bool:
    if not dados:
        print ("Nenhum dado encontrado!")
        return False
    try:
        df = pd.DataFrame(dados)
        df.drop_duplicates(subset=["Link"], inplace=True)
        df.to_csv(filename, index=False, encoding="utf-8")
        print (f"Sucesso {len(df)} noticias guardadas em {filename}")
        return True
    except Exception as e:
        print (f"Erro ao salvar: {e}")
        return False
