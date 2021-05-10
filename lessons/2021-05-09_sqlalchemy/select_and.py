""" Task 6:
List the titles of movies from the Crime category that were made after 1994.
Use select () and query ().
"""

from cinematic import engine, Movies, session
from sqlalchemy import select, and_

with engine.connect() as connection:
    print(connection
          .execute(select([Movies.title])
                   .where(and_(Movies.category == 'Crime', Movies.year > 1994)))
          .fetchall())

print(session
      .query(Movies.title)
      .filter(and_(Movies.category == 'Crime', Movies.year > 1994))
      .all())
