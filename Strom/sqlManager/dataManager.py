
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData, Boolean, Float, UniqueConstraint, Index, ForeignKey, Interval
from sqlalchemy.orm import sessionmaker, relationship


# 1. 链接数据库
engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/storm?charset=utf8', echo=True)
# 2. 创建数据库表
Base = declarative_base()


# =============================================== 电影 与其他表关系
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
    # 多对多操作
    movie = relationship("Movie", backref='atm')
    cel = relationship("Celebrity", backref='atm')
    # 关系
    relationship = Column(Integer) # 主演、导演、演员、编剧

# 电影 和 类型
class TypeToMovie(Base):

    __tablename__ = "type_to_movie"
    # id
    id = Column(Integer, primary_key=True)
    # 电影
    movie_id = Column(Integer, ForeignKey('movie.id'))
    # 电影类型
    type_id = Column(Integer, ForeignKey('movietype.id'))

# 电影 和 国家
class CountryToMovie(Base):

    __tablename__ = "country_to_movie"

    # id
    id = Column(Integer, primary_key=True)
    # 电影
    movie_id = Column(Integer, ForeignKey('movie.id'))
    # 电影类型
    country_id = Column(Integer, ForeignKey('country.id'))

# 电影 和 图片
class ImageToMovie(Base):
    # 表名
    __tablename__ = "image_to_movie"

    # id
    id = Column(Integer, primary_key=True)
    # 电影
    movie_id = Column(Integer, ForeignKey('movie.id'))
    # 电影类型
    image_id = Column(Integer, ForeignKey('images.id'))

# 电影 和 视频
class VoideToMovie(Base):
    # 表名
    __tablename__ = "video_to_movie"

    # id
    id = Column(Integer, primary_key=True)
    # 电影
    movie_id = Column(Integer, ForeignKey('movie.id'))
    # 电影类型
    video_id = Column(Integer, ForeignKey('video.id'))

# 电影 和 资源
class ResourceToMovie(Base):
    # 表名
    __tablename__ = "resource_to_movie"

    # id
    id = Column(Integer, primary_key=True)
    # 电影
    movie_id = Column(Integer, ForeignKey('movie.id'))
    # 电影类型
    resource_id = Column(Integer, ForeignKey('resource.id'))

# =============================================== 电影人 与其他表关系

# 电影人 和 图片
class ImageToCelebrity(Base):
    __tablename__ = "image_to_celebrity"

    # id
    id = Column(Integer, primary_key=True)
    # 电影人
    celebrity_id = Column(Integer, ForeignKey('celebrity.id'))
    # 电影类型
    image_id = Column(Integer, ForeignKey('images.id'))

# 电影人 和 国家
class CountryToCelebrity(Base):
    __tablename__ = "country_to_celebrity"

    # id
    id = Column(Integer, primary_key=True)
    # 电影人
    celebrity_id = Column(Integer, ForeignKey('celebrity.id'))
    # 电影类型
    country_id = Column(Integer, ForeignKey('country.id'))

# 电影人 和 视频
class VideoToCelebrity(Base):
    #
    __tablename__ = "video_to_celebrity"

    # id
    id = Column(Integer, primary_key=True)
    # 电影人
    celebrity_id = Column(Integer, ForeignKey('celebrity.id'))
    # 视频
    video_id = Column(Integer, ForeignKey('video.id'))


# =============================================== 电影公司 与其他表关系

# 电影与电影公司
class MovieToCompany(Base):
    __tablename__ = "movie_to_company"

    # id
    id = Column(Integer, primary_key=True)
    # 电影人
    company_id = Column(Integer, ForeignKey('company.id'))
    # 电影类型
    movie_id = Column(Integer, ForeignKey('movie.id'))


# =============================================== 影集 与 类型
# 影集 与 电影类型
class MovieListToType(Base):
    __tablename__ = "list_to_type"
    # id
    id = Column(Integer, primary_key=True)
    # 电影列表
    list_id = Column(Integer, ForeignKey('moviealbum.id'))
    # 电影类型
    type_id = Column(Integer, ForeignKey('movietype.id'))

