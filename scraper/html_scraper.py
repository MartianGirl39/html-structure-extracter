import re
from http.client import RemoteDisconnected, IncompleteRead
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse

import validators
from urllib.request import urlopen

from html_classes import Tag
from html_classes.html_full import Html


class HtmlScraper:

    __slots__ = ('__strategy', '__pool')

    def __new__(cls, strategy):
        if not hasattr(cls, 'instance'):
            cls.instance = super(HtmlScraper, cls).__new__(cls)
            cls.instance.__pool = {}
        return cls.instance

    def __init__(self, strategy):
        self.__strategy = strategy

    def get_structure_from(self, *url):
        if url in self.__pool:
            return self.__pool[url]
        if isinstance(url[0], (list, tuple)):
            url = url[0]
        if isinstance(url[0], (dict)):
            url = url[0].values()
        html = self.__strategy.scrape(url)
        for i in range(0, len(url)):
            if html[i] is not None:
                self.__pool[url[i]] = html[i]
        return html

    def set_strategy(self, strategy):
        self.__strategy = strategy