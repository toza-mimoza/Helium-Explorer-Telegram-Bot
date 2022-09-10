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

from telegram.ext import ApplicationBuilder, CallbackQueryHandler

from zope.generations.interfaces import ISchemaManager
from zope.generations.generations import evolveMinimumSubscriber
from zope.component import provideUtility
from bot.db.DBManager import DBManager

from bot.db.db_events import DatabaseOpenedEventStub
from bot.handlers import *
from util.read_secrets import read_secrets
from bot.db.DBUpgradeSchemaManager import DBUpgradeSchemaManager

from util.constants import DbConstants
SECRETS = read_secrets()


def init_bot():
    """! Initializes the Telegram Bot and message handlers.

    @return An initialized Telegram Bot.
    """
    application = ApplicationBuilder().token(SECRETS['BOT_TOKEN']).build()
    application.add_handlers(
        handlers=(
            # command handlers
            start_command_handler, 
            # echo_command_handler,
            bc_stats_command_handler,
            tk_supply_command_handler,
            hotspot_data_command_handler,
            hotspot_all_activity_command_handler,
            hotspot_recent_activity_command_handler,

            # message handlers
            ui_message_handler,
        )
    )

    return application

def register_db_schema_manager():
    db_schema_manager = DBUpgradeSchemaManager()
    provideUtility(db_schema_manager, ISchemaManager, name=DbConstants.DB_APP_NAME)
    evolveMinimumSubscriber(DatabaseOpenedEventStub(DBManager.get_db_ref()))
    return db_schema_manager