from typing import List
from operator import attrgetter

from bot.ui.menu.MenuNode import MenuNode
from util.constants import UiLabels
from util.time_helper import get_iso_utc_time, get_time_diff_timedelta


class MenuManager:
    def __init__(self) -> None:
        self.nodes: List[MenuNode] = []
        self.current: MenuNode = None

    def set_current_menu(self, menu: MenuNode):
        self.current = menu

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

    def delete_oldest_periodically(self, period_seconds):
        
        oldest = max(self.nodes, key=attrgetter('last_used_at'))
        if(oldest == UiLabels.UI_LABEL_MAIN_MENU):
            nodes_wo_main_menu = list(self.nodes)
            nodes_wo_main_menu.remove(oldest)
            oldest = max(nodes_wo_main_menu, key=attrgetter('last_used_at'))
        
        # begin deleting if 
        if(len(self.nodes) > 2):
            for i in range(len(self.nodes)):
                if(self.nodes[i] == oldest):
                    if(get_time_diff_timedelta(oldest.last_used_at, get_iso_utc_time()).seconds > period_seconds):
                        self.nodes.pop(i)
    def update_last_active(self, node):
        for i in range(len(self.nodes)):
            if(self.nodes[i] == node):
                self.nodes[i].last_used_at = get_iso_utc_time()

    def __str__(self):
        return 'Menu Manager contains <{num_menus}> menus'.format(num_menus = len(self.nodes))
    
    def __repr__(self):
        return self.__str__
   