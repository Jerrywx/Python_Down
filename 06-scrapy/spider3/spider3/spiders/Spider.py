
import scrapy

class DomzSpider(scrapy.Spider):
    name = "mv"

    # allwed_domains = ["80s.tw"]

    start_urls = [
        "https://movie.douban.com/j/search_subjects?type=movie&tag=热门&sort=recommend&page_limit=20&page_start=20"
        # "https://www.80s.tw/",
        # "https://www.80s.tw/movie/list/",
        # "https://www.80s.tw/movie/list/-----p2",
        # "https://www.80s.tw/movie/list/-----p3",
        # "https://www.80s.tw/movie/list/-----p4",
    ]

    def parse(self, response):
        # print(response.url)
        print(response.body_as_unicode())




