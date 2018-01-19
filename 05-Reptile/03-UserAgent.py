import urllib.request
import random

url = "http://www.baidu.com"

ua_list = [
    "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
]

# 在User-Agent列表中随机随机酸则一个User-Agent
user_agent = random.choice(ua_list)

# 构建一个请求
request = urllib.request.Request(url)

# 使用 add_header() 方法 添加/修改 一个HTTP报头
request.add_header("User-Agent", user_agent)

# get_header() 获取一个已有的HTTP报头的值【User-agent】
print(request.get_header("User-agent"))



