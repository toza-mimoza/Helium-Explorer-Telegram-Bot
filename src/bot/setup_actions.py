
import re
from telegram.ext import ContextTypes, ConversationHandler
from telegram import Update
from bot.db import DBUtil
from bot.db.model import Owner, User
from bot.helium.actions import insert_hotspots_for_owner
from bot.jobs.jobs_manager import register_helium_jobs_for_user
from bot.message_actions import send_message
from util.constants import DbConstants
from util.update_helper import get_telegram_user_id
from util import address_regex

# conversation handler state
INPUT = 0

# Setup conversation handler functions 
async def setup_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """! Start the conversation and ask user for input."""
    
    msg = "Hi! Before you go on, I'll need to know your account address. Using this address I can assign your hotspot(s) for monitoring."
    await send_message(msg, update, context)

    msg = "What is you account (or owner) address?"    
    await send_message(msg, update, context)   
    
    return INPUT

async def setup_end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """! End the conversation once address is given."""
    
    return ConversationHandler.END

async def setup_input(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """! Callback when user enters and sends message containing an (Helium) address"""

    telegram_user_id = get_telegram_user_id(update)
    text = update.message.text

    account_address = text
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
        await insert_hotspots_for_owner(account_address, telegram_user_id, update, context)
        
        # register Helium jobs for that user
        register_helium_jobs_for_user(telegram_user_id, context)
        
        # send reply message notifying user of registration
        msg = "Alright.Done! I'll send you a message as soon as I notice activity in your hotspots. 🤗"
        await send_message(msg, update, context)
        
        # import locally here since it produces circular import error
        from bot.ui.actions import ui_start
        # basically execute /start command
        await ui_start(update, context)
        return ConversationHandler.END
    else:
        return INPUT
