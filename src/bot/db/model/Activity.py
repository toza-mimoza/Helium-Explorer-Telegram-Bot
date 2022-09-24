from .BaseModel import BaseModel
from util.constants import DbConstants

class Activity(BaseModel):
    def __init__(self, hash_value: str, helium_address: str, hotspot_address: str):
        super().__init__(DbConstants.TREE_ACTIVITIES, custom_uuid=hash_value)
        self.owner_address = helium_address
        self.hotspot_address = hotspot_address
        self.hash_value = hash_value # PK

    def __hash__(self) -> int:
        return self.hash_value
    
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, self.__class__) and self.hash_value == __o.hash_value