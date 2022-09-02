from typing import List
import BaseModel

class Owner(BaseModel):
    '''
    Hotspot owner class
    '''
    def __init__(self, helium_address, fk_user_id) -> None:
        # owner id is the helium user address 
        self.helium_address = helium_address
        self.telegram_user_id = fk_user_id
