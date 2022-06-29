# 作者 ： 赖鑫
# 2022年06月23日11时39分54秒
# with open('readme', 'w', encoding='utf8') as f:
#     f.write('人生苦短')
# print(f.closed)

f = open('readme', 'w', encoding='utf8')
f.close()
print(f.closed)
