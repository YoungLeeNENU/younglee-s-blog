#!/usr/bin/python
#-*- coding:utf-8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
from resources import LeemacsResources

class manPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('man-younglee.html')
    def write_error(self, status_code, **kwargsd):
        self.write("Operation is not defined.")
    # def get(self):
    #     aboutme = self.get_argument('', '李旸:')
    #     self.write(aboutme + '1991年程序员')
    # def write_error(self, status_code, **kwargsd):
    #     self.write("Operation is not defined.")
