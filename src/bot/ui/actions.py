from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes
from bot.helium.helium_requests import *
from util.constants import UiLabels
from .items import menu_manager, main_menu, sub_menu_overview, sub_menu_snooze, sub_menu_settings

async def ui_start(update: Update, context: ContextTypes):
    '''
    Start bot UI action.
    '''
    # await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    
    await context.bot.send_message(chat_id=update.message.chat_id,
                     text = UiLabels.UI_LABEL_STUB,
                     reply_markup=main_menu.get_menu())

async def ui_stop(update: Update, context: ContextTypes):
    '''
    Stop button bot UI action.
    '''
    # await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    menu_manager.set_menu(main_menu)
    await context.bot.send_message(chat_id=update.message.chat_id,
                     text = UiLabels.UI_LABEL_STUB,
                     reply_markup=main_menu.get_menu())


async def ui_back(update: Update, context: ContextTypes):
    '''
    Back button bot UI action.
    '''
    # await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    menu_manager.delete_oldest_periodically(5)
    menu_manager.update_last_active(menu_manager.backward())
    await context.bot.send_message(chat_id=update.message.chat_id,
                     text = UiLabels.UI_LABEL_STUB,
                     reply_markup=menu_manager.backward().get_menu())


async def ui_overview(update: Update, context: ContextTypes):
    '''
    Overview menu bot UI action.
    '''
    # await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    
    menu_manager.set_menu(sub_menu_overview)
    await context.bot.send_message(chat_id=update.message.chat_id,
                     text = UiLabels.UI_LABEL_STUB,
                     reply_markup=sub_menu_overview.get_menu())


async def ui_snooze(update: Update, context: ContextTypes):
    '''
    Snooze notifications menu UI action.
    '''
    # await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    
    menu_manager.set_menu(sub_menu_snooze)
    await context.bot.send_message(chat_id=update.message.chat_id,
                     text = UiLabels.UI_LABEL_STUB,
                     reply_markup=sub_menu_snooze.get_menu())


async def ui_settings(update: Update, context: ContextTypes):
    '''
    Settings menu UI action.
    '''
    # await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    
    menu_manager.set_menu(sub_menu_settings)
    await context.bot.send_message(chat_id=update.message.chat_id,
                     text = UiLabels.UI_LABEL_STUB,
                     reply_markup=sub_menu_settings.get_menu())

