# 作者 ： 赖鑫
# 2022年06月27日19时05分35秒

from pymysql import connect


def main():
    find_name = input("请输入查询内容：")
    # 创建connectino连接
    conn = connect(host='10.211.55.3', user='root', password='123',
                   database='python6', charset='utf8')
    # 获取cursor对象
    cs1 = conn.cursor()
    # 构造参数列表
    params = [find_name]
    # 将sql语句放到execute接口里进行拼接，可以防止sql注入
    count = cs1.execute('select * from students where name = %s', params)
    for i in range(count):
        result = cs1.fetchone()
        print(result)

    # 关闭cursor对象
    cs1.close()
    # 关闭连接
    conn.close()


if __name__ == '__main__':
    main()
