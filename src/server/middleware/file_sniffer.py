#!/usr/bin/python
# -*- coding: utf-8 -*-
# @brief: 单独开辟一个线程，做文件嗅探使用
# @author: Young Lee
# @email: youngleemails@gmail.com
# @time: 01-03-2017
# @license GPL V3
import os, sys
import hashlib
import os.path
import traceback
import time
import threading
import daemon

root = '/var/ylpn/ylpn-data/'

class FileSniffer():
    """ File Sniffering """
    def __init__(self, ):
        """ Construct """
        self.files_record = None
        self.threads = []
    def sniffering(self, file_change_cb = None):
        """ Sniffering for file/folder changes """
        while True:
            try:
                print 'sniffering...'
                record = self._walk() # 一次 walk 的结果
                print record
                if self.files_record == record:
                    pass
                else:
                    self._diff(self.files_record, record)
                    self.files_record = record
                time.sleep(10)
            except Exception:
                break
    def _diff(self, cache, record):
        """ Diffing between files and folders """
        print "diffing..."
    def _walk(self, ):
        """ Walking through the folders """
        files_record = []
        def path_adjust(raw_path):
            if raw_path[-1:] == '/': return raw_path
            else: return raw_path + '/'
        try:
            for e in os.walk(root):
                dirpath, dirnames, raw_filenames, filenames = e[0], e[1], e[2], []
                for f in raw_filenames:
                    fp = open(path_adjust(dirpath) + f, 'rb')
                    md5obj = hashlib.md5()
                    md5obj.update(fp.read())
                    hash_key = md5obj.hexdigest() # 文件哈希
                    file_info = { 'filename': dirpath + '/' + f,
                                  'md5': hash_key }
                    filenames.append(file_info)
                files_record.append({ 'dirpath': dirpath,
                                           'dirnames': dirnames,
                                           'filenames': filenames })
        except Exception, e:
            # TODO: 这里不太清楚应该放什么处理方式
            print 'can\'t walk'
        return files_record

# Test
if __name__ == '__main__':
    f_sniffer = FileSniffer()
    f_sniffer.sniffering()
