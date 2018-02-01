
import urllib.request
import ssl
import json
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import sys
sys.path.append("../sqlManager")
from movieApi import top250, baseApi, celebrity, movieInfo
from dataManager import Movie, Country, MovieType, Celebrity

# ==========================================================
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

        # 检查电影是否存在
        ret = session.query(Movie).filter_by(movie_douban_id=item['id']).first()
        if ret:
            print("---- 存在的电影:" + item['title'])
        else:
            print("--------------------:" + item['title'])
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
            # types = item['genres']
            # movie.movie_type = ','.join(types)

            # 上映时间
            movie.movie_release = item['year']

            session.add(movie)

    session.commit()


# ==========================================================
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
    urlString = baseApi + movieInfo
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
    file = open("./resource/movieDetial.json", "r")
    content = json.loads(file.read())

    # 获取 电影ID
    movieId = content['id']

    # 根据 id 从数据库获取电影

    movie = session.query(Movie).filter_by(movie_douban_id=movieId).first()


    if movie:
        print("------------------------------")

        # ------------------------------------- 更新英文名字
        movie.movie_name_en = content['original_title']

        # ------------------------------------- 更新描述
        movie.movie_summary = content['summary']

        # ------------------------------------- 更新别名
        otherName = content['aka']
        movie.movie_name_ot = ",".join(otherName)

        # ------------------------------------- 获取国家
        country = content['countries']
        countrys = []
        for name in country:

            # 1. 检测国家是否已经存在
            country = session.query(Country).filter_by(name = name).first()

            if country == None:
                c = Country()
                c.name = name
                countrys.append(c)
            else:
                print("---- 已经存在:" + name)

        # 更新国家
        session.add_all(countrys)
        movie.movie_location = countrys

        # ------------------------------------- 类别
        types = content['genres']
        typeList = []

        for type in types:

            # 1. 检测类型是否存在
            ty = session.query(MovieType).filter_by(type=type).first()

            if ty == None:
                t = MovieType()
                t.type = type
                typeList.append(t)
            else:
                print("----- 类型存在")

        session.add_all(typeList)
        movie.movie_type = typeList

        # ------------------------------------- 电影人
        casts = content['casts']
        castsList = []
        for cast in casts:

            # 1. 检测电影人是否存在
            cel = session.query(Celebrity).filter_by(douban_id=cast['id']).first()

            # 2. 不存在
            if cel == None:
                c = Celebrity()
                c.name_cn = cast['name']
                c.douban_id = cast['id']
                c.doubanUrl = cast['alt']
                castsList.append(c)
            else:
                print("----- 演员存在:" + cast['name'])

        casts = content['directors']
        for cast in casts:

            # 1. 检测电影人是否存在
            cel = session.query(Celebrity).filter_by(douban_id=cast['id']).first()

            # 2. 不存在
            if cel == None:
                c = Celebrity()
                c.name_cn = cast['name']
                c.douban_id = cast['id']
                c.doubanUrl = cast['alt']
                castsList.append(c)
            else:
                print("----- 导演存在:" + cast['name'])

        session.add_all(castsList)
        movie.movie_actors = castsList

        # Celebrity

        session.commit()
    else:
        print("========= 电影不存在")

    pass


# ==========================================================
# 获取电影人信息
def spiderCelebrity():

    # 1. 链接数据库
    engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/storm?charset=utf8', echo=False)
    # 2. 创建数据库表
    Base = declarative_base()

    Session = sessionmaker(bind=engine)
    session = Session()

    # 获取第一个电影
    item = session.query(Celebrity).first()
    pId = str(item.douban_id)

    print("========== 电影人ID", pId)

    # 1. 处理 https
    ssl._create_default_https_context = ssl._create_unverified_context

    # 2. 自定义 User_Agent
    ua_heaeders = {
        "User_Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }

    # 3. 拼接url 创建请求
    urlString = baseApi + celebrity
    urlString = urlString.replace("{id}", pId)

    request = urllib.request.Request(urlString, headers=ua_heaeders)

    # 4. 向指定url地址发送请求
    response = urllib.request.urlopen(request)

    # 5. read() 方法读取文件里的全部内容，返回字符串
    html = response.read()

    # 6. 保存json
    file = open("./resource/celebrity.json", "w")
    file.write(html.decode("utf-8"))

# 保存电影人信息
def storeCelebrity():
    # 1. 链接数据库
    engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/storm?charset=utf8', echo=False)
    # 2. 创建数据库表
    Base = declarative_base()

    Session = sessionmaker(bind=engine)
    session = Session()

    # 3. 读取文件中的 json
    file = open("./resource/celebrity.json", "r")
    content = json.loads(file.read())



    # 存储数据


    print(content)


# spiderMovieDetial()
# storeTop250()
# 保存电影详细信息
# storeMovieDetial()

storeCelebrity()



















































