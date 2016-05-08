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

# sys.path.append('gitignore')    # 隐私文件

class ConfigUtils(object):
    """
    Operate configuration files
    """
    def __init__(self, ):
        self.db_config = "./gitignore/db.json"
    def get_json_config(self, target_file):
        """
        Get Json configuration file, and return a dictionary
        """
        try: 
            import simplejson as json # 引入 simplejson 用来 json 文件的解析
            
            try: 
                json_obj = json.load(file(target_file))
                return json_obj
            except:
                print 'Error JSON reading with simplejson'
                return False
        except ImportError:
            print 'No module installed named simplejson'
            import json
            
            try: 
                json_obj = json.load(file(target_file))
                return json.dumps(json_obj)
            except:
                print 'Error JSON reading with json'
                return False

            
## Test
# if __name__ == '__main__':
#     sample = ConfigUtils()
#     print sample.db_config
#     print sample.get_json_config(sample.db_config)
