#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

# 链接数据库
engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/info?charset=utf8', echo=False)

#
Base = declarative_base()



class Son(Base):
    # 表名
    __tablename__ = "son"

    # ID
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 名字
    name = Column(String(32))
    # 年龄
    age = Column(String(3))
    # 父亲
    father_id = Column(Integer, ForeignKey("father.id"))
    # relationship
    father = relationship("Father", backref="son", order_by=id)

    __table_args__ = (
        UniqueConstraint('age', 'name', name='uix_id_name'),
        Index('ix_id_name', 'name', 'age'),
    )

class Father(Base):

    # 表名
    __tablename__ = "father"

    # ID
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 名字
    name = Column(String(32))
    # 年龄
    age = Column(String(3))
    # 儿子
    # son = relationship("Son")
    __table_args__ = (
        UniqueConstraint('age', 'name', name='uix_id_name'),
        Index('ix_id_name', 'name', 'age'),
    )


# 创建表
# Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)


# 创建 Session
Session = sessionmaker(bind=engine)
session = Session()

#
# ret = session.query(Father).all()
#
#
# for p in ret:
#     print("=========" + p.name)


zhangsan = Father(name = "zhang312", age = 33)
lisi = Father(name = "李  四111", age = 11)
wangwu = Father(name = "王  五111", age = 11)

list = [zhangsan, lisi, wangwu]
nList = []

for pp in list:
    ret = session.query(Father).filter_by(name=pp.name).first()
    if ret:
        print("------- "+pp.name)
    else:
        print("======= " + pp.name)
        session.add_all([pp])
        # nList.append(pp)
print("==============================" + str(len(nList)))

# session.add_all(nList)
session.commit()

# # zhang = Son(name = "xiaozhang")
#
# session.add_all([lisi])
# session.add_all([zhangsan, lisi, wangwu])
# session.add_all([wangwu])
# session.commit()







