"""! @brief Main Python file for the program."""
##
# @file main.py
#
# @brief Main Python File for the Telegram Bot.
#
# @section description_main Description
# Main driving Python file for the Telegram Bot.
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

import os
from email.mime import application
from bot.db.DBManager import DBManager
import util.logger as logger
from util.read_secrets import read_secrets
from bot.init import init_bot
from definitions import LOGS_DIR
from bot.init import register_db_schema_manager
SECRETS = read_secrets()

if __name__ == "__main__":
    filename = SECRETS['BOT_NAME'] + '.log'
    logger.init_logger(os.path.join(LOGS_DIR, filename))
    
    db_schema_manager = register_db_schema_manager()
    db_schema_manager.install(DBManager.get_db_ref().open())
    application = init_bot()
    application.run_polling()