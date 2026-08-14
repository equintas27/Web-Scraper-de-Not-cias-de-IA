from exporter import save_as_csv
from fetcher import fetch_html
from parser import parsing_html

URL = "https://techcrunch.com/category/artificial-intelligence/"
OUTPUT = "noticias_csv"

def run():
    html = fetch_html(URL)
    if html is not None:
        dados = parsing_html(html)
        done = save_as_csv(dados, OUTPUT)
        if not done:
            print ("Não foi possível criar arquivo")
            return None
        print ("Arquivo criado")
    return None

if __name__ == "__main__":
    run()