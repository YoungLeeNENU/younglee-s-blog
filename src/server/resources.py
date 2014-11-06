#!/usr/bin/python
#-*- coding:utf-8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

class LeemacsResources():
    def __init__(self):
        self._html = '../client/html/'
        self._css = '../client/css/'
        self._js = '../client/css/'
        self._statusMap = {
            400: self._html + 'status/400.html',
            404: self._html + 'status/404.html',
            405: self._html + 'status/405.html',
            500: self._html + 'status/500.html'
        }
