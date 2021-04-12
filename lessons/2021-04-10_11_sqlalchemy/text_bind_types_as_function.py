"""
The created query should be marked with the function get_directors_statistics, which will take the following arguments:

a session
years range as two arguments
Test the function you have created.
"""

from main import engine
from sqlalchemy import text, bindparam, Integer
from sqlalchemy.orm import sessionmaker


def get_directors_statistics(session, **kwargs):
    query = text("""
        SELECT count(movies.movie_id) AS count_1, directors.name, directors.surname, avg(movies.rating) AS avg_1 
        FROM directors
        JOIN movies ON directors.director_id = movies.director_id 
        WHERE movies.year BETWEEN :start_year AND :end_year 
        GROUP BY directors.director_id
    """)

    query.bindparams(
        bindparam('start_year', type_=Integer),
        bindparam('end_year', type_=Integer)
    )

    print(session
          .query('count_1', 'name', 'surname', 'avg_1')
          .from_statement(query)
          .params(kwargs)
          .all())


get_directors_statistics(sessionmaker(bind=engine)(), start_year=1995, end_year=2005)
