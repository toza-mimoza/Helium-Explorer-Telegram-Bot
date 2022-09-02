import BaseModel
from util.time_helper import get_iso_utc_time

class User(BaseModel):
    '''
    Telegram user class for the user talking to the bot
    '''
    def __init__(self, telegram_id, telegram_username: str) -> None:
        self.telegram_id = telegram_id
        self.telegram_username = telegram_username
        self.last_active_at = get_iso_utc_time()

    def set_last_active(self, iso_time):
        self.last_active_at = iso_time

    def set_last_active_now(self):
        self.last_active_at = get_iso_utc_time()