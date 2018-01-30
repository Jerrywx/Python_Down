import urllib.request
import ssl
import json
# import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String, MetaData, Boolean, Float
from sqlalchemy.orm import sessionmaker, relationship
import sys
sys.path.append("../sqlManager")
from dataManager import Movie

type = ["热门", "最新", "经典", "可播放", "豆瓣高分",
        "冷门佳片", "华语", "欧美", "韩国", "日本",
        "动作", "喜剧", "爱情", "科幻", "悬疑", "恐怖", "治愈"]

baseUrl = "https://movie.douban.com/j/search_subjects"


ssl._create_default_https_context = ssl._create_unverified_context

ua_heaeders = {
    "User_Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}

# 通过 urllib.request() 方法构造一个请求对象
# request = urllib.request.Request("http://www.80s.tw/", headers = ua_heaeders)
# 热门
# urlString = "https://movie.douban.com/j/search_subjects?type=movie&tag=%e7%83%ad%e9%97%a8&sort=recommend&page_limit=100&page_start=300"
# 最新
urlString = "https://movie.douban.com/j/search_subjects?type=movie&tag=%e6%9c%80%e6%96%b0&sort=recommend&page_limit=100&page_start=500"
# 豆瓣高分
# urlString = "https://movie.douban.com/j/search_subjects?type=movie&tag=%e8%b1%86%e7%93%a3%e9%ab%98%e5%88%86&sort=recommend&page_limit=100&page_start=0"
# 冷梦佳片
# urlString = "https://movie.douban.com/j/search_subjects?type=movie&tag=%e5%86%b7%e9%97%a8%e4%bd%b3%e7%89%87&sort=recommend&page_limit=100&page_start=500"
#
# urlString = "https://movie.douban.com/j/search_subjects?type=movie&tag=%e5%8d%8e%e8%af%ad&sort=recommend&page_limit=100&page_start=100"


request = urllib.request.Request(urlString, headers=ua_heaeders)

# 向指定url地址发送请求
response = urllib.request.urlopen(request)

# read() 方法读取文件里的全部内容，返回字符串
html = response.read()

# 打印网页内容
# print(html.decode("utf-8"))

file = open("./resource/list2.json", "w")
file.write(html.decode("utf-8"))



# ------- 存储数据
# 1. 链接数据库
engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/storm?charset=utf8', echo=False)
# 2. 创建数据库表
Base = declarative_base()

# =============================================================================================
# 读取json文件
# file = open("./resource/list.json", "r")
# content = json.loads(file)

# 读取web内容
content = json.loads(html.decode("utf-8"))


movies = []
Session = sessionmaker(bind=engine)
session = Session()

movieList = content['subjects']

if len(movieList) > 0:

    # 遍历数据
    for item in content['subjects']:

        # 检查电影是否存在
        ret = session.query(Movie).filter_by(movie_douban_id=item['id']).first()
        if ret:
            print("---- 存在的电影:" + item['title'])
        else:
            print("===== 不存在的电影:" + item['title'])

            movie = Movie()

            movie.movie_name_cn     = item['title']
            movie.movie_douban_mark = item['rate']
            movie.movie_cover       = item['cover']
            movie.movie_doubanUrl   = item['url']
            movie.movie_douban_id   = item['id']

            # movies.append(movie)

            session.add(movie)

else:
    print("--------- 数据为空 ---------")

session.commit()


# print(movies)



# session.add_all(movies)
# session.commit()










