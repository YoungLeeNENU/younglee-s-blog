#-*- coding:utf-8 -*-
#!/usr/bin/python
# @brief: URL router for younglee's personal network
# @author: Young Lee
# @email: youngleemails@gmail.com
# @time: 02-12-2015
# @license GPL V3
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

from ylpn import youngleePersonalNetwork as ylpn
from eshell import ylpnEshellHandler as eshell
from whoami import manPageHandler as whoami
from leemail import blogEmailHandler as blogemail

from resources import LeemacsResources as resources

define("port", default=8888, help="run on the given port", type=int)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers = [(r"/", ylpn),
                                              (r"/eshell", eshell),
                                              (r"/leemail", blogemail),
                                              (r"/whoami", whoami)])    # 正则表达式 + RequestHandler 类的实例对
    http_server = tornado.httpserver.HTTPServer(app)    # 把 Application 对象传递给 Tornado 的 HTTPServer 对象
    http_server.listen(options.port)    # 侦听端口　通过 define 得到的 port 成为了 options 下的全局变量
    tornado.ioloop.IOLoop.instance().start()    # 创建 Tornado IOloop 实例
