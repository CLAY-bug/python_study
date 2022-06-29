# 作者: 王道 龙哥
# 2022年06月13日10时15分15秒


def bsearch(arr,target):
    high=len(arr)-1
    low=0
    while low<=high: #这里必须是相等的
        mid=(low+high)//2
        if arr[mid]>target:
            high=mid-1
        elif arr[mid]<target:
            low=mid+1
        else:
            return mid
    return -1

MAXKEY=1000 #hash表大小是1000

#elf_hash将字符串计算为哈希值进行返回
def elf_hash(hash_str):
    h = 0
    g = 0
    for i in hash_str:
        h = (h << 4) + ord(i)
        g = h & 0xf0000000
        if g:
            h ^= g >> 24
        h &= ~g
    return h % MAXKEY

#用python自己实现一个链表，自行实现
class Node:
    def __init__(self,student,node=None):
        self.student=student
        self.next=node

if __name__ == '__main__':
    # list1=[3, 9, 13, 27, 41, 42, 71, 71, 83, 98]
    # print(bsearch(list1,3))
    str_list = ["xiongda", "lele", "hanmeimei", "wangdao", "fenghua"]
    hash_table=[None]*MAXKEY
    for i in str_list:
        hash_table[elf_hash(i)]=i
    pass
    #两个字符串的哈希值一样，就是哈希冲突