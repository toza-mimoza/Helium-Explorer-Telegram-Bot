from util import get_int32_hash
from .BaseModel import BaseModel
from util.constants import DbConstants

class Hotspot(BaseModel):
    def __init__(self, hotspot_address: str, animal_name: str, account_address: str, status_online: str = 'online') -> None:
        super().__init__(DbConstants.TREE_HOTSPOTS, custom_uuid=get_int32_hash(hotspot_address))
        self.animal_name = animal_name
        self.hotspot_address = hotspot_address # PK
        self.account_address = account_address
        self.status_online = status_online


    def get_owner_address(self):
        return self.account_address

    def __hash__(self) -> int:
        return hash(self.hotspot_address, self.account_address)
    
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, self.__class__) and self.hotspot_address == __o.hotspot_address
