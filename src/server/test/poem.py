# -*- coding: utf-8 -*-
#!/usr/bin/python
import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
from tornado.template import Template
define("port", default = 8888, help="run on the given port", type = int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        return self.render('index.html')

class PoemPageHandler(tornado.web.RequestHandler):
    def post(self):
        noun1 = self.get_argument('noun1')
        noun2 = self.get_argument('noun2')
        verb = self.get_argument('verb')
        noun3 = self.get_argument('noun3')
        # Map from html A to html B, will call template functions when render.
        self.render('poem.html', roads = noun1, wood = noun2, made = verb, difference = noun3)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers = [(r'/', IndexHandler), (r'/poem', PoemPageHandler)],
        # Additional template_path parameter
        template_path = os.path.join(os.path.dirname(__file__), "../client/html/template")
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
