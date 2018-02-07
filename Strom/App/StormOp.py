

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
# from movieApi import top250, baseApi, celebrity, movieInfo, comingSoon, movieList
from dataManager import Movie, Country, MovieType, Celebrity, MovieAlbum, Resource
import math


# 请求处理函数类
class StormOp(tornado.web.RequestHandler):
    page_size = 20
    page_numb = 1

    def get(self, *args, **kwargs):
        # 返回内容


        number = self.get_argument("page", 1)
        self.page_numb = int(number) - 1

        movieList = self.fetchMovies()
        self.page_numb = self.page_numb + 1

        session = self.sqlSession()
        count = session.query(Movie).count()


        # 获取页数
        numb = math.ceil(count/self.page_size)
        print("====================== ", str(number))

        # self.render('StormOp.html')
        self.render('StormOp.html', movieList=movieList, count=numb)


    def post(self, *args, **kwargs):
        name = self.get_argument("name")

        # INPUTS_LIST.append(name)
        self.render('StormOp.html')


    # 获取数据库句柄
    def sqlSession(self):
        # 1. 链接数据库
        engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/storm?charset=utf8', echo=False)
        # 2. 创建数据库表
        Base = declarative_base()

        Session = sessionmaker(bind=engine)
        session = Session()

        return session


    # 从数据库读取电影数据
    def fetchMovies(self):

        session = self.sqlSession()
        # ll = session.query(Movie).count()
        list = session.query(Movie).limit(self.page_size).offset(self.page_size * self.page_numb)
        return list


# 电影详情
class MovieDetial(tornado.web.RequestHandler):

    # 获取数据库句柄
    def sqlSession(self):
        # 1. 链接数据库
        engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/storm?charset=utf8', echo=False)
        # 2. 创建数据库表
        Base = declarative_base()

        Session = sessionmaker(bind=engine)
        session = Session()

        return session


    def get(self, *args, **kwargs):

        movieId = self.get_argument("movieid")

        movie = self.movieDerial(movieId)

        self.render('moviedetial.html', movie=movie)


    def movieDerial(self, movieId):

        session = self.sqlSession()

        movie = session.query(Movie).filter_by(id=movieId).first()

        return movie


# 影集
class MovieList(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render('movieList.html')


# Top250
class Top250(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render('top250.html')


# 正在热映
class Online(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render('online.html')