from bs4 import BeautifulSoup

def parsing_html(html_content: str) -> list(dict[str, str]):
    soup = BeautifulSoup(html_content, 'html.parser')
    noticias = []
    artigos = soup.find_all("a", class_= "oop-card__title-link")
    for artigo in artigos:
        titulo = artigo.get_text(strip=True)
        link = artigo.get("href", "")

        if titulo and link:
            noticias.append({
                "Titulo": titulo,
                "Link": link
            })
    return noticias

