from telegram import ReplyKeyboardMarkup
from .buttons import *
kb_main_menu_var_setup = [
    [btn_setup, btn_overview],
    [btn_snooze, btn_settings]
    ]

main_menu_keyboard_var_setup = ReplyKeyboardMarkup(kb_main_menu_var_setup)

kb_main_menu_var_start = [
    [btn_start, btn_overview],
    [btn_snooze, btn_settings]
    ]

main_menu_keyboard_var_start = ReplyKeyboardMarkup(kb_main_menu_var_start)

kb_main_menu_var_stop = [
    [btn_stop, btn_overview],
    [btn_snooze, btn_settings]
    ]

main_menu_keyboard_var_stop = ReplyKeyboardMarkup(kb_main_menu_var_stop)

kb_snooze = [
    [btn_snooze_one_hour, btn_snooze_six_hours],
    [btn_snooze_until_wake_up, btn_back]
    ]

snooze_sub_menu_keyboard = ReplyKeyboardMarkup(kb_snooze)

kb_settings = [
    [btn_settings_account, btn_settings_bot],
    [btn_settings_notifications, btn_back]
    ]

settings_sub_menu_keyboard = ReplyKeyboardMarkup(kb_settings)

kb_overview = [
    [btn_overview_rewards, btn_overview_witness],
    [btn_overview_all_time, btn_back]
    ]

overview_sub_menu_keyboard = ReplyKeyboardMarkup(kb_overview)

# second lvl

kb_settings_account = [
    [btn_settings, btn_settings],
    [btn_settings, btn_back]
    ]

settings_account_sub_menu_keyboard = ReplyKeyboardMarkup(kb_settings_account)

kb_settings_bot = [
    [btn_settings, btn_settings],
    [btn_settings, btn_back]
    ]

settings_bot_sub_menu_keyboard = ReplyKeyboardMarkup(kb_settings_bot)
