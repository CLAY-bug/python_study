# 作者 ： 赖鑫
# 2022年06月13日19时40分20秒

from distutils.core import setup

setup(name="lx_message",  # 包名
      version="1.0",  # 版本
      description="lx's 发送和接收消息模块",  # 描述信息
      long_description="完整的发送和接收消息模块",  # 完整描述信息
      author="lx",  # 作者
      author_email=" lx@520.com",  # 作者邮箱
      url="www.lx520.com",  # 主页
      py_modules=["lx_message.send_message",
                  "lx_message.receive_message"])