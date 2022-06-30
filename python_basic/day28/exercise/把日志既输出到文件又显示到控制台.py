# 作者 ： 赖鑫
# 2022年06月30日19时13分10秒

import logging

# 先创建一个logger对象
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # 设置日志的总开关，低于这个等级的日志将不会显示

# 创建一个handler，一个用于写入日志，一个用于输出控制台
logfile = './exercise.log'  # 写入日志的文件路径
fh = logging.FileHandler(logfile, mode='a')
fh.setLevel(logging.DEBUG)  # 用于输入日志文件的等级开关，小于总开关的日志不会输入

ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)

# 定义日志的输出格式
formatter = logging.Formatter('%(asctime)s - %(filename)s - '
                              '%(process)d:[line:%(lineno)d]'
                              '%(levelname)s: %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 将logger添加到hander里
logger.addHandler(fh)
logger.addHandler(ch)

logging.debug('this is debug log')  # 日志级别10，越高月严格
logging.info('this is info log')  # 20
logging.warning('this is warning log')  # 30
logging.error('this is error log')  # 40
logging.critical('this is critical log')  # 50
