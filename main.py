# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import queue
import asyncio
import aiohttp
from codetiming import Timer

from scraper.crawler.crawler import SiteCrawler
from scraper.html_scraper import HtmlScraper
from scraper.scraper_strategies.scraper import Scraper


def main():
    """
    This is the main entry point for the program
    """
    scraper = Scraper()
    spider = SiteCrawler(HtmlScraper(scraper))
    spider.set_webpage("https://www.google.com")
    spider.scrape(100)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
