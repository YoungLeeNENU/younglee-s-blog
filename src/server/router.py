#!/usr/bin/python
#-*- coding:utf-8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from leemacs import LeemacsHandler
from leeshell import LeeshellHandler
from whoami import WhoamiHandler

from tornado.options import define, options
define("port", default=8888, help="run on the given port", type=int)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", LeemacsHandler),
                                            (r"/leeshell", LeeshellHandler),
                                            (r"/whoami", WhoamiHandler)])    # 正则表达式 + RequestHandler 类的实例对
    http_server = tornado.httpserver.HTTPServer(app)    # 把 Application 对象传递给 Tornado 的 HTTPServer 对象
    http_server.listen(options.port)    # 侦听端口　通过 define 得到的 port 成为了 options 下的全局变量
    tornado.ioloop.IOLoop.instance().start()    # 创建 Tornado IOloop 实例
