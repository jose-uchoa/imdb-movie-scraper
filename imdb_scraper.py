import csv
import time
import random
import requests
import concurrent.futures

from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}

# Número máximo de threads a serem usadas para execução concorrente
MAX_THREADS = 10


def extract_movie_details(movie_link):
    # Adiciona um pequeno atraso entre as requisições
    time.sleep(random.uniform(0, 0.2))

    # Encontra a tabela de dados dos filmes na página
    table_data = movie_link.find("tbody", attrs={"class": "lister-list"})
    # Encontra todas as linhas da tabela
    table_rows = table_data.find_all("tr")

    # Encontra a tabela de dados dos filmes na página de filmes populares
    movies_table = movie_link.find(
        "table", attrs={"data-caller-name": "chart-moviemeter"}
    ).find("tbody")
    # Encontra todas as linhas da tabela de filmes populares
    movies_table_rows = movies_table.find_all("tr")

    # Extrai os links dos filmes
    movie_links = [
        "https://imdb.com" + movie.find("a")["href"] for movie in movies_table_rows
    ]

    # Caracteres a serem removidos de algumas informações
    remove_chars = "()"

    # Loop através das linhas da tabela de dados dos filmes
    for data in table_rows:
        # Extrai o título do filme
        movie_titles = data.find("td", attrs={"class": "titleColumn"})
        movie_name = movie_titles.find("a").text

        # Extrai a data de lançamento do filme e remove caracteres indesejados
        movie_date_with_chars = movie_titles.find(
            "span", attrs={"class": "secondaryInfo"}
        ).text[0]
        movie_date = "".join(
            (filter(lambda char: char not in remove_chars, movie_date_with_chars))
        )
        if movie_date == "":
            movie_date = "Without Date"

        # Extrai a classificação IMDb do filme
        movie_rating = data.find("td", attrs={"class": "ratingColumn imdbRating"}).text[
            1:4
        ]
        if movie_rating == "":
            movie_rating = "Without IMDb Rating"

        # Extrai o elenco do filme
        movie_cast = movie_titles.find("a").get("title")

        # Escreve as informações do filme em um arquivo CSV
        with open("movies.csv", mode="a") as file:
            movie_writer = csv.writer(
                file, delimiter=",", lineterminator="\r", quoting=csv.QUOTE_MINIMAL
            )
            movie_writer.writerow(
                [movie_name, movie_date, movie_rating, movie_cast, movie_links[0]]
            )


def extract_movies(movie_links):
    # Executa a função extract_movie_details de forma concorrente para cada link de filme
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        executor.map(extract_movie_details, movie_links)


def main():
    start_time = time.time()

    # Faz uma requisição GET para a página de filmes populares
    popular_movies_url = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"
    response = requests.get(popular_movies_url, headers=headers)

    # Faz o parse do conteúdo HTML da resposta
    soup = BeautifulSoup(response.content, "html.parser")

    # Escreve os cabeçalhos das colunas no arquivo CSV
    with open("movies.csv", mode="w") as file:
        movie_writer = csv.writer(
            file, delimiter=",", lineterminator="\r", quoting=csv.QUOTE_MINIMAL
        )
        movie_writer.writerow(
            ["movie_name", "movie_date", "movie_rating", "movie_cast", "movie_link"]
        )

    # Chama a função extract_movies para extrair os detalhes dos filmes
    extract_movies(soup)

    end_time = time.time()

    # Imprime o tempo total de execução do programa
    print("Total time taken: ", end_time - start_time)


if __name__ == "__main__":
    main()
