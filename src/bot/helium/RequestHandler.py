from asyncio import sleep
from asyncore import read
import json
from typing import List, Optional
import aiohttp

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
        response = await RequestHandler.get(api_version='v1', res='stats')
        return response

    async def get_token_supply():
        response = await RequestHandler.get(api_version='v1', res='stats/token_supply')
        return response
         
    async def get_hotspot_data():
        '''! Get request for hotspot data.'''
        response = await RequestHandler.get(api_version='v1', res='hotspots/'+SECRETS['HOTSPOT_ADDRESS'])
        return response

    async def get_hotspot_activity():
        response = await RequestHandler.get(api_version='v1', res='hotspots/'+SECRETS['HOTSPOT_ADDRESS']+'/roles')
        return response

    async def get_recent_hotspot_activity():
        response = await RequestHandler.get(api_version='v1', res='hotspots/'+SECRETS['HOTSPOT_ADDRESS']+'/roles')
        return response
    
    async def get_roles_for_account(account_address):
        response = await RequestHandler.get(api_version='v1', res=f'accounts/{account_address}/roles')
        
        if(response['data'] == []):
            responses = []
            params = {
                'cursor': ''
            }
            while('cursor' in response):
                params['cursor'] = response['cursor']
                response = await RequestHandler.get(api_version='v1', res=f'accounts/{account_address}/roles', params=params)
                responses.append(response)
                print(response)
                await sleep(0.4)
        return len(str(responses))
         