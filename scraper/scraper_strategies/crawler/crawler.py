import time
from urllib.error import URLError
from urllib.request import urlopen

import re
import requests
from time import sleep
import numpy as np
import random
from multiprocessing import Pool

class SiteCrawler:

    __slots__ = ('__scraper', '__url_list', '__break_point')
    def __new__(cls, scraper):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SiteCrawler, cls).__new__(cls)
            cls.instance.__scraper = scraper
        return cls.instance

    def __init__(self, scraper):
        self.__url_list = ""
        self.__break_point = 0

    def __attempt_open_robots(self, url):
        host = re.search(r'https://www(.*?)com', url).group(0)
        robots_url = host + '/robots.txt'
        page = requests.get(robots_url)
        if page.status_code == 200:
            return page.content.decode()
        return None

    def __create_sitemap_from_url(self, url):
        print("robots not found")

    def __get_sitemap_from_robots(self, robots):
        sitemap = re.findall('Sitemap: (.*?).xml', robots)
        if sitemap == []:
            return sitemap
        return self.__init_list_from_site_map(sitemap[0] + '.xml')

    def __init_list_from_site_map(self, map):
        links = []
        page = requests.get(map)
        if page.status_code != 200:
            return None
        page = page.content.decode()
        if page.find("sitemapindex") > -1:
            tags = re.findall("<loc>(.*?)</loc>", page)
            for tag in tags:
                lst = self.__init_list_from_site_map(tag)
                if lst is not None and len(lst) > 0:
                    [links.append(x) for x in lst]
            return links
        else:
            return re.findall('<loc>(.*?)</loc>', page)

    def setWebpage(self, url):
        robots = self.__attempt_open_robots(url)
        if robots is None:
            self.__url_list = self.__create_sitemap_from_url(url)
        else:
            sitemap = self.__get_sitemap_from_robots(robots)
            if sitemap is None:
                self.__url_list = self.__create_sitemap_from_url(url)
            else:
                self.__url_list = sitemap
        return self.__url_list

    def getSiteMap(self):
        return self.__url_list

    def get_break_point(self):
        return self.__break_point

    def scrape(self, max_links):
        html = []
        print("scraping")
        for url in self.__url_list[self.__break_point: max_links]:
            html.append(self.__scraper.get_structure_from(url))
        print("done!")
        self.__break_point += max_links
        return html

    def set_scraper(self, scraper):
        self.__scraper = scraper