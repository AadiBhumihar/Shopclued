import scrapy
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class QuotesSpider(scrapy.Spider):
    name = "smartphones"
    allowed_domains = ['www.shopclues.com']
    start_urls = ['https://www.shopclues.com/mobiles-smartphones.html']
    self.options = Options()
    self.options.headless = True

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)