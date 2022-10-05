from .BaseModel import BaseModel
from util.constants import DbConstants
from util import get_int32_hash

class Activity(BaseModel):
    def __init__(self, hash_value: str, account_address: str, hotspot_address: str, activity_type: str, time: str, role: str, height: str):
        super().__init__(DbConstants.TREE_ACTIVITIES, custom_uuid=get_int32_hash(hash_value))
        self.account_address = account_address
        self.hotspot_address = hotspot_address
        self.hash_value = hash_value # PK
        self.activity_type = activity_type
        self.time = time
        self.role = role
        self.block_height = height

    def __hash__(self) -> int:
        return self.hash_value
    
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, self.__class__) and self.hash_value == __o.hash_value