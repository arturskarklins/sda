"""
For the previous text query, bind the parameters using bind_params (), specifying the required types.
"""

from main import engine, session
from sqlalchemy import text, bindparam, Integer

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

params = {
    'start_year': 1995,
    'end_year': 2007
}

with engine.connect() as connection:
    print(connection.execute(query, params).fetchall())

print(session
      .query('count_1', 'name', 'surname', 'avg_1')
      .from_statement(query)
      .params(params)
      .all())