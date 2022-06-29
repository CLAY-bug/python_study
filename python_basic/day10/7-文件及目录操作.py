# 作者: 王道 龙哥
# 2022年06月09日15时06分30秒
import os
import sys

def use_rename():
    os.rename('file1', 'file2')


def use_remove():
    os.remove('dir/file2')


def use_dir():
    """
    使用跟目录相关的函数
    :return:
    """
    print(os.listdir('dir'))
    # os.mkdir('dir2')
    # os.rmdir('dir2')
    print(os.getcwd())
    os.chdir('dir')
    print(os.getcwd())
    os.mkdir('dir2')
    print(os.path.isdir('file1'))


def dfs(path_name,width):
    """
    深度优先遍历
    :param path_name:
    :param width:
    :return:
    """
    file_names=os.listdir(path_name)
    for i in file_names:
        print(' '*width+i) #先打印文件名
        current_name=path_name+'/'+i  #路径拼接
        if os.path.isdir(current_name):
            dfs(current_name,width+4)


def python_argv():
    """
    给python文件传参数
    :return:
    """
    print(len(sys.argv))
    print(sys.argv)  #sys.argv[0]
    # print(sys.argv[5])  #演示报错
if __name__ == '__main__':
    # use_remove()
    # use_dir()
    dfs(sys.argv[0],0)
    # python_argv()