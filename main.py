from email.mime import application
import util.logger as logger
from util.read_secrets import read_secrets
from bot.init import init_bot
from bot.handlers import *

SECRETS = read_secrets()

if __name__ == "__main__":
    logger.init_logger(f"logs/"+SECRETS['BOT_NAME']+".log")
    
    application = init_bot()
    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(bc_stats_handler)
    
    application.run_polling()