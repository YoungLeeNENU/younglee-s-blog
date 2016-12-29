# -*- coding: utf-8 -*-
#!/usr/bin/python
import os
import sys
import simplejson as json

env_file = file('/var/ylpn/env.json')
env_obj = json.load(env_file)
root = ''
if env_obj['env'] == 'dev': root += '/Users/younglee/Documents/project/github/younglee-s-blog/'
elif env_obj['env'] == 'product': root += '/root/Documents/my-blog/'

sys.path.insert(0, root + 'src/server/homepage') # 主页
sys.path.insert(0, root + 'src/server/console')  # 控制台
sys.path.insert(0, root + 'src/server/gallery')  # 图片
sys.path.insert(0, root + 'src/server/blog')     # 博客
sys.path.insert(0, root + 'src/server/cv')       # 简历
sys.path.insert(0, root + 'src/server/test')     # 测试

# from leemail import blogEmailHandler        as blogemail
from eshell  import ylpnEshellHandler       as eshell
from whoami  import manPageHandler          as whoami
from reframe import ReframeHandler          as reframe
from ylpn    import youngleePersonalNetwork as ylpn

class Navigator(object):
    def __init__(self):
        self._handlers = [ (r"/", reframe),      # Homepage
                           (r"/eshell", eshell),    # Console
                           # (r"/leemail", blogemail), # Email me
                           ("/whoami", whoami),
                           ("/old", ylpn) ]
    def get_handlers(self):
        return self._handlers
