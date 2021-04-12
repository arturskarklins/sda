from main import Movies, engine
from sqlalchemy import select, and_, bindparam

# https://docs.sqlalchemy.org/en/13/core/sqlelement.html?highlight=bindparam#sqlalchemy.sql.expression.bindparam


# get movie by category
# with older than
def get_movies_by_criteria(**kwargs):
    with engine.connect() as connection:
        print(connection
              .execute(select([Movies])
                       .where(and_(Movies.category == bindparam('category'), Movies.year < bindparam('year'))),
                       kwargs)
              .fetchall())


get_movies_by_criteria(category='Crime', year=1990, title='Terminator')
