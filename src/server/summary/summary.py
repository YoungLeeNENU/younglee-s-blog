#!/usr/bin/python
#-*- coding:utf-8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
from resources import LeemacsResources

class summaryHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('2016summary.html')
    def write_error(self, status_code, **kwargsd):
        self.write("Operation is not defined.")
