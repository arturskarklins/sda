"""
List all movies for the Drama category.
Use select () and query ().
"""

from main import engine, Movies, session
from sqlalchemy import select

# https://docs.sqlalchemy.org/en/13/orm/query.html

with engine.connect() as connection:
    print(connection
          .execute(select([Movies])
                   .where(Movies.category == 'Drama'))
          .fetchall())

print(session
      .query(Movies)
      .filter(Movies.category == 'Drama')
      .all())
