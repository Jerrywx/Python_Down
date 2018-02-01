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


class ManToWoman(Base):
    __tablename__ = "man_to_woman"

    id = Column(Integer, primary_key=True)

    man_id = Column(Integer, ForeignKey('man.id'))
    woman_id = Column(Integer, ForeignKey('woman.id'))

# class Men_to_Wemon(Base):
#     __tablename__ = 'men_to_wemon'
#     nid = Column(Integer, primary_key=True)
#     men_id = Column(Integer, ForeignKey('men.id'))
#     women_id = Column(Integer, ForeignKey('women.id'))


class Man(Base):

    __tablename__ = "man"

    id = Column(Integer, primary_key=True)

    name = Column(String(32))
    age = Column(String(32))

    woman = relationship("Woman", secondary=ManToWoman.__table__, backref="man")
# movie_location  = relationship("Country", secondary=CountryToCelebrity.__table__, backref='works')

class Woman(Base):

    __tablename__ = "woman"

    id = Column(Integer, primary_key=True)

    name = Column(String(32))
    age = Column(String(32))


Base.metadata.create_all(engine)

# 创建 Session
Session = sessionmaker(bind=engine)
session = Session()

man1 = Man(name="hah1", age="23")
man2 = Man(name="hah2", age="23")

woman1 = Woman(name="woamn1", age="18")
woman2 = Woman(name="woamn2", age="18")

man1.woman = [woman1]
man2.woman = [woman2]


session.add_all([man1, man2, woman1, woman2])

session.commit()