#-*- coding:utf-8 -*-
#!/usr/bin/python
# @brief: Create Database
# @author: Young Lee
# @email: youngleemails@gmail.com
# @time: 04-18-2016
# @license GPL V3

import os
import sys
import os.path

# Third Party
from pymongo    import MongoClient

# Local
from mongo_base import MongoBase

class MongoUtils(MongoBase):
    def __init__(self):
        pass
    def get_database(self):
        """
        @brief: 
        """
        pass


if __name__ == '__main__':
    test = MongoUtils()
    # client = test.db_connect()
    # test.db_disconnect(client)
