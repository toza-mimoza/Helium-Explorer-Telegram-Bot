from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def echo(update: Update, context: ContextTypes):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
