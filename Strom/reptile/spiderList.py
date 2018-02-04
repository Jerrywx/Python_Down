
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
from movieApi import top250, baseApi, celebrity, movieInfo, comingSoon, movieList
from dataManager import Movie, Country, MovieType, Celebrity, MovieAlbum, Resource

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

        # 主演
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
                session.add(c)
                castsList.append(c)
            # 存在
            else:
                castsList.append(cel)

        # 存储对应关系
        movie.movie_actors = castsList

        for ii in movie.movie_actors:
            # ii.atm.fil
            for r in ii.atm:
                if r.movie_id == movie.id:
                    r.relationship = 2

        session.commit()
        castsList2 = []
        # 导演
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
                session.add(c)
                castsList2.append(c)
            # 存在
            else:
                castsList2.append(cel)

        #
        # session.add_all(castsList)
        movie.movie_actors = castsList + castsList2

        # 存储对应关系
        # movie.movie_actors = castsList
        for ii in movie.movie_actors:
            for r in ii.atm:
                if r.movie_id == movie.id:
                    if r.relationship == None:
                        r.relationship = 1

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

    # 4. 获取电影人 ID
    pId = content['id']
    person = session.query(Celebrity).filter_by(douban_id=pId).first()

    #
    if person == None:
        # 不存在
        person = Celebrity()

        person.name_cn = content['name']
        person.name_en = content['name_en']
        names = content['aka_en']
        person.name_other = ",".join(names)
        person.gender = content['gender']
        person.bornPlace = content['born_place']
        person.doubanUrl = content['alt']

        # 作品
        for work in content['works']:
            print(work)

    else:
        # 存在
        pass
















    # 存储数据


    print(content)


# ========================================================== 批量电影详情

# 电影详细信息数据
class MovieDetial():

    # 打开数据库
    def session(self):
        # 1. 链接数据库
        engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/storm?charset=utf8', echo=False)
        # 2. 创建数据库表
        Base = declarative_base()

        Session = sessionmaker(bind=engine)
        session = Session()

        return session


    # 获取电影ID列表
    def movieIdList(self):

        session = self.session()

        # 获取第一个电影
        items = session.query(Movie).all()

        # id 列表
        idList = []

        # 获取电影ID
        for item in items:
            if item.movie_name_en == None:
                print("-----", item.movie_name_en)
                # 添加数据完整新判断
                idList.append(item.movie_douban_id)

        # 关闭数据库
        session.close()

        return idList


    # 根据 电影ID 获取电影链接
    def movieLink(self, movieId):

        urlString = baseApi + movieInfo
        urlString = urlString.replace("{id}", str(movieId))

        return urlString

    # 抓取数据
    def spiderMpvie(self):
        # 1. 处理 https
        ssl._create_default_https_context = ssl._create_unverified_context

        # 2. 自定义 User_Agent
        ua_heaeders = {
            "User_Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
        }

        # 电影ID列表
        movieList = self.movieIdList()

        movieList = []

        # 遍历电影ID列表
        for movieId in movieList:

            tt = random.randint(1, 4)
            print('-------------sleep:', str(tt))
            # time.sleep(tt)

            # 电影URL
            urlString = self.movieLink(movieId)

            print(urlString)
            # 请求数据
            request = urllib.request.Request(urlString, headers=ua_heaeders)
            # 向指定url地址发送请求
            try:
                response = urllib.request.urlopen(request)
                break
            except urllib.error.HTTPError as err:
                print("URL:", urlString,  "\nurllib.error.HTTPError: ", err)
                continue

            print("go on")
            print("go on")
            print("go on")
            print("go on")


            # read() 方法读取文件里的全部内容，返回字符串
            html = response.read()
            content = html.decode("utf-8")


            js = json.loads(content)
            movieName = js.get('title', "抓取数据失败!")
            if movieName == "抓取数据失败!":
                print("------- 抓取电影:", str(movieId), " 失败")
                continue
            else:
                print("------- 抓取电影:", movieName, " 成功")

            # 保存json
            # file = open("./resource/" + str(movieId) + ".json", "w")
            # file.write(html.decode("utf-8"))
            # file.write(content)
            # 解析数据
            # self.analysisMovie(content)


    def analysisMovie(self, content):

        # 打开数据库
        session = self.session()

        # 获取 Json 数据
        content = json.loads(content)

        # 获取 电影ID
        movieId = content['id']

        # 根据 id 从数据库获取电影
        movie = session.query(Movie).filter_by(movie_douban_id=movieId).first()

        # 如果电影不存在
        if movie == None:
            print("电影:", content['title'], "不存在!! id:", content['id'])
            return

        # 电影存在
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
            country = session.query(Country).filter_by(name=name).first()

            # 国家不存在
            if country == None:
                # 创建国际
                c = Country()
                c.name = name
                # 保存国家
                session.add(c)
                countrys.append(c)
            else:
                countrys.append(country)

        # 更新国家
        # session.add_all(countrys)
        movie.movie_location = countrys

        # ------------------------------------- 类别
        types = content['genres']
        typeList = []

        for type in types:

            # 1. 检测类型是否存在
            ty = session.query(MovieType).filter_by(type=type).first()

            # 分类不存在
            if ty == None:
                # 创建分类
                t = MovieType()
                t.type = type
                # 保存分类
                session.add(t)
                typeList.append(t)
            else:
                # print("----- 类型存在")
                typeList.append(ty)

        # 存储类别对应关心
        # session.add_all(typeList)
        movie.movie_type = typeList

        # ------------------------------------- 电影人

        # 主演
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
                session.add(c)
                castsList.append(c)
            # 存在
            else:
                castsList.append(cel)

        # 存储对应关系
        movie.movie_actors = castsList

        for ii in movie.movie_actors:
            # ii.atm.fil
            for r in ii.atm:
                if r.movie_id == movie.id:
                    r.relationship = 2

        session.commit()
        castsList2 = []
        # 导演
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
                session.add(c)
                castsList2.append(c)
            # 存在
            else:
                castsList2.append(cel)

        #
        # session.add_all(castsList)
        movie.movie_actors = castsList + castsList2

        # 存储对应关系
        # movie.movie_actors = castsList
        for ii in movie.movie_actors:
            for r in ii.atm:
                if r.movie_id == movie.id:
                    if r.relationship == None:
                        r.relationship = 1

        session.commit()

