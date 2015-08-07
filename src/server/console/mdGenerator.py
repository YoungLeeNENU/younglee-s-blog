#!/usr/bin/python
# -*- coding: utf-8 -*-
# 根据配置自动生成空的日志 markdown 文件
# 通过轮询动态的更新 HTML
import os, sys
import os.path
import codecs
import markdown
import json

class mdToHtml():
    """
    Markdown 日志生成器
    """
    def __init__(self, conf = {}):
        self._conf = conf    # 设置配置文件
    def getSingleHtml(self, name):
        """
        读取一个 .md 文件，生成一个对应的 .html 文件
        """
        source, target = './', './'
        if self._conf.has_key('md_path'): source = self._conf['md_path']
        if self._conf.has_key('html_path'): target = self._conf['html_path']
        source, target = source + name + '.md', target + name + '.html'
        try:
            md_file = codecs.open(source, 'r', encoding = "utf-8")
            html_file = codecs.open(target, 'w', encoding = "utf-8")
            try:
                md_text = md_file.read()
                # TODO: 字符编码转换
                html_text = markdown.markdown(md_text)
                html_file.write(html_text)
            except IOError:
                html_file.close()
                md_file.close()
            finally:
                md_file.close()
                html_file.close()
        except IOError:
            pass
    def refreshMd(self, conf):    # TODO: 动态更新 HTML
        """
        刷新 Markdown 文件
	"""
        pass

if __name__ == '__main__':
    # 暂时的配置
    config = {
        'md_path': "../markdown/md/",    # markdown 源文件路径
        'html_path': "../markdown/html/"    # 生成 HTML 的路径
    }
    mdGen = mdToHtml(config)
    mdGen.getSingleHtml('hoisting')
