import hashlib

def get_int32_hash(string: str):
    """! This function returns a 32 digits long integer, which is used for assigning uuid to OOBTree (=>tables in DB) items (=>records). 
    Since a BTree collection such as OOBTree used in this bot only accepts integers as keys, this function is used to hash an existing unique key for the item in OBTree.
    
    @param string: str unique string to be hashed (e.g. hotspot_address for hotspots)
    
    @return 32 digit long integer hash value of the string
    """
    hash_obj = hashlib.sha256(string.encode('utf-8')) 
    int_hash = int(hash_obj.hexdigest(), base=16) % 10**32
    return int_hash