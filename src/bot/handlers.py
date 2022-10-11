from telegram.ext import filters, CommandHandler, MessageHandler, ConversationHandler
from telegram.ext import ContextTypes

from bot.actions import bg_sc
from bot.setup_actions import setup_input, setup_end, setup_start
from bot.setup_actions import INPUT
from util.message_filters.UIMessageFilter import UI

from .helium.actions import *
from .ui.actions import *
from util.constants import UiLabels
from util import address_regex


start_command_handler = CommandHandler('start', ui_start)
setup_start_command_handler = CommandHandler('setup_start', ui_setup)
background_script_command = CommandHandler('bg', bg_sc)

# echo_command_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo, block=False)
bc_stats_command_handler = CommandHandler('bc_stats', send_blockchain_stats)
tk_supply_command_handler = CommandHandler('tk_supply', send_token_supply)
hotspot_data_command_handler = CommandHandler('hs_data', send_hotspot_data)
hotspot_all_activity_command_handler = CommandHandler('hs_activity_all', send_all_hotspot_activity)
hotspot_recent_activity_command_handler = CommandHandler('hs_activity_recent', send_recent_hotspot_activity)

roles_for_account_command_handler = CommandHandler('roles', send_roles_for_account)
hotspot_activity_command_handler = CommandHandler('hs_activity', send_hotspot_activity)
hotspot_rewards_command_handler = CommandHandler('hs_rewards', send_hotspot_rewards)

async def ui_message_processor(update: Update, context: ContextTypes):
    
    received = update.message.text
    if UiLabels.UI_LABEL_MENU_START in received:
        # start invoked
        await ui_start(update, context)
    elif UiLabels.UI_LABEL_MENU_STOP in received:
        # end invoked 
        await ui_stop(update, context)
    elif UiLabels.UI_LABEL_MENU_BACK in received:
        # end invoked 
        await ui_back(update, context)
    elif UiLabels.UI_LABEL_MENU_OVERVIEW in received:
        # end invoked 
        await ui_overview(update, context)
    elif UiLabels.UI_LABEL_MENU_SNOOZE in received:
        # snooze options
        await ui_snooze(update, context)
    elif UiLabels.UI_LABEL_MENU_SETTINGS in received:
        # settings main menu 
        await ui_settings(update, context)
    # else:
    #     msg = "It seems that something went wrong. Please retry your input."
    #     await send_html_message(msg, update, context)


ui_message_handler = MessageHandler(
    UI, # custom filter for UI messages/buttons 
    ui_message_processor, 
    block=False
    )

setup_conv_handler = ConversationHandler(
    entry_points=[MessageHandler(filters.Regex(UiLabels.UI_LABEL_MENU_SETUP), setup_start)],
    states={
        INPUT: [
            MessageHandler(
                filters.Regex(address_regex) & (~filters.COMMAND), 
                setup_input
            )
        ],
    },
    fallbacks=[CommandHandler("cancel", setup_end)],
    # allow_reentry=True,
)