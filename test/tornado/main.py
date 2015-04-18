#!/usr/bin/python
# -*- coding: utf-8 -*-
import os.path
import random

import tornado.httpserver
import tornado.options
import tornado.ioloop
import tornado.web

from tornado.options import options, define
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # index.html 中包括要提交的表单
        self.render('index.html')

class MungedPageHandler(tornado.web.RequestHandler):
    def map_by_first_letter(self, text):
        
    def post(self):
        self.render()

if __name__ == '__main__':
    pass
