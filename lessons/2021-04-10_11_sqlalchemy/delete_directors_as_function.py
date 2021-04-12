"""
Wrap the transaction created in the previous task in a function that will take the first and last name as a kwarg.
Based on the given name or surname, the function will decide which query to use to search for a director and then
delete him/her. The search query should be in the text form ().
"""

from main import Directors, Movies, engine
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker


def delete_director_by_name(**kwargs):
    query = None
    if kwargs.get('name') is not None:
        query = text('SELECT directors.director_id FROM directors WHERE directors.name = :name')
    elif kwargs.get('surname') is not None:
        query = text('SELECT directors.director_id FROM directors WHERE directors.surname = :surname')
    else:
        print('Requirement not met!')
        exit(1)

    session = sessionmaker(bind=engine, autocommit=True)()
    with session.begin():
        director_id = session\
            .query(Directors.director_id)\
            .from_statement(query)\
            .params(kwargs)\
            .first()

        if director_id is not None:
            print(session
                  .query(Movies)
                  .filter(Movies.director_id == director_id[0])
                  .delete())

            print(session
                  .query(Directors)
                  .filter(Directors.director_id == director_id[0])
                  .delete())
        else:
            print('Director not found!')


delete_director_by_name(surname='Frank')
