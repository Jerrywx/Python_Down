import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import urllib.request
import ssl
import json
import time
import random
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import sys
sys.path.append("../sqlManager")
sys.path.append("../reptile")
from movieApi import top250, baseApi, celebrity, movieInfo, comingSoon, movieList
from dataManager import Movie, Country, MovieType, Celebrity, MovieAlbum, Resource, Image
import math
from sqlalchemy.ext.declarative import DeclarativeMeta
from datetime import datetime

# 公司
class Company(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('company.html')


# 编辑
class CompanyEdit(tornado.web.RequestHandler):

    addEdList = []

    #
    def get(self, *args, **kwargs):

        # 判断是否有搜索id
        movieId = self.get_argument("movieId", None)
        if movieId != None:
            # 搜索
            movieList = self.searchMovie(movieId)
            # 搜索结果转 json
            jsonData = json.dumps(movieList, cls=new_alchemy_encoder(), check_circular=False)

            self.write(jsonData)
            # self.render('companyEdit.html', movieList=movieList)
            return

        # 判断是否有添加
        addId = self.get_argument("addId", None)
        if addId != None:
            movieList = self.searchMovie(addId)
            self.addEdList = self.addEdList + movieList
            self.render('companyEdit.html', movieList=self.addEdList)
            return

        # 渲染页面
        self.render('companyEdit.html', movieList=[])

    # 搜索电影
    def searchMovie(self, movieId):
        session = Session.session()

        if movieId.isdigit():

            movie = session.query(Movie).filter_by(id=movieId).all()
            return movie
        else:
            value = "%" + movieId + "%"
            movie = session.query(Movie).filter(Movie.movie_name_cn.like(value)).all()

            return movie



# 数据库管理类
class Session():

    @classmethod  # 类方法
    def session(cls):
        # 1. 链接数据库
        engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/storm?charset=utf8', echo=False)
        # 2. 创建数据库表
        Base = declarative_base()

        Session = sessionmaker(bind=engine)
        session = Session()

        return session


def new_alchemy_encoder():
    _visited_objs = []

    class AlchemyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj.__class__, DeclarativeMeta):
                # don't re-visit self
                if obj in _visited_objs:
                    return None
                _visited_objs.append(obj)

                # an SQLAlchemy class
                fields = {}
                for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                    data = obj.__getattribute__(field)
                    try:
                        if isinstance(data, datetime):
                            data = data.strftime('%Y-%m-%d %H:%M:%S')
                        json.dumps(data)  # this will fail on non-encodable values, like other classes
                        fields[field] = data
                    except TypeError:
                        fields[field] = None
                return fields

            return json.JSONEncoder.default(self, obj)

    return AlchemyEncoder