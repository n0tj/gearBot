import aiohttp
import async_timeout
import asyncio

loop = asyncio.get_event_loop()
session = aiohttp.ClientSession(loop=loop)

#URL Checker
async def urlCheck(session, url):
    with async_timeout.timeout(10000):
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    return True
                else:
                    return False
   
        except Exception as error:
            return ("Your link is unreachable.")
