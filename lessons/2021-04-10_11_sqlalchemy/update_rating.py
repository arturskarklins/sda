"""
Increase the rating by 1 for all the directors whose films were made prior to 2001 and whose film
titles start with 'T'. Use a subquery.
"""

from main import Directors, Movies, session
from sqlalchemy import and_

subquery = session\
    .query(Movies.director_id)\
    .filter(and_(Movies.year < 2001, Movies.title.like('T%')))\
    .subquery()

print(session
      .query(Directors.name, Directors.surname)
      .filter(Directors.director_id.in_(subquery))
      .update({'rating': Directors.rating + 1}, synchronize_session='fetch'))

session.commit()
