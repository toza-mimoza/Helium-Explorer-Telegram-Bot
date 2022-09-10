from .BaseModel import BaseModel
from src.util.time_helper import get_iso_utc_time
from src.util.constants import DbConstants

class User(BaseModel):
    '''
    Telegram user class for the user talking to the bot
    '''
    def __init__(self, telegram_id, telegram_username: str) -> None:
        super().__init__(DbConstants.TREE_NAME_USERS)
        self.telegram_user_id = telegram_id
        self.telegram_username = telegram_username
        self.last_active_at = get_iso_utc_time()
    
    def __hash__(self) -> int:
        return hash(self.telegram_user_id, self.telegram_username)
    
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, self.__class__) and self.telegram_id == __o.telegram_id

    def set_last_active(self, iso_time):
        self.last_active_at = iso_time

    def set_last_active_now(self):
        self.last_active_at = get_iso_utc_time()