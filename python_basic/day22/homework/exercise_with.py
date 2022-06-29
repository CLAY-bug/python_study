# 作者 ： 赖鑫
# 2022年06月23日19时57分45秒


with open('homework', 'r+', encoding='utf8') as f:
    text = f.read()
    print(text)
    f.write("人生苦短，我用python")
