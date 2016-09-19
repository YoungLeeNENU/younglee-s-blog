#!/usr/bin/python
#-*- coding:utf-8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
from resources import LeemacsResources

class DayOneHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('day1.html')
    def write_error(self, status_code, **kwargsd):
        self.write("Operation is not defined.")
