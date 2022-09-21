import persistent
from uuid import uuid4
from util.time_helper import get_iso_utc_time
from bot.db.DBManager import DBManager

from typing import Optional

class BaseModel(persistent.Persistent):
    def __init__(self, tree_name):
        self.active = True
        self.uuid = uuid4()
        self.last_updated_at = get_iso_utc_time()
        self.tree_name = tree_name

    def set_event(self, event):
        self.event = event
        
    def __repr__(self):
        return '{}-{}'.format(self.__class__.__name__, self.uuid)
    
    def __str__(self):
        return '{}-{}'.format(self.__class__.__name__, self.uuid)
    
    def update(self):
        '''! This method updates/refreshes DB record for the object.
        '''
        DBManager.update_record(self.tree_name, str(self.uuid), self)