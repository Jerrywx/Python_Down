#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

# 链接数据库
engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/test', echo=True)

# 构造表
Base = declarative_base()
# 儿子表
class Son(Base):
    # 表名
    __tablename__ = 'son'
    # 属性
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    age = Column(String(16))
    # 一对多
    father_id = Column(Integer, ForeignKey('father.id'))

    # father = relationship('Father')

    # __table_args__ = (
    #     UniqueConstraint('id', 'name', name='uix_id_name'),
    #     Index('ix_id_name', 'name', 'extra'),
    # )

# 父亲类
class Father(Base):
    # 表名
    __tablename__ = 'father'

    # 属性
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    age = Column(String(16))
    son = relationship('Son')


# 创建表
Base.metadata.create_all(engine)

#
Session = sessionmaker(bind=engine)
session = Session()

# ---------- 1. 插入数据
# f1 = Father(name='alvin', age=50)
# w1 = Son(name='little alvin1', age=4)
# w2 = Son(name='little alvin2', age=5)
#
# f1.son = [w1, w2]
# session.add(f1)
# session.commit()


# ---------- 2. 插入数据
f1 = Father(name="manman", age=26)
s1 = Son(name="man-son", age=3, father_id=4)
s2 = Son(name="man-son2", age=3, father_id=4)

session.add_all([f1, s1, s2])
session.commit()

# fa = session.query(Father).filter(Father.name=='manman')[0]
# print(fa.id)

