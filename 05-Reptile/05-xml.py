# 1、BeautifulSoup 安装
#   1. pip3 install beautifulsoup4
#   2. pip3 install lxml
#   3. pip3 install html5lib

# 2、使用
#   1. 创建 : file_object = open('douban.html')
#   2. 使用 :


# 导入 BeautifulSoup
from bs4 import BeautifulSoup

file_object = open('douban.html')
html = file_object.read()
# print(all_the_text)
soup = BeautifulSoup(html)

# 获取标题
# print(soup.find('title'))
# 获取头部
# print(soup.find('header'))


cont = soup.find_all(class_="screening-bd")
print(cont)
