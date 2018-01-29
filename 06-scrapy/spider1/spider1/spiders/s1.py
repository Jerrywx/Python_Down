

import scrapy
from scrapy.selector import HtmlXPathSelector

class XiaoHua(scrapy.spiders.Spider):
    name = "s1"

    start_urls = [
        "http://www.xiaohuar.com/2014.html",
    ]

    def parse(self, response):
        current_url = response.url
        body = response.body
        # print(response.body_as_unicode())

        hxs = HtmlXPathSelector(response)
        items = hxs.select('//div[@class="item masonry_brick"]').extract_first()
        print(items)