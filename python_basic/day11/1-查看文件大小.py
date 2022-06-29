# 作者: 王道 龙哥
# 2022年06月10日09时51分21秒
import os
file_info=os.stat('file.txt')
print('size{},uid{},mode{:x},mtime{}'.format(file_info.st_size,file_info.st_uid, \
                                           file_info.st_mode,file_info.st_mtime))
from time import strftime
from time import gmtime
#把秒数转为字符串时间
print(strftime("%Y-%m-%d %H:%M:%S", gmtime(file_info.st_mtime)))
