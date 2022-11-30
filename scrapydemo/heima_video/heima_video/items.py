# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HeimaVideoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    video_name = scrapy.Field()
    video_desc = scrapy.Field()
    study_num = scrapy.Field()
    video_link = scrapy.Field()
    pass
