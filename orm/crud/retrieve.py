from orm.basic.session import session
from orm.crud.create_table import *

print(session.query(User).filter_by(username = 'James Yoder').first().password)
print(session.query(User).filter(User.password =='key',User.username == 'James Yoder').first())

print(session.query(User).all())