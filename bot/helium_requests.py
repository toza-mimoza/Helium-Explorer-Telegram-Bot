from asyncore import read
import aiohttp

from util.read_secrets import read_secrets
from util.request_formatter import get_human_readable_text

SECRETS = read_secrets()
BASE_URL = 'https://api.helium.io'
API_URL = BASE_URL + '/' + '{api_version}' + '/' + '{route}'

header = {
    'User-Agent': '1.20.3 (linux-gnu)'
}


hotspot_activity = {
    '''
    Last 24h of hotspot activity.
    '''
    'transactions': [],
    'witnessed': [],
    'last_updated_at': ''
}

async def get_request(URL, par = None):
    async with aiohttp.ClientSession(headers=header) as session:
        async with session.get(URL) as resp:
            return await resp.json()

async def get_bc_stats():
    return await get_request(API_URL.format(api_version='v1', route='stats'))

async def get_token_supply():
    return await get_request(API_URL.format(api_version='v1', route='stats/token_supply'))

async def get_hotspot_data():
    return await get_request(API_URL.format(api_version='v1', route='hotspots/'+SECRETS['HOTSPOT_ADDRESS']))

async def get_hotspot_activity():
    return await get_request(API_URL.format(api_version='v1', route='hotspots/'+SECRETS['HOTSPOT_ADDRESS']+'/roles'))

async def get_recent_hotspot_activity():
    return await get_request(API_URL.format(api_version='v1', route='hotspots/'+SECRETS['HOTSPOT_ADDRESS']+'/roles'))
