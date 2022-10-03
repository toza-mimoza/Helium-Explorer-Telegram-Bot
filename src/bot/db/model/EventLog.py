from .BaseModel import BaseModel
from util.constants import DbConstants

class EventLog(BaseModel):
    def __init__(self, event) -> None:
        super().__init__(DbConstants.TREE_EVENTS_LOG)
        self.event = event

    def __hash__(self) -> int:
        return hash(self.event)
    
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, self.__class__) and self.event == __o.event
