from orm.basic.session import session
from orm.crud.create_table import User, Category, Tag,Article
from faker import Factory
import random

# 创建一个 faker 工厂对象
faker = Factory.create()

faker_users = [User(
    # 使用 faker 生成一个人名
    username=faker.name(),
    # 使用 faker 生成一个单词
    password=faker.word(),
     # 使用 faker 生成一个邮箱
    email=faker.email(),
) for i in range(10)]
# add_all 一次性添加多个对象
session.add_all(faker_users)

# 生成 5 个分类
faker_categories = [Category(name=faker.word()) for i in range(5)]
session.add_all(faker_categories)

# 生成 20 个标签
faker_tags= [Tag(name=faker.word()) for i in range(20)]
session.add_all(faker_tags)

# 生成 100 篇文章
for i in range(100):
    article = Article(
        # sentence() 生成一句话作为标题
        title=faker.sentence(),
        # 文章内容为随机生成的 10-20句话
        content=' '.join(faker.sentences(nb=random.randint(10, 20))),
        # 从生成的用户中随机取一个作为作者
        author=random.choice(faker_users),
        # 从生成的分类中随机取一个作为分类
        category=random.choice(faker_categories)
    )
    # 从生成的标签中随机取 2-5 个作为分类，注意 sample() 函数的用法
    for tag in random.sample(faker_tags, random.randint(2, 5)):
        article.tags.append(tag)
    session.add(article)

session.commit()