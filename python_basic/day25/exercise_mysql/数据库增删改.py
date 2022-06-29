# 作者 ： 赖鑫
# 2022年06月27日14时17分28秒
from pymysql import connect


def main():
    conn = connect(host='10.211.55.3', user='root', password='123',
                   database='jing_dong', charset='utf8')
    # 获得cursor对象
    cs1 = conn.cursor()
    # 执行insert语句，进行数据插入
    # count = cs1.execute('insert into goods_cates(name) values ("硬盘")')
    # print(count)
    # count = cs1.execute('insert into goods_cates(name) values ("光盘")')
    # print(count)

    # 更新表中数据
    # count = cs1.execute("update goods_cates set name='固态硬盘' where name = '硬盘'")
    # print(count)

    # 删除表中数据
    count = cs1.execute("delete from goods_cates where name = '光盘'")
    print(count)
    # 把之前进行的操作都进行提交
    conn.commit()
    # 关闭cursor对象
    cs1.close()
    # 关闭connection对象
    conn.close()


if __name__ == '__main__':
    main()
