
import urllib.request
import ssl
import json
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData, Boolean, Float, UniqueConstraint, Index, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
import sys
sys.path.append("../sqlManager")

# 1. 链接数据库
engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/test?charset=utf8', echo=False)
# 2. 创建数据库表
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


# 国家
class Country(Base):

    # 表名
    __tablename__ = "country"

    # 设置ID 类型 主键
    id = Column(Integer, primary_key=True)

    # 国家名
    name = Column(String(32))

    __table_args__ = (
        UniqueConstraint('name', name='uix_name'),
        Index('ix_name', 'name'),
    )


# 创建表
# Base.metadata.create_all(engine)

# array = ["中国", "英国", "美国", "加拿大", "加勒比"]
array = ["中国", "发过", "比利时", "澳大利亚", "加勒比"]

for i in array:
    con = session.query(Country).filter_by(name=i).first()

    if con == None:
        c = Country(name=i)
        session.add(c)

session.commit()

