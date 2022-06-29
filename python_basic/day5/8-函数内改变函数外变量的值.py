# 作者: 王道 龙哥
# 2022年06月04日11时36分07秒

#要在子函数内改变外面的变量值，要用接口，取下标去修改
def change_list(demo_list1):
    demo_list1[0]=2
    demo_list1[1] = 3
    demo_list1[2]=4
    print('change_list 地址 %x' % id(demo_list1))


demo_list = [1, 2, 3]
change_list(demo_list)
print('demo_list地址 %x' % id(demo_list))
print(demo_list)

