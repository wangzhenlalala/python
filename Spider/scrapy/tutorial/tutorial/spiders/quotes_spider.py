'''
    spiders  must subclass scrapy.Spider 
    and define the initial requests to make, 
    optionally how to follow links in the pages, and how to parse the downloaded page content to extract data.

    how to start a spider: 
        go to the project's top level directory and run 
        scrapy crawl spider-name
    how to interactively parse html:
        scrapy shell url and play with response
    how to store data:
        scrapy crawl spider-name -o quotes.json (easiest way) called [Feed exports]
'''
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    def start_requests(self):
        '''
        must return an iterable of Requests 
        (you can return a list of requests or write a generator function) 
        which the Spider will begin to crawl from.
        '''
        urls = [
            "http://quotes.toscrape.com/page/1/",
            "http://quotes.toscrape.com/page/2/"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        '''
        The parse() method will be called to handle each of the requests
        This happens because parse() is Scrapy’s default callback method, 
        which is called for requests without an explicitly assigned callback.
        '''
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
        for quote in response.css('div.quote'):
            text = quote.css('span.text::text').extract_first()
            author = quote.css('small.author::text').extract_first()
            tags = quote.css('div.tags a.tag::text').extract()
            yield dict(text=text, author=author, tags=tags)

