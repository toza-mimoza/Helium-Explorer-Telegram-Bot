import BaseModel

class Hotspot(BaseModel):
    def __init__(self, hotspot_id: str) -> None:
        super().__init__(hotspot_id)
        # hotspot id is the hotspot address
        self.hotspot_id = hotspot_id