#!/usr/bin/python
#-*- coding:utf-8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
from resources import LeemacsResources

class blogEmacsHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('commond: ', 'ls, ')
        self.write(greeting + 'man, whoami...')
    def write_error(self, status_code, **kwargs):
        self.write("Operation is not defined.")
