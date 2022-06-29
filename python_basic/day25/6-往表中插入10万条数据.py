# 作者: 王道 龙哥
# 2022年06月27日16时26分05秒
from pymysql import connect

def main():
    # 创建Connection连接
    conn = connect(host='192.168.19.130',port=3306,
                   database='python6',user='root',
                   password='123',charset='utf8')
    # 获得Cursor对象
    cursor = conn.cursor()
    # 插入10万次数据
    for i in range(100000):
        cursor.execute("insert into text_index values('ha-%d')" % i)
    # 提交数据
    conn.commit()

if __name__ == "__main__":
    main()