# 导入了一些Tornado模块
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

# Tornado包括了一个有用的模块（tornado.options）来从命令行中读取设置。
from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)

# 请求处理函数类
#
class IndexHandler(tornado.web.RequestHandler):
    # get 方法
    def get(self):
        # 获取参数
        greeting = self.get_argument('greeting', 'Hello')
        # 以一个字符串作为函数的参数，并将其写入到HTTP响应中。
        self.write(greeting + ', friendly user!\n')

# 运行Tornado
if __name__ == "__main__":
    # Tornado的options模块来解析命令行
    tornado.options.parse_command_line()
    # 创建一个Tornado的Application类的实例
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


# python 01-hello.py --port=8000