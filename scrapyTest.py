# This is to import scrapy.py file
import scrapy

#create a class "new_spider" to perform crawl to URL
class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['https://brickset.com/sets/year-2013']

    def parse(self, response):
        #xpath_selector = '//img'
        css_selector = 'img'
        #for x in response.xpath(xpath_selector):
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }
    # To recurse to next page
        Page_selector = '.next a ::attr(href)'
        next_page = response.css(Page_selector).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
            callback=self.parse
            )






