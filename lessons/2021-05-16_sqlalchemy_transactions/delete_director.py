"""
Wrap the transaction created in the previous task in a function that will take the first and
last name as a kwarg. Based on the given name or surname, the function will decide which query
to use to search for a director and then delete him/her. The search query should be in the text
form ().
"""

# https://docs.python.org/3/library/argparse.html
# allows us to define input arguments and help
import argparse

from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from cinematic import Movies, Directors, engine

# define the argparser, with description
ARG_PARSER = argparse.ArgumentParser(
    description="Deletes directors from db"
)

# create 2 arguments name and surname
ARG_PARSER.add_argument('-n', '--name', dest='name', help='handles directors name')
ARG_PARSER.add_argument('-s', '--surname', dest='surname', help='handles directors surname')
# parse all arguments from input
ARGS = ARG_PARSER.parse_args()


def delete_director(**kwargs):
    """ Deletes director """
    if kwargs.get('name') is not None:  # 'name' in kwargs:
        query = text('SELECT * FROM directors WHERE name = :name')
    elif kwargs.get('surname') is not None:
        query = text('SELECT * FROM directors WHERE surname = :surname')
    else:
        print('No valid arguments parsed')
        return

    # important, use autocommit=True
    session = sessionmaker(bind=engine, autocommit=True)()

    with session.begin():
        # select first found director, remember value is tuple with one elem: tuple(elem,)
        director_id = session\
                    .query(Directors.director_id)\
                    .from_statement(query)\
                    .params(kwargs)\
                    .first()

        try:
            # return deleted movies amount
            print('movies:', session
                  .query(Movies)
                  .filter(Movies.director_id == director_id[0])
                  .delete())

            # return deleted director amount
            print('directors', session
                  .query(Directors)
                  .filter(Directors.director_id == director_id[0])
                  .delete())
        # if no director found, catch exception, return human readable message
        except TypeError:
            print(f'No director found for {kwargs}')


# call function with two arguments
delete_director(name=ARGS.name, surname=ARGS.surname)
