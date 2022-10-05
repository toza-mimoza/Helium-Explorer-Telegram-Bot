import zope.component
from .events import *

@zope.component.adapter(TriggerNotificationEvent)
def notification_event_handler(event):
    # logic for sending any kind of notification
    event.processed = True
    
@zope.component.adapter(UpdateHotspotEvent)
def update_hotspot_event_handler(event):
    # logic for updating a hotspot
    event.processed = True

@zope.component.adapter(UpdateHotspotsGloballyEvent)
def update_hotspots_globally_event_handler(event):
    # logic for updating a hotspot
    event.processed = True
