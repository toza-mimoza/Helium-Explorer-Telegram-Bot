import ZODB, ZODB.FileStorage, zc.zlibstorage

storage = ZODB.FileStorage.FileStorage('data.fs')
compressed_storage = zc.zlibstorage.ZlibStorage(storage)
db = ZODB.DB(compressed_storage)

def store_obj(obj):
    '''
    Store an object in ZODB.
    '''
    with db.transaction() as connection: 
        connection.root[str(obj)] = obj