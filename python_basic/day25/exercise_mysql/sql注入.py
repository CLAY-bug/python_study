# 作者 ： 赖鑫
# 2022年06月27日19时11分43秒
from pymysql import connect


def main():
    # 创建connectino连接
    conn = connect(host='10.211.55.3', user='root', password='123',
                   database='python6', charset='utf8')
    # 获得cursor对象
    cs1 = conn.cursor()
    id = '1 or 1'
    sql = 'select * from students where id={}'.format(id)
    print(sql)
    count = cs1.execute(sql)
    s = cs1.fetchall()
    print(s)
    cs1.close()
    conn.close()


if __name__ == '__main__':
    main()
