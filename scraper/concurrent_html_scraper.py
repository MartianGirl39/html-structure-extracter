import asyncio
import concurrent.futures
import re


from concurrent.futures import ProcessPoolExecutor, as_completed, wait
from multiprocessing import cpu_count

import aiohttp
import numpy as np
from aiohttp import ClientConnectorError

from html_classes import Tag
from html_classes.html_full import Html
from scraper.scraper_strategies.scraper import Scraper


class ConcurrentHtmlScraper:

    __slots__ = ('__strategy', '__pool')

    def __init__(self):
        self.__strategy = Scraper()
        self.__pool = {}

    async def __extract_data(self, url, session):
        print("scraping %s" % url)
        try:
            async with session.get(url) as response:
                try:
                    page = await response.text()
                except Exception as exception:
                    print("exception was thrown, so return was none")
                    return None
                if page is None:
                    print("page was not opened, so return was none")
                    return None
                html = self.__strategy.scrape(page)
                if html is None:
                    print("strategy.scrape return none so return was none")
                    return None
                self.__pool[url] = html
                return html
        except ClientConnectorError as e:
            # maybe a custom exception here
            print("error in session so return was none")
            return None

    async def __extract_data_tasks(self, urls):
        async with aiohttp.ClientSession() as session:
            tasks = [
                self.__extract_data(url, session)
                for url in urls
            ]
            results = await asyncio.gather(*tasks)
            return_val = []
            for result in results:
                if result is not None:
                    return_val.append(result)
            # print(return_val)
            return return_val

    def async_wrapper(self, urls):
        return asyncio.run(self.__extract_data_tasks(urls))

    def scrape(self, urls):
        cores = cpu_count()
        executor = ProcessPoolExecutor()
        tasks = [
            executor.submit(self.async_wrapper, task_urls)
            for task_urls in np.array_split(urls, cores)
        ]
        fin, _ = wait(tasks)

        results = [
            task.result()
            for task in fin
        ]
        print("all tasks completed")
        return results

        #
        #
        # async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=10, limit_per_host=3)) as session:
        #     tasks = [
        #         self.__extract_data(url, session)
        #         for url in urls
        #     ]
        #     results = await asyncio.gather(*tasks)
        #     return results

    def get_structure_from(self, urls):
        return self.scrape(urls)
        # return asyncio.run(self.scrape(urls))

    def set_strategy(self, strategy):
        self.__strategy = strategy
