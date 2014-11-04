#!/usr/bin/python
#-*- coding:utf-8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)

class LeemacsHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')    # 第二个作为默认值
        self.write(greeting + ', This is Young Lee\'s web log!')    # GET 请求返回的字符串

class LeeshellHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('commond: ', 'ls, ')
        self.write(greeting + 'man, whoami...')

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", LeemacsHandler),
                                            (r"/leeshell", LeeshellHandler)])    # 正则表达式 + RequestHandler 类的实例对
    http_server = tornado.httpserver.HTTPServer(app)    # 把 Application 对象传递给 Tornado 的 HTTPServer 对象
    http_server.listen(options.port)    # 侦听端口　通过 define 得到的 port 成为了 options 下的全局变量
    tornado.ioloop.IOLoop.instance().start()    # 创建 Tornado IOloop 实例
