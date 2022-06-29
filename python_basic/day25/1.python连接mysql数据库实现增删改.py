# 作者: 王道 龙哥
# 2022年06月27日10时30分32秒
from pymysql import connect


def main():
    conn = connect(host='10.211.55.3', user='root', password='123',
                   database='python6', charset='utf8')
    # 获得Cursor对象
    cs1 = conn.cursor()
    # 执行insert语句，并返回受影响的行数：添加一条数据
    # 增加
    # count=cs1.execute("insert into goods_cates(name) values('硬盘')")
    # print(count)

    # 更新
    # count=cs1.execute("update goods_cates set name='机械硬盘' "
    #                   "where name='硬盘'")
    # print(count)
    # 删除
    # count = cs1.execute("delete from goods_cates where name='机械硬盘'")
    # print(count)

    # 提交之前的操作，如果之前已经之执行过多次的execute，那么就都进行提交
    # conn.commit()

    # cs1.close()
    conn.close()


if __name__ == '__main__':
    main()
