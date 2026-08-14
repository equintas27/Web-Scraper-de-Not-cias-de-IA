# Web Scrapper

O objetivo é criar um script Python modular para recolher automaticamente os títulos e os respetivos links das noticias mais recents sobre Inteligência Artificial (de um site como o TechCrunch) e exportar esses dados limpos para um ficheiro CSV.

---

## Funcionalidades

- **Fetch a URL:** Obter o código HTML através da biblioteca requests.
- **Parsing do conteúdo HTML:** Obter os titulos e os links de notícias por meio da biblioteca BeatifulSoup. 
- **Export para o arquivo:** Criar o arquivo contendo os titulos e o links das noticias por meio da biblioteca pandas.
- **Arquitetura Modular:** Separação clara de responsabilidades por módulos/ficheiros (`exporter`, `fetcher`, `parser`).
- **Código Limpo (Clean Code):** Tipagem estática  e zero *warnings* em analisadores como o PyCharm.

---

## Tecnologias Utilizadas

- **Linguagem:** [Python 3.10+](https://www.python.org/)
- **Biblioteca HTTP:** [Requests](https://requests.readthedocs.io/)
- **Biblioteca de análise e extracção:** [Beautifulsoup4](Beautiful Soup Documentation — Beautiful Soup 4.4.0 document…)
- **Biblioteca de exportacção:** [Pandas](Beautiful Soup Documentation — Beautiful Soup 4.4.0 document…)


---

## Estrutura do Projeto

```text
Web-Scraper-de-Not-cias-de-IA/
├── main.py          # Ponto de entrada (coordena o fluxo)
├── fetcher.py       # Responsável por descarregar o HTML da web
├── parser.py        # Responsável por extrair títulos e links com BeautifulSoup
├── exporter.py      # Responsável por salvar os dados em CSV com Pandas
├── README.md        # Documentação do projeto
└── noticias_csv  # Ficheiro gerado automaticamente com os resultados
