#!/usr/bin/python
# -*- coding: utf-8 -*-
# @brief: 单独开辟一个(守护)线程，做文件嗅探使用
# TODO: 文件夹：增/删/重命名
# TODO: 文件：增/删/重命名
# TODO: 线程池优雅控制的问题
# TODO: 如何关闭守护线程的问题
# @author: Young Lee
# @email: youngleemails@gmail.com
# @time: 01-03-2017
# @license GPL V3
from __future__ import unicode_literals
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import codecs
import hashlib
import traceback
import threading
from copy import deepcopy
from time import sleep, ctime
from pprint import pprint
import uniout

root = '/var/ylpn/ylpn-data/'

class ThreadCtrl(threading.Thread):
    """ """
    def __init__(self, func, args, name = ''):
        """ """
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name
    def run(self, ):
        """ """
        self.func(self.args)

class FileSniffer():
    """
    File Sniffering
    """
    def __init__(self, ):
        self.files_record = []
    def sniffering(self, dirpath):
        """
        嗅探文件的修改
        """
        while True:
            try:
                print '... Sniffering ...'
                record = self._walk(dirpath) # 一次 walk 的结果
                if self.files_record == record:
                    pass
                else:
                    self._diff(self.files_record, record)
                    self.files_record = record
                sleep(1)
            except Exception:
                break
    def _diff(self, cache, record):
        """
        检查最新更新的文件和文件夹
        """
        print "... Diffing ..."
        pprint (cache)
        pprint (record)
        _cache, _record = deepcopy(cache), deepcopy(record)
        _cache.reverse()
        _record.reverse()
    def _walk(self, dirpath):
        """
        遍历指定的路径
        """
        files_record = []
        def path_adjust(raw_path):
            """
            处理 walk 结果的路径末尾的 / 问题
	    """
            if raw_path[-1:] == '/': return raw_path
            else: return raw_path + '/'
        def exclude_rule(name):
            """
            排除 emacs 和 vi/vim 的编辑态下的临时文件
	    """
            if name[:2] == '.#': return False # emacs
            if name[-4:] == '.swp': return False # vi/vim
            return True
        try:
            for e in os.walk(dirpath):
                dirpath, dirnames, raw_filenames, filenames = e[0], e[1], filter(exclude_rule, e[2]), []
                for f in raw_filenames:
                    fp = open(path_adjust(dirpath) + f, 'rb')
                    md5obj = hashlib.md5()
                    md5obj.update(fp.read())
                    hash_key = md5obj.hexdigest() # 文件哈希
                    # file_info = { 'filename': (path_adjust(dirpath) + f).decode('utf8'),
                    file_info = { 'filename': path_adjust(dirpath) + f,
                                  'md5': hash_key }
                    filenames.append(file_info)
                files_record.append({ 'dirpath': dirpath,
                                      'dirnames': dirnames,
                                      'filenames': filenames })
        except Exception, e:
            traceback.print_exc()
        return files_record

class DaemonicFileSniffer():
    """
    """
    def __init__(self, ):
        """
        TODO 线城池的控制这里弱智了一点
        """
        self.f_sniffer = FileSniffer()
        self.thread = []        # 线程池
        t = ThreadCtrl(self.f_sniffer.sniffering, (root), self.f_sniffer.sniffering.__name__)
        self.thread.append(t)
    def start(self, daemonic):
        """
        开始运行一个线程
        """
        self.thread[0].setDaemon(daemonic)
        self.thread[0].start()
    def isAlive(self, ):
        """
        判断线程是否还在运行
        """
        return self.thread[0].isAlive()
    def join(self, timeout = None):
        """
        主线程挂起，直到线程池里的线程结束，timeout 是挂起时间
        """
        self.thread[0].join(timeout)

# Test
if __name__ == '__main__':
    f_sniffer = FileSniffer()
    f_sniffer.sniffering(root)

    # file_sniffer = DaemonicFileSniffer()
    # file_sniffer.start(False)
    # file_sniffer.join(4)