# 电影Top 250
class MovieTop250():

    # 抓取次数
    timer = 0
    # 每次抓取个数
    limit = 20

    # 获取每次 链接
    def listUrl(self):

        starNumb = self.timer * self.limit

        numString = "?start={start}&count={count}"
        urlString = baseApi + top250 + numString
        urlString = urlString.replace("{start}", str(starNumb))
        urlString = urlString.replace("{count}", str(self.limit))

        return urlString

    # 抓取开始
    def spiderAction(self):

        numb = (self.timer + 1) * self.limit

        while numb <= 260:

            print(self.listUrl())

            self.spiderMovieList(self.listUrl(), str(self.timer))

            self.timer = self.timer + 1
            numb = (self.timer + 1) * self.limit

    # 抓取数据、保存数据 操作
    def spiderMovieList(self, urlString, name):
        # 1. 处理 https
        ssl._create_default_https_context = ssl._create_unverified_context

        # 2. 自定义 User_Agent
        ua_heaeders = {
            "User_Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
        }

        # 3. 拼接url 创建请求
        # urlString = baseApi + top250
        request = urllib.request.Request(urlString, headers=ua_heaeders)

        # 4. 向指定url地址发送请求
        response = urllib.request.urlopen(request)

        # 5. read() 方法读取文件里的全部内容，返回字符串
        html = response.read()
        content = html.decode("utf-8")

        # 6. 保存json
        file = open("./resource/name.json", "w")
        file.write(content)

        # 1. 链接数据库
        engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/storm?charset=utf8', echo=False)
        # 2. 创建数据库表
        Base = declarative_base()

        Session = sessionmaker(bind=engine)
        session = Session()

        # 3. 读取文件中的 json
        # file = open("./resource/list2.json", "r")
        content = json.loads(content)

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
                # types = item['genres']
                # movie.movie_type = ','.join(types)

                # 上映时间
                movie.movie_release = item['year']

                session.add(movie)

        session.commit()

# 即将上映电影
class MovieComingSoon():
    # 抓取次数
    timer = 0
    # 每次抓取个数
    limit = 20

    # 获取每次 链接
    def listUrl(self):
        starNumb = self.timer * self.limit

        numString = "?start={start}&count={count}"
        urlString = baseApi + comingSoon + numString
        urlString = urlString.replace("{start}", str(starNumb))
        urlString = urlString.replace("{count}", str(self.limit))

        return urlString

    # 抓取开始
    def spiderAction(self):

        numb = (self.timer + 1) * self.limit

        while True:

            print(self.listUrl())

            goon = self.spiderMovieList(self.listUrl(), str(self.timer))

            if goon == False:
                break

            self.timer = self.timer + 1
            numb = (self.timer + 1) * self.limit


    # 抓取数据、保存数据 操作
    def spiderMovieList(self, urlString, name):
        # 1. 处理 https
        ssl._create_default_https_context = ssl._create_unverified_context

        # 2. 自定义 User_Agent
        ua_heaeders = {
            "User_Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
        }

        # 3. 拼接url 创建请求
        # urlString = baseApi + top250
        request = urllib.request.Request(urlString, headers=ua_heaeders)

        # 4. 向指定url地址发送请求
        response = urllib.request.urlopen(request)

        # 5. read() 方法读取文件里的全部内容，返回字符串
        html = response.read()
        content = html.decode("utf-8")

        # 6. 保存json
        file = open("./resource/Soon"+name+".json", "w")
        file.write(content)

        # 1. 链接数据库
        engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/storm?charset=utf8', echo=False)
        # 2. 创建数据库表
        Base = declarative_base()

        Session = sessionmaker(bind=engine)
        session = Session()

        # 3. 读取文件中的 json
        # file = open("./resource/list2.json", "r")
        content = json.loads(content)

        cont = content.get('subjects', None)

        # 判断抓取数据是否成功
        if content == None:
            return False

        # 4. 遍历数据
        for item in cont:

            # 检查电影是否存在
            ret = session.query(Movie).filter_by(movie_douban_id=item['id']).first()
            if ret:
                print("---- 存在的电影:" + item['title'])
            else:
                print("--------------------:" + item['title'])
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
                # types = item['genres']
                # movie.movie_type = ','.join(types)

                # 上映时间
                movie.movie_release = item['year']

                session.add(movie)

        session.commit()

        count = content.get('count', 0)
        start = content.get('start', 0)
        total = content.get('total', 0)

        # 是否继续抓取
        if total < start + count:
            return False
        return True


