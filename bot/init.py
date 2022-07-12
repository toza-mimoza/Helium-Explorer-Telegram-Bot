from telegram.ext import ApplicationBuilder

from bot.handlers import *
from util.read_secrets import read_secrets

SECRETS = read_secrets()

def init_bot():
    application = ApplicationBuilder().token(SECRETS["BOT_TOKEN"]).build()
    application.add_handlers(
        handlers=(
            start_handler, 
            echo_handler,
            bc_stats_handler,
            tk_supply_handler,
            hotspot_data_handler
        )
    )
    return application