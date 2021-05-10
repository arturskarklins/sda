"""
Increase the rating by 1 for all the directors whose films
were made prior to 2001 and whose film titles start with 'T'. Use a subquery.
"""

from cinematic import engine, Movies, Directors, session
from sqlalchemy import select, and_, update

# https://docs.sqlalchemy.org/en/14/orm/query.html?highlight=update#sqlalchemy.orm.Query.update
# https://docs.sqlalchemy.org/en/14/core/dml.html?highlight=update#sqlalchemy.sql.expression.update

# sub_query = (session
#              .query(Movies.director_id)
#              .filter(and_(Movies.year < 2001, Movies.title.like('T%')))
#              .subquery())
#
# print(session
#       .query(Directors)
#       .filter(Directors.director_id.in_(sub_query))
#       .update({'rating': Directors.rating + 1}, synchronize_session='fetch'))
#
# session.commit()

sub_query_core = (select([Movies.director_id])
                  .where(and_(Movies.year < 2001, Movies.title.like('T%'))))

with engine.connect() as connection:
    print(connection
          .execute(update(Directors)
                   .where(Directors.director_id.in_(sub_query_core))
                   .values(rating=(Directors.rating + 1))
                   .execution_options(synchronize_session='fetch')))
