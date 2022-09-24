import json
import os
import logging

from BTrees.OOBTree import OOBTree

log = logging.getLogger(__name__)
from .db import db, __location__
from .DBConnection import DBConnection
from util.read_secrets import read_secrets

SECRETS = read_secrets()
class DBManager():
    
    def init_db() -> None:
        """! Initialization method for the DB. This method inserts all OOBTree objects at the root of the ZODB database.
        @return None
        """
        DBManager._create_all_trees()
        conn = db.open()
        DBConnection.set_connection(conn)

    ###############################################
    # Initalization methods for trees.            #
    ###############################################     
    
    @staticmethod
    def tree_exists(tree_name: str):
        """! Method that checks if given tree name exists in the DB.
        @param tree_name name of the OOBTree tree to be checked
        @return boolean
        """
        with db.transaction() as connection: 
            return tree_name in connection.root()

    @staticmethod
    def _create_tree(tree_name: str):
        """! Internal method for creating a tree with tree_name.
        @param tree_name name of the OOBTree tree to be created
        @return OOBTree inserted into DB named after tree_name parameter
        """
        if not DBManager.tree_exists(tree_name):    
            with db.transaction() as connection: 
                connection.root()[tree_name] = OOBTree()
                log.info('Created %s tree in the DB.', tree_name)
                return connection.root()[tree_name]    
    
    @staticmethod
    def _create_all_trees():
        """! Internal method for creating trees from trees JSON file.
        @return None
        """
        with open(os.path.join(__location__, 'trees.json'), 'r') as f:
            trees = json.load(f)
        # loop through tree names in json and create OOBTrees for each of them
        for tree in trees['trees']: 
            DBManager._create_tree(tree['name'])
        log.info('Finished tree structure creation in the DB.')
    
    ###############################################
    # Shortcut getter methods for trees.          #
    ###############################################

    @staticmethod
    def get_users_tree():
        """! Getter for 'users' tree.
        @return OOBTree named 'users'
        """ 
        if DBManager.tree_exists('users'):    
            with db.transaction() as connection: 
                return connection.root.users
        else:
            return DBManager._create_tree('users')

    @staticmethod
    def get_owners_tree():
        """! Getter for 'owners' tree.
        @return OOBTree named 'owners'
        """   
        if DBManager.tree_exists('owners'):    
            with db.transaction() as connection: 
                return connection.root.owners
        else:
            return DBManager._create_tree('owners')
      
    @staticmethod
    def get_hotspots_tree():
        """! Getter for 'hotspots' tree.
        @return OOBTree named 'hotspots'
        """  
        if DBManager.tree_exists('hotspots'):    
            with db.transaction() as connection: 
                return connection.root.hotspots
        else:
            return DBManager._create_tree('hotspots')
    
    @staticmethod
    def get_activities_tree():
        """! Getter for 'activities' tree.
        @return OOBTree named 'activities'
        """
        if DBManager.tree_exists('activities'):    
            with db.transaction() as connection: 
                return connection.root.activities
        else:
            return DBManager._create_tree('activities')