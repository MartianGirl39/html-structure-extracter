import unittest

from scraper.html_scraper import HtmlScraper
from scraper.scraper_strategies.scraper import Scraper


class MyTestCase(unittest.TestCase):

    def test_html(self):
        strategy = Scraper()
        scraper = HtmlScraper()
        scraper.set_strategy(strategy)
        html = scraper.get_structure_from("https://www.w3schools.com/")[0]
        self.assertEqual("en-US", html.langauge())

    def test_get_attribute_value(self):
        strategy = Scraper()
        scraper = HtmlScraper()
        scraper.set_strategy(strategy)
        html = scraper.get_structure_from("https://www.w3schools.com/")[0]
        #self.assertEqual("/java/default.asp", html_classes.tag_attribute_value("a-153", "href"))
        self.assertEqual("startscrolling_subtopnav(event)", html.tag_attribute_value("subtopnav", "onmousedown"))
        self.assertEqual("100%", html.tag_attribute_value("svg", "width"))
        self.assertEqual("none", html.tag_attribute_value("svg", "preserveAspectRatio"))
        self.assertEqual("0 0 100 100", html.tag_attribute_value("svg", "viewbox"))
        self.assertEqual("0 0 170 143", html.tag_attribute_value('w3_cert_arrow_default', 'viewBox'))

    def test_get_styles(self):
        strategy = Scraper()
        scraper = HtmlScraper()
        scraper.set_strategy(strategy)
        html = scraper.get_structure_from("https://www.w3schools.com/")[0]
        self.assertEqual("64px", html.tag_style_value("getdiploma", "padding-bottom"))

    def test_get_classes(self):
        strategy = Scraper()
        scraper = HtmlScraper()
        scraper.set_strategy(strategy)
        html = scraper.get_structure_from("https://www.w3schools.com/")[0]
        expected = ["footer", "w3-container", "w3-white"]
        self.assertEqual(expected, html.get_classes("footer"))

    def test_get_title(self):
        strategy = Scraper()
        scraper = HtmlScraper()
        scraper.set_strategy(strategy)
        html = scraper.get_structure_from("https://www.w3schools.com/")[0]
        self.assertEqual('W3Schools Online Web Tutorials', html.get_title())

    def test_get_charset(self):
        strategy = Scraper()
        scraper = HtmlScraper()
        scraper.set_strategy(strategy)
        html = scraper.get_structure_from("https://www.w3schools.com/")[0]
        self.assertEqual('utf-8', html.get_charset())

    def test_get_meta(self):
        strategy = Scraper()
        scraper = HtmlScraper()
        scraper.set_strategy(strategy)
        html = scraper.get_structure_from("https://www.w3schools.com/")[0]

if __name__ == '__main__':
    unittest.main()
