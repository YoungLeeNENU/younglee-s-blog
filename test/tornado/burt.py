#!/usr/bin/python
# -*- coding: utf-8 -*-
import os.path

import tornado.web
import tornado.options
import tornado.httpserver
import tornado.ioloop

from tornado.options import options, define

define("port", default = 8888, help = "run on the given port", type = int)

class BooksHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("books.html",
                    page_title = "Burt's Book|Home",
                    header_text = "Welcome to Burt's Books!")

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r'/', BooksHandler)]
        settings = dict(
            template_path = os.path.join(os.path.dirname(__file__), "templates"),
            static_path = os.path.join(os.path.dirname(__file__), "static"),
            debug = True
        )
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
