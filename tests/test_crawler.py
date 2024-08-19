import unittest

import pytest
import pytest_asyncio

from scraper.crawler.crawler import SiteCrawler
from scraper.html_scraper import HtmlScraper
from scraper.scraper_strategies.scraper import Scraper


class MyTestCase(unittest.TestCase):

    async def test_fetch_all_from_url_runs(self):
        scraper = Scraper()
        crawler = SiteCrawler(HtmlScraper(scraper))
        crawler.set_webpage("https://www.google.com")
        crawler.scrape(100)

if __name__ == '__main__':
    unittest.main()
