

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

        if movieId.isdigit():

            movie = session.query(Movie).filter_by(id=movieId).all()
            return movie
        else:
            value = "%" + movieId + "%"
            movie = session.query(Movie).filter(Movie.movie_name_cn.like(value)).all()

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
            # content = "电影详情" + spiderId
            movie = spiderMovieDetial.spiderMovie(spiderId)
            self.render('moviedetial.html', movie=movie)
            return

        # 返回数据库中的电影详细信息
        movieId = self.get_argument("movieid")
        movie = self.movieDerial(movieId)

        if movie == None:
            print("================== 获取电影信息为空")

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

# 公司
class Company(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('company.html')

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

# 电影人详情
class CelDetial(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        # 获取电影人ID
        celId = self.get_argument("celId", 0)

        # 获取电影人信息
        person = self.celDetial(celId)

        # 渲染页面
        return self.render('celDetial.html', person=person)

    def celDetial(self, celId):
        session = Session.session()
        person = session.query(Celebrity).filter_by(douban_id=celId).first()
        if person == None:
            return None
        return person

#================================================= 根据电影ID获取电影详细信息
# 
class spiderMovieDetial():

    # 抓取电影详细信息并保存
    @classmethod
    def spiderMovie(self, movieId):

        # 获取电脑详细数据
        data = self.spiderAction(movieId)

        # 查询数据库电影
        session = Session.session()
        movie = session.query(Movie).filter_by(movie_douban_id=movieId).first()

        # 保存更新数据库数据
        if movie != None:
            # 电影存在
            self.updateMovie(movie, data, session)
        else:
            # 电影不存在
            # movie = Movie()
            self.updateMovie(movie, data, session)

        session.commit()

        return movie


    @classmethod
    def spiderAction(self, movieId):
        # 1. 处理 https
        ssl._create_default_https_context = ssl._create_unverified_context

        # 2. 自定义 User_Agent
        ua_heaeders = {
            "User_Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
        }

        # 3. 拼接url 创建请求
        urlString = baseApi + movieInfo
        urlString = urlString.replace("{id}", movieId)
        request = urllib.request.Request(urlString, headers=ua_heaeders)

        print("urlString ", urlString)

        # 4. 向指定url地址发送请求
        # response = urllib.request.urlopen(request)

        try:
            response = urllib.request.urlopen(request)
        except urllib.error.HTTPError as err:
            print("URL:", urlString, "\nurllib.error.HTTPError: ", err)
            return None

        # 5. read() 方法读取文件里的全部内容，返回字符串
        html = response.read()

        # # 6. 保存json
        filePath = "./resource/detial" + movieId + ".json"
        file = open(filePath, "w")
        file.write(html.decode("utf-8"))

        return html#content


    @classmethod
    def updateMovie(cls, movie, jsonData, session):

        # 数据安全判断
        if movie == None or jsonData == None:
            return None

        # 解析json
        js = json.loads(jsonData)

        # 中文名
        movie.movie_name_cn = js.get("title", "")
        # 原名
        movie.original_title = js.get("original_title", "")
        # 上映年份
        movie.movie_release = js.get("year", "")
        # 别名
        movie.movie_name_ot = ",".join(js.get("aka", []))
        # 评分
        movie.movie_douban_mark = js.get("rating", {}).get("average", "")
        # 封面
        movie.movie_cover = js.get("images", {}).get("large", "")
        # 豆瓣链接
        movie.movie_doubanUrl = js.get("alt", "")
        # 简介
        movie.movie_summary = js.get("summary", "")
        # 时长
        # movie.movie_length = js.get("",0)

        # 国家
        countrys = js.get("countries", "")
        counrtyList = []
        for ctName in countrys:
            c = session.query(Country).filter_by(name=ctName).first()
            if c == None:
                c = Country()
                c.name = ctName
                counrtyList.append(c)
            else:
                counrtyList.append(c)
        movie.movie_location = counrtyList

        # 类型
        types = js.get("genres", [])
        typeList = []
        for t in types:
            typ = session.query(MovieType).filter_by(type=t).first()
            if typ == None:
                tt = MovieType()
                tt.type = t
                typeList.append(tt)
            else:
                typeList.append(typ)

        # 电影人
        # 导演
        person = js.get("directors", [])
        pList = []
        for p in person:
            ID = p.get("id", "")
            cel = session.query(Celebrity).filter_by(douban_id=ID).first()
            if cel == None:
                cel = Celebrity()
                cel.doubanUrl = p.get("alt","")
                cel.name_cn = p.get("name", "")
                cel.douban_id = p.get("id", "")
                image = Image()
                image.large = p.get("avatars", {}).get("large", "")
                cel.images = [image]
                pList.append(cel)
                session.add(image)
                session.add(cel)
            else:
                cel.doubanUrl = p.get("alt", "")
                cel.name_cn = p.get("name", "")
                cel.douban_id = p.get("id", "")
                image = Image()
                image.large = p.get("avatars", {}).get("large", "")
                cel.images = [image]
                session.add(image)
                session.add(cel)
                pList.append(cel)
        movie.movie_actors = pList
        session.commit()

        for p in pList:
            for item in p.atm:
                item.relationship = 1

        # 主演
        casts = js.get("casts", [])
        pList = []
        for p in casts:
            ID = p.get("id", "")
            cel = session.query(Celebrity).filter_by(douban_id=ID).first()
            if cel == None:
                cel = Celebrity()
                cel.doubanUrl = p.get("alt", "")
                cel.name_cn = p.get("name", "")
                cel.douban_id = p.get("id", "")
                image = Image()
                image.large = p.get("avatars", {}).get("large", "")
                cel.images = [image]
                pList.append(cel)
                session.add(image)
                session.add(cel)
            else:
                cel.doubanUrl = p.get("alt", "")
                cel.name_cn = p.get("name", "")
                cel.douban_id = p.get("id", "")
                image = Image()
                image.large = p.get("avatars", {}).get("large", "")
                cel.images = [image]
                session.add(image)
                session.add(cel)
                pList.append(cel)
        movie.movie_actors = pList + movie.movie_actors
        session.commit()

        for p in pList:
            for item in p.atm:
                item.relationship = 2

        return movie