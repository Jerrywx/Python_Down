
import urllib.request

# 向指定的url地址发送请求，并返回服务器相应的类文件对象

response = urllib.request.urlopen("http://www.80s.tw/")

# 服务器返回的类文件对象支持Python文件对象的操作方法。
# read() 方法就是读取文件里的全部内容, 返回字符串
html = response.read()

# 打印相应内容
print(html.decode("utf-8"))