import logging
from re import S
from bot.db.DBConnection import DBConnection
from bot.db.DBManager import DBManager

from util.constants import DbConstants
from .db import db, transaction_manager
from typing import Any, Optional
from uuid import uuid4
from zope.generations.generations import generations_key
import ZODB, transaction

from util.exceptions import TreeReferencedDoesNotExist

log = logging.getLogger(__name__)

# last version: conn: Optional[ZODB.connection] = None

class DBUtil:
    """! Database utility class for inserting, updating and deleting DB records."""
    conn = DBConnection.connection

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def get_db_ref():
        """! Getter method for the DB reference.
        @return ZODB.DB object
        """
        return db

    @staticmethod
    def get_current_db_generation():
        """! Getter method for the DB upgrade generation.
        @param conn optional DB connection
        @return int
        """
        return DBUtil.conn.root()[generations_key][DbConstants.DB_APP_NAME] 

    
   ###############################################
    # Get, Insert, Update and Delete methods.     #
    ###############################################

    @staticmethod
    def get_record(tree_name: str, uuid: str):
        """! Get method for records in the DB.
        @param tree_name name of the OOBTree tree for the record
        @param uuid unique id of the record
        @return record if found, None otherwise
        """
        if not DBUtil.conn:
            DBUtil.conn = db.open()

        if uuid == -1:
            # return the first found record
            if len(DBUtil.conn.root()[tree_name].values()) == 0:
                return 0
            return None

        return DBUtil.conn.root()[tree_name].get(uuid)
            
    @staticmethod
    def insert_record(tree_name: str, uuid: str, object: Any):
        """! Insert method for records into DB.
        @param tree_name name of the OOBTree tree for the record to be inserted into
        @param uuid unique id of the record for later reference
        @param object data for the record 
        @return 1 if the item was inserted, or 0 otherwise
        """
        if not DBUtil.conn:
            DBUtil.conn = db.open()
        DBUtil.conn.root()[tree_name].insert(uuid, object)

    @staticmethod
    def insert_or_update_record(tree_name: str, uuid: str, object: Any):
        """! Insert or update method for records in the DB.
        @param tree_name name of the OOBTree tree for the record
        @param uuid unique id of the record or -1 if first found
        @param object data for the record 
        @return 1 if record added, 0 if not updated or not found
        """
        if not DBUtil.conn:
            DBUtil.conn = db.open()
        if(DBManager.tree_exists(tree_name)):
            if uuid == -1:
                if len(DBUtil.conn.root()[tree_name].values()) == 0:
                    # no records exist in the tree
                    return 0
                # update the last record
                DBUtil.conn.root()[tree_name].values()[-1] = object 
                return 1

            if DBUtil.conn.root()[tree_name].get(uuid) == 0:
                # specific uuid not found as a key in the tree
                return 0
            else:
                # key found and value updated
                DBUtil.conn.root()[tree_name][uuid] = object
                print(object)
                print(60*'*')
                print('INSERTED OR UPDATED RECORD')
                print(60*'*')
                transaction.commit()
                return 1
        else:
            log.warn(f'Tree {tree_name} does not exist. No error thrown because it\'s an update of a record.')
            return 0
    

    @staticmethod
    def update_record(tree_name: str, uuid: str, object: Any):
        """! Update method for records in the DB.
        @param tree_name name of the OOBTree tree for the record
        @param uuid unique id of the record
        @param object data for the record 
        @return 1 if record added, 0 if not updated or not found
        """
        
        if(DBManager.tree_exists(tree_name)):
            if(DBUtil.conn.root()[tree_name].get(uuid) == 0):
                return 0
            else:
                DBUtil.conn.root()[tree_name][uuid] = object
                print(object)
                print(60*'*')
                print('COMMITTING UPDATE RECORD')
                transaction.commit()
                print(60*'*')
                
                return 1
        else:
            log.warn(f'Tree {tree_name} does not exist. No error thrown because it\'s an update of a record.')
            return 0
    
    @staticmethod
    def delete_record(tree_name: str, uuid: str):
        """! Delete method marks record as active = False and thereby ready for later deletion from DB.
        @param tree_name name of the OOBTree tree for the record to be inserted into
        @param uuid unique id of the record 
        @return None
        """

        DBUtil.conn.root()[tree_name].get(uuid).active = False
        transaction.commit()

    ###############################################
    # General getters.                            #
    ###############################################   
    @staticmethod
    def _get_objects_from_tree(tree_name: str):
        """! Get all objects unfiltered from a tree."""
        if not DBManager.tree_exists(tree_name):
            raise TreeReferencedDoesNotExist(f'Referenced tree: {tree_name} does not exist!')
        return DBUtil.conn.root()[tree_name].values()

    @staticmethod
    def get_all(tree_name: str, **kwargs):
        """! Get all objects from a tree."""
        
        all_objs = DBUtil._get_objects_from_tree(tree_name)
        
        if kwargs:
            result = []
            for k, v in kwargs.items():
                for obj in all_objs:
                    if obj[k] == v and obj['active'] == True:
                        result.append(obj)

        return all_objs


    ###############################################
    # Object getters.                             #
    ###############################################   
    
    @staticmethod
    def get_users():
        """! Get all users from tree.
        @return all User type objects
        """ 
        return DBUtil.get_all(DbConstants.TREE_USERS)   

    @staticmethod
    def get_owners():
        """! Get all owners from tree.
        @return all User type objects
        """ 
        return DBUtil.get_all(DbConstants.TREE_OWNERS)   

    @staticmethod
    def get_hotspots():
        """! Get all hotspots from tree.
        @return all Hotspot type objects
        """ 
        return DBUtil.get_all(DbConstants.TREE_HOTSPOTS)   

    @staticmethod
    def get_activities():
        """! Get all activities from tree.
        @return all Activity type objects
        """ 
        return DBUtil.get_all(DbConstants.TREE_ACTIVITIES)   

    @staticmethod
    def get_menus():
        """! Get all menus from tree.
        @return all MenuNode type objects
        """ 
        return DBUtil.get_all(DbConstants.TREE_MENU_NODES)   
    
    @staticmethod
    def get_menus_by_user(telegram_user_id: str):
        """! Get all menus from a tree for specific user.
        @return all MenuNode type objects
        """ 
        return DBUtil.get_all(DbConstants.TREE_MENU_NODES, telegram_user_id=telegram_user_id)   
    
    @staticmethod
    def get_menu_manager_for_user(telegram_user_id: str):
        """! Get menu manager for specific user.
        @return all MenuNode type objects
        """
        query =  DBUtil.get_all(DbConstants.TREE_MENU_MANAGERS, telegram_user_id=telegram_user_id)
        if len(query) == 0:
            return None
        return query[0]
    
    @staticmethod
    def get_owner_by_telegram_id(telegram_user_id: str):
        """! Get owner record by specifying Telegram user ID."""
        return DBUtil.get_all(DbConstants.TREE_OWNERS, telegram_user_id=telegram_user_id)   
    
    @staticmethod
    def get_bots():
        """! Get all bots from tree.
        @return all BotInstance type objects
        """ 
        return DBUtil.get_all(DbConstants.TREE_BOT_INSTANCE)   

    @staticmethod
    def get_bot_for_user(telegram_user_id: str):
        """! Returns Bot type object. """
        query = DBUtil.get_all(DbConstants.TREE_BOT_INSTANCE, telegram_user_id=telegram_user_id)
        if len(query) == 0:
            return None
        return query[0]
         
    @staticmethod
    def is_bot_active(telegram_user_id: str) -> bool:
        """! Returns Bot.active field value. """
        instance = DBUtil.get_bot_for_user(telegram_user_id)

        if not instance:
            return False
        return instance.active
    
    @staticmethod
    def deactivate_bot_for_user(telegram_user_id: str) -> bool:
        """! Sets Bot.active field value to false. """
        instance = DBUtil.get_bot_for_user(telegram_user_id)
        instance.active = False
        DBUtil.insert_or_update_record()


    ###############################################
    # Other methods for objects                   #
    ###############################################
    
    @staticmethod
    def is_in_db(tree_name: str, uuid: str):
        """! Check if an uuid exists in all trees."""
        if not DBManager.tree_exists(tree_name):
            raise TreeReferencedDoesNotExist(f'Referenced tree: {tree_name} does not exist!')
            
        return True if DBUtil.conn.root()[tree_name].get(uuid) else False
    