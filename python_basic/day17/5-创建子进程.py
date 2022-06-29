# 作者: 王道 龙哥
# 2022年06月17日16时47分21秒
import time
from multiprocessing import Process

def run_proc():
    while True:
        print('---2----')
        time.sleep(1)

if __name__ == '__main__':
    p=Process(target=run_proc)
    p.start()
    while True:
        print('---1----')
        time.sleep(1)