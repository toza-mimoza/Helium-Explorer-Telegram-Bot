from .BaseModel import BaseModel
from util.constants import DbConstants

class BotInstance(BaseModel):
    def __init__(self, name: str, username: str, telegram_user_id: str) -> None:
        super().__init__(DbConstants.TREE_BOT)
        self.name = name
        self.username = username
        self.telegram_user_id = telegram_user_id

    def __hash__(self) -> int:
        return hash(self.name)
    
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, self.__class__) and self.name == __o.name and self.telegram_user_id == __o.telegram_user_id
