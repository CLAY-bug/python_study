# 作者: 王道 龙哥
# 2022年06月03日15时02分54秒
name = 'clay'
print("我的名字叫 %5s，请多多关照！" % name)
student_no = 123
print("我的学号是 %06d结束" % student_no)  # 06就是不足补0
price = 9.5
weight = 3.127
money = price * weight
# 默认有四舍五入
print("苹果单价%6.02f元／斤，购买 %.02f 斤，需要支付 %.02f 元" % (price, weight, money))
scale = 0.023
print("数据比例是 %.1f%%" % (scale * 100))
