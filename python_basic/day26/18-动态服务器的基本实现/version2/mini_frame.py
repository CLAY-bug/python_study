#!/usr/bin/python
# author luke

import time


def login():
    return "i----login--welcome wangdao website.......time:%s" % time.ctime()


def register():
    return "-----register---welcome wangdao website.......time:%s" % time.ctime()


def profile():
    return "-----profile----welcome wangdao website.......time:%s" % time.ctime()


def application(file_name):
    # 不同的url请求，跳转到不同的函数，以便实现不同的功能
    if file_name == "/login.py":
        return login()
    elif file_name == "/register.py":
        return register()
    else:
        return "not found you page...."
