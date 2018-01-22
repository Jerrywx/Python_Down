#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

# 链接数据库
engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/info?charset=utf8', echo=True)

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


# 创建表
Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)


# 创建 Session
Session = sessionmaker(bind=engine)
session = Session()

zhangsan = Father(name = "zhang3", age = 33)
lisi = Father(name = "李四", age = 34)
wangwu = Father(name = "王五", age = 27)
#
# # zhang = Son(name = "xiaozhang")
#
# session.add_all([lisi])
session.add_all([zhangsan, lisi, wangwu])
session.commit()







