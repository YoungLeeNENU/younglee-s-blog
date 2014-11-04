#!/usr/bin/python
#-*- coding:utf-8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

class LeemacsHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')    # 第二个作为默认值
        self.write(greeting + ', This is Young Lee\'s web log!')    # GET 请求返回的字符串

