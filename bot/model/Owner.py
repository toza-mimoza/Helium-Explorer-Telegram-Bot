from typing import List
import BaseModel

class Owner(BaseModel):
    '''
    Hotspot owner class
    '''
    def __init__(self, owner_id: str, hotspots: List) -> None:

        super().__init__(self.owner_id)
        # owner id is the helium user address 
        self.owner_id = owner_id
        # list of hotspots 
        self.hotspots = hotspots
