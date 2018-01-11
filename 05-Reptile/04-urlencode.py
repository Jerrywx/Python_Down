
import urllib.request
import urllib
from urllib import urlencode

url = "http://www.baidu.com/s"

headers = {"User-Agent" : "Mozilla....."}

keyword = "哈哈"#raw_input("请输入:")
wd = {"wd" : keyword}

# wd = urllib.request.urlencode(wd)
wd = urlencode(wd)

print(wd)

