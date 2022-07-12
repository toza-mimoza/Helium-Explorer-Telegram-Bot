import json
import asyncio
import aiohttp

API_URL = 'https://api.helium.io'

headers = {
    'User-Agent': '1.20.3 (linux-gnu)'
}
# TO DO: aiohttp async requests

async def get_bc_stats():

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(API_URL+'/v1/stats') as resp:
            r = json.loads(await resp.read())
            print(r)
            return r