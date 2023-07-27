# IMDb Movie Scraper

### Topics

- [Description](#description)
- [Features](#features)
- [How to use](#how-to-use)
- [Settings](#settings)
- [Used Technologies](#used-technologies)
- [Contribution](#contribution)
- [Developers](#developers)

## Description

<p align="justify">The IMDb Movie Scraper is a Python web scraping project that extracts details of popular movies from the IMDb website (https://www.imdb.com/) and stores them in a CSV file. This project uses popular libraries such as requests, beautifulsoup4, and concurrent.futures to perform HTTP requests, parse HTML, extract data, and execute the scraping process concurrently using threads.</p>

## Features

✓ `Funcionalidade 1:` Extrai detalhes de filmes populares do IMDb, incluindo nome do filme, data de lançamento, classificação IMDb e elenco.

✓ `Funcionalidade 2:` Armazena os detalhes extraídos em um arquivo CSV para posterior análise ou uso em outras aplicações.

✓ `Funcionalidade 3:` Utiliza threads para realizar o processo de scraping de forma concorrente, o que pode melhorar a velocidade de execução em relação a scraping sequencial.

## How to use

#### 1. Ambiente virtual padrão:

1-1. Clone o repositório para o seu ambiente local:

```
git clone https://github.com/jose-uchoa/imdb-movie-scraper.git
```

1-2. Instale as dependências do projeto. Recomenda-se o uso de um ambiente virtual para evitar conflitos de dependências:

```
cd imdb-movie-scraper
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

1-3. Execute o script imdb_scraper.py para iniciar o processo de scraping:

```
python imdb_scraper.py
```

#### 2. Poetry:

2-1. Clone o repositório para o seu ambiente local:

```
git clone https://github.com/jose-uchoa/imdb-movie-scraper.git
```

2-2. Instale as dependências do projeto, lembrando que você precisa ter o Poetry instalado:

```
cd imdb-movie-scraper
poetry install --no-root
poetry run python imdb_scraper.py
```

<br>
O script irá extrair os detalhes de filmes populares do IMDb e armazená-los em um arquivo CSV chamado movies.csv no mesmo diretório do script.
Após a conclusão da execução, você pode abrir o arquivo movies.csv para visualizar os detalhes dos filmes extraídos.

## Settings

<p align="justify">Você pode ajustar o número máximo de threads a serem usadas para execução concorrente editando a variável MAX_THREADS no início do script imdb_scraper.py. Recomenda-se ajustar esse valor de acordo com a capacidade de processamento do seu sistema.</p>

## Used Technologies

✓ `Linguagem de programação:` Python

✓ `Frameworks:` requests e beautifulsoup4

## Contribution

<p align="justify">Este projeto foi desenvolvido como um exemplo simples de web scraping em Python e pode ser utilizado como base para projetos mais complexos ou para fins educacionais. Se você deseja contribuir com melhorias ou correções, sinta-se à vontade para abrir issues ou pull requests neste repositório.

Espero que este projeto seja útil para você!</p>

## Developers

| [<img src="https://avatars.githubusercontent.com/jose-uchoa" width=115><br><sub>José Uchôa</sub>](https://github.com/jose-uchoa) |
| :------------------------------------------------------------------------------------------------------------------------------: |
