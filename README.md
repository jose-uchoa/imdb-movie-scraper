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

✓ `Feature 1:` Extracts details of popular movies from IMDb, including the movie name, release date, IMDb rating, and cast.

✓ `Feature 2:` Stores the extracted details in a CSV file for further analysis or use in other applications.

✓ `Feature 3:` Uses threads to perform the scraping process concurrently, which can improve the execution speed compared to sequential scraping.

## How to use

#### 1. Standard Virtual Environment:

- Clone the repository to your local environment:

  ```
  git clone https://github.com/jose-uchoa/imdb-movie-scraper.git
  ```

- Install project dependencies. It is recommended to use a virtual environment to avoid dependency conflicts:

  ```
  cd imdb-movie-scraper
  python -m venv env
  source venv/bin/activate  # No Windows: venv\Scripts\activate
  pip install -r requirements.txt
  ```

- Run the script imdb_scraper.py to start the scraping process:

  ```
  python imdb_scraper.py
  ```

#### 2. Poetry:

- Clone the repository to your local environment:

  ```
  git clone https://github.com/jose-uchoa/imdb-movie-scraper.git
  ```

- Install project dependencies. Note that you need to have Poetry installed:

  ```
  cd imdb-movie-scraper
  poetry install
  poetry run python imdb_scraper.py
  ```

<br>
The script will extract details of popular movies from IMDb and store them in a CSV file named movies.csv in the same directory as the script. After the execution is complete, you can open the movies.csv file to view the extracted movie details.

## Settings

<p align="justify">You can adjust the maximum number of threads to be used for concurrent execution by editing the MAX_THREADS variable at the beginning of the "imdb_scraper.py" script. It is recommended to adjust this value according to your system's processing capacity.</p>

## Used Technologies

✓ `Programming Language:` Python

✓ `Frameworks:` Requests e BeautifulSoup4

## Contribution

<p align="justify">This project was developed as a simple example of web scraping in Python and can be used as a foundation for more complex projects or for educational purposes. If you wish to contribute with improvements or corrections, feel free to open issues or pull requests in this repository.

I hope this project is helpful for you!</p>

## Developers

| [<img src="https://avatars.githubusercontent.com/jose-uchoa" width=115><br><sub>José Uchôa</sub>](https://github.com/jose-uchoa) |
| :------------------------------------------------------------------------------------------------------------------------------: |
