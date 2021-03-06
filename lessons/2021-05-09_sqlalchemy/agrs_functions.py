"""
List the total number of films created by each director, their full name, and the average rating for
each director based on their film ratings. Use select () and query ().
"""

from cinematic import engine, Movies, Directors, session
from sqlalchemy import select, join, func

# https://docs.sqlalchemy.org/en/14/core/functions.html

with engine.connect() as connection:
    print(connection
          .execute(select([func.count(Movies.movie_id), Directors.name, Directors.surname, func.avg(Movies.rating)])
                   .select_from(join(Directors, Movies))
                   .group_by(Directors.director_id))
          .fetchall())

print(session
      .query(func.count(Movies.movie_id), Directors.name, Directors.surname, func.avg(Movies.rating))
      .join(Movies)
      .group_by(Directors.director_id)
      .all())
