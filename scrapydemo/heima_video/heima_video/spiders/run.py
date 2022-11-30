"""
今天也是努力码代码的一天，啾咪
2022-11-14 20:30
代码任务：
"""
from scrapy import cmdline
# cmdline.execute("scrapy crawl software_test_info".split())
cmdline.execute(">scrapy crawl software_test_info -o videoinfo.json -s FEED_EXPORT_ENCODING=utf-8".split())
# cmdline.execute("scrapy crawl itcast -o teacher.json ".split())
