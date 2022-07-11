from telegram.ext import ApplicationBuilder

from util.read_secrets import read_secrets

SECRETS = read_secrets()

def init_bot():
    return ApplicationBuilder().token(SECRETS["BOT_TOKEN"]).build()