# ========================================================== 影集
# 抓取影集
class MovieList():

    # 年份
    year = 2017
    tipNumb = 1
    tipLimit = 28


    # 影集 Url
    def moveListUrl(self):

        urlSting = movieList
        urlSting = urlSting.replace("{year}", str(self.year))
        urlSting = urlSting.replace("{tip}", str(self.tipNumb))
        return urlSting


    # 抓取开始
    def spiderAction(self):

        # 遍历 url
        for tip in range(self.tipNumb, self.tipLimit):

            # 获取 url
            urlString = self.moveListUrl()
            # 获取名字
            name = str(self.year) + "年" + str(self.tipNumb)
            self.spiderMovieList(urlString, name)

            tt = random.randint(1, 4)
            print('sleep:', str(tt), urlString)
            # time.sleep(tt)

            self.tipNumb = self.tipNumb + 1


    # 抓取数据、保存数据 操作
    def spiderMovieList(self, urlString, name):
        # 1. 处理 https
        ssl._create_default_https_context = ssl._create_unverified_context

        # 2. 自定义 User_Agent
        ua_heaeders = {
            "User_Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
        }

        # # 3. 拼接url 创建请求
        # # urlString = baseApi + top250
        # request = urllib.request.Request(urlString, headers=ua_heaeders)
        #
        # # 4. 向指定url地址发送请求
        # response = urllib.request.urlopen(request)
        #
        # # 5. read() 方法读取文件里的全部内容，返回字符串
        # html = response.read()
        # content = html.decode("utf-8")
        #
        # # 6. 保存json
        # file = open("./resource/"+name+".json", "w")
        # file.write(content)

        # 1. 链接数据库
        engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/storm?charset=utf8', echo=False)
        # 2. 创建数据库表
        Base = declarative_base()

        Session = sessionmaker(bind=engine)
        session = Session()

        # 3. 读取文件中的 json
        file = open("./resource/"+name+".json", "r")
        content = json.loads(file.read())
        # content = json.loads(content)

        content = content.get('res', None)
        if content == None:
            return False

        # 获取 影集 内容
        works = content['subjects']

        # 不是影集
        if len(works) == 0:
            print(name + " 不是影集！！！！")
            return False

        # 解析影集
        assemble = content['payload']
        list_id = content['id']
        list = session.query(MovieAlbum).filter_by(douban_id=list_id).first()

        if list == None:
            album = MovieAlbum()
            album.douban_id = list_id
            album.year = self.year
            album.title = assemble['title']
            album.cover_image = assemble['background_img']
            album.cover_image_m = assemble.get('mobile_background_img', "")
            album.description = assemble['description']
            album.works_id = assemble['subject_ids']
            session.add(album)


        # 解析电影列表

        for work in works:

            movie = session.query(Movie).filter_by(movie_douban_id=work['id']).first()
            # 电影不存在时 添加
            if movie == None:
                print("--------", work['title'])
                m = Movie()
                m.movie_name_cn     = work['title']
                m.movie_douban_mark = work['rating']
                m.movie_name_en     = work['orig_title']
                m.movie_doubanUrl   = work['url']
                m.movie_douban_id   = work['id']
                m.movie_cover       = work['cover']
                session.add(m)
            else:
                print("====== 存在的电影:", work['title'])

        session.commit()

def timess():

    pass
    # 数组安全判断
    # dict = {"name":"wxiao",
    #         "age":26}
    # print(dict['name'])
    # print(dict['age'])
    # print(dict.get('sex', "男"))


    # 随机延时
    # for i in range(1, 5):
    #     tt = random.randint(1, 4)
    #     print("-----------------", str(i), "  " , str(tt))
    #     time.sleep(tt)

timess()


# spiderMovieDetial()
# storeTop250()
# 保存电影详细信息
# storeMovieDetial()

# storeMovieDetial()


# top = MovieTop250()
# top.spiderAction()

# soon = MovieComingSoon()
# soon.spiderAction()

list = MovieList()
list.spiderAction()

#
# movie = MovieDetial()
# movie.spiderMpvie()
# print(movie.movieIdList())

















































