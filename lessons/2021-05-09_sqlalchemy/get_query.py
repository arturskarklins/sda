"""
Show the query
"""

from cinematic import Movies, Directors, session
from sqlalchemy import select, join, func

print(select([func.count(Movies.movie_id), Directors.name, Directors.surname, func.avg(Movies.rating)])
      .select_from(join(Directors, Movies))
      .group_by(Directors.director_id))

print()

print(session
      .query(func.count(Movies.movie_id), Directors.name, Directors.surname, func.avg(Movies.rating))
      .join(Movies)
      .group_by(Directors.director_id)
      )
