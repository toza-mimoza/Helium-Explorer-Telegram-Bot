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

from email.mime import application
import util.logger as logger
from util.read_secrets import read_secrets
from bot.init import init_bot

SECRETS = read_secrets()

if __name__ == "__main__":
    logger.init_logger(f"../logs/"+SECRETS['BOT_NAME']+".log")
    
    application = init_bot()
    application.run_polling()