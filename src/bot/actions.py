from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

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
