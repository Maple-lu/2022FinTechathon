import scrapy
from scrapydemo.heima_video.heima_video.items import HeimaVideoItem


class SoftwareTestInfoSpider(scrapy.Spider):
    name = 'software_test_info'
    allowed_domains = ['itheima.com']
    start_urls = ['http://yun.itheima.com/course/c144.html?hm$spk$czpc']

    def parse(self, response):
        items=[]
        for i in response.xpath("//ul[@class='clears cur']/li"):

            item = HeimaVideoItem()
            video_link = i.xpath('a/@href').extract()
            video_name = i.xpath('a/div[@class="maintop"]/h2/text()').extract()
            video_desc = i.xpath('a/div[@class="maintop"]/p/text()').extract()
            study_num  = i.xpath('a/div[@class="btm"]/p/span/text()').extract()

            item['video_link'] = "http://yun.itheima.com/"+video_link[0]
            item['video_name'] = video_name[0]
            item['video_desc'] = video_desc[0]
            item['study_num'] = study_num[0]+"人学习"
            items.append(item)

        with open("software_test_info.txt",'w',encoding='utf-8') as f:
            f.write(str(items))

        return  items

