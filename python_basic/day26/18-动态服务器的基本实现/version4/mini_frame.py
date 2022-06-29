#!/usr/bin/python
# author luke

import time


def login():
    return "i----login--welcome wangdao website.......time:%s" % time.ctime()


def index():
    return "这是主页"


def register():
    return "-----register---welcome wangdao website.......time:%s" % time.ctime()


def profile():
    return "-----profile----welcome wangdao website.......time:%s" % time.ctime()


def application(environ, start_response):
    # 由mini_frame框架添加响应码和头部
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = environ['PATH_INFO']  # 从environ拿到url
    
    if file_name == "/index.py":
        return index()
    elif file_name == "/login.py":
        return login()
    else:
        return 'Hello World! 我爱你中国....'
