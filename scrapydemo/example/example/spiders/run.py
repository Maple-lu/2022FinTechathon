"""
今天也是努力码代码的一天，啾咪
2022-11-22 13:54
代码任务：
"""
from scrapy import cmdline
cmdline.execute("scrapy crawl toscrape -o books.csv".split())