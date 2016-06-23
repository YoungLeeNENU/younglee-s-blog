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
import datetime

from pymongo       import MongoClient
from bson.objectid import ObjectId

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
        except:
            print 'Close connection failed'
            return -1
    def insert_doc(self, insert_type = "normal"):
        """
        @brief: Insert
        """
        if insert_type == "normal":
            pass
        elif insert_type == "bulk":
            pass
        else:
            print "Not a valid insert type"
            return
    def update_doc(self):
        """
        @brief: Update
        """
        pass
    def save_doc(self):
        """
        @brief: Save
        """
        pass
    def querying_one(self, cond):
        """
        @breif: querying_one
        """
        pass
    def querying_many(self, cond):
        """
        @breif: querying_many
        """
        pass
    def counting(self, bson):
        """
        @brief: 
        """
        return bson.count()

                
if __name__ == '__main__':
    test = MongoBase()
    
    client = test.db_connect('127.0.0.1', 27017)   # connect db
    
    db = client['a'];           # use a
    
    # for x in dir(db):
    #     print x
    # print db, db.name
    
    post = {
        "author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()
    }
    posts = db.a                                         # use posts
    print posts, posts.name
    post_id = posts.insert_one(post).inserted_id # db.posts.insert(...)
    print posts.find({ 'author': 'Mike' }).count()   # db.posts.find()
    test.db_disconnect(client)
