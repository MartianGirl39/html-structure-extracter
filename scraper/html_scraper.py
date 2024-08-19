import re
from http.client import RemoteDisconnected, IncompleteRead
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse

import validators
from urllib.request import urlopen

from concurrent.futures import ProcessPoolExecutor, as_completed

from html_classes import Tag
from html_classes.html_full import Html


class HtmlScraper:

    __slots__ = ('__strategy', '__pool')

    def __new__(cls, strategy):
        if not hasattr(cls, 'instance'):
            cls.instance = super(HtmlScraper, cls).__new__(cls)
            cls.instance.__pool: dict = {}
        return cls.instance

    def __init__(self, strategy):
        self.__strategy = strategy

    def __attempt_open(self, url):
        try:
            page = urlopen(url).read().decode("utf-8")
        except (URLError, UnicodeDecodeError, ConnectionError) as e:
            return None
        return page

    def get_structure_from(self, *urls):
        results = []
        if len(urls) == 1 and isinstance(urls[0], (list, tuple, set)):
            urls = urls[0]
        elif len(urls) == 1 and isinstance(urls[0], dict):
            urls = urls[0].values()
        for url in urls:
            if url in self.__pool:
                results.append(self.__pool[url])
                continue
            page = self.__attempt_open(url)
            html = self.__strategy.scrape(page)
            if html is None:
                continue
            self.__pool[url] = html
            results.append(html)
        return results

    def set_strategy(self, strategy):
        self.__strategy = strategy