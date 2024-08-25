from scraper.concurrent_html_scraper import ConcurrentHtmlScraper
from scraper.crawler.crawler import SiteCrawler
from scraper.html_scraper import HtmlScraper
from scraper.scraper_strategies.scraper import Scraper


def main():
    """
    This is the main entry point for the program
    """
    strategy = Scraper()
    scraper = ConcurrentHtmlScraper()
    scraper.set_strategy(strategy)
    spider = SiteCrawler()
    spider.set_scraper(scraper)
    spider.set_webpage("https://www.google.com")
    result = spider.scrape(100)
    # print(result)

def scrape_pages(url, scraper):
    scraper.scrape(url)

def scrape_host(host, scraper):
    spider = SiteCrawler()
    spider.set_scraper(scraper)
    spider.set_webpage(host)
    spider.scrape(100)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
