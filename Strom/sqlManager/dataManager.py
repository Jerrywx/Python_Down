
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData, Boolean, Float, UniqueConstraint, Index, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship


# 1. 链接数据库
engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/storm?charset=utf8', echo=True)
# 2. 创建数据库表
Base = declarative_base()


# 电影 和 人 关系 【演员、导演、编剧】
class ActorToMovie(Base):

    # 表名
    __tablename__ = "actor_to_movie"

    # id
    aid = Column(Integer, primary_key=True)
    # 电影
    movie_id = Column(Integer, ForeignKey('movie.id'))
    # 人员
    actor_id = Column(Integer, ForeignKey('celebrity.id'))
    # 关系
    relationship = Column(Integer)
#     主演、导演、演员、编剧


# 电影
class Movie(Base):

    # 设置表名
    __tablename__ = "movie"


    # 设置ID 类型 主键
    id              = Column(Integer, primary_key=True)

    # 数据是否完善
    complete        = Column(Boolean, default=False)

    # ------------------------------------------------ 电影名【中文名、英文名、别名、封面】
    # 电影中文名
    movie_name_cn   = Column(String(32))
    # 电影英文名
    movie_name_en   = Column(String(32))
    # 电影其他名字
    movie_name_ot   = Column(String(128))
    # 电影封面 url地址
    movie_cover     = Column(String(256))

    # ------------------------------------------------ 电影信息【时长、发行地、类型、上映时间、语言】
    # 电影时长
    movie_length    = Column(Integer)
    # 电影发行地
    movie_location  = Column(String(32))
    # 电影上映时间
    movie_release   = Column(String(128))
    # 语言
    movie_language = Column(String(128))

    # ------------------------------------------------ 电影评分【豆瓣评分、烂番茄】
    # 豆瓣评分
    movie_douban_mark   = Column(String(32))
    # 豆瓣地址
    movie_doubanUrl     = Column(String(256))
    # 豆瓣 ID
    movie_douban_id     = Column(Integer)
    # 烂番茄
    movie_tomato_mark1  = Column(String(32))
    movie_tomato_mark2  = Column(String(32))


    # ------------------------------------------------ 主演导演编剧 【导演、编剧、主演、演员】
    # 主演列表
    # movie_actors        = Column(String(256))           #???
    movie_actors = relationship("Men", secondary=ActorToMovie.__table__, backref='works')

    # movie_actors2       = Column(String(256))           #???
    # 导演列表
    # movie_director      = Column(String(256))           #???
    # 编剧
    # movie_writer        = Column(String(256))           #???

    # 电影类型
    movie_type          = Column(String(128))           # ???

    # ------------------------------------------------ 电影资源【预告、照片、解析、原片】
    # 电影资源
    movie_resource      = Column(String(2048))          #???


    # ------------------------------------------------ 联合唯一
    __table_args__ = (
        UniqueConstraint('movie_douban_id', 'movie_name_cn', name='uix_id_name'),
        Index('ix_id_name', 'movie_douban_id', 'movie_name_cn'),
    )


# 演员
class Celebrity(Base):

    # 设置表名
    __tablename__ = "celebrity"

    # 设置ID 类型 主键
    id = Column(Integer, primary_key=True)

    # ------------------------------------------------ 基本信息【中文名、英文名、别名、昵称、性别、出生地】
    # 人名
    # 中文名
    name_cn     = Column(String(64))
    # 英文名
    name_en     = Column(String(64))
    # 别名
    name_other  = Column(String(512))
    # 昵称
    name_aka    = Column(String(512))


    # 性别
    gender      = Column(String(3))
    # 出生地
    bornPlace   = Column(String(128))

    # 作品
    # works       = Column(String(1024))

    # 图片
    image       = Column(String(256))

    # ------------------------------------------------ 豆瓣
    # 豆瓣链接
    doubanUrl   = Column(String(256))

# 电影类型
class MovieType(Base):
    # 设置表名
    __tablename__ = "movietype"

    # 设置ID 类型 主键
    id = Column(Integer, primary_key=True)

    # 类名
    type = Column(String(32))
    # 权重
    weight = Column(Integer)

# 国家
class Country(Base):

    # 表名
    __tablename__ = "country"

    # 设置ID 类型 主键
    id = Column(Integer, primary_key=True)

    # 国家名
    name = Column(String(32))

# 图片
class Image(Base):

    # 表名
    __tablename__ = "images"

    # 设置ID 类型 主键
    id = Column(Integer, primary_key=True)

    # 图片
    imageName   = Column(String(32))
    # 小图
    small       = Column(String(256))
    # 中图
    medium      = Column(String(256))
    # 小图
    large       = Column(String(256))

    # 是否有多图
    hasMore     = Column(Boolean)

    # 图片描述
    desc        = Column(String(256))
    # MD5
    md5         = Column(String(32))



# 创建表
Base.metadata.create_all(engine)



# if __name__ == '__main__':
#     print(sqlalchemy.__version__)