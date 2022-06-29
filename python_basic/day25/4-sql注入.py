# 作者: 王道 龙哥
# 2022年06月27日11时34分36秒
# 作者: 王道 龙哥
# 2022年06月27日11时17分32秒
from pymysql import *


def main():
    conn = connect(host='192.168.19.130', user='root', password='123',
                   database='python6', charset='utf8')
    # 获得Cursor对象
    cs1 = conn.cursor()
    # 下面
    id = '1 or 1'
    sql = 'select * from students where id={}'.format(id)
    print(sql)
    # 执行select语句，返回值是查出的数据总条数
    count = cs1.execute(sql)
    # 打印受影响的行数
    s = cs1.fetchall()
    print(s)
    cs1.close()
    conn.close()


if __name__ == '__main__':
    main()
