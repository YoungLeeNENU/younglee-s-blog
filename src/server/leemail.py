#!/usr/bin/python
#-*- coding:utf-8 -*-
import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
from resources import LeemacsResources

class LeemailHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('leemail.html')        
