import unittest

from scraper.scraper_strategies.crawler.crawler import SiteCrawler
from scraper.html_scraper import HtmlScraper
from scraper.scraper_strategies.scraper import Scraper


class MyTestCase(unittest.TestCase):
    def test_fetch_all_from_url(self):
        scraper = Scraper()
        crawler = SiteCrawler(HtmlScraper(scraper))
        crawler.setWebpage("https://www.google.com")
        crawler.scrape(100)
        self.assertEqual(100, crawler.get_break_point())

if __name__ == '__main__':
    unittest.main()
