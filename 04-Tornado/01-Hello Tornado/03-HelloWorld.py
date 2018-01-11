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


import tornado.ioloop
import tornado.web
import uimethod as mt
import uimodule as md

INPUTS_LIST = []

class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # 返回内容
        # self.write("Hello World!")
        self.render('index.html', list=INPUTS_LIST)

    def post(self, *args, **kwargs):
        name = self.get_argument("name")

        INPUTS_LIST.append(name)
        self.render('index.html', list=INPUTS_LIST)

        # self.write("哈哈😁" + name)

# 模板路径配置、静态文件配置
settings = {
    "template_path" : "template",
    "static_path" : "static",
    'ui_methods': mt,
    'ui_modules' : md,
}

#


# 路由映射、模板路径配置
application = tornado.web.Application([
    (r"/index", MainHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()