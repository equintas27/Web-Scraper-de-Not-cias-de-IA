import pandas as pd

def save_as_csv(dados: list[dict[str, str]], filename: str = "noticias_ia.csv")-> bool:
    if not dados:
        print ("Nenhum dado encontrado!")
        return False
    try:
        df = pd.DataFrame(dados)
        df.drop_duplicates