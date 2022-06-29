# 作者 ： 赖鑫
# 2022年06月18日16时11分39秒

from multiprocessing import Process
from time import sleep

# 全局变量
nums = [520, 13, 14]


def son_process(*args, **kwargs):
    """子进程"""
    for i in range(4):
        nums.append(i)
        print(nums)
        sleep(0.5)
    print(args)
    sleep(0.5)
    for name, age in kwargs.items():
        # 修改传入参数的值
        kwargs[name] = age + 1
    print(kwargs)


if __name__ == "__main__":
    print(f"调用子进程之前的全局变量：{nums}")
    dict1 = {'Tom': 21, 'jack': 23}
    p = Process(target=son_process, args=('John', 18), kwargs=dict1)
    p.start()
    p.join()
    print(f"调用子进程之后的全局变量:{nums}")  # 子进程并不会改变全局变量的值
    print(dict1)  # 子进程并不会改变父进程传入参数的值
