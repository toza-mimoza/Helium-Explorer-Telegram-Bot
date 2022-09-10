from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes
from bot.helium.helium_requests import *
from util.constants import UiLabels
from .ui_items import main_menu_keyboard

async def ui_start(update: Update, context: ContextTypes):
    '''
    Start bot UI action.
    '''
    # await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    
    await context.bot.send_message(chat_id=update.message.chat_id,
                     text = UiLabels.UI_LABEL_STUB,
                     reply_markup=main_menu_keyboard())

async def ui_end(update: Update, context: ContextTypes):
    '''
    End bot UI action.
    '''
    # await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    
    await context.bot.send_message(chat_id=update.message.chat_id,
                     text = UiLabels.UI_LABEL_STUB,
                     reply_markup=main_menu_keyboard())


async def ui_snooze(update: Update, context: ContextTypes):
    '''
    Snooze notifications UI action.
    '''
    # await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    
    await context.bot.send_message(chat_id=update.message.chat_id,
                     text = UiLabels.UI_LABEL_STUB,
                     reply_markup=main_menu_keyboard())


async def ui_settings(update: Update, context: ContextTypes):
    '''
    Settings UI action.
    '''
    # await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    
    await context.bot.send_message(chat_id=update.message.chat_id,
                     text = UiLabels.UI_LABEL_STUB,
                     reply_markup=main_menu_keyboard())

