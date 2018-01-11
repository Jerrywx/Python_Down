
import urllib.request

# User-Agent 是爬虫和反扒虫斗争的第一步
ua_heaeders = {
    "User_Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}

# 通过 urllib.request() 方法构造一个请求对象
request = urllib.request.Request("http://www.baidu.com", headers = ua_heaeders)

# 向指定url地址发送请求
response = urllib.request.urlopen(request)

# read() 方法读取文件里的全部内容，返回字符串
html = response.read()

# 打印网页内容
print(response.getcode())
print(response.geturl())


