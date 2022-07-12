from setuptools import Command
from .actions import *

from telegram.ext import filters, CommandHandler, MessageHandler

start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
bc_stats_handler = CommandHandler('bc_stats', send_blockchain_stats)
tk_supply_handler = CommandHandler('tk_supply', send_token_supply)
hotspot_data_handler = CommandHandler('hs_data', send_hotspot_data)
