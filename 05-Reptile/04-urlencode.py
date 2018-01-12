
import urllib.request
import urllib.parse
# from urllib import urlencode

url = "http://www.80s.tw/"

ua_heaeders = {
    # "User_Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0 Mobile/15C153 Safari/604.1"
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    # "Host":"www.80s.tw:443",
    # "Proxy-Connection":"keep-alive"

}

keyword = "哈哈"#raw_input("请输入:")
wd = {"wd" : keyword}

wd = urllib.parse.urlencode(wd)

fullurl = url + "?" + wd


request = urllib.request.Request(url, headers=ua_heaeders)

response = urllib.request.urlopen(request)

html = response.read()

print(html.decode("utf-8"))
