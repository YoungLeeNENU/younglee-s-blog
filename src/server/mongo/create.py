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

from pymongo      import MongoClient
from mongo_config import MongoUtils  as MongoBase

class MongoCreate(MongoBase):
    def __init__(self):
        pass
