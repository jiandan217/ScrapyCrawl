#引入文件
import scrapy
from scrapytest.items import ScrapytestItem

class MySpider(scrapy.Spider):
    def __init__(self):  
        self.headers = {  
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',  
            'Accept-Encoding':'gzip, deflate'  
        }
    #用于区别Spider
    name = "MySpider"
    #允许访问的域
    #allowed_domains = []
    #爬取的地址
    start_urls = ["https://www.eastbay.com/Womens/New-Balance/Running/Shoes/Casual-Sneakers/_-_/N-1qZykZ1dwZneZdn?cm_REF=New%20Balance&crumbs=491%201244"]
    #爬取方法
    def parse(self, response):
        #这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
        #先获取每个商品分类大图
        for box in response.xpath('//div[@class="prod_slot"]/a[1]'):
            #获取每个分类下商品
            url= 'https://www.eastbay.com' + box.xpath('@href').extract()[0]
            if url :
                #返回url
                yield scrapy.Request(url,callback=self.itemall)
    def itemall(self, response):
        for boxall in response.xpath('//div[@id="endeca_search_results"]//li/a[1]'):
            urlitemall=boxall.xpath('@href').extract()[0]
            if urlitemall :
                #返回url
                yield scrapy.Request(urlitemall,callback=self.itemone)

    def itemone(self, response):
        item = ScrapytestItem()
        item['title'] =response.xpath('//h1[@id="product_title"]/text()').extract()[0]
        #item['price'] =response.xpath('//div[@id="product_price"]/text()').extract()[0]
        #item['color'] =response.xpath('//a[@class="colors_badge"]/span').extract()[0]
        #item['size'] =response.xpath('//span[@id="size_selection_list"]/text()').extract()[0]
        item['sku'] =response.xpath('//span[@id="productSKU"]/text()').extract()[0]
        item['details'] =response.xpath('//div[@id="pdp_description"]/text()').extract()[0]
        #item['img_urls'] =response.xpath('//h1[@id="product_titl0"]').extract()[0]
        yield item