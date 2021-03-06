"""
List the names of all directors whose ranking is greater than or equal to 6 and whose first name starts with 'D' or
ends with 'n'. Use select () and query ().
"""

from main import engine, Directors, session
from sqlalchemy import select, and_, or_

with engine.connect() as connection:
    print(connection
          .execute(select([Directors.name, Directors.rating])
                   .where(and_(Directors.rating >= 6, or_(Directors.name.like('D%'), Directors.name.like('%n')))))
          .fetchall())

print(session
      .query(Directors.name, Directors.rating)
      .filter(and_(Directors.rating >= 6, or_(Directors.name.like('D%'), Directors.name.like('%n'))))
      .all())
