# https://pymysql.readthedocs.io/en/latest/
# https://www.python.org/dev/peps/pep-0249/
import pymysql


# drop and re-creates DB with clean environment
def db_create(db_name):
    with pymysql.connect(host='localhost', user='cinemauser', password='cinema123!') as db_connection:
        with db_connection.cursor() as db_cursor:
            db_cursor.execute(f'DROP DATABASE IF EXISTS {db_name}')
            db_cursor.execute(f'CREATE DATABASE {db_name}')


# creates directors table and inserts data
def create_directors(directors_cursor):
    directors_cursor.execute("""
        CREATE TABLE directors(
            director_id INTEGER PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(20) NOT NULL,
            surname VARCHAR(20) NOT NULL,
            rating INTEGER NOT NULL
        )
    """)

    directors = [('Frank', 'Darabont', 7), ('Francis Ford', 'Coppola', 8), ('Quentin', 'Tarantino', 10),
                 ('Christopher', 'Nolan', 9), ('David', 'Fincher', 7)]

    query = """
        INSERT INTO directors (name, surname, rating) VALUES (%s, %s, %s)
    """

    directors_cursor.executemany(query, directors)


# creates movies table and inserts data
def create_movies(movies_cursor):
    movies_cursor.execute("""
        CREATE TABLE movies(
            movie_id INTEGER PRIMARY KEY AUTO_INCREMENT,
            title VARCHAR(50) NOT NULL,
            year INTEGER NOT NULL,
            category VARCHAR(10) NOT NULL,
            director_id INTEGER NOT NULL,
            rating INTEGER NOT NULL,
            FOREIGN KEY(director_id) REFERENCES directors(director_id)
        )
    """)

    movies = [('The Shawshank Redemption', 1994, 'Drama', 1, 8), ('The Green Mile', 1999, 'Drama', 1, 6),
              ('The Godfather', 1972, 'Crime', 2, 7), ('The Godfather III', 1990, 'Crime', 2, 6),
              ('Pulp Fiction', 1994, 'Crime', 3, 9), ('Inglourious Basterds', 2009, 'War', 3, 8),
              ('The Dark Knight', 2008, 'Action', 4, 9), ('Interstellar', 2014, 'Sci-fi', 4, 8),
              ('The Prestige', 2006, 'Drama', 4, 10), ('Fight Club', 1999, 'Drama', 5, 7),
              ('Zodiac', 2007, 'Crime', 5, 5), ('Seven', 1995, 'Drama', 5, 8), ('Alien 3', 1992, 'Horror', 5, 5)]

    query = """
        INSERT INTO movies (title, year, category, director_id, rating)
        VALUES (%s, %s, %s, %s, %s)
    """

    movies_cursor.executemany(query, movies)


database = 'cinematic'
db_create(database)

# creates connection object with relevant configuration
with pymysql.connect(host='localhost', user='cinemauser', password='cinema123!', database=database) as connection:
    # cursor object for managing DB and tables
    with connection.cursor() as cursor:
        create_directors(cursor)
        create_movies(cursor)
        # for insert, remember autocommit is False, so commit or use autocommit in connection definition
        connection.commit()
