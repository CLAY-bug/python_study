# 作者 ： 赖鑫
# 2022年06月21日21时00分15秒

import re

text = "大数据,数理统计，机器学习，sklearn，高性能，大并发"
ret = re.search('[a-z]+', text)
print(ret.group())
