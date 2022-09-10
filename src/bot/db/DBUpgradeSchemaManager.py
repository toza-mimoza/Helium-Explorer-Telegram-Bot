from zope.component import globalregistry
gsm = globalregistry.getGlobalSiteManager()
from zope.generations.interfaces import IInstallableSchemaManager
from zope.interface import implementer


@implementer(IInstallableSchemaManager)
class DBUpgradeSchemaManager(object):
    minimum_generation = 1
    generation = 1
    
    def install(self, context):
        from .DBManager import DBManager    
        # preload db here
        DBManager.init_db()
        # root = context.connection.root()
        # end preload db
    
    def evolve(self, context, generation):
        root = context.connection.root()

        if generation == 1:
            pass
        elif generation == 2:
            pass
        else:
            raise ValueError('Given generation does not exist!')
