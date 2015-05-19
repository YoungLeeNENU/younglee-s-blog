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
import json

from tornado.options import define, options

from resources import LeemacsResources as resources

class youngleePersonalNetwork(tornado.web.RequestHandler):
    def get(self):
        self.render('ylpn.html',
                    domain = self.get_domain_str(0),
                    domains = self.get_domain(),
                    test = self._domain,
                    jsonload = json.loads,
                    jsondump = json.dumps,
        )
    def get_domain(self):
        JSONdomain = {
            '攻殼': "d:rwxr--r--:younglee:4096",
            '博文': "d:rwxr--r--:younglee:4096",
            '圖志': "d:rwxr--r--:younglee:4096",
            '電郵': "d:rwxr--r--:younglee:4096",
            '關於': "-:rwxr--r--:younglee:0"    # 这个应该从数据库中获得
        }
        self._domain = json.dumps(JSONdomain)
        return ['攻殼', '博文', '圖志', '電郵', '關於']
    def get_domain_str(self, dft = 0):
        """
        dft: 默认的域
	"""
        domain_info = self.get_domain()[dft]
        domain_str  = " ".join(["*", domain_info, "*"])
        return domain_str
    def write_error(self, status_code, **kwargs):
        self.write(status_code, "Operation is not defined.")
