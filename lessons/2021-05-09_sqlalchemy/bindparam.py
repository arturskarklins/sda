from cinematic import engine, Movies
from sqlalchemy import select, between, bindparam, text

# https://docs.sqlalchemy.org/en/14/core/sqlelement.html?highlight=bindparam#sqlalchemy.sql.expression.bindparam

params = {
    'start_year': 1995,
    'end_year': 2005
}

# with engine.connect() as connection:
#     print(connection
#           .execute(select([Movies])
#                    .where(between(Movies.year, params.get('start_year'), params.get('end_year'))))
#           .fetchall())
#
# with engine.connect() as connection:
#     print(connection
#           .execute(select([Movies])
#                    .where(between(Movies.year, bindparam('start_year'), bindparam('end_year'))), params)
#           .fetchall())

rating = '7 AND year = 1999'

query = text(f"""
    SELECT * FROM movies
    WHERE rating = :rating
""")

with engine.connect() as connection:
    print(connection
          .execute(query, rating=rating)
          .fetchall())
