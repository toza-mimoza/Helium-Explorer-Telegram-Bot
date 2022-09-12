from telegram.ext import filters, CommandHandler, MessageHandler
from telegram.ext import ContextTypes

from .helium.actions import *
from .ui.actions import *
from util.constants import UiLabels
from .ui.actions import *

start_command_handler = CommandHandler('start', ui_start)
echo_command_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
bc_stats_command_handler = CommandHandler('bc_stats', send_blockchain_stats)
tk_supply_command_handler = CommandHandler('tk_supply', send_token_supply)
hotspot_data_command_handler = CommandHandler('hs_data', send_hotspot_data)
hotspot_all_activity_command_handler = CommandHandler('hs_activity_all', send_all_hotspot_activity)
hotspot_recent_activity_command_handler = CommandHandler('hs_activity_recent', send_recent_hotspot_activity)

async def ui_message_processor(update: Update, context: ContextTypes):
    
    received = update.message.text
    if UiLabels.UI_LABEL_MENU_START in received:
        # start invoked
        await ui_start(update, context)
    elif UiLabels.UI_LABEL_MENU_STOP in received:
        # end invoked 
        await ui_stop(update, context)
        pass
    elif UiLabels.UI_LABEL_MENU_BACK in received:
        # end invoked 
        await ui_back(update, context)
        pass
    elif UiLabels.UI_LABEL_MENU_OVERVIEW in received:
        # end invoked 
        await ui_overview(update, context)
        pass
    elif UiLabels.UI_LABEL_MENU_SNOOZE in received:
        # snooze options
        await ui_snooze(update, context)
        pass
    elif UiLabels.UI_LABEL_MENU_SETTINGS in received:
        # settings main menu 
        await ui_settings(update, context)
        pass
    pass

ui_message_handler = MessageHandler(filters.TEXT, ui_message_processor)

