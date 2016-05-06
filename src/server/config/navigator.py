# -*- coding: utf-8 -*-
#!/usr/bin/python
import os
import sys

sys.path.append('../')          # 根目录
sys.path.append('homepage')     # 主页
sys.path.append('console')      # 控制台
sys.path.append('gallery')      # 图片
sys.path.append('blog')         # 博客
sys.path.append('cv')           # 简历
sys.path.append('test')         # 测试

from ylpn    import youngleePersonalNetwork as ylpn
from eshell  import ylpnEshellHandler       as eshell
from whoami  import manPageHandler          as whoami
# from leemail import blogEmailHandler        as blogemail

class Navigator(object):
    def __init__(self):
        self._handlers = [ (r"/",        ylpn),      # Homepage
                           (r"/eshell",  eshell),    # Console
                           # (r"/leemail", blogemail), # Email me
                           ("/whoami",   whoami) ]   # CV
    def get_handlers(self):
        return self._handlers
