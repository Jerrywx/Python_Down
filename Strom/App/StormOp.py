

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

# 请求处理函数类
class StormOp(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # 返回内容

        self.render('StormOp.html')

    def post(self, *args, **kwargs):
        name = self.get_argument("name")

        # INPUTS_LIST.append(name)
        self.render('StormOp.html')