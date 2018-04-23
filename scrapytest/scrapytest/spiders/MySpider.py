#�����ļ�
import scrapy
from scrapytest.items import ScrapytestItem

class MySpider(scrapy.Spider):
    def __init__(self):  
        self.headers = {  
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',  
            'Accept-Encoding':'gzip, deflate'  
        }
    #��������Spider
    name = "MySpider"
    #������ʵ���
    #allowed_domains = []
    #��ȡ�ĵ�ַ
    start_urls = ["https://www.eastbay.com/Womens/New-Balance/Running/Shoes/Casual-Sneakers/_-_/N-1qZykZ1dwZneZdn?cm_REF=New%20Balance&crumbs=491%201244"]
    #��ȡ����
    def parse(self, response):
        #�ⲿ������ȡ���֣�ʹ��xpath�ķ�ʽѡ����Ϣ�����巽��������ҳ�ṹ����
        #�Ȼ�ȡÿ����Ʒ�����ͼ
        for box in response.xpath('//div[@class="prod_slot"]/a[1]'):
            #��ȡÿ����������Ʒ
            url= 'https://www.eastbay.com' + box.xpath('@href').extract()[0]
            if url :
                #����url
                yield scrapy.Request(url,callback=self.itemall)
    def itemall(self, response):
        for boxall in response.xpath('//div[@id="endeca_search_results"]//li/a[1]'):
            urlitemall=boxall.xpath('@href').extract()[0]
            if urlitemall :
                #����url
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