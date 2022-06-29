# 作者 ： 赖鑫
# 2022年06月10日20时23分56秒

time_num = input("请输入时间：")
time1 = time_num.replace('年', '-').replace('月', '-').replace('日', '')
time2 = time1.replace('时', ':').replace('分',':').replace('秒','')
print(time2)
