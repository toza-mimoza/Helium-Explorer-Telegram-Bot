from util.time_helper import get_iso_utc_time

class BaseEvent:
    def __init__(self) -> None:
        self.name = self.__repr__()
        self.created_on = get_iso_utc_time()
        self.processed = False
        
    def __hash__(self) -> int:
        return hash(self.name, self.created_on)
    
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, self.__class__) and self.name == __o.name and self.created_on == __o.created_on

    def __repr__(self) -> str:
        self.__class__.__name__

class TriggerNotificationEvent(BaseEvent):
    '''! Event for triggering notifications to a specified user.'''
    def __init__(self, target, content) -> None:
        # user who receives the notification
        self.target = target
        # notification content
        self.content = content

class UpdateHotspotEvent(BaseEvent):
    def __init__(self, hotspot_address) -> None:
        self.hotspot_address = hotspot_address
        pass

class UpdateHotspotsGloballyEvent(BaseEvent):
    pass