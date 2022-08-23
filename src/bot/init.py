"""! @brief Initializer for the Telegram Bot."""
##
# @file init.py
# @package bot
# @brief Initializer for the Telegram Bot.
#
# @section description_init_bot Description
# Initializes the Telegram Bot with all handlers.
#
# @section notes_init_bot Notes
# - Bot is initialized using unique Telegram Bot ID.
#
# @section todo_init_bot TODO
# - None.
#
# @section author_init_bot Author(s)
# - Created by Svetozar Stojanovic on 08/23/2022.
# - Modified by Svetozar Stojanovic on 08/23/2022.
#
# Copyright (c) 2022 Svetozar Stojanovic.  All rights reserved.

from telegram.ext import ApplicationBuilder

from bot.handlers import *
from util.read_secrets import read_secrets

SECRETS = read_secrets()


def init_bot():
    """! Initializes the Telegram Bot.

    @return An initialized Telegram Bot.
    """
    application = ApplicationBuilder().token(SECRETS["BOT_TOKEN"]).build()
    application.add_handlers(
        handlers=(
            start_handler, 
            echo_handler,
            bc_stats_handler,
            tk_supply_handler,
            hotspot_data_handler,
            hotspot_all_activity_handler,
            hotspot_recent_activity_handler
        )
    )
    return application