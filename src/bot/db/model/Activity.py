from .BaseModel import BaseModel
from src.util.constants import DbConstants

class Activity(BaseModel):
    def __init__(self, fk_owner_address: str, fk_hotspot_address: str) -> None:
        super().__init__(DbConstants.TREE_NAME_ACTIVITIES)
        self.owner_address = fk_owner_address
        self.hotspot_address = fk_hotspot_address

    def __hash__(self) -> int:
        return hash(self.uuid, self.owner_address, self.hotspot_address)
    
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, self.__class__) and self.helium_address == __o.helium_address