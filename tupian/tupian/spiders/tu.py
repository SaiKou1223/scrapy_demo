import scrapy
from ..items import TupianItem

class TuSpider(scrapy.Spider):
    name = 'tu'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['http://sc.chinaz.com/tupian/']

    def parse(self, response):
        div_list = response.xpath('//div[@id="container"]/div')
        for item in div_list:
            src = item.xpath('./div/a/img/@src2').extract_first()
            print(src)
            item = TupianItem()
            item['src'] = src
            yield item