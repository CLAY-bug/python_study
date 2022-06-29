# 作者: 王道 龙哥
# 2022年06月04日11时02分29秒

def test(num):
    print('test内 %d  地址 %x' % (num,id(num)))
    num=5  #Python 的所有变量，赋值后，都是指向另外一个地方了
    print('test内修改后 %d  地址 %x' % (num,id(num)))
    return num

a=10

print('调用函数前，a的地址是%x' % id(a))  #num=a
ret=test(a)
print('调用函数后，a的值%d,a的地址%x' % (a,id(a)))
#返回值就是把num赋值给ret
print("调用函数后 返回值%d 内存地址是 %x" % (ret,id(ret)))