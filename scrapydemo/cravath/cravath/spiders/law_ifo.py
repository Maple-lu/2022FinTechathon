import scrapy
from scrapydemo.cravath.cravath.items import CravathItem


class LawIfoSpider(scrapy.Spider):
    name = 'law_ifo'
    allowed_domains = ['cravath.com']
    start_urls = ['https://www.cravath.com/people/index.html']

    def parse(self, response):
        items=[]

        for i in response.xpath("//div[@class='styles__personCard--78ed242f']"):

            item = CravathItem()

            #这里的解析有点问题
            name = i.xpath('dl//dd[@class="type__h3"]/a/text()').extract()

            offices = i.xpath('dl//li/a/text()').extract()

            practices = i.xpath('dl//dd[@class="type__label styles__title--f614a682"]/a/text()').extract()

            email = i.xpath('dl//dd[@class="color-dodger-blue hover-color-light-navy"]/a/text()').extract()


            item['name'] =name[0]
            item['offices'] = offices[0]
            item['practices'] = practices[0]
            item['email'] = email[0]
            items.append(item)

        with open("laws_info.txt", 'w', encoding='utf-8') as f:
            f.write(str(items))

        return items

        pass


