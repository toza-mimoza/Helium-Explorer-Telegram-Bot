from .BaseModel import BaseModel
from src.util.constants import DbConstants

class Configuration(BaseModel):
    def __init__(self, version: str, is_active: bool) -> None:
        super().__init__(DbConstants.TREE_CONFIGURATION)
        self.version = version
        self.version_active = is_active

    def __hash__(self) -> int:
        return hash(self.version)
    
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, self.__class__) and self.version == __o.version
