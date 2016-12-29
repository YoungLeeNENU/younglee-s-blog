#-*- coding:utf-8 -*-
#!/usr/bin/python
# @brief: URL router for younglee's personal network
# @author: Young Lee
# @email: youngleemails@gmail.com
# @time: 02-12-2015
# @license GPL V3
import os
import sys
import os.path
import simplejson as json

env_file = file('/var/ylpn/env.json')
env_obj = json.load(env_file)
root = ''
if env_obj['env'] == 'dev': root += '/Users/younglee/Documents/project/github/younglee-s-blog/'
elif env_obj['env'] == 'product': root += '/root/Documents/my-blog/'

sys.path.insert(0, root + 'src/server/config')

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

from navigator import Navigator
from resources import LeemacsResources as resources

# Globals
define("port", default = 8888, help = "Run on the given port", type = int)
define("templates", default = "../client/templates/html/", help = "Template files path", type = str)
define("static", default = "../client/static/", help = "Static files path", type = str)
define("blogs", default = "../server/blogs/", help = "Blog files path", type = str)

class Application(tornado.web.Application):
    '''
    Url Navigation
    '''
    def __init__(self):
        # Navigator
        navigator = Navigator()
        handlers  = navigator.get_handlers()
        # Resources
        settings = dict(
            template_path = os.path.join(os.path.dirname(__file__), options.templates),
            static_path = os.path.join(os.path.dirname(__file__), options.static), # 指定 static path
            debug = True    # TODO: Comment this when the site is done
        )
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    # Load application
    http_server = tornado.httpserver.HTTPServer(Application(), xheaders = True)
    # Listen to given port
    http_server.listen(options.port)
    # Start application
    tornado.ioloop.IOLoop.instance().start()
