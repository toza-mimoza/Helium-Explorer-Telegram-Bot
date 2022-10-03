from asyncio import sleep
from asyncore import read
import json
from typing import List, Optional
import aiohttp
import logging

from bot.db.model import Activity 

log = logging.getLogger(__name__)

from telegram.constants import ParseMode

from util.read_secrets import read_secrets
from bot.helium.formatters import *

SECRETS = read_secrets()
BASE_URL = 'https://api.helium.io'
API_URL = BASE_URL + '/{api_version}/{res}'

header = {
    'User-Agent': '1.20.3 (linux-gnu)'
}

class RequestHandler:
    async def get(api_version, res, params: Optional[dict] = None):
        async with aiohttp.ClientSession(headers=header) as session:
            async with session.get(API_URL.format(api_version=api_version, res=res), params = params) as resp:
                return json.loads(await resp.read())     

    async def get_bc_stats():
        route = 'stats'
        response = await RequestHandler.get(api_version='v1', res=route)
        return response

    async def get_token_supply():
        route = 'stats/token_supply'
        response = await RequestHandler.get(api_version='v1', res=route)
        return response
         
    async def get_hotspot_data(hotspot_address):
        route = f'hotspots/{hotspot_address}'
        response = await RequestHandler.get_helium_request(route=route, use_limit=False, use_cursor=False)
        return response

    async def get_account_roles(account_address, cursor_depth=5, filter_types=None, min_time=None, max_time=None, limit=10):
        route = f'accounts/{account_address}/roles'
        responses = await RequestHandler.get_helium_request(route=route, cursor_depth=cursor_depth, filter_types=filter_types, min_time=min_time, max_time=max_time, limit=limit)
        return responses
    
    async def get_hotspot_rewards(hotspot_address, min_time=None, max_time=None, limit=10):
        route = f'hotspots/{hotspot_address}/rewards'
        responses = await RequestHandler.get_helium_request(route, use_limit = False, use_cursor=True, filter_types=None, min_time=min_time, max_time=max_time, limit=limit)
        return responses
        
    async def get_hotspot_roles(hotspot_address, cursor_depth=5, filter_types=None, min_time=None, max_time=None, limit=10):
        route = f'hotspots/{hotspot_address}/roles'
        responses = await RequestHandler.get_helium_request(route=route, use_limit=True, use_cursor=True, cursor_depth=cursor_depth, filter_types=filter_types, min_time=min_time, max_time=max_time, limit=limit)
        return responses

    async def get_helium_request(route: str, cursor_depth=5, filter_types=None, min_time=None, max_time=None, limit=10, use_cursor=True, use_limit = True):
        params = {}        
        if use_limit: 
            params['limit'] = limit

        if filter_types:
            params['filter_types'] = filter_types

        if min_time:
            params['min_time'] = min_time
        
        if max_time:
            params['max_time'] = max_time
        
        req_count = cursor_depth
        responses = []
        
        response = await RequestHandler.get(api_version='v1', res=route, params=params)
        
        if use_cursor:
            while('cursor' in response and req_count>0):
                req_count=req_count-1
                params['cursor'] = response['cursor']
                response = await RequestHandler.get(api_version='v1', res=route, params=params)
                responses.append(response['data'])
                # 0.4s delay between requests to ensure requests are processed
                await sleep(0.4)
        else:
            response = await RequestHandler.get(api_version='v1', res=route, params=params)
            response=response['data']

        log.info(f'''************************************
        Sent request to Helium API:
        Route: /{route}

        Params: {params}
        ***************************************
        ''')

        if not use_cursor:
            return response
        return responses