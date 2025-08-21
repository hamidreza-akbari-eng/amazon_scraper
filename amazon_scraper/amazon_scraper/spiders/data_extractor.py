import csv

import scrapy
from scrapy_playwright.page import PageMethod


class DataExtractorSpider(scrapy.Spider):
    name = "data_extractor"

    custom_settings = {
        "FEEDS": {
            "monitors_info.csv": {
                "format": "csv",
                "encoding": "utf8",
                "overwrite": True,  # overwrite file each run
            },
        },
    }

    def start_requests(self):
        with open("pages_url.csv", "r") as f:
            csv_reader = csv.reader(f)
            next(csv_reader, None)
            for row in csv_reader:
                if row:
                    url = row[0]
                    yield scrapy.Request(
                        url,
                        meta={
                            "playwright": True,
                            "playwright_include_page": True,
                            "playwright_page_methods": [
                                PageMethod("wait_for_load_state", "domcontentloaded"),
                            ],
                        },
                        callback=self.parse,
                    )

    def parse(self, response):
        products = response.css(
            "div.sg-col-4-of-24.sg-col-4-of-12.s-result-item.s-asin.sg-col-4-of-16.sg-col.s-widget-spacing-small.sg-col-4-of-20"
        )
        for product in products:
            yield {
                "title": product.css(
                    "h2.a-size-base-plus.a-spacing-none.a-color-base.a-text-normal span::text"
                ).get(default=""),
                "price": product.css("span.a-price span.a-offscreen::text").get(
                    default=""
                ),
                "rate": product.css("span.a-icon-alt::text").get(default=""),
                "image_urls": product.css("img.s-image::attr(src)").getall(),
            }
