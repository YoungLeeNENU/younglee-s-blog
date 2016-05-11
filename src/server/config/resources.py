#!/usr/bin/python
#-*- coding:utf-8 -*-
import os
import sys
import os.path

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

class SiteResources(object):
    """
    @brief: define resources for the site
    """

    def __init__(self, ):
        """
        """
        self.resources = {
            'configs': {
                'pathname': '/var/ylpn/config/',
                'db_config': {
                    'mongo': {
                        'filename': 'db.json'
                        # ...
                    },
                    'mysql': { # ...
                    },
                    'redis': { # ...
                    },
                    # ...
                }
            }
        }
        self.site_configs = '/config'
    def get_db_config_file(self, ):
        """
        @brief: Get db config file location
	"""
        try:
            pathname = self.resources['configs']['pathname']
            filename = self.resources['configs']['db_config']['mongo']['filename']
            return pathname + filename
        except KeyError:
            return None


# if __name__ == '__main__':
#     sample = SiteResources()
#     print sample.get_db_config_file()
