import logging

import ZODB, ZODB.FileStorage, zc.zlibstorage
from BTrees.OOBTree import OOBTree

log = logging.getLogger(__name__)

# def store_obj(group, obj):
#     '''
#     Store an object in ZODB.
#     '''
#     with db.transaction() as connection: 
#         connection.root[group] = obj
storage = ZODB.FileStorage.FileStorage('data.fs')
compressed_storage = zc.zlibstorage.ZlibStorage(storage)
db = ZODB.DB(compressed_storage)

class DBManager():
    def init_db() -> None:
        DBManager._create_all_trees()

    def tree_exists(tree_name):
        with db.transaction() as connection: 
            return tree_name in connection.root()

    # Create all Trees
    def _create_all_trees(self):
        DBManager._create_users_tree()
        DBManager._create_owners_tree()
        DBManager._create_hotspots_tree()
        DBManager._create_activities_tree()
        log.info('Finished tree structure creation in the DB.')
    
    # Create Telegram Users Tree
    def _create_users_tree():
        if not DBManager.tree_exists('users'):    
            with db.transaction() as connection: 
                connection.root.users = OOBTree()
                log.info('Created users tree in the DB.')
                return connection.root.users
            
    # Create Hotspot Owners Tree
    def _create_owners_tree():
        if not DBManager.tree_exists('owners'):    
            with db.transaction() as connection: 
                connection.root.owners = OOBTree() 
                log.info('Created owners tree in the DB.') 
                return connection.root.owners

    # Create Hotspots Tree
    def _create_hotspots_tree():
        if not DBManager.tree_exists('hotspots'):    
            with db.transaction() as connection: 
                connection.root.hotspots = OOBTree()
                log.info('Created hotspots tree in the DB.')
                return connection.root.hotspots  

    # Create Activities Tree
    def _create_activities_tree():
        if not DBManager.tree_exists('activities'):    
            with db.transaction() as connection: 
                connection.root.activities = OOBTree()
                log.info('Created activities tree in the DB.') 
                return connection.root.activities 

    def get_users_tree():
        if DBManager.tree_exists('users'):    
            with db.transaction() as connection: 
                return connection.root.users
        else:
            return DBManager._create_users_tree()
    
    def get_owners_tree():
        if DBManager.tree_exists('owners'):    
            with db.transaction() as connection: 
                return connection.root.owners
        else:
            return DBManager._create_owners_tree()
    
    def get_hotspots_tree():
        if DBManager.tree_exists('hotspots'):    
            with db.transaction() as connection: 
                return connection.root.hotspots
        else:
            return DBManager._create_hotspots_tree()
    
    def get_activities_tree():
        if DBManager.tree_exists('activities'):    
            with db.transaction() as connection: 
                return connection.root.activities
        else:
            return DBManager._create_activities_tree()