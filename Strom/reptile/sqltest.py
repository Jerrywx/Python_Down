
import urllib.request
import ssl
import json
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData, Boolean, Float, UniqueConstraint, Index, ForeignKey, Interval
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

# 影集
class MovieList(Base):

    # 表名
    __tablename__   = "movielist"

    # 设置ID 类型 主键
    id = Column(Integer, primary_key=True)

    # 时间
    # time            = Column(Interval)
    # 时间
    timeString      = Column(String(32))
    # 标题
    title           = Column(String(32))
    # 封面图
    cover_image     = Column(String(256))
    # 描述
    description     = Column(String(2048))
    # 创建用户
    user_id         = Column(Integer)
    # 作品列表
    works_id        = Column(String(1025))
    # 评分
    mark            = Column(Float)

    # movie_type = relationship("MovieType", secondary=MovieListToType.__table__, backref='list')



# 创建表
Base.metadata.create_all(engine)
#
# # array = ["中国", "英国", "美国", "加拿大", "加勒比"]
# array = ["中国", "发过", "比利时", "澳大利亚", "加勒比"]
#
# for i in array:
#     con = session.query(Country).filter_by(name=i).first()
#
#     if con == None:
#         c = Country(name=i)
#         session.add(c)
#
# session.commit()

