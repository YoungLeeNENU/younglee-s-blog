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
import tornado.httputil

from tornado.options import define, options

from resources import LeemacsResources as resources

class youngleePersonalNetwork(tornado.web.RequestHandler):
    def __init(self):    # __init 不是自动执行的
        self._domain = ['外殼', '博文', '圖志', '電郵', '關於']    # 这个应该从数据库中获得
    def get(self):
        self.render('ylpn.html', domain = "* 外殼 *")
    def write_error(self, status_code, **kwargs):
        self.write(status_code, "Operation is not defined.")

