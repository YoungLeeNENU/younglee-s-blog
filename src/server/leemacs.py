#!/usr/bin/python
#-*- coding:utf-8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
from resources import LeemacsResources

class LeemacsHandler(tornado.web.RequestHandler, LeemacsResources):
    def get(self):
        self.render('../client/html/leemacs.html')
        # greeting = self.get_argument('greeting', 'Hello')    # 第二个作为默认值
        # self.write(greeting + ', This is Young Lee\'s web log!')    # GET 请求返回的字符串
        # self.write(self._resources._html)    # GET 请求返回的字符串
    def write_error(self, status_code, **kwargs):
        self.write("Operation is not defined.")