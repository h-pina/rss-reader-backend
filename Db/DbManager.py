from pymongo import MongoClient
import DbCollectionManager

#Maybe separate this class in two? ConnectionManager to connect to server and DB manager to DB spacific operations
class DbManager():

    def __init__(self) -> None:
        self.collectionList  = []
        self.client = None
        self.selectedDb = None
        pass

    def connect(self, connectionString, db = None):
        self.client = MongoClient(connectionString)
        if db:
            self.selectDb(db)


    def selectDb(self, dbName):
        if dbName in self.client.list_database_names():
            self.selectedDb = self.client[dbName]
            collectionNames = self.selectedDb.list_collection_names()
            self.collectionList = [DbCollectionManager(self.selectedDb[colName]) for colName in collectionNames] #TODO: talvez mudar isso pra um key-value pair pra acessar melhor
        else:
            raise Exception("Database doesnt exist")
        
    def createCollection(self, collectionName):
        if collectionName in self.client.list_collection_names():
            return False
        else:
            newCollection = self.selectedDb[collectionName]
            self.collectionList.append(DbCollectionManager(newCollection))
            return True

    def __del__(self):
        self.client.close()