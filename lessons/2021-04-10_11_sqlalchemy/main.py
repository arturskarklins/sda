import logging

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, insert
from sqlalchemy.exc import ProgrammingError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
# needed for DB level management
from sqlalchemy_utils import create_database, drop_database

# create logger for detailed info behind the sqlalchemy processes and queries ran
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

# https://docs.sqlalchemy.org/en/14/core/engines.html
url = 'mysql+pymysql://cinemadb:cinema123!@localhost:3306/cinematic'
engine = create_engine(url)

# base class for table objects
SQLBase = declarative_base()

# session object
session = sessionmaker(bind=engine)()


# definition of directors table
class Directors(SQLBase):
    # !important, defines the table name
    __tablename__ = 'directors'

    # https://docs.sqlalchemy.org/en/13/core/metadata.html
    # https://docs.sqlalchemy.org/en/13/core/metadata.html#sqlalchemy.schema.Column
    director_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
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

    # repr method to show data content not object
    def __repr__(self):
        return f'({self.movie_id}, \'{self.title}\', {self.year}, \'{self.category}\', {self.director_id}, {self.rating})'


def create_environment():
    # create database
    try:
        create_database(url)
    except ProgrammingError:
        drop_database(url)
        create_database(url)

    # creates the tables with columns
    # https://docs.sqlalchemy.org/en/13/core/metadata.html?highlight=metadata%20create_all#sqlalchemy.schema.MetaData.create_all
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

    # insert data with engine/connection object
    with engine.connect() as connection:
        connection.execute(insert(Directors), directors)

    # insert data with session object
    session.add_all((Movies(**movie) for movie in movies))
    # !important, automcommit is off by default, commit need to be invoked manually
    session.commit()


if __name__ == '__main__':
    create_environment()
