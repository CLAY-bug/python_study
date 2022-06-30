# 作者 ： 赖鑫
# 2022年06月30日19时03分17秒

import logging

logging.basicConfig(level=logging.WARNING,
                    filename='./exercise.log',  # 设置日志输出路径
                    filemode='a',  # 设置日志输入模式，与文件读写模式一样
                    format='%(asctime)s - %(filename)s - %(process)d:[line:%(lineno)d]'
                           '%(levelname)s: %(message)s')

logging.debug('this is debug log')  # 日志级别10，越高月严格
logging.info('this is info log')  # 20
logging.warning('this is warning log')  # 30
logging.error('this is error log')  # 40
logging.critical('this is critical log')  # 50
