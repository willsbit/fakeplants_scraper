import scrapy


class PlantsSpiderSpider(scrapy.Spider):
    name = 'plants'
    allowed_domains = ['fake-plants.co.uk']
    start_urls = ['https://www.fake-plants.co.uk/']

    def parse(self, response):
        for link in response.css('li.product-category a::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_categories)

    def parse_categories(self, response):
        products = response.css('div.astra-shop-summary-wrap')
        for product in products:
            yield {
                'category': product.css('span.ast-woo-product-category::text').get().strip(),
                'name': product.css('h2.woocommerce-loop-product__title::text').get().strip()
            }

