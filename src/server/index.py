#-*- coding:utf-8 -*-
#!/usr/bin/python
# @brief: URL router for younglee's personal network
# @author: Young Lee
# @email: youngleemails@gmail.com
# @time: 02-12-2015
# @license GPL V3
import os.path

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

# Globals
define("port", default = 8888, help = "run on the given port", type = int)
define("templates", default = "../client/templates/", help = "template files path", type = str)
define("static", default = "../client/static/", help = "static files path", type = str)
define("blogs", default = "../server/blogs/", help = "blog files path", type = str)

class Application(tornado.web.Application):
    '''
    定义 URL 导航和资源位置
    '''
    def __init__(self):
        # Navigator
        handlers = [(r"/", ylpn),
                    # (r"/eshell", eshell),
                    # (r"/leemail", blogemail),
                    # (r"/whoami", whoami)
        ]
        # Resources
        settings = dict(
            template_path = os.path.join(os.path.dirname(__file__), options.templates),
            static_path = os.path.join(os.path.dirname(__file__), options.static),
            debug = True    # TODO: Comment this when the site is done
        )
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())    # Load application
    http_server.listen(options.port)    # Listen to given port
    tornado.ioloop.IOLoop.instance().start()    # Start application
