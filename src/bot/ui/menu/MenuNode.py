from telegram import ReplyKeyboardMarkup

from util.time_helper import get_iso_utc_time

class MenuNode:
    def __init__(self, label: str, ui_object: ReplyKeyboardMarkup, parent = None, previous = None, next = None) -> None:
        self.label = label
        self.ui_object = ui_object
        self.parent = parent
        self.previous_node = (self, previous)[previous != None]
        self.next_node = (self,next)[next != None]
        self.created_at = get_iso_utc_time()
        self.last_used_at = get_iso_utc_time()
        
    def go_back(self):
        return self.previous_node

    def go_next(self):
        if(self.next_node):
            return self.next_node
        return None
    
    def set_previous_node(self, node):
        self.previous_node = node

    def set_next_node(self, node):
        self.next_node = node

    def get_menu(self):
        return self.ui_object

    def __repr__(self):
        return self.label
    
    def __str__(self):
        return self.label

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, self.__class__) and self.label == __o.label and self.created_at == __o.created_at
