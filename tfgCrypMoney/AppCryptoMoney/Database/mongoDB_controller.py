
from pymongo import MongoClient
from bson import json_util

class database_Mongo:

    def __init__(self):
        print "[*] Conecting to MongoBD"
        self.client = MongoClient('localhost', 27017)
        #self.client = MongoClient('mongodb://IP:27017')
        self.db = None
        self.select_database('cryptomoney')

    def select_database(self, database):
        print "[*] Selecting database " + database
        self.db = self.client[database]
        #AUTH
        self.db.authenticate('user', 'pass')

    def view_all_collections(self):
        print "[*] View collection of " + str(self.db.name)
        collection = self.db.collection_names()
        return collection

    def insert_data(self, collection_name, data):
        print "[*] Insert data to new colection"
        print data
        Money_Collection = self.db.collection_name
        self.db.Money_Collection.insert(data)
        print "[*] Data is in MongoDB"

    def view_data_incollection(self, collection):
        print "[*] View data of " + collection
        posts = self.db[collection]
        scotts_posts = posts.find()
        collectionList = []
        for coin in scotts_posts:
            print(coin)
            collectionList.append(coin)
        return collectionList
