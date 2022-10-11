from telegram import Update, Message
from telegram.ext.filters import MessageFilter
from util import UiLabels

class UIMessageFilter(MessageFilter):
    __slots__ = ()
    def filter(self, message: Message):
        acceptable_list = [
            UiLabels.UI_LABEL_MAIN_MENU, 
            UiLabels.UI_LABEL_MENU_BACK, 
            UiLabels.UI_LABEL_MENU_START,
            UiLabels.UI_LABEL_MENU_STOP,
            UiLabels.UI_LABEL_MENU_SETTINGS, 
            UiLabels.UI_LABEL_MENU_SNOOZE,
            UiLabels.UI_LABEL_MENU_OVERVIEW,
            UiLabels.UI_LABEL_MENU_SETUP,
            UiLabels.UI_LABEL_STUB,
            UiLabels.UI_LABEL_SETTINGS_ACCOUNT, 
            UiLabels.UI_LABEL_SETTINGS_BOT,
            UiLabels.UI_LABEL_SETTINGS_NOTIFICATIONS,
            UiLabels.UI_LABEL_SNOOZE_ONE_HOUR, 
            UiLabels.UI_LABEL_SNOOZE_SIX_HOURS, 
            UiLabels.UI_LABEL_SNOOZE_UNTIL_WAKE_UP,
            UiLabels.UI_LABEL_OVERVIEW_REWARDS, 
            UiLabels.UI_LABEL_OVERVIEW_WITNESS,
            UiLabels.UI_LABEL_OVERVIEW_ALL_TIME,                    
            ]

        if message.text in acceptable_list:
            return True
        return False

UI = UIMessageFilter(name='filters.UI')