from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from tenyuan_pic.items import TenyuanPicItem

class TenyuanSpider(CrawlSpider):
    name = "tenyuan_pic_spider"
    start_urls = ['https://movie.douban.com/celebrity/1016930/photo/2520355510/']
    rules = (Rule(LinkExtractor(allow=(r'https://movie.douban.com/celebrity/1016930/photo/\d+')), callback='parse_item', follow=True),)
    
    def parse_item(self, response):
        item = TenyuanPicItem()
        item['image_urls'] = response.xpath('//a[@class="mainphoto"]/img/@src').extract()
        yield item
