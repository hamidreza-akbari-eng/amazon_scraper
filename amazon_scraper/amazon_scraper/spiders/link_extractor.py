import scrapy
from scrapy_playwright.page import PageMethod


class LinkExtractorSpider(scrapy.Spider):
    name = "link_extractor"

    custom_settings = {
        "FEEDS": {
            "pages_url.csv": {
                "format": "csv",
                "encoding": "utf8",
                "overwrite": True,  # overwrite file each run
            },
        },
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_pages = 15  # enter number of pages you want to crawl
        self.links_list = []

    def start_requests(self):
        yield scrapy.Request(
            url="https://www.amazon.com/s?i=specialty-aps&bbn=16225007011&rh=n%3A16225007011%2Cn%3A1292115011&ref=nav_em__nav_desktop_sa_intl_monitors_0_2_7_8",
            meta={
                "playwright": True,
                "playwright_include_page": True,
                "playwright_page_methods": [
                    PageMethod("wait_for_load_state", "domcontentloaded"),
                ],
            },
            callback=self.parse,
        )

    async def parse(self, response):
        page = response.meta["playwright_page"]
        try:
            page_counter = 0
            while page_counter < self.max_pages:
                current_page_url = page.url
                yield {"URL": current_page_url}

                await page.click("a.s-pagination-next")
                await page.wait_for_load_state("domcontentloaded")

                page_counter += 1

        finally:
            await page.close()
