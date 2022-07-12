import asyncio
from telegram import Update
from telegram.ext import ContextTypes
from bot.helium_requests import get_bc_stats

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

async def get_blockchain_stats(update: Update, context: ContextTypes):
    '''
    Echo Helium Blockchain API
    '''
    response = await get_bc_stats()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)
