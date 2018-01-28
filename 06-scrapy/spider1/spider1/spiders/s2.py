

import scrapy
from scrapy.selector import HtmlXPathSelector

class Woman(scrapy.spiders.Spider):

    name = "s2"

    start_urls = [
        "http://www.xiaohuar.com/2014.html",
    ]

    def parse(self, response):
        # <class 'scrapy.http.response.html.HtmlResponse'>
        # print(type(response))
        # print(response.body)
        # print(response.body_as_unicode())
        # body = response.body
        hxs = HtmlXPathSelector(response)
        # items = hxs.select('//div[@class=""]')


        items = hxs.select('//div[@class="item masonry_brick"]')

        print(len(items))
        for item in items:
            # 名字
            name = item.xpath('div[@class="item_t"]/div[@class="img"]/span/text()').extract_first()
            # 学校
            school = item.xpath('div[@class="item_t"]/div[@class="img"]/a/img/@alt').extract_first()
            # pic url
            url = item.xpath('div[@class="item_t"]/div[@class="img"]/a/img/@src').extract_first()

            print(name + "\t\t" + school + "\t" + url)

