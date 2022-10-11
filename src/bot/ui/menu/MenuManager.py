from typing import List
from operator import attrgetter
from bot.db.model.BaseModel import BaseModel

from bot.ui.menu.MenuNode import MenuNode
from bot.ui.template.menus import build_main_menu
from util.constants import DbConstants, UiLabels
from util.time_helper import get_iso_utc_time, get_time_diff_timedelta

import logging
log = logging.getLogger(__name__)
from persistent.list import PersistentList
from persistent.dict import PersistentDict

class MenuManager(BaseModel):
    def __init__(self, telegram_user_id: str) -> None:
        super().__init__(DbConstants.TREE_MENU_MANAGERS, custom_uuid=telegram_user_id)
        self.nodes: PersistentList[MenuNode] = PersistentList()
        self.current: MenuNode = None
        self.telegram_user_id = telegram_user_id
        self.menu_order = -1
        self.menu_mapping: PersistentDict = PersistentDict()

    def set_current_menu(self, menu: MenuNode):
        self.current = menu
    
    def get_current_menu(self) -> MenuNode:
        return self.current

    def set_menu(self, node: MenuNode):
        self.menu_order += 1

        # update last active field of new menu
        node.last_used_at = get_iso_utc_time()
        node.set_menu_order(self.menu_order)

        # store menu with menu_order
        self.menu_mapping[self.menu_order] = node
        
        last = max(self.menu_mapping.keys())

        if len(self.menu_mapping) >= 2: 
            self.menu_mapping[last].previous_node = self.menu_mapping[last - 1]
            self.menu_mapping[last - 1].next_node = self.menu_mapping[last]

        # set current menu to that menu
        self.set_current_menu(self.menu_mapping[last])

    def backward(self):
        if len(self.menu_mapping)==0:
            # fallback to main menu
            log.info(f'Fallback to Main Menu via back button.')
            return build_main_menu(self.telegram_user_id)
        elif len(self.menu_mapping) == 1:
            return self.current
        else:
            self.menu_mapping[self.menu_order - 1].previous_node = self.menu_mapping[self.menu_order]
            self.menu_mapping[self.menu_order].next_node = self.menu_mapping[self.menu_order - 1]
            
            self.set_current_menu(self.menu_mapping[self.menu_order - 1])

            return self.current

    def get_menu(self):
        return self.current.get_menu()

    def delete_oldest_periodically(self, threshold_seconds=5):
        # To Do
        pass

    def __str__(self):
        return 'Menu Manager contains <{num_menus}> menus'.format(num_menus = len(self.menu_mapping))
    
    def __repr__(self):
        return self.__str__
   