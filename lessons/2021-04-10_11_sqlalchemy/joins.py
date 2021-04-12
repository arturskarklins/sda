"""
List the names and surnames of all directors who made their films between 2011 and 2014 and whose films were rated
lower than 9. Use select () and query ().
"""

from main import Directors, Movies, engine, session
from sqlalchemy import select, and_, between, join

with engine.connect() as connection:
    print(connection
          .execute(select([Directors.name, Directors.surname, Movies.title])
                   .select_from(join(Directors, Movies), )
                   .where(and_(between(Movies.year, 2011, 2014), Movies.rating < 9)))
          .fetchall())

print(session
      .query(Directors.name, Directors.surname, Movies.title)
      .join(Movies)
      .filter(and_(between(Movies.year, 2011, 2014), Movies.rating < 9))
      .all())
