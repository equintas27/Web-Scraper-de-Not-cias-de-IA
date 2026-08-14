from bs4 import BeautifulSoup

def parsing_html(html_content: str) -> list[dict[str, str]]:
    soup = BeautifulSoup(html_content, 'html.parser')
    noticias: list[dict[str, str]] = []
    artigos = soup.find_all("a", class_= "loop-card__title-link")
    print (artigos)
    for artigo in artigos:
        titulo = artigo.get_text(strip=True)
        link = str(artigo.get("href") or "")
        if titulo and link:
            noticias.append({
                "Titulo": titulo,
                "Link": link
            })
    return noticias

