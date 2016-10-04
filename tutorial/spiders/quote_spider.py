import scrapy
from tutorial.items import TutorialItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://icooon-mono.com/category/event-en/page/1/?lang=en',
            'http://icooon-mono.com/category/event-en/page/2/?lang=en',
            'http://icooon-mono.com/category/event-en/page/3/?lang=en',
            'http://icooon-mono.com/category/event-en/page/4/?lang=en',
            'http://icooon-mono.com/category/event-en/page/5/?lang=en',
            'http://icooon-mono.com/category/event-en/page/6/?lang=en',
            'http://icooon-mono.com/category/event-en/page/7/?lang=en',
            'http://icooon-mono.com/category/event-en/page/8/?lang=en',
            'http://icooon-mono.com/category/event-en/page/9/?lang=en',
            'http://icooon-mono.com/category/event-en/page/10/?lang=en',
            'http://icooon-mono.com/category/event-en/page/11/?lang=en',
            'http://icooon-mono.com/category/event-en/page/12/?lang=en'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for sel in response.xpath('//div[@id="topMaincolumn"]/ul/li/a'):
            p = sel.xpath('img/@src')[0].extract()
            title = sel.xpath('p/text()').extract()
            link = response.urljoin(p)
            cardImage = TutorialItem()
            cardImage['title'] = title
            cardImage['image_urls'] =  [link]
            yield cardImage