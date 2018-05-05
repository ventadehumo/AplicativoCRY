
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
        print collection

    def insert_data(self, collection_name, data):
        print "[*] Insert data to new colection"
        #new_collection = self.db[collection]
        #result = posts.insert_one(data)
        print data
        Money_Collection = self.db.collection_name
        self.db.Money_Collection.insert(data)
        #print('[*] One post: {0}'.format(collection.inserted_id))
        print "[*] Data is in MongoDB"

    def view_data_incollection(self, collection):
        print "[*] View data of " + collection
        posts = self.db[collection]
        scotts_posts = posts.find()
        for post in scotts_posts:
            print(post)
