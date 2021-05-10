"""
Change the query from the previous task into text using text (). Modify it so that the range of years
in which the directors created movies was a parameter to the query.
"""

from cinematic import engine, session
from sqlalchemy import text, bindparam, Integer

"""
The created query should be marked with the function get_directors_statistics, which will take the following arguments:

a session
years range as two arguments

Test the function you have created.
"""


def get_directors_statistics(session, **params):
    query = text("""
        SELECT count(movies.movie_id) AS count_1, directors.name, directors.surname, avg(movies.rating) AS avg_1 
        FROM directors 
        JOIN movies ON directors.director_id = movies.director_id 
        WHERE movies.year BETWEEN :start_year AND :end_year
        GROUP BY directors.director_id
    """)

    """
    For the previous text query, bind the parameters using bind_params (), specifying the required types.
    """
    query.bindparams(
        bindparam('start_year', Integer),
        bindparam('end_year', Integer)
    )

    # with engine.connect() as connection:
    #     print(connection
    #           .execute(query, params)
    #           .fetchall())

    print(session
          .query('count_1', 'name', 'surname', 'avg_1')
          .from_statement(query)
          .params(params)
          .all())


get_directors_statistics(session, start_year=1995, end_year=2005)
