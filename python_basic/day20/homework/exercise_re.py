# 作者 ： 赖鑫
# 2022年06月21日19时23分16秒
import re

url_list = ["http://www.interoem.com/messageinfo.asp?id=35",
            "http://3995503.com/class/class09/news_show.asp?id=14",
            "http://lib.wzmc.edu.cn/news/onews.asp?id=769",
            "http://www.zy-ls.com/alfx.asp?newsid=377&id=6",
            "http://www.fincm.com/newslist.asp?id=415"]

for url in url_list:
    ret = re.search(r'^http://.*\.(com|cn)', url)
    print(ret.group())
