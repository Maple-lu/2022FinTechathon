import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['itcast.cn']
    start_urls = ['https://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        with open('teacher_info.txt','w',encoding='utf-8') as f:
            f.write(response.text)
        title=response.xpath("//html/head/title/text()")
        print(title)

