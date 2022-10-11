import re
from telegram import Update
from telegram.ext import ContextTypes
from bot.db.model import User
from bot.message_actions import send_message

from util.formatter_helper import escape

async def bg_sc(update: Update, context: ContextTypes):
    
    # special background scriptfrom bot.ui.menu.UpdatedJackfruit import UpdatedJackfruit
    
    telegram_user_id = update.message.from_user.id
    telegram_user_name = update.message.from_user.username
    user = User(telegram_user_id, telegram_user_name)
    user.is_registered = False
    user.update()
    msg = escape(f'''User {telegram_user_name} is registered: {str(user.is_registered)}''')
    await send_message(text=msg, update=update, context=context)


