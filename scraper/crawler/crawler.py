import time
from urllib.error import URLError
from urllib.request import urlopen

import re
import requests
from time import sleep
import numpy as np
import random
import asyncio
import aiohttp
from aiohttp import ClientSession, ClientConnectorError

from multiprocessing import Pool, Process
from concurrent.futures import ProcessPoolExecutor, wait, ALL_COMPLETED, as_completed

from scraper.concurrent_html_scraper import ConcurrentHtmlScraper


class SiteCrawler:

    __slots__ = ('__scraper', '__url_list', '__break_point')
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SiteCrawler, cls).__new__(cls)
            cls.instance.__scraper = ConcurrentHtmlScraper()
        return cls.instance

    def __init__(self):
        self.__url_list = ""
        self.__break_point = 0

    def __attempt_open_robots(self, url):
        host = re.search(r'https://www(.*?)com', url).group(0)
        robots_url = host + '/robots.txt'
        page = requests.get(robots_url)
        if page.status_code != 200:
            return None
        return page.content.decode()

    def __create_sitemap_from_url(self, url):
        # TODO: implement this function
        print("robots not found")

    async def __get_sitemap_from_robots_async(self, robots):
        sitemap = re.findall(('Sitemap: (.*?).xml'), robots)
        # there is no sitemap
        if not sitemap:
            return None
        # there is only one sitemap in robots
        else:
            maps = []
            async with aiohttp.ClientSession() as session:
                tasks = [
                    self.__get_directories_in_maps(url + '.xml', session)
                    for url in sitemap
                ]
                results = await asyncio.gather(*tasks)
                if len(results) <= 1:
                    maps = results[0]
                else:
                    for result in results:
                        for url in result:
                            maps.append(url)
            values = []
            async with aiohttp.ClientSession() as session:
                tasks = [
                    self.__extract_links_from_maps(url, session)
                    for url in maps
                ]
                results = await asyncio.gather(*tasks)
                if len(results) <= 1:
                    values = results[0]
                else:
                    for result in results:
                        for url in result:
                            values.append(url)
                return values

    async def __get_directories_in_maps(self, url, session):
        try:
            async with session.get(url) as response:
                page = await response.text()
                # print("page from sitemap index is", page)
                if page.find("sitemapindex") > -1:
                    return re.findall("<loc>(.*?)</loc>", page)
                return []
        except ClientConnectorError as e:
            return []

    def set_webpage(self, url):
        robots = self.__attempt_open_robots(url)
        if robots is None:
            self.__url_list = self.__create_sitemap_from_url(url)
        else:
            sitemap = asyncio.run(self.__get_sitemap_from_robots_async(robots))
            if sitemap is None:
                self.__url_list = self.__create_sitemap_from_url(url)
            else:
                self.__url_list = sitemap
        # print(self.__url_list)
        return self.__url_list

    def getSiteMap(self):
        return self.__url_list

    def get_break_point(self):
        return self.__break_point

    def scrape(self, max_links=None):
        if (max_links is None):
            max_links = len(self.__url_list)
        html = []
        print("scraping")
        start = time.perf_counter()
        html = self.__scraper.get_structure_from(self.__url_list[:max_links])[0]
        print("done!")
        finish = time.perf_counter()
        print(f"It took {finish-start: .2f} second(s) to finish")
        self.__break_point += max_links
        return html

    def set_scraper(self, scraper):
        self.__scraper = scraper

    def get_num_of_links(self):
        return len(self.__url_list)

    async def __extract_links_from_maps(self, url, session):
        # print("scraping ", url)
        try:
            async with session.get(url) as response:
                page = await response.text()
                return re.findall("<loc>(.*?)</loc>", page)
        except ClientConnectorError as e:
            return []