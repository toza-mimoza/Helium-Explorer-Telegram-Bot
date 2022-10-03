from typing import List

from util import get_int64_hash
from .BaseModel import BaseModel
from util.constants import DbConstants

class Owner(BaseModel):
    '''
    Hotspot owner class
    '''
    def __init__(self, account_address, telegram_user_id) -> None:
        # owner id is the helium account address 
        super().__init__(DbConstants.TREE_OWNERS, custom_uuid=get_int64_hash(account_address))
        self.account_address = account_address # PK
        self.telegram_user_id = telegram_user_id

    def get_account_address(self):
        return self.account_address

    def __hash__(self) -> int:
        return hash(self.account_address, self.telegram_user_id)
    
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, self.__class__) and self.account_address == __o.account_address
