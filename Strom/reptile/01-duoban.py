
import urllib.request
import ssl
from bs4 import BeautifulSoup
# from actor import Actor

# ssl._create_default_https_context = ssl._create_unverified_context
# # User-Agent 是爬虫和反扒虫斗争的第一步
# ua_heaeders = {
#     "User_Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
# }
#
# # 通过 urllib.request() 方法构造一个请求对象
# # request = urllib.request.Request("http://www.80s.tw/", headers = ua_heaeders)
# request = urllib.request.Request("https://movie.douban.com/subject/26004132/?from=showing", headers = ua_heaeders)
#
# # 向指定url地址发送请求
# response = urllib.request.urlopen(request)
#
# # read() 方法读取文件里的全部内容，返回字符串
# html = response.read()
#
# # 打印网页内容
# print(html.decode("utf-8"))


file_object = open('01.html', 'rb')

html = file_object.read()

soup = BeautifulSoup(html)



# span property="v:itemreviewed"



# 1、---- 抓取电影名称
names = soup.find('body').find_all(property="v:itemreviewed")
movieName = names[0].get_text()
# print(movieName)

# 2、---- 抓取电影信息
movieInfo = soup.find('body').find_all(id="info")
# print(movieInfo)

# 1. 获取主演列表
actor = movieInfo[0].find_all('span', class_="actor")
# for actor in actor[0].find_all('a'):
    # 主演名称
    # print(actor.get_text())
    # 主演豆瓣主页
    # print(actor.attrs["href"])

# 2. 导演
actor = movieInfo[0].find('a')
# # 导演
# print(actor.get_text())
# # 导演主页
# print(actor.attrs["href"])

# 3. 编剧
list = movieInfo[0].find_all('span')[3]

# for a in list.find_all('a'):
    # # 编辑
    # print(a.get_text())
    # # 编辑主页
    # print(a.attrs["href"])


# 4. 类型
type = movieInfo[0].find_all('span')
for span in type:
    if 'property' in span.attrs:
        if span.attrs['property'] == "v:genre":
            # 类型
            print(span.get_text())
        elif span.attrs['property'] == "v:initialReleaseDate":
            # 上映日期
            print(span.get_text())
        elif span.attrs['property'] == "v:runtime":
            # 片长
            print(span.get_text())

    if span.get_text().startswith("IMDb链接:"):
        # "IMDb链接:"
        print(span.next_sibling.next_sibling.attrs['href'])

    elif "制片国家/地区:" in span.get_text():
        print(span.next_sibling)
    elif "语言:" in span.get_text():
        print(span.next_sibling)
    elif "又名:" in span.get_text():
        print(span.next_sibling)

# 5. 上映日期



# print(movieInfo[0].stripped_strings)

# for string in movieInfo[0].stripped_strings:
#     print(repr(string))


print(movieInfo[0])









