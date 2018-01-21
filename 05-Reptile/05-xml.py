# 1、BeautifulSoup 安装
#   1. pip3 install beautifulsoup4
#   2. pip3 install lxml
#   3. pip3 install html5lib

# 2、使用
#   1. 创建 : file_object = open('douban.html')
#   2. 使用 :


# 导入 BeautifulSoup
from bs4 import BeautifulSoup
from movie import Movie

# 读取全部 html
file_object = open('douban.html', 'r')


html = file_object.read()
# print(all_the_text)
soup = BeautifulSoup(html)

# 获取标题
# print(soup.find('title'))
# 获取头部
# print(soup.find('header'))

# 读取
cont = soup.find_all(class_="screening-bd")

soup = BeautifulSoup(html)

# ui-slide-content

tags = soup.find_all('li', class_="ui-slide-item")

movies = []

for tag in tags:
    # print("=========================")
    # print(tag)
    # soup.select('li[data-actors]')
    # print(tag.li)

    movie = Movie()
    # 主演
    movie.actors = tag.attrs['data-actors']
    # 导演
    movie.director = tag.attrs['data-director']
    # 时长
    movie.duration = tag.attrs['data-duration']
    # 豆瓣评分
    movie.rate = tag.attrs["data-rate"]
    # 发布地区
    movie.region = tag.attrs["data-region"]
    # 发布时间
    movie.release = tag.attrs["data-release"]
    # 电影名称
    movie.title = tag.attrs["data-title"]
    # 相关视频地址
    movie.trailer = tag.attrs["data-trailer"]
    # 电影封面
    movie.cover = tag.img.attrs["src"]
    # 豆瓣地址
    movie.threadUrl = tag.a.attrs["href"]

    print(movie)
    movies.append(movie)

    # ls = tag.li
    # for li in ls:
    #     print("--------")



# print(cont)


# data-actors="章子怡 / 黄晓明 / 张震"
# data-director="李芳芳"
# data-duration="138分钟"
# data-enough="true"
# data-intro=""
# data-rate="7.4"
# data-rater="99901"
# data-region="中国大陆"
# data-release="2018"
# data-star="40"
# data-ticket="https://movie.douban.com/ticket/redirect/?url=https%3A%2F%2Fm.maoyan.com%2Fcinema%2Fmovie%2F71946%3F_v_%3Dyes%26merCode%3D1000011"
# data-title="无问西东"
# data-trailer="https://movie.douban.com/subject/6874741/trailer">
