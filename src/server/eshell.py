#!/usr/bin/python
#-*- coding:utf-8 -*-
# @brief: eshell for younglee's personal network
# @author: Young Lee
# @email: youngleemails@gmail.com
# @time: 02-12-2015
# @license GPL V3
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import textwrap

from tornado.options import define, options

from resources import LeemacsResources as resources

class ylpnEshellHandler(tornado.web.RequestHandler):
    def get(self):
        # print self.get_argument('a')
        # print self.get_argument('b')
        greeting = self.get_argument('commond: ', 'ls, ')
        test = {
            'a': 1,
            'b': 2
        }
        self.write(test)
    def post(self):
        text = self.get_argument('text')
        width = self.get_argument('width', 40)
        self.write(textwrap.fill(text, int(width)))
    def write_error(self, status_code, **kwargs):
        self.write(status_code, "Operation is not defined.")
