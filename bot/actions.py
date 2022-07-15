import asyncio
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes
from bot.helium_requests import *

async def start(update: Update, context: ContextTypes):
    '''
    /start bot command.
    '''
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def echo(update: Update, context: ContextTypes):
    '''
    Text that is not a command will be echoed back to the user.
    '''
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def send_blockchain_stats(update: Update, context: ContextTypes):
    '''
    Get Helium Blockchain stats
    '''
    response = await get_bc_stats()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response, parse_mode=ParseMode.MARKDOWN)


async def send_token_supply(update: Update, context: ContextTypes):
    '''
    Get current token supply
    '''
    response = await get_token_supply()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

async def send_hotspot_data(update: Update, context: ContextTypes):
    '''
    Get current token supply
    '''
    response = await get_hotspot_data()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

async def send_all_hotspot_activity(update: Update, context: ContextTypes):
    '''
    Get current token supply
    '''
    response = await get_hotspot_activity()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

async def send_recent_hotspot_activity(update: Update, context: ContextTypes):
    '''
    Get recent 24h hotspot activity
    '''
    response = await get_hotspot_activity()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)
