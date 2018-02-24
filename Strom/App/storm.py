# 1、Tornado 基本使用
# 2、html 文件映射
# 3、模板路径配置 (html)
# 4、静态文件配置 (js、css、图片等)
# 5、添加post 接收提交参数
# 6、向html传递参数
# 7、使用模板语言
# 8、模板语言
#       {{}}
#       {% if %} {% endif %}
#       自定义模板语言'
#              1. ui_methods
#              2. ui_modules
# 9、html 调用 Python 语言
# 10、static_url  MD5
# 运行 tornado: python 01-hello.py --port=8000


# 导入了一些Tornado模块
import tornado.httpserver
import tornado.ioloop
import tornado.options
import os
import tornado.web
from StormOp import StormOp, MovieDetial, MovieList, Top250, Online, AlbumDetial, CelDetial
from Company import Company, CompanyEdit
from Spider import Spider

# Tornado包括了一个有用的模块（tornado.options）来从命令行中读取设置。
from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)

# 模板路径配置、静态文件配置
settings = {
    "template_path" : "templates",
    "static_path" : "static",
}

# 路由映射、模板路径配置
application = tornado.web.Application([
    (r"/op", StormOp),
    (r"/spider", Spider),
    (r"/moviedetial", MovieDetial),
    (r"/movielist", MovieList),
    (r"/company", Company),
    (r"/companyEdit", CompanyEdit),
    (r"/top250", Top250),
    (r"/online", Online),
    (r"/album", AlbumDetial),
    (r"/cel", CelDetial)],
    **settings )

# 运行Tornado
if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
