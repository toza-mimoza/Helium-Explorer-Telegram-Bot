from typing import Optional
import persistent
from uuid import uuid4
from bot.db.DBUtil import DBUtil
from util.time_helper import get_iso_utc_time


class BaseModel(persistent.Persistent):
    def __init__(self, tree_name, custom_uuid: Optional[str] = None):
        
        self.active = True
        self.use_custom_id = False
        
        if custom_uuid: 
            self.use_custom_id = True
            self.uuid = custom_uuid # PK
        
        if not self.use_custom_id:
            self.uuid = uuid4() # PK (backup in children classes)
        
        self.last_updated_at = get_iso_utc_time()
        self.tree_name = tree_name
        
    def set_event(self, event):
        self.event = event
        
    def __repr__(self):
        return '{}-{}'.format(self.__class__.__name__, self.uuid)
    
    def __str__(self):
        return '{}-{}'.format(self.__class__.__name__, self.uuid)
    
    def __getitem__(self, key):
        return getattr(self, key)
    
    def update(self):
        '''! This method updates/refreshes DB record for the object.
        '''
        DBUtil.update_record(self.tree_name, str(self.uuid), self)