# -*- coding: utf-8 -*-
#!/usr/bin/python
from ylpn    import youngleePersonalNetwork as ylpn
from eshell  import ylpnEshellHandler       as eshell
from whoami  import manPageHandler          as whoami
from leemail import blogEmailHandler        as blogemail

class SiteNavigator(object):
    def __init__(self):
        self._handlers = [ (r"/",        ylpn),          # Index page
                           (r"/eshell",  eshell),       # Operations on eshell
                           (r"/leemail", blogemail),    # Email me
                           ("/whoami",   whoami) ]      # Man page
    def get_handlers(self):
        return self._handlers