# =============================================== 基础表

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
    movie_name_cn   = Column(String(128))
    # 电影英文名
    movie_name_en   = Column(String(128))
    # 电影其他名字
    movie_name_ot   = Column(String(128))
    # 电影封面 url地址
    movie_cover     = Column(String(256))
    # 电影简介
    movie_summary   = Column(String(2048))

    # ------------------------------------------------ 电影信息【时长、发行地、类型、上映时间、语言】
    # 电影时长
    movie_length    = Column(Integer)
    # 电影发行地
    # movie_location  = Column(String(32))
    movie_location  = relationship("Country", secondary=CountryToMovie.__table__, backref='works')
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
    movie_actors          = relationship("Celebrity", secondary=ActorToMovie.__table__, backref='works')

    # movie_actors2       = Column(String(256))           #???
    # 导演列表
    # movie_director      = Column(String(256))           #???
    # 编剧
    # movie_writer        = Column(String(256))           #???

    # 电影类型
    # movie_type          = Column(String(128))           # ???
    movie_type            = relationship("MovieType", secondary=TypeToMovie.__table__, backref='works')

    # ------------------------------------------------ 电影资源【预告、照片、解析、原片】
    # 电影资源
    # movie_resource      = Column(String(2048))          #???
    movie_resource        = relationship("Resource", secondary=ResourceToMovie.__table__, backref='works')

    # 图片
    movie_images        = relationship("Image", secondary=ImageToMovie.__table__, backref="works")
    # 视频
    movie_video         = relationship("Video", secondary=VoideToMovie.__table__, backref='works')

    # ------------------------------------------------ 联合唯一
    __table_args__ = (
        UniqueConstraint('movie_douban_id', 'movie_name_cn', name='uix_id_name'),
        Index('ix_id_name', 'movie_douban_id', 'movie_name_cn'),
    )

    # ------------------------------------------------ json 字典转模型

# 电影人
class Celebrity(Base):

    # 设置表名
    __tablename__ = "celebrity"

    # 设置ID 类型 主键
    id = Column(Integer, primary_key=True)

    douban_id   = Column(Integer)

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
    bornPlace   = relationship("Country", secondary=CountryToCelebrity.__table__, backref='celebrity')
    # 视频
    video       = relationship("Video", secondary=VideoToCelebrity.__table__, backref='celebrity')

    # 图片
    images      = relationship("Image", secondary=ImageToCelebrity.__table__, backref='celebrity')

    # ------------------------------------------------ 豆瓣
    # 豆瓣链接
    doubanUrl   = Column(String(256))

    __table_args__ = (
        UniqueConstraint('douban_id', 'name_cn', name='uix_id_name'),
        Index('ix_id_name', 'douban_id', 'name_cn'),
    )

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

    __table_args__ = (
        UniqueConstraint('type', name='uix_type'),
        Index('ix_type', 'type'),
    )

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

# 视频
class Video(Base):

    __tablename__ = "video"

    id          = Column(Integer, primary_key=True)

    # 类型
    type        = Column(Integer)
    # 截图
    image       = Column(String(256))
    # 描述
    desc        = Column(String(512))
    # 附加内容
    attach      = Column(String(512))

    # 创建时间
    time        = Column(String(32))
    # 时长
    length      = Column(Integer)

    # 发布人
    person_id   = Column(Integer)

# 电影资源
class Resource(Base):
    # 表名
    __tablename__ = "resource"

    id = Column(Integer, primary_key=True)

    low         = Column(String(1024))
    medio       = Column(String(1024))
    height      = Column(String(1024))

    com_low     = Column(String(1024))
    com_medio   = Column(String(1024))
    com_height  = Column(String(1024))

    back        = Column(String(1024))


    othre_link = Column(String(1024))

# 影集
class MovieAlbum(Base):
    # 表名
    __tablename__   = "moviealbum"

    # 设置ID 类型 主键
    id = Column(Integer, primary_key=True)

    douban_id       = Column(Integer)

    # 年份
    year            = Column(Integer)
    # 月份
    moth            = Column(Integer)
    # 时间
    time            = Column(Interval)
    # 时间
    timeString      = Column(String(32))
    # 标题
    title           = Column(String(32))
    # 封面图
    cover_image     = Column(String(256))
    # 封面图
    cover_image_m   = Column(String(256))
    # 描述
    description     = Column(String(2048))
    # 创建用户
    user_id         = Column(Integer)
    # 作品列表
    works_id        = Column(String(1025))
    # 评分
    mark            = Column(Float)

    movie_type      = relationship("MovieType", secondary=MovieListToType.__table__, backref='list')

# 电影公司
class Company(Base):

    # 表名
    __tablename__   = "company"

    # 设置ID 类型 主键
    id = Column(Integer, primary_key=True)

    # ========================================== 基本信息
    # 公司名称
    name            = Column(String(128))
    name_en         = Column(String(128))

    # 总部地址
    address         = Column(String(128))

    # 创建时间
    create_time     = Column(String(128))

    # 经营范围
    deal_with       = Column(String(128))

    # 公司性质
    nature          = Column(String(128))

    # 母公司
    p_company       = Column(String(128))

    # 子公司
    s_company       = Column(String(128))

    # 创立者
    create_person   = Column(String(128))

    # 简介
    desc_info       = Column(String(2048))

    # 作品
    works           = relationship("Movie", secondary=MovieToCompany.__table__, backref="company")

# 创建表
Base.metadata.create_all(engine)

# if __name__ == '__main__':
#     print(sqlalchemy.__version__)