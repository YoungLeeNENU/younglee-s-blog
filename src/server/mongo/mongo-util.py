#-*- coding:utf-8 -*-
#!/usr/bin/python
# @brief: MongoDb operation for the site
# @author: Young Lee
# @email: youngleemails@gmail.com
# @time: 04-18-2016
# @license GPL V3

import os
import sys
import json
import os.path

from pymongo import MongoClient

class MongoUtils(object):
    def __init__(self, config = None):
        """
        MongoDb operations
        """
        if config == None:
            self.config = {               # Default
                "username": "younglee",   # User
                "host": "108.61.160.134", # Server Ip
                "port": 27017,            # Server Port
                "db":   "blog-site"       # Using db
            }
        else: self.config = config
    def get_config(self, key = None):
        """
        Get specific configuration
        """
        if key == None:
            return self.config
        else:
            try:
                return self.config[key]
            except KeyError:
                return {}
    def db_connect(self, host = None, port = None):
        """
        Connect to MongoDb
        """
        host = host or self.get_config('host')
        port = port or self.get_config('port')
        client = MongoClient(host + ":" + str(port))
        return client

if __name__ == '__main__':
    test = MongoUtils()
    # print test.get_config()
    instance = test.db_connect()
    print dir(instance)
