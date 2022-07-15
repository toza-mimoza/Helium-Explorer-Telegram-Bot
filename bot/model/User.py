import BaseModel

class User(BaseModel):
    '''
    Telegram user class for the user talking to the bot
    '''
    def __init__(self, telegram_id: str) -> None:

        super().__init__(self.telegram_id)
        self.telegram_id = telegram_id
