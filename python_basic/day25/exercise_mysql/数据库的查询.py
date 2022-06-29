# 作者 ： 赖鑫
# 2022年06月27日17时40分22秒
from pymysql import connect


def main():
    # 创建connection连接
    conn = connect(host='10.211.55.3', user='root',
                   password='123', database='jing_dong', charset='utf8')
    # 获得cursor对象
    cs1 = conn.cursor()

    # 执行select语句，返回受影响的行数
    count = cs1.execute("select id, name from goods where price > 4000")

    # 获取查询结果 常用
    # for i in range(count):
    #     result = cs1.fetchone()
    #     print(result)

    # 少用
    result = cs1.fetchmany(3)
    # result = cs1.fetchall()
    print(result)

    # 关闭cursor对象
    cs1.close()
    # 关闭连接对象
    conn.close()


if __name__ == '__main__':
    main()
