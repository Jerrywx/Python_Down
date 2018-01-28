

import scrapy

class XiaoHua(scrapy.spiders.Spider):
    name = "s1"

    start_urls = [
        "http://www.xiaohuar.com/2014.html",
    ]

    def parse(self, response):
        current_url = response.url
        body = response.body
        print(response.body_as_unicode())