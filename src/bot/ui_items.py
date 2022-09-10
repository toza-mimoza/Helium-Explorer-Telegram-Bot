from telegram import KeyboardButton, ReplyKeyboardMarkup
from util.constants import UiLabels

def main_menu_keyboard():
    kb = [
        [KeyboardButton(UiLabels.UI_LABEL_OPTION_START), KeyboardButton(UiLabels.UI_LABEL_OPTION_END)],
        [KeyboardButton(UiLabels.UI_LABEL_OPTION_SNOOZE), KeyboardButton(UiLabels.UI_LABEL_OPTION_SETTINGS)]
        ]

    return ReplyKeyboardMarkup(kb)

def snooze_sub_menu_keyboard():
    kb = [
        [KeyboardButton(UiLabels.UI_LABEL_OPTION_START), KeyboardButton(UiLabels.UI_LABEL_OPTION_END)],
        [KeyboardButton(UiLabels.UI_LABEL_OPTION_SNOOZE), KeyboardButton(UiLabels.UI_LABEL_OPTION_SETTINGS)]
        ]

    return ReplyKeyboardMarkup(kb)

def settings_sub_menu_keyboard():
    kb = [
        [KeyboardButton(UiLabels.UI_LABEL_OPTION_START), KeyboardButton(UiLabels.UI_LABEL_OPTION_END)],
        [KeyboardButton(UiLabels.UI_LABEL_OPTION_SNOOZE), KeyboardButton(UiLabels.UI_LABEL_OPTION_SETTINGS)]
        ]

    return ReplyKeyboardMarkup(kb)
