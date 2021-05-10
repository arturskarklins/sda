from cinematic import engine, Movies, session
from sqlalchemy import select

# CORE
with engine.connect() as connection:
    print(connection
          .execute(select([Movies])
                   .where(Movies.category == 'Drama'))
          .fetchall())

# ORM
print(session
      .query(Movies)
      .filter(Movies.category == 'Drama')
      .all())
