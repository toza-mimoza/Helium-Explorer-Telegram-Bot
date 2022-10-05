from telegram import KeyboardButton
from util.constants import UiLabels

# first level - Main Menu
btn_setup = KeyboardButton(UiLabels.UI_LABEL_MENU_SETUP)
btn_start = KeyboardButton(UiLabels.UI_LABEL_MENU_START)
btn_stop = KeyboardButton(UiLabels.UI_LABEL_MENU_STOP)
btn_end = KeyboardButton(UiLabels.UI_LABEL_MENU_BACK)
btn_overview = KeyboardButton(UiLabels.UI_LABEL_MENU_OVERVIEW)
btn_snooze = KeyboardButton(UiLabels.UI_LABEL_MENU_SNOOZE)
btn_settings = KeyboardButton(UiLabels.UI_LABEL_MENU_SETTINGS)

# second level - Settings
btn_settings_account = KeyboardButton(UiLabels.UI_LABEL_SETTINGS_ACCOUNT)
btn_settings_bot = KeyboardButton(UiLabels.UI_LABEL_SETTINGS_BOT)
btn_settings_notifications = KeyboardButton(UiLabels.UI_LABEL_SETTINGS_NOTIFICATIONS)

# second level - Snooze
btn_snooze_one_hour = KeyboardButton(UiLabels.UI_LABEL_SNOOZE_ONE_HOUR)
btn_snooze_six_hours = KeyboardButton(UiLabels.UI_LABEL_SNOOZE_SIX_HOURS)
btn_snooze_until_wake_up = KeyboardButton(UiLabels.UI_LABEL_SNOOZE_UNTIL_WAKE_UP)

# second level - Settings
btn_overview_rewards = KeyboardButton(UiLabels.UI_LABEL_OVERVIEW_REWARDS)
btn_overview_witness = KeyboardButton(UiLabels.UI_LABEL_OVERVIEW_WITNESS)
btn_overview_all_time = KeyboardButton(UiLabels.UI_LABEL_OVERVIEW_ALL_TIME)

# special
btn_back = KeyboardButton(UiLabels.UI_LABEL_MENU_BACK)


