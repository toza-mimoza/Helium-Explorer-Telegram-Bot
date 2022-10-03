from .BaseModel import BaseModel
from util.constants import DbConstants

class BotInstance(BaseModel):
    def __init__(self, telegram_user_id: int) -> None:
        super().__init__(DbConstants.TREE_BOT_INSTANCE, custom_uuid = telegram_user_id)
        self.telegram_user_id = telegram_user_id # PK

    def __hash__(self) -> int:
        return hash(self.telegram_user_id + '_BotInstance')
    
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, self.__class__) and self.telegram_user_id == __o.telegram_user_id
