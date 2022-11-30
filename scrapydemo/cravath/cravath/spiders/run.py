"""
今天也是努力码代码的一天，啾咪
2022-11-14 21:17
代码任务：
"""
from  scrapy import  cmdline
cmdline.execute("scrapy crawl law_ifo -o videoinfo.json -s FEED_EXPORT_ENCODING=utf-8".split())

