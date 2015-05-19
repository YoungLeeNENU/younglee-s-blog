#!/usr/bin/python
# -*- coding: utf-8 -*-
# 根据配置自动生成空的日志 markdown 文件
import os, sys
import sys.path
import markdown

class mdGenerator():
    """
    Markdown 日志生成器
    """
    def __init__(self, conf):
        self._conf = conf
    def setConfig(self, conf):
        """
        修改 Markdown 文件的配置
	"""
        pass
    def touchMd(self, conf):
        """
        在相关目录创建新的 Markdown 文件
        """
        pass
    def refreshMd(self, conf):
        """
        刷新 Markdown 文件
	"""
        pass

if __name__ == '__main__':
    config = {
        
    }
    instance = mdGenerator(conf)
