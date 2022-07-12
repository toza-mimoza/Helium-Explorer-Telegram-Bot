from setuptools import Command
from .actions import *

from telegram.ext import filters, CommandHandler, MessageHandler

start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
bc_stats_handler = CommandHandler('bc_stats', get_blockchain_stats)