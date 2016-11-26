# encoding:utf-8
from peewee import *
from datetime import date

db = SqliteDatabase('people.db')  # 新建数据库 db（默认当前路径）
# db = MySQLDatabase("...", host="", user="",passwd="")连接MySQL


class Person(Model):  # 表格模型 Person：这是一个Model的概念
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db  # 所用数据库为db


class Pet(Model):
    owner = ForeignKeyField(Person, related_name='pets')  # 外连接的声明(和Person关联)
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db

db.connect()  # 连接数据库db


'''
classmethoddrop_table([fail_silently=False])
    Parameters:     fail_silently –如果是True，在删除之前会检查该表是否存在.

classmethod table_exists()
    Return type:    返回该数据库是否存在，返回bool值
'''
# 此处用try语句无法完成表的创建
if Person.table_exists():
    pass
else:  # 在db中建表Person
    db.create_table(Person)      # 注意参数：直接写表名
    # db.create_tables([Person]) # 注意参数：元组、列表皆可，不能是字符串

    # Storing Data添加数据
    uncle_bob = Person(name='Bob', birthday=date(
        1967, 1, 28), is_relative=True)
    uncle_bob.save()

    grandma = Person(name='Grandma', birthday=date(
        1935, 3, 1), is_relative=True)
    # 有create，可以省略save()，没有create，必须有save()
    herb = Person.create(name='Herb', birthday=date(
        1950, 5, 1), is_relative=False)

    grandma.name = 'Marry'
    grandma.save()

grandma = Person.select().where(Person.name == 'Marry').get()  # 查询名字为Marry的person
print 1, grandma, type(grandma)  # 类型为<class '__main__.Person'>
grandma = Person.select().where(Person.name == 'Marry')
print 2, grandma, type(grandma)  # 类型为<class 'peewee.SelectQuery'>


for person in Person.select():  # 列出Person表中所有的person
    print 3, person.name, person.is_relative, '\t',
print


if Pet.table_exists():
    pass
else:
    db.create_table(Pet)
    bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
    herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
    herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
    herb_mittens_jr = Pet.create(
        owner=herb, name='Mittens Jr', animal_type='cat')

    herb_mittens.delete_instance()  # delete Data
    # return the value of delete_instance() is the number of rows removed form
    # the database

    herb_fido.owner = uncle_bob  # Modify Data
    herb_fido.save()
    bob_fido = herb_fido

# 查询Pet表中animal_type为cat的所有pet
query = Pet.select(Pet, Person).join(Person).where(
    Pet.animal_type == 'cat')
for pet in query:
    print 4, pet.name, pet.owner.name,
print

for pet in Pet.select().join(Person).where(Person.name == 'Bob'):  # 查询Pet表中主人名为Bob的所有pet
    print 5, pet.name,
print


try:  # 第一次运行时走的是try路线，以后因为没有创表，会略过try，走except
    for pet in Pet.select().where(Pet.owner == uncle_bob):  # 查询Pet表中person为uncle_bob的所有pet
        print 6, pet.name,
    print
    for pet in Pet.select().where(Pet.owner == uncle_bob).order_by(Pet.name):  # 查询Pet表中person为uncle_bob结果按pet名排列
        print 7, pet.name,
except:
    pass
    print
print


for person in Person.select().order_by(Person.birthday.desc()):  # 将Person表中的person按生日降序查询
    print 8, person.name, person.birthday,
print

for person in Person.select():  # 查询Person表中person所拥有的pet数量及名字和类型
    print 9, person.name, person.pets.count(), 'pets',
    for pet in person.pets:
        print '\t', pet.name, pet.animal_type,
print


# 查询Person表中生日小于1940或大于1960的person
d1940 = date(1940, 1, 1)
d1960 = date(1960, 1, 1)
query = Person.select().where((Person.birthday < d1940) |
                              (Person.birthday > d1960))  # 注意条件句写法
for person in query:
    print 10, person.name, person.birthday, '\t',
print

# 查询Person表中生日在1940和1960之间的person
query = Person.select().where((Person.birthday > d1940) & (Person.birthday < d1960))
for person in query:
    print 11, person.name, person.birthday, '\t',
print

# 按照expression查询person名开头为小写或大写 b 的person
expression = (fn.Lower(fn.Substr(Person.name, 1, 1)) == 'b')
for person in Person.select().where(expression):
    print 12, person.name, '\t',
print
'''
#Person, Pet—>Update操作
q=User.update(active=False).where(User.registration_expired==True)
q.execute()

#Person, Pet—>Insert操作
q=User.insert(username='admin',active=True,registration_expired=False)
q.execute()

#Person, Pet—>Delete操作
q=User.delete().where(User.active==False)
q.execute()
'''
# 关闭数据库
db.close()
