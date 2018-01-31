
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
# # User-Agent 是爬虫和反扒虫斗争的第一步
ua_heaeders = {
    "User_Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}

# 通过 urllib.request() 方法构造一个请求对象
# request = urllib.request.Request("http://www.80s.tw/", headers = ua_heaeders)
request = urllib.request.Request("https://movie.douban.com/", headers = ua_heaeders)

# 向指定url地址发送请求
response = urllib.request.urlopen(request)

# read() 方法读取文件里的全部内容，返回字符串
html = response.read()

# 打印网页内容
print(html.decode("utf-8"))



# ======================================================================

# proxySwitch = True
#
# httpproxy_handler = urllib.request.ProxyHandler({"http":"61.135.217.7:80"})
#
# nullproxy_handler = urllib.request.ProxyHandler({})
#
# if proxySwitch:
#     opener = urllib.request.build_opener(httpproxy_handler)
# else:
#     opener = urllib.request.build_opener(nullproxy_handler)
#
# urllib.request.install_opener(opener)
#
# # # 构建一个HTPHandler处理器对象, 支持处理HTTP请求
# # http_handler = urllib.request.HTTPHandler(debuglevel=1)
# #
# # # 调用 build_opener() 自定义一个 opener 对象
# # opener = urllib.request.build_opener(http_handler)
#
# request = urllib.request.Request("https://movie.douban.com/", headers = ua_heaeders)
#
# response = opener.open(request)
#
# html = response.read()
# print(html.decode("utf-8"))



