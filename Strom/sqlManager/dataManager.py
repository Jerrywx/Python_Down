
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData, Boolean, Float, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship


# 1. 链接数据库
engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/storm?charset=utf8', echo=True)
# 2. 创建数据库表
Base = declarative_base()

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
    # 电影类型
    movie_type      = Column(String(128))               #???
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
    movie_actors        = Column(String(256))           #???
    movie_actors2       = Column(String(256))           #???
    # 导演列表
    movie_director      = Column(String(256))           #???
    # 编剧
    movie_writer        = Column(String(256))           #???

    # ------------------------------------------------ 电影资源【预告、照片、解析、原片】
    # 电影资源
    movie_resource      = Column(String(2048))          #???


    # ------------------------------------------------ 联合唯一
    __table_args__ = (
        UniqueConstraint('movie_douban_id', 'movie_name_cn', name='uix_id_name'),
        Index('ix_id_name', 'movie_douban_id', 'movie_name_cn'),
    )

# 创建表
Base.metadata.create_all(engine)



# if __name__ == '__main__':
#     print(sqlalchemy.__version__)