
# 创建数据库表

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker

print(sqlalchemy.__version__)


# 链接数据库
engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/test', echo=True)


# ===================== 0、创建数据库表
# 生成一个 SQLORM 基类
Base = declarative_base()

class Man(Base):

    __tablename__ = "man"
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    age = Column(String(8))

    def __repr__(self):
        return self.name

class Woman(Base):

    __tablename__ = "woman"

    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    age = Column(String(32))

    men_id = Column(Integer, ForeignKey('man.id'))


# 创建所有表
# Base.metadata.create_all(engine)





















