"""
List the names and surnames of all directors who made their films between 2011 and 2014
and whose films were rated lower than 9. Use select () and query ().
"""

# https://docs.sqlalchemy.org/en/14/orm/query.html?highlight=join#sqlalchemy.orm.join

from cinematic import engine, Movies, Directors, session
from sqlalchemy import select, and_, between, join, outerjoin

with engine.connect() as connection:
    print(connection
          .execute(select([Directors.name, Directors.surname, Movies.title])
                   .select_from(join(Directors, Movies, Directors.rating == Movies.rating))
                   .where(and_(between(Movies.year, 2011, 2014), Movies.rating < 9)))
          .fetchall())

print(session
      .query(Directors.name, Directors.surname, Movies.title)
      .join(Movies, Movies.rating == Directors.rating)
      .filter(and_(between(Movies.year, 2011, 2014), Movies.rating < 9))
      .all())

# outerjoin ORM
# print(session
#       .query(Directors.name, Directors.surname, Movies.title)
#       .outerjoin(Directors, Movies.rating == Directors.rating)
#       .all())

# outerjoin CORE
# with engine.connect() as connection:
#     print(connection
#           .execute(select([Directors.name, Directors.surname, Movies.title])
#                    .select_from(outerjoin(Movies, Directors, Directors.rating == Movies.rating)))
#           .fetchall())
