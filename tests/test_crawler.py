import unittest

import pytest
import pytest_asyncio

from scraper.crawler.crawler import SiteCrawler
from scraper.scraper_strategies.scraper import Scraper


class MyTestCase(unittest.TestCase):

    def test_fetch_all_from_url_runs(self):
        crawler = SiteCrawler()
        crawler.set_webpage("https://www.google.com")
        results = crawler.scrape(100)
        print("results are ", results)

if __name__ == '__main__':
    unittest.main()
