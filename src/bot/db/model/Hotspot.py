from .BaseModel import BaseModel

class Hotspot(BaseModel):
    def __init__(self, hotspot_address: str, animal_name: str, fk_owner_address: str) -> None:
        super().__init__()
        self.animal_name = animal_name
        self.hotspot_address = hotspot_address
        self.owner_address = fk_owner_address