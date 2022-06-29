# 作者: 王道 龙哥
# 2022年06月21日10时00分35秒
import re

# 使用|
ret = re.match('[1-9]?\d$|100$', '100')
print(ret.group())

# 需求：匹配出163、126、qq邮箱
email_list = ["xiaoWang@163.com", "xiaoWang@qq.com", "xiaoWang@126.com", "xiaoWang@163.comheihei",
              ".com.xiaowang@qq.com"]
for email in email_list:
    ret = re.match('\w{4,20}@(163|126|qq)\.com$', email)
    if ret:
        print('{} 邮箱符合要求'.format(ret.group()))
    else:
        print('{} 邮箱不符合要求'.format(email))

print('-' * 50)
# 匹配手机号码

tels = ["13100001234", "18912344321", "10086", "18800007777"]

for tel in tels:
    ret = re.match("1\d{9}[0-35-68-9]$", tel)
    if ret:
        print(ret.group())
    else:
        print("%s 不是想要的手机号" % tel)

# 提取区号和电话号码
ret = re.match('(\d+)-(\d+)', '010-66668888')
if ret:
    print(ret.group())
    print(ret.group(1))
    print(ret.group(2))
# ([^-]+) 代表没有遇到小横杠-就一直进行匹配，一直匹配下去
ret = re.match('([^-]+)-(\d+)', '我很帅abc123-66668888')
if ret:
    print(ret.group())
    print(ret.group(1))
    print(ret.group(2))

print('-' * 50)
# 引用分组\
# 能够完成对正确的字符串的匹配
ret = re.match("<[a-zA-Z]*>\w*</[a-zA-Z]*>", "<html>hh</htmlhh>")  # 有误
print(ret.group())

ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", "<html>hh</html>")  # 前后一样
print(ret.group())

# 多个引用分组
labels = ["<html><h1>www.cskaoyan.com</h1></html>",
          "<html><h1>www.cskaoyan.com</h2></html>"]

for label in labels:
    ret = re.match(r'<(\w+)><(\w*)>.*</\2></\1>', label)
    if ret:
        print("%s 是符合要求的标签" % ret.group())
    else:
        print("%s 不符合要求" % label)

# 给分组起别名，通过别名来引用分组

ret = re.match(r'<(?P<n1>\w*)><(?P<n2>\w*).*</(?P=n2)></(?P=n1)>',
               "<html><h1>www.cskaoyan.com</h1></html>")
print(ret.group())

ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>",
               "<html><h1>www.cskaoyan.com</h2></html>")
if ret:
    print("%s 是符合要求的标签" % ret.group())
else:
    print("%s 不符合要求" % label)
