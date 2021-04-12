"""
Perform transactions to remove a director from the database using his name. Test it for the name 'Frank'.
"""

from main import Directors, Movies, engine
from sqlalchemy.orm import sessionmaker

session = sessionmaker(bind=engine, autocommit=True)()

with session.begin():
    subquery = session\
        .query(Directors.director_id)\
        .filter(Directors.name == 'Frank')\
        .subquery()

    print(session
          .query(Movies)
          .filter(Movies.director_id.in_(subquery))
          .delete(synchronize_session='fetch'))

    print(session
          .query(Directors)
          .filter(Directors.name == 'Frank')
          .delete())
