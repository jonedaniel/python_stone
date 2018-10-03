from orm.basic.session import session
from orm.crud.create_table import *

a = session.query(Article).get(1)
# 更新字段内容
# a.title = 'test update title'
# session.add(a)
# session.commit()

print(a.tags)
# 添加一个标签
# a.tags.append(Tag(name='testUpdate'))
# session.add(a)
# session.commit()
