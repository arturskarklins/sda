""" Task 7:
List the categories of all movies and their rankings, for the films that were produced
between 2000 and 2010 and had rankings greater than 7, also, sort them by their ranking.
Use select () and query ().
"""

from cinematic import engine, Movies, session
from sqlalchemy import select, and_, between

with engine.connect() as connection:
    print(connection
          .execute(select([Movies.title, Movies.category, Movies.rating])
                   .where(and_(Movies.rating > 7, between(Movies.year, 2000, 2010)))
                   .order_by(Movies.rating.desc()))
          .fetchall())

print(session
      .query(Movies.title, Movies.category, Movies.rating)
      .filter(and_(Movies.rating > 7, between(Movies.year, 2000, 2010)))
      .order_by(Movies.rating.desc())
      .all())
