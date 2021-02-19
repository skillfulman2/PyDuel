import scrapy

class Player(scrapy.item):
name = scrapy.Field()
position = scrapy.Field()
