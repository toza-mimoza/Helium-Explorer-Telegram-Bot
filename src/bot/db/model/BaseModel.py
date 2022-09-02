import persistent
import uuid
from src.util.time_helper import get_iso_utc_time

class BaseModel(persistent.Persistent):
    def __init__(self):
        self.active = True
        self.uuid = uuid.uuid4()
        self.last_updated_at = get_iso_utc_time()
    def __repr__(self):
        return '{}-{}'.format(self.__class__.__name__, self.uuid)
    def __str__(self):
        return '{}-{}'.format(self.__class__.__name__, self.uuid)
