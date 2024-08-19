import inspect
from functools import wraps

from aiohttp import ClientSession
import async_to_sync


def _create_new_session(f):
    async def wrapper(self, url):
        self.__session = ClientSession(url)
        try:
            response = await f(self, url)
            return response.content
        finally:
            print("closing session")
            await self.__session.close()

    return wrapper


class AsyncHtmlExtracter:

    __slots__ = "__session"

    def __init__(self):
        self.__session: ClientSession

    @_create_new_session
    async def fetch_html(self, url):
        print("fetching url")
        response = await self.__session.get(url)
        if response.status == 200:
            return response.content
        return response.status

