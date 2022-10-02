from typing import List
from operator import attrgetter
from bot.db.model.BaseModel import BaseModel

from bot.ui.menu.MenuNode import MenuNode
from util.constants import DbConstants, UiLabels
from util.time_helper import get_iso_utc_time, get_time_diff_timedelta

import logging
log = logging.getLogger(__name__)

class MenuManager(BaseModel):
    def __init__(self, telegram_user_id: str) -> None:
        super().__init__(DbConstants.TREE_MENU_NODES, custom_uuid=telegram_user_id)
        self.nodes: List[MenuNode] = []
        self.current: MenuNode = None
        self.telegram_user_id = telegram_user_id
        
    def set_menu_nodes(self, nodes):
        """! Sets MenuNode list for the manager."""
        self.nodes = nodes
        self.update()

    def set_current_menu(self, menu: MenuNode):
        self.current = menu
        self.update()
    
    def get_current_menu(self) -> MenuNode:
        return self.current

    def set_menu(self, node: MenuNode):
        found = False
        for i in range(len(self.nodes)):
            if(self.nodes[i] == node):
                found = True
                if(len(self.nodes)>0):
                    self.nodes[i].set_previous_node(self.nodes[-1])
                    self.nodes[-1].set_next_node(self.nodes[i])
                self.set_current_menu(self.nodes[i])
                self.update_last_active(self.nodes[i])
                 
        if not found:
            if(len(self.nodes)>0):
                node.set_previous_node(self.nodes[-1])
                self.nodes[-1].set_next_node(node)
            self.nodes.append(node)
            self.set_current_menu(node)
            self.update_last_active(self.nodes[-1])
        
        self.update()

    def backward(self):
        if(len(self.nodes)<=1):
            return self.current
        last = self.nodes[-1]
        new = self.nodes[-1].go_back()

        self.nodes[-1] = new
        self.nodes[-2] = last

        self.set_current_menu(self.nodes[-1])

        return self.current
    
    def get_menu(self):
        return self.current.get_menu()

    def delete_oldest_periodically(self, threshold_seconds=5):
        
        did_delete = False

        oldest = max(self.nodes, key=attrgetter('last_used_at'))
        if(oldest == UiLabels.UI_LABEL_MAIN_MENU):
            nodes_wo_main_menu = list(self.nodes)
            nodes_wo_main_menu.remove(oldest)
            oldest = max(nodes_wo_main_menu, key=attrgetter('last_used_at'))
        
        # begin deleting if 
        if(len(self.nodes) > 2):
            for node in self.nodes[:]:
                if(node == oldest):
                    if(get_time_diff_timedelta(oldest.last_used_at, get_iso_utc_time()).seconds > threshold_seconds):
                        self.nodes.remove(node)
                        log.info('Deleted oldest menu.')
                        self.update()


    def update_last_active(self, node):
        for i in range(len(self.nodes)):
            if(self.nodes[i] == node):
                self.nodes[i].last_used_at = get_iso_utc_time()

        self.update()

    def __str__(self):
        return 'Menu Manager contains <{num_menus}> menus'.format(num_menus = len(self.nodes))
    
    def __repr__(self):
        return self.__str__
   