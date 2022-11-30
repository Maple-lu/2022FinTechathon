import scrapy
from scrapydemo.itcastSpider.itcastSpider.items import ItcastspiderItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['https://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):


        for each in response.xpath("//div[@class='li_txt']"):
            #创建MyspiderItem类对象
            item = ItcastspiderItem()
            name=each.xpath('h3/text()').extract()
            level=each.xpath('h4/text()').extract()
            resume=each.xpath('p/text()').extract()

            item['name']=name[0]
            item['level']=level[0]
            item['resume']=resume[0]


        yield item

