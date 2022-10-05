from bot.db.DBUtil import DBUtil
from bot.ui.menu.MenuNode import MenuNode

from util.constants import UiLabels
from .keyboards import *
def build_main_menu(telegram_user_id):
    if not DBUtil.is_user_registered(telegram_user_id):
        keyboard = main_menu_keyboard_var_setup
        return MenuNode(label='', telegram_user_id=telegram_user_id, ui_object=keyboard, previous=None)

    if DBUtil.is_bot_active(telegram_user_id):
        keyboard = main_menu_keyboard_var_stop
    else:
        keyboard = main_menu_keyboard_var_start
    return MenuNode(label=UiLabels.UI_LABEL_MAIN_MENU, telegram_user_id=telegram_user_id, ui_object=keyboard, previous=None)

def build_sub_menu_settings(telegram_user_id):
    return MenuNode(label=UiLabels.UI_LABEL_MENU_SETTINGS, telegram_user_id=telegram_user_id, ui_object=settings_sub_menu_keyboard)

def build_sub_menu_snooze(telegram_user_id):
    return MenuNode(label=UiLabels.UI_LABEL_MENU_SNOOZE, telegram_user_id=telegram_user_id, ui_object=snooze_sub_menu_keyboard)

def build_sub_menu_overview(telegram_user_id):
    return MenuNode(label=UiLabels.UI_LABEL_MENU_OVERVIEW, telegram_user_id=telegram_user_id, ui_object=overview_sub_menu_keyboard)


