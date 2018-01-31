

import urllib.request
import ssl
import json
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import sys
sys.path.append("../sqlManager")
from movieApi import top250, baseApi, celebrity
from dataManager import Movie

# 抓取 Json 数据
def spiderTop250():
    # 1. 处理 https
    ssl._create_default_https_context = ssl._create_unverified_context

    # 2. 自定义 User_Agent
    ua_heaeders = {
        "User_Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }

    # 3. 拼接url 创建请求
    urlString = baseApi + top250
    request = urllib.request.Request(urlString, headers=ua_heaeders)

    # 4. 向指定url地址发送请求
    response = urllib.request.urlopen(request)

    # 5. read() 方法读取文件里的全部内容，返回字符串
    html = response.read()

    # 6. 保存json
    file = open("./resource/list2.json", "w")
    file.write(html.decode("utf-8"))


# 存储 Json 数据
def storeTop250():

    # 1. 链接数据库
    engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/storm?charset=utf8', echo=False)
    # 2. 创建数据库表
    Base = declarative_base()

    Session = sessionmaker(bind=engine)
    session = Session()

    # 3. 读取文件中的 json
    file = open("./resource/list2.json", "r")
    content = json.loads(file.read())

    # 4. 遍历数据
    for item in content["subjects"]:
        # print(item['title'])

        # 检查电影是否存在
        ret = session.query(Movie).filter_by(movie_douban_id=item['id']).first()
        if ret:
            print("---- 存在的电影:" + item['title'])
        else:
            print("===== 不存在的电影:" + item['title'])

            movie = Movie()
            # 名称
            movie.movie_name_cn     = item['title']
            # id
            movie.movie_douban_id = item['id']
            # 评分
            movie.movie_douban_mark = item['rating']['average']
            # 封面
            movie.movie_cover       = item['images']['large']
            # 豆瓣链接
            movie.movie_doubanUrl   = item['alt']

            # 类型
            types = item['genres']
            movie.movie_type = ','.join(types)

            # 上映时间
            movie.movie_release = item['year']

            session.add(movie)

    session.commit()


# 获取单个电影详细信息
def spiderMovieDetial():

    # 0 从数据库中获取电影

    # 1. 链接数据库
    engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/storm?charset=utf8', echo=False)
    # 2. 创建数据库表
    Base = declarative_base()

    Session = sessionmaker(bind=engine)
    session = Session()

    # 获取第一个电影
    item = session.query(Movie).first()
    movieId = str(item.movie_douban_id)

    # 1. 处理 https
    ssl._create_default_https_context = ssl._create_unverified_context

    # 2. 自定义 User_Agent
    ua_heaeders = {
        "User_Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }

    # 3. 拼接url 创建请求
    urlString = baseApi + celebrity
    urlString = urlString.replace("{id}", movieId)

    request = urllib.request.Request(urlString, headers=ua_heaeders)

    # 4. 向指定url地址发送请求
    response = urllib.request.urlopen(request)

    # 5. read() 方法读取文件里的全部内容，返回字符串
    html = response.read()

    # 6. 保存json
    file = open("./resource/movieDetial.json", "w")
    file.write(html.decode("utf-8"))


def storeMovieDetial():
    # 1. 链接数据库
    engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/storm?charset=utf8', echo=False)
    # 2. 创建数据库表
    Base = declarative_base()

    Session = sessionmaker(bind=engine)
    session = Session()

    # 3. 读取文件中的 json
    file = open("./resource/list2.json", "r")
    content = json.loads(file.read())

    # 4. 遍历数据
    for item in content["subjects"]:
        # print(item['title'])

        # 检查电影是否存在
        ret = session.query(Movie).filter_by(movie_douban_id=item['id']).first()
        if ret:
            print("---- 存在的电影:" + item['title'])
        else:
            print("===== 不存在的电影:" + item['title'])

            movie = Movie()
            # 名称
            movie.movie_name_cn = item['title']
            # id
            movie.movie_douban_id = item['id']
            # 评分
            movie.movie_douban_mark = item['rating']['average']
            # 封面
            movie.movie_cover = item['images']['large']
            # 豆瓣链接
            movie.movie_doubanUrl = item['alt']

            # 类型
            types = item['genres']
            movie.movie_type = ','.join(types)

            # 上映时间
            movie.movie_release = item['year']

            session.add(movie)

    session.commit()

    pass

# spiderMovieDetial()






















































