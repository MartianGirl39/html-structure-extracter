import unittest
import aiohttp
import asyncio

import pytest

from scraper.sessions.async_html_extracter import AsyncHtmlExtracter

pytest_plugins = ('pytest_asyncio',)


class MyTestCase(unittest.TestCase):

    async def _call_this(self):
        async  with aiohttp.ClientSession() as session:
            extracter = AsyncHtmlExtracter(session)
            await extracter.fetch_html("http://www.google.com")

    @pytest.mark.asynci
    async def test_something(self):
        await self._call_this()
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
