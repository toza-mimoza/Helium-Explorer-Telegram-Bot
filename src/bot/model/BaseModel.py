import persistent

class BaseModel(persistent.Persistent):
    def __init__(self,name) -> None:
        self.name = name
    def __repr__(self):
        return '{}-{}'.format(self.__class__.__name__, self.name)
    def __str__(self):
        return '{}-{}'.format(self.__class__.__name__, self.name)
