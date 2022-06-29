# 作者: 王道 龙哥
# 2022年06月20日16时32分22秒
# 导入re模块
import re

# 使用match方法进行匹配操作
result = re.match('wangdao', 'wangdao.cn')

# 如果上一步匹配到数据的话，可以使用group方法来提取数据
print(result.group())