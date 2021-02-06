import scrapy

class NFLSpider(scrapy.Spider):
    name = "nfl"
    start_urls = [
	'https://www.pro-football-reference.com/players/A/',
    ]

    def parse(self, response):
        for player in response.xpath('//div[@id="div_players"]//p'): 
            yield {
                'name': player.css('a::text').get(),
                'position': player.xpath('//p/text()').get() #.re_first('\([^)]+\)'),
            }


        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


