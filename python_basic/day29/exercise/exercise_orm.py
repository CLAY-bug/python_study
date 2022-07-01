# 作者 ： 赖鑫
# 2022年07月01日13时32分09秒


# 自定义实现ORM，能够通过python代码自动生成SQL语句
# 自定义元类需要继承type类
class ModelMetaClass(type):
    # 重写__new__方法来接收元类的参数
    def __new__(cls, class_name, class_parents, attrs):
        mappings = {}  # 把符合要求的属性添加进来
        for name, value in attrs.items():
            # name: 对应sql里的字段
            # value: 对应sql字段的类型和限制等，用一个元祖来表示的
            if isinstance(value, tuple):
                print(f'Found mapping:{name} ==>{value}')
                mappings[name] = value
        # 把在mapping中已经存在的属性从元来的地方删除掉，也就是删掉齐类属性
        for k in mappings.keys():
            attrs.pop(k)

        attrs['__mapping__'] = mappings  # 相当于数据库中一个表所包含的内容
        attrs['__table__'] = class_name  # 相当于数据库的表名
        return type.__new__(cls, class_name, class_parents, attrs)


class Model(metaclass=ModelMetaClass):
    """使用元类生成而来的类"""

    # 接收attrs里的内容，即__mapping__和__table__
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

    def save(self):
        fields = []  # 存放字段
        args = []  # 存放要插入的值
        for k, v in self.__mapping__.items():
            fields.append(v[0])  # 字段名，例如：uid
            args.append(getattr(self, k, None))  # 默认不放值的时候为None
        sql = "insert into %s (%s) values (%s)" % (self.__table__, ','.join(fields),
                                                   ','.join(
                                                       ["'" + i + "'" if isinstance(i, str) else str(i) for i in args]))
        print(f"SQL:{sql}")


class User(Model):
    uid = ('uid', 'int unsigned')
    name = ('name', 'varchar(30)')
    email = ('email', 'varchar(30)')
    password = ('password', 'varchar(30)')
    

u = User(uid=123, name='john', email='520@qq.com', password='123')
u.save()
