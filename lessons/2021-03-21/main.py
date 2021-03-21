# https://pypi.org/project/PyMySQL/
# https://www.python.org/dev/peps/pep-0249/

# need to pip install `pymysql` and `cryptography`
import pymysql

# create connection to db
with pymysql.connect(
    host='localhost',
    user='cinemadb',
    password='cinema123!',
    database='cinematic'
    # cursorclass=pymysql.cursors.DictCursor
    # autocommit=True
) as connection:
    # create cursor, object to modify the db
    with connection.cursor() as cursor:
        drop_db = 'DROP DATABASE IF EXISTS cinematic;'
        create_db = 'CREATE DATABASE cinematic;'
        # cursor.execute(drop_db)
        # cursor.execute(create_db)

        # define directors table as per task
        directors_table = """
            CREATE TABLE directors(
                director_id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
                name VARCHAR(20) NOT NULL,
                surname VARCHAR(20) NOT NULL,
                rating INTEGER NOT NULL
            );
        """

        # define movies table as per task
        # check UNSIGNED SQL data type, could be used for year
        movies_table = """
            CREATE TABLE movies(
                movie_id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
                title VARCHAR(50) NOT NULL,
                year INTEGER NOT NULL,
                category VARCHAR(30) NOT NULL,
                director_id INTEGER NOT NULL,
                rating INTEGER NOT NULL,
                FOREIGN KEY(director_id) REFERENCES directors(director_id)
            );
        """
        # cursor.execute(directors_table)
        # cursor.execute(movies_table)

        # data for directors as list of tuples
        directors = [('Frank', 'Darabont', 7),
                     ('Francis Ford', 'Coppola', 8),
                     ('Quentin', 'Tarantino', 10),
                     ('Christopher', 'Nolan', 9),
                     ('David', 'Fincher', 7)]

        # data for movies as list of tuples
        movies = [('The Shawshank Redemption', 1994, 'Drama', 1, 8),
                  ('The Green Mile', 1999, 'Drama', 1, 6),
                  ('The Godfather', 1972, 'Crime', 2, 7),
                  ('The Godfather III', 1990, 'Crime', 2, 6),
                  ('Pulp Fiction', 1994, 'Crime', 3, 9),
                  ('Inglourious Basterds', 2009, 'War', 3, 8),
                  ('The Dark Knight', 2008, 'Action', 4, 9),
                  ('Interstellar', 2014, 'Sci-fi', 4, 8),
                  ('The Prestige', 2006, 'Drama', 4, 10),
                  ('Fight Club', 1999, 'Drama', 5, 7),
                  ('Zodiac', 2007, 'Crime', 5, 5),
                  ('Seven', 1995, 'Drama', 5, 8),
                  ('Alien 3', 1992, 'Horror', 5, 5)]

        # insert queries for
        insert_directors = """
            INSERT INTO directors (name, surname, rating)
            VALUES (%s, %s, %s)
        """
        insert_movies = """
            INSERT INTO movies (title, year, category, director_id, rating)
            VALUES (%s, %s, %s, %s, %s)
        """

        # for director in directors:
        #     cursor.execute(insert_directors, director)
        #
        # #  cursor.executemany(insert_movies, movies)
        # for movie in movies:
        #     cursor.execute(insert_movies, movie)

        # select all data based on movies + directors
        select_query = """
            SELECT * FROM movies
            JOIN directors USING(director_id)
        """  # JOIN directors ON movies.director_id = directors.director_id
        cursor.execute(select_query)
        # fetch data from cursor: fetchall(), fetchone(), fetchmany()
        for entry in cursor.fetchall():
            print(entry)

        # drop both tables
        # note! mind the order due foreign key
        # cursor.execute('DROP TABLE movies;')
        # cursor.execute('DROP TABLE directors;')

        # commit changes done to db, like INSERT queries
        # connection.commit()
