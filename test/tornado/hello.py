# -*- coding: utf-8 -*-
#!/usr/bin/python
import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default = 8888, help = "run on the given port", type = int)

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('inner.html', header_text = "header", footer_text = "footer")

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers = [(r'/', HelloHandler)],
        template_path = os.path.join(os.path.dirname(__file__), "templates"),
        static_path = os.path.join(os.path.dirname(__file__), "static"),
        debug = True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
