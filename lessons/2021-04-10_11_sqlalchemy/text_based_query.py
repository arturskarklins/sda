"""
Change the query from the previous task into text using text (). Modify it so that the range of years in which
the directors created movies was a parameter to the query.
"""

from main import engine, session
from sqlalchemy import text

query = text("""
    SELECT count(movies.movie_id) AS count_1, directors.name, directors.surname, avg(movies.rating) AS avg_1 
    FROM directors
    JOIN movies ON directors.director_id = movies.director_id 
    WHERE movies.year BETWEEN :start_year AND :end_year 
    GROUP BY directors.director_id
""")

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
