import configparser
import dotenv
import logging
import os

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, insert
from sqlalchemy.exc import ProgrammingError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy_utils import create_database, drop_database

# allows to read config from separate file
cfg_parser = configparser.ConfigParser()
cfg_parser.read('db.ini')

# loads .env file by default, project specific
dotenv.load_dotenv()

# https://docs.sqlalchemy.org/en/14/core/engines.html#configuring-logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

# https://docs.sqlalchemy.org/en/14/core/engines.html
# https://docs.sqlalchemy.org/en/14/core/engines.html#mysql
# url = 'mysql+pymysql://cinemauser:cinema123!@localhost:3306/cinematic'

# https://docs.python.org/3/library/configparser.html
# url = f'mysql+pymysql://{cfg_parser.get("db", "user")}:{cfg_parser.get("db", "pass")}@' \
#       f'{cfg_parser.get("db", "host")}:{cfg_parser.get("db", "port")}/{cfg_parser.get("db", "db")}'

# https://pypi.org/project/python-dotenv/
url = f'mysql+pymysql://{os.environ.get("CINEMA_USER")}:{os.environ.get("CINEMA_PASS")}@' \
      f'{os.environ.get("CINEMA_HOST")}:{os.environ.get("CINEMA_PORT")}/{os.environ.get("CINEMA_DB")}'

engine = create_engine(url)
# https://docs.sqlalchemy.org/en/14/orm/declarative_tables.html
SQLBase = declarative_base()
# Session = sessionmaker(bind=engine)
# session = Session()
session = sessionmaker(bind=engine)()


class Directors(SQLBase):
    __tablename__ = 'directors'

    # director_id INTEGER PRIMARY KEY AUTO_INCREMENT
    director_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    surname = Column(String(20), nullable=False)
    rating = Column(Integer, nullable=False)
    movies = relationship('Movies', back_populates='director')


class Movies(SQLBase):
    __tablename__ = 'movies'

    movie_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)
    category = Column(String(10), nullable=False)
    director_id = Column(Integer, ForeignKey('directors.director_id'), nullable=False)
    rating = Column(Integer, nullable=False)
    director = relationship('Directors', back_populates='movies')

    # https://rszalski.github.io/magicmethods/#representations
    def __repr__(self):
        return f'({self.movie_id}, \'{self.title}\', {self.year}, \'{self.category}\', ' \
               f'{self.director_id}, {self.rating})'


def create_environment():
    # https://sqlalchemy-utils.readthedocs.io/en/latest/database_helpers.html
    try:
        create_database(url)
    except ProgrammingError:
        drop_database(url)
        create_database(url)

    SQLBase.metadata.create_all(engine)

    directors = [{'name': 'Frank', 'surname': 'Darabont', 'rating': 7},
                 {'name': 'Francis Ford', 'surname': 'Coppola', 'rating': 8},
                 {'name': 'Quentin', 'surname': 'Tarantino', 'rating': 10},
                 {'name': 'Christopher', 'surname': 'Nolan', 'rating': 9},
                 {'name': 'David', 'surname': 'Fincher', 'rating': 7}]

    movies = [{'title': 'The Shawshank Redemption', 'year': 1994, 'category': 'Drama', 'director_id': 1, 'rating': 8},
              {'title': 'The Green Mile', 'year': 1999, 'category': 'Drama', 'director_id': 1, 'rating': 6},
              {'title': 'The Godfather', 'year': 1972, 'category': 'Crime', 'director_id': 2, 'rating': 7},
              {'title': 'The Godfather III', 'year': 1990, 'category': 'Crime', 'director_id': 2, 'rating': 6},
              {'title': 'Pulp Fiction', 'year': 1994, 'category': 'Crime', 'director_id': 3, 'rating': 9},
              {'title': 'Inglourious Basterds', 'year': 2009, 'category': 'War', 'director_id': 3, 'rating': 8},
              {'title': 'The Dark Knight', 'year': 2008, 'category': 'Action', 'director_id': 4, 'rating': 9},
              {'title': 'Interstellar', 'year': 2014, 'category': 'Sci-fi', 'director_id': 4, 'rating': 8},
              {'title': 'The Prestige', 'year': 2006, 'category': 'Drama', 'director_id': 4, 'rating': 10},
              {'title': 'Fight Club', 'year': 1999, 'category': 'Drama', 'director_id': 5, 'rating': 7},
              {'title': 'Zodiac', 'year': 2007, 'category': 'Crime', 'director_id': 5, 'rating': 5},
              {'title': 'Seven', 'year': 1995, 'category': 'Drama', 'director_id': 5, 'rating': 8},
              {'title': 'Alien 3', 'year': 1992, 'category': 'Horror', 'director_id': 5, 'rating': 5}]

    # CORE
    with engine.connect() as connection:
        connection.execute(insert(Directors), directors)

    # ORM
    # Movies(**movie) == Movies(title='The Green Mile', year=1994, ..)
    session.add_all((Movies(**movie) for movie in movies))
    session.commit()


if __name__ == '__main__':
    create_environment()
