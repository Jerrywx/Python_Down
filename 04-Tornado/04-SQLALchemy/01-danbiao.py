# 创建数据库表

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker

print(sqlalchemy.__version__)


# 链接数据库
engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/test', echo=True)


# ===================== 0、创建数据库表
# 生成一个 SQLORM 基类
Base = declarative_base()

class Users(Base):
    # 设置表名
    __tablename__ = 'users'

    def __init__(self, name, fulname, password):
        self.name = name
        self.fullname = fulname
        self.password = password

    def __str__(self):
        return "ID:" + str(self.id) + "\t" \
               + "name:" + self.name + "    full:" \
               + self.fullname + "\t" + self.password

    def __repr__(self):
        return self.fullname

    # 设置ID 类型、主键
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    fullname = Column(String(32))
    password = Column(String(32))

# 创建所有表结构
# Base.metadata.create_all(engine)
# 删除数据库所有表
# Base.metadata.drop_all(engine)

# ===================== 1、插入数据
MySession = sessionmaker(bind=engine)
session = MySession()

# --------- 插入数据 1
# 创建用户
# user = Users("wx", "wxiao1", "123546")
# session.add(user)

# --------- 插入数据 2
# session.add_all([
#     Users("wx", "wxiao2", "123546"),
#     Users("wx", "wxiao3", "123546"),
#     Users("wx", "wxiao4", "123546"),
# ])

# --------- 提交插入数据操作
# session.commit()


# ===================== 2、查询数据
# 1. 查询所有数据
# print(session.query(Users).all())

# 2. 遍历查询结果
# for user in session.query(Users).all():
#     print(user)

# 3. 查询结果排序
# for user in session.query(Users).order_by(Users.fullname):
#     print(user)

# 4. 查询匹配 1
# for user in session.query(Users).filter(Users.fullname.in_(["wxiao", "wxiao2", "wxiao4"])):
#     print(user)

# 5. 查询匹配 2
# for user in session.query(Users).filter(Users.fullname.in_(["wxiao", "wxiao2", "wxiao4"])):
#     print(user)

# 6. 查询匹配 3
print("-------")
print(session.query(Users).filter(Users.fullname=='wxiao1').count())
print("-------")










# 常见ORM基类
# Base = declarative_base()
#
#
# # 创建学生表
# class Student(Base):
#     __tablename__ = 'student'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(32))
#     password = Column(String(64))
#     mobile = Column(Integer)
#     gradesclasses = Column(String(64))
#
#
# # 创建老师表
# class Teacher(Base):
#     __tablename__ = 'teacher'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(32))
#     password = Column(String(64))
#     mobile = Column(Integer)
#
#
# if __name__ == "__main__":
#     Base.metadata.create_all(engine)