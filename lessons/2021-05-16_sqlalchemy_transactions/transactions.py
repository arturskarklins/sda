"""
Perform transactions to remove a director from the database using his name. Test it for the name 'Frank'.
"""

from cinematic import Movies, Directors, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, delete

# search pattern
name = 'Frank'

# https://docs.sqlalchemy.org/en/14/orm/session_transaction.html
session = sessionmaker(bind=engine, autocommit=True)()

with session.begin():
    sub_query = session\
        .query(Directors.director_id)\
        .filter(Directors.name == name)\
        .subquery()

    print(session
          .query(Movies)
          .filter(Movies.director_id.in_(sub_query))
          .delete(synchronize_session='fetch'))

    # savepoints, https://docs.sqlalchemy.org/en/14/orm/session_transaction.html#using-savepoint
    sp_1 = session.begin_nested()
    print(session
          .query(Directors)
          .filter(Directors.name == name)
          .delete())
    sp_1.rollback()


# with engine.begin() as connection:
#     sub_query = select([Directors.director_id])\
#         .where(Directors.name == name)
#
#     print(connection
#           .execute(delete(Movies)
#                    .where(Movies.director_id.in_(sub_query))
#                    .execution_options(synchronize_session='fetch')))
#
#     print(connection
#           .execute(delete(Directors)
#                    .where(Directors.name == name)))
