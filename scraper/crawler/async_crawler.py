import time
from asyncio import Queue
from urllib.error import URLError
from urllib.request import urlopen

import re
import numpy as np
import random
from multiprocessing import Pool
import asyncio

import requests
from aiohttp import ClientSession
from codetiming import Timer

from scraper.scraper_strategies.scraper import Scraper
from scraper.sessions.async_html_extracter import AsyncHtmlExtracter

class SiteCrawler:

    __slots__ = ('__scraper', '__url_queue', '__site_map_queue', '__break_point')
    def __new__(cls, scraper: Scraper):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SiteCrawler, cls).__new__(cls)
            cls.instance.__scraper = scraper
        return cls.instance

    def __init__(self, scraper):
        self.__url_queue: Queue
        self.__site_map_queue: Queue
        self.__break_point: int

    def __get_robots(self, url):
        host = re.search(r'https://www(.*?)com', url).group(0)
        robots_url = host + '/robots.txt'
        response = requests.get(robots_url)
        if response.status_code == 200:
            return response.content
        return None

    def __init_sitemap_queue(self, robots):
        urls = re.findall('Sitemap: (.*?).xml', robots)
        if urls == []:
            return None
        for url in urls:
            self.__site_map_queue(url)

    def set_web_url(self, url):
        pass