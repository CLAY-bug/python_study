# 作者 ： 赖鑫
# 2022年06月27日21时09分00秒
from pymysql import connect


def main():
    # 创建connection连接
    conn = connect(host='10.211.55.3', user='root', password='123',
                   database='jing_dong', charset='utf8')
    # 获取cursor对象
    cs1 = conn.cursor()
    # 插入数据
    for i in range(100000):
        cs1.execute("insert into test_index values ('test-%d')" % i)
    conn.commit()


if __name__ == '__main__':
    main()
