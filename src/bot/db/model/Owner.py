from typing import List
from .BaseModel import BaseModel

class Owner(BaseModel):
    '''
    Hotspot owner class
    '''
    def __init__(self, helium_address, fk_user_id) -> None:
        # owner id is the helium user address 
        super().__init__()
        self.helium_address = helium_address
        self.telegram_user_id = fk_user_id

    def __hash__(self) -> int:
        return hash(self.helium_address, self.telegram_user_id)
    
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, self.__class__) and self.helium_address == __o.helium_address
