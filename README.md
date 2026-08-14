# Web Scrapper

O objetivo é criar um script Python modular para recolher automaticamente os títulos e os respetivos links das noticias mais recents sobre Inteligência Artificial (de um site como o TechCrunch) e exportar esses dados limpos para um ficheiro CSV.











































Web-Scraper-de-Not-cias-de-IA/
├── main.py          # Ponto de entrada (coordena o fluxo)
├── fetcher.py       # Responsável por descarregar o HTML da web
├── parser.py        # Responsável por extrair títulos e links com BeautifulSoup
├── exporter.py      # Responsável por salvar os dados em CSV com Pandas
├── README.md        # Documentação do projeto
└── noticias_ia.csv  # Ficheiro gerado automaticamente com os resultados
