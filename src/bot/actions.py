import re
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes, ConversationHandler
from bot.db import DBUtil
from bot.db.model import User
from bot.db.model.Owner import Owner
from bot.helium.actions import insert_hotspots_for_owner
from bot.jobs.jobs_manager import register_helium_jobs_for_user
from bot.ui.menu.MenuManager import MenuManager
from bot.ui.template.menus import build_main_menu

from util import get_telegram_user_id, address_regex
from util.constants import DbConstants, UiLabels
from util.formatter_helper import escape

async def bg_sc(update: Update, context: ContextTypes):
    
    # special background script
    
    telegram_user_id = update.message.from_user.id
    telegram_user_name = update.message.from_user.username
    user = User(telegram_user_id, telegram_user_name)
    user.is_registered = False
    user.update()
    msg = escape(f'''User {telegram_user_name} is registered: {str(user.is_registered)}''')
    await send_message(text=msg, update=update, context=context)


def _init_menu_manager_for_user(update: Update):
    telegram_user_id = update.message.from_user.id
    menu_manager = DBUtil.get_menu_manager_for_user(telegram_user_id)
    if not menu_manager:
        menu_manager = MenuManager(telegram_user_id)
    DBUtil.insert_or_update_record(
        DbConstants.TREE_MENU_MANAGERS, telegram_user_id, menu_manager)

    return menu_manager
# conversation handler state
INPUT = 0

async def send_message(text: str, update: Update, context: ContextTypes):
    '''! Text that is not a command will be echoed back to the user.
    '''
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode=ParseMode.MARKDOWN)

async def send_mdv2_message(text: str, update: Update, context: ContextTypes):
    '''! Text that is not a command will be echoed back to the user.
    '''
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode=ParseMode.MARKDOWN_V2)

async def send_html_message(text: str, update: Update, context: ContextTypes):
    '''! Text that is not a command will be echoed back to the user.
    '''
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode=ParseMode.HTML)

# Setup conversation handler functions 
async def setup_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """! Start the conversation and ask user for input."""
    await update.message.reply_text(
        "Hi! Before you go on, I'll need to know your account address. Using this address I can assign your hotspot(s) for monitoring. "
        "What is you account (or owner) address?",
    )

    return INPUT

async def setup_end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """! End the conversation once address is given."""
    
    return ConversationHandler.END

async def setup_input(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """! Callback when user enters and sends message containing an (Helium) address"""

    telegram_user_id = get_telegram_user_id(update)
    text = update.message.text

    regex_result = re.findall(address_regex, text)
    if len(regex_result)>0:
        account_address = regex_result[0]
    else:
        account_address = None

    if account_address:
        owner = Owner(account_address, telegram_user_id)
        owner.update()
        telegram_user_id = update.message.from_user.id
        telegram_user_name = update.message.from_user.username
        
        # update the user to registered
        user = User(telegram_user_id, telegram_user_name)
        user.is_registered = True
        user.update()
        
        # activate bot
        DBUtil.activate_bot_for_user(telegram_user_id)
        
        # assign hotspots for user
        await insert_hotspots_for_owner(account_address, telegram_user_id, context)
        
        # register Helium jobs for that user
        register_helium_jobs_for_user(telegram_user_id, context)
        
        # send reply message notifying user of registration
        await update.message.reply_text(
            "Alright.Done! I'll send you a message as soon as I notice activity in your hotspots. 🤗",
            parse_mode=ParseMode.MARKDOWN
        )
        menu_manager = _init_menu_manager_for_user(update)
        menu_manager.set_menu(build_main_menu(telegram_user_id))
        await context.bot.send_message(chat_id=update.message.chat_id,
                                    text=UiLabels.UI_MSG_MAIN,
                                    reply_markup=menu_manager.get_current_menu().get_menu())


        return ConversationHandler.END
    else:
        return INPUT
