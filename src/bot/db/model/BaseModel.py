import persistent
import uuid
from src.util.time_helper import get_iso_utc_time
from src.bot.db.db import DBManager
class BaseModel(persistent.Persistent):
    def __init__(self, tree_name):
        self.active = True
        self.uuid = uuid.uuid4()
        self.last_updated_at = get_iso_utc_time()
        self.tree_name = tree_name

    def __repr__(self):
        return '{}-{}'.format(self.__class__.__name__, self.uuid)
    
    def __str__(self):
        return '{}-{}'.format(self.__class__.__name__, self.uuid)
    
    def update(self):
        '''! This method updates/refreshes DB record for the object.
        '''
        DBManager.update_record(self.tree_name, str(self.uuid), self)