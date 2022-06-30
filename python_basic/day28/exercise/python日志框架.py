# 作者 ： 赖鑫
# 2022年06月30日17时30分07秒
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s - '
                           '%(process)s:[line:%(lineno)d] - '
                           '%(levelname)s:%(message)s')

# 开始使用日志功能
logging.debug('this is debug log')  # 日志级别10，越高月严格
logging.info('this is info log')  # 20
logging.warning('this is warning log')  # 30
logging.error('this is error log')  # 40
logging.critical('this is critical log')  # 50
