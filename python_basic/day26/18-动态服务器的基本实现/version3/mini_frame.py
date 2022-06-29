#!/usr/bin/python
# author luke

import time


def login():
    return "i----login--welcome wangdao website.......time:%s" % time.ctime()


def register():
    return "-----register---welcome wangdao website.......time:%s" % time.ctime()


def profile():
    return "-----profile----welcome wangdao website.......time:%s" % time.ctime()


def application(environ, start_response):
    # 由mini_frame框架添加响应码和头部
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    return 'Hello World! 我爱你中国....'
