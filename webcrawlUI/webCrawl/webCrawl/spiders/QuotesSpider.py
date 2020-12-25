import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"


    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        f = open("kk.txt", "w")
        f.write("hello123")
        f.close()
        hrefs = response.css('a').getall()
        atext = response.css('a::text').getall()
        index = [index for index, value in enumerate(atext) if value == '(about)']
        url = response.css('a::attr(href)').getall()
        for i in index:
            # print(hrefs[i])
            # print(url[i])
            yield response.follow(url[i], callback=self.parse)





