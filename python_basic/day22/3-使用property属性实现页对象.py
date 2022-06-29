# 作者: 王道 龙哥
# 2022年06月23日09时59分37秒
class Pager:
    def __init__(self,current_page):
        self.current_page=current_page
        self.page_nums=10

    @property
    def start(self):
        return (self.current_page-1)*self.page_nums

    @property
    def end(self):
        return self.current_page*self.page_nums

p=Pager(1)
print(p.start)
print(p.end)