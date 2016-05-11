#-*- coding:utf-8 -*-
#!/usr/bin/python
# @brief: MongoDb operation for the site
# @author: Young Lee
# @email: youngleemails@gmail.com
# @time: 04-18-2016
# @license GPL V3

import os
import sys
import os.path

from pymongo import MongoClient

sys.path.append('../config')              # 配置目录

from config import ConfigUtils

class MongoBase(object):
    def __init__(self, dft_config = None):
        """
        MongoDb operations
        """
        if dft_config == None:
            config_utils = ConfigUtils()
            self.config = config_utils.parse_json_config(config_utils.db_config)
        else: self.config = dft_config    # 如果有默认的配置使用之
    def _get_config(self, key = None):
        """
        @brief: Get specific configuration
        """
        if key == None:
            return self.config
        else:
            try:
                return self.config[key]
            except KeyError:
                return {}
    def db_connect(self, host = None, port = None):   # 加上多用户要重写
        """
        @brief: Connect to MongoDb
        """
        host = host or self._get_config('host')
        port = port or self._get_config('port')
        client = MongoClient(host + ":" + str(port))
        return client
    def db_disconnect(self, client):
        """
        @brief: Disconnect to MongoDb
        """
        try:
            client.close();
            print dir(client)
        except:
            print 'Close connection failed'
            return -1
        

# if __name__ == '__main__':
#     test = MongoBase()
#     client = test.db_connect()
#     test.db_disconnect(client)
