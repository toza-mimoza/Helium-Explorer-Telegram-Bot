from typing import Optional
import persistent, logging
from uuid import uuid4
from bot.db.DBUtil import DBUtil
from util.time_helper import get_iso_utc_time
from util import get_int32_hash

log = logging.getLogger(__name__)
class BaseModel(persistent.Persistent):
    def __init__(self, tree_name, custom_uuid: Optional[int] = None):
        
        self.active = True
        self.use_custom_id = False
        
        if custom_uuid: 
            self.use_custom_id = True
            self.uuid = custom_uuid # any length PK specified in children classes
        
        if not self.use_custom_id:
            self.uuid = get_int32_hash(str(uuid4().hex) + get_iso_utc_time()) # 32 digits length as int PK (backup in children classes)
        
        self.last_updated_at = get_iso_utc_time()
        self.tree_name = tree_name
        
    def __repr__(self):
        return '{}-{}'.format(self.__class__.__name__, self.uuid)
    
    def __str__(self):
        return '{}-{}'.format(self.__class__.__name__, self.uuid)
    
    def __getitem__(self, key):
        return getattr(self, key)
    
    def update(self):
        '''! This method updates/refreshes DB record for the object.
        '''
        
        DBUtil.update_record(self.tree_name, self.uuid, self)
        