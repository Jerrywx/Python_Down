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
from dataManager import Movie, Country, MovieType, Celebrity, MovieAlbum, Resource, Image, Company
import math
from sqlalchemy.ext.declarative import DeclarativeMeta
from datetime import datetime

# 公司
class Companys(tornado.web.RequestHandler):

    # get 方法
    def get(self, *args, **kwargs):

        list = self.getCompanyList()

        self.render('company.html', company=list)


    # 获取公司列表
    def getCompanyList(self):

        session = Session.session()

        list = session.query(Company).all()

        return list



# 编辑
class CompanyEdit(tornado.web.RequestHandler):

    addEdList = []
    count = 1

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

            print("============= ADDDDDDDDDD", addId, "----", str(self.count))
            self.count = self.count + 1

            jsonData = json.dumps(self.addEdList, cls=new_alchemy_encoder(), check_circular=False)
            self.write(jsonData)

            # self.render('companyEdit.html', movieList=self.addEdList)
            return

        # 渲染页面
        self.render('companyEdit.html', movieList=[])

    # 提交表单
    def post(self, *args, **kwargs):
        session = Session.session()
        company = Company()
        company.name = self.get_argument("name_cn")
        company.name_en = self.get_argument("name_en")
        company.address = self.get_argument("address")
        company.create_time = self.get_argument("time")

        company.deal_with = self.get_argument("job")
        company.nature = self.get_argument("type")
        company.create_person = self.get_argument("person")
        company.p_company = self.get_argument("p_company")

        company.desc_info = self.get_argument("desc")

        session.add(company)
        session.commit()

        list = session.query(Company).all()

        # 渲染页面
        self.render('company.html', company=list)


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

# 模型转json
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