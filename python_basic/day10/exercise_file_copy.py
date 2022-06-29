# 作者 ： 赖鑫
# 2022年06月13日23时13分25秒

# 打开文件
file_read = open("readme")
file_write = open("Readme[复件]", 'w')

# 读取并写入文件
text = file_read.read()
file_write.write(text)

# 关闭文件
file_read.close()
file_write.close()