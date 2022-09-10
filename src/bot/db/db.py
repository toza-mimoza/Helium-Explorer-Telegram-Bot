import logging
import json
import os
import ZODB, ZODB.FileStorage, zc.zlibstorage

log = logging.getLogger(__name__)
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
zstorage = ZODB.FileStorage.FileStorage('dataz.fs')

try:
    db = ZODB.DB(zstorage)
except:
    zstorage.close()
    zstorage = zc.zlibstorage.ZlibStorage(ZODB.FileStorage.FileStorage('dataz.fs'))
    db = ZODB.DB(zstorage)