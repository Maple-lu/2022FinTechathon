import scrapy
from ..items import TxmoviesItem


class TxmoviesSpider(scrapy.Spider):
    name = 'txmovies'
    allowed_domains = ['v.qq.com']
    start_urls = ['https://v.qq.com/channel/movie/list?filter_params=sort%3D75&page_id=channel_list_second_page']

    def parse(self, response):
        items = TxmoviesItem()
        lists=response.xpath("//div[@class='info-wrap']")
        print(lists)
        # for i in lists:
        #     items["name"]=i.xpath("")
        pass
