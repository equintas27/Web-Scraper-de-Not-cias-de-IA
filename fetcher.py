import  requests
from parser import parsing_html

def fetch_html(url: str) -> str | None:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64)"
            "AppleWebKit/537.36 (KHTML, like Gecko)"
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.Timeout:
        print ("[Erro]: o site está demorando 10 segundos")
        return None
    except requests.exceptions.RequestException as e:
        print (f"Ocorreu um erro: {e}")
        return None

if __name__ == "__main__":
    ur1 = "https://techcrunch.com/category/artificial-intelligence/"
    ur2 = "Novo Modelo de IA Lançado"
    html = fetch_html(ur1)
    if html is not None:
        b = parsing_html(html)
        print (f"Tamanho do html {len(html)}")
        print (b)
    c = parsing_html(ur2)
    print (c)