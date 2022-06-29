# 作者: 王道 龙哥
# 2022年06月21日09时55分31秒
import re

email_list = ["xiaoWang@163.com", "xiao.Wang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com"]

for email in email_list:
    ret = re.match('\w{4,20}@163\.com$', email)
    if ret:
        print('{} 邮箱符合要求'.format(ret.group()))
    else:
        print('{} 邮箱不符合要求'.format(email))
