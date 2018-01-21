import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker, relationship


# 1. 查看书库版本
print(sqlalchemy.__version__)

# 2. 链接数据库
engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/movies', echo=True)

# 3. 创建数据库表
Base = declarative_base()

# 电影
class Movie(Base):

    # 设置表名
    __tablename__ = "movie"

    # 设置ID 类型 主键
    id              = Column(Integer, primary_key=True)
    # 电影中文名
    movie_name_cn   = Column(String(32))
    # 电影英文名
    movie_name_en   = Column(String(32))
    # 电影其他名字
    movie_name_ot   = Column(String(32))


# 导演
class Director(Base):

    # 设置表名字
    __tablename__ = "director"

    # 设置ID
    id              = Column(Integer, primary_key=True)
    # 名字
    name            = Column(String(32))
    # 国家
    country         = Column(String(32))
    # 性别
    sex             = Column(String(1))

# 电影、导演 [多对多]
class MovieToDirector(Base):
    __tablename__   = "movietodirector"
    nid             = Column(Integer, primary_key=True, autoincrement=True)
    movie_id        = Column(String(32))
    director_id     = Column(String(32))
    movie           = relationship("Movie", backref='m2d')
    director        = relationship("Director", backref='m2d')


# 主演
class Actors(Base):
    # 设置表名字
    __tablename__ = "director"

    # 设置ID
    id = Column(Integer, primary_key=True)
    # 名字
    name = Column(String(32))
    # 国家
    country = Column(String(32))
    # 性别
    sex = Column(String(1))




Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)













