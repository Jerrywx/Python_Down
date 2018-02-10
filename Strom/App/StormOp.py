

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

# 电影列表
class StormOp(tornado.web.RequestHandler):
    page_size = 20
    page_numb = 1

    def get(self, *args, **kwargs):
        # 返回内容


        # 判断是不是搜索
        id = self.get_argument("content", None)
        if id != None:
            list = self.search(id)
            self.render('StormOp.html', movieList=list, count=len(list))
            return


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
        list = session.query(Movie).limit(self.page_size).offset(self.page_size * self.page_numb)
        return list

    # 搜索
    def search(self, movieId):
        session = Session.session();
        movie = session.query(Movie).filter_by(id=movieId).all()
        return movie

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

        # 抓取电影详情
        spiderId = self.get_argument("spiderId", None)
        if spiderId != None:
            content = "电影详情" + spiderId
            self.write(content)
            return

        # 返回数据库中的电影详细信息
        movieId = self.get_argument("movieid")
        movie = self.movieDerial(movieId)
        self.render('moviedetial.html', movie=movie)


    def movieDerial(self, movieId):

        session = Session.session()#self.sqlSession()

        movie = session.query(Movie).filter_by(id=movieId).first()

        return movie

# 影集
class MovieList(tornado.web.RequestHandler):

    page_size = 15
    page_numb = 1

    def get(self, *args, **kwargs):

        albumId = self.get_argument("content", None)

        if albumId != None:
            albums = self.getAlbum(albumId)
            self.render('movieList.html', movieAlbum=albums, count=len(albums))

        session = Session.session()

        number = self.get_argument("page", 1)
        self.page_numb = int(number) - 1

        count = session.query(MovieAlbum).count()
        movieList = session.query(MovieAlbum).all()

        list = session.query(MovieAlbum).limit(self.page_size).offset(self.page_size * self.page_numb)

        numb = math.ceil(count / self.page_size)

        self.render('movieList.html', movieAlbum=list, count=numb)


    def getAlbum(self, albumId):

        session = Session.session()
        return session.query(MovieAlbum).filter_by(id=albumId).all()

# Top250
class Top250(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render('top250.html')

# 正在热映
class Online(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render('online.html')

# 影集详情
class AlbumDetial(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):

        # 获取参数
        albumId = self.get_argument("albumId", 1)
        # 获取影集详细信息
        album = self.getAlbumDetial(albumId)
        # 获取电影列表
        movieList = self.getAlbumList(album.works_id)

        self.render('albumDetial.html', album=album, movieList=movieList)

    # 获取电脑详细信息
    def getAlbumDetial(self, albumId):

        # 数据库 session
        session = Session.session()

        album = session.query(MovieAlbum).filter_by(id=albumId).first()

        return album

    # 获取电影列表
    def getAlbumList(self, listId):

        arrayOfId = listId.split(",")


        # query.filter(User.name.in_(['ed', 'wendy', 'jack']))
        session = Session.session()
        list = session.query(Movie).filter(Movie.movie_douban_id.in_(arrayOfId)).all()

        return list
