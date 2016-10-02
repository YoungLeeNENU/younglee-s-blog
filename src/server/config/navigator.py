# -*- coding: utf-8 -*-
#!/usr/bin/python
import os
import sys

root = '/root/Documents/my-blog/src/server/'
# root = '/Users/younglee/Documents/project/github/younglee-s-blog/src/server/'

# sys.path.insert('../')          # 根目录
sys.path.insert(0, root + 'homepage')     # 主页
sys.path.insert(0, root + 'console')      # 控制台
sys.path.insert(0, root + 'gallery')      # 图片
sys.path.insert(0, root + 'blog')         # 博客
sys.path.insert(0, root + 'cv')           # 简历
sys.path.insert(0, root + 'test')         # 测试
sys.path.insert(0, root + 'dayone')         # day1


# from leemail import blogEmailHandler        as blogemail
from eshell  import ylpnEshellHandler       as eshell
from whoami  import manPageHandler          as whoami
from ylpn    import youngleePersonalNetwork as ylpn
from dayone  import DayOneHandler           as dayone

class Navigator(object):
    def __init__(self):
        self._handlers = [ (r"/",        ylpn),      # Homepage
                           (r"/eshell",  eshell),    # Console
                           # (r"/leemail", blogemail), # Email me
                           ("/whoami",   whoami) ]
    def get_handlers(self):
        return self._handlers
