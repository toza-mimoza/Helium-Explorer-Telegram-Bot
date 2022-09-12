from telegram import KeyboardButton, ReplyKeyboardMarkup
from bot.ui.menu.MenuManager import MenuManager
from util.constants import UiLabels
from .menu.MenuNode import MenuNode

btn_start = KeyboardButton(UiLabels.UI_LABEL_MENU_START)
btn_end = KeyboardButton(UiLabels.UI_LABEL_MENU_BACK)
btn_overview = KeyboardButton(UiLabels.UI_LABEL_MENU_OVERVIEW)
btn_snooze = KeyboardButton(UiLabels.UI_LABEL_MENU_SNOOZE)
btn_settings = KeyboardButton(UiLabels.UI_LABEL_MENU_SETTINGS)
btn_back = KeyboardButton(UiLabels.UI_LABEL_MENU_BACK)


kb_main_menu = [
    [btn_start, btn_overview],
    [btn_snooze, btn_settings]
    ]

main_menu_keyboard = ReplyKeyboardMarkup(kb_main_menu)

kb_snooze = [
    [btn_snooze, btn_snooze],
    [btn_snooze, btn_back]
    ]

snooze_sub_menu_keyboard = ReplyKeyboardMarkup(kb_snooze)

kb_settings = [
    [btn_settings, btn_settings],
    [btn_settings, btn_back]
    ]

settings_sub_menu_keyboard = ReplyKeyboardMarkup(kb_settings)

kb_overview = [
    [btn_overview, btn_overview],
    [btn_overview, btn_back]
    ]

overview_sub_menu_keyboard = ReplyKeyboardMarkup(kb_overview)

main_menu = MenuNode(UiLabels.UI_LABEL_MAIN_MENU, main_menu_keyboard, None)
sub_menu_settings = MenuNode(UiLabels.UI_LABEL_MENU_SETTINGS, settings_sub_menu_keyboard, main_menu)
sub_menu_snooze = MenuNode(UiLabels.UI_LABEL_MENU_SNOOZE, snooze_sub_menu_keyboard, main_menu)
sub_menu_overview = MenuNode(UiLabels.UI_LABEL_MENU_OVERVIEW, overview_sub_menu_keyboard, main_menu)

menu_manager = MenuManager()
menu_manager.set_menu(main_menu)
