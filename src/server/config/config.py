# -*- coding: utf-8 -*-
#!/usr/bin/python
# @brief: Get configuration file
# @author: Young Lee
# @email: youngleemails@gmail.com
# @time: 05-06-2016
# @license GPL V3

import os
import sys
import os.path

from resources import SiteResources as BaseResources

root = '/root/Documents/my-blog/src/server/'
# root = '/Users/younglee/Documents/project/github/younglee-s-blog/src/server/'

sys.path.insert(0, root + 'config/gitignore')    # 隐私文件

class ConfigUtils(object):
    """
    @brief: Operate configuration files
    """
    def __init__(self, ):
        baseResources = BaseResources()

        self.db_config = file(baseResources.get_db_config_file())
    def parse_json_config(self, target_file):

        """
        @brief: Get Json configuration file, and return a dictionary
        """
        try:
            if isinstance(target_file, str):
                target_file = file(target_file)
            import simplejson as json # 引入 simplejson 用来 json 文件的解析

            try:
                json_obj = json.load(target_file)
                return json_obj
            except:
                print 'Error JSON reading with simplejson'
                return False
        except ImportError:
            print 'No module installed named simplejson'
            import json

            try:
                if isinstance(target_file, str):
                    target_file = file(target_file)
                json_obj = json.load(target_file)
                return json.dumps(json_obj)
            except:
                print 'Error JSON reading with json'
                return False

# if __name__ == '__main__':
#     sample = ConfigUtils()
#     print sample.parse_json_config(sample.db_config)
