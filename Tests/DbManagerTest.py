import unittest
from 


class DbManagerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.db = DbManager()
        pass

    def test_connect(self):
        connectionString = ""
        response = self.db.connectToServer(connectionString)
        self.assertEqual(response, True)

    def test_selectCollection(self):
        self.db.selectDb('test') #collectionsFilled 
        returnedCollections = self.db.collections
        collectionList = []
        self.assertListEqual(returnedCollections,collectionList)
        pass

    def test_createCollection(self):
        res = self.db.createCollection('newTestCollection')
        self.assertEqual(res, True)
        pass
    
    def test_removeCollection(self):
        res = self.db.removeCollection('newTestCollection')
        self.assertEqual(res, True)
        pass

    def test_disconnect(self):
        res = self.db.disconnect()
        self.assertEqual(res, True)
        pass