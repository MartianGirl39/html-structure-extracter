import unittest

from scraper.html_scraper import HtmlScraper
from scraper.scraper_strategies.body_only_scraper import BodyOnlyScraper


class MyTestCase(unittest.TestCase):
    def test_something(self):
        scraper = BodyOnlyScraper()
        html = HtmlScraper(scraper).get_structure_from("https://www.w3schools.com/")[0]
        self.assertEqual("", html.get_title())
        self.assertEqual("startscrolling_subtopnav(event)", html.tag_attribute_value("subtopnav", "onmousedown"))
        self.assertEqual("100%", html.tag_attribute_value("svg", "width"))
        self.assertEqual("none", html.tag_attribute_value("svg", "preserveAspectRatio"))
        self.assertEqual("0 0 100 100", html.tag_attribute_value("svg", "viewbox"))
        self.assertEqual("0 0 170 143", html.tag_attribute_value('w3_cert_arrow_default', 'viewBox'))
        # add assertion here


if __name__ == '__main__':
    unittest.main()
