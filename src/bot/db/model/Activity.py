from .BaseModel import BaseModel

class Activity(BaseModel):
    def __init__(self, activity_id: str, fk_owner_address: str, fk_hotspot_address: str) -> None:
        super().__init__()
        self.activity_id = activity_id
        self.owner_address = fk_owner_address
        self.hotspot_address = fk_hotspot_address