#!/usr/bin/python
#-*- coding:utf-8 -*-
# @brief: Home page for Young Lee's personal network
# @author: Young Lee
# @email: youngleemails@gmail.com
# @time: 02-12-2015
# @license GPL V3
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

from resources import LeemacsResources as resources

class youngleePersonalNetwork(tornado.web.RequestHandler):
    def get(self):
        # print self._resins._html
        self.render('../client/html/ylpn.html')
        # greeting = self.get_argument('greeting', 'Hello')    # 第二个作为默认值
        # self.write(greeting + ', This is Young Lee\'s web log!')    # GET 请求返回的字符串
        # self.write(self._resources._html)    # GET 请求返回的字符串
    def write_error(self, status_code, **kwargs):
        self.write(status_code, "Operation is not defined.")
