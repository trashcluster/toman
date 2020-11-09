import pymongo
import os
import sys
import dns

# stop the program if no mongodb url is detected
try:  
    os.environ['MONGODBURL']
    MongoDbAccessLink = os.getenv('MONGODBURL')
except KeyError: 
    print ("ERROR, Please pass MongoDB full url in the system environment variables")
    sys.exit(1)

# Class used to interact with the database without having to initialize it in the main app
class Database:
    database = None

    # Initialize database, pass a database name
    @classmethod
    def initialize(cls, database):
        client = pymongo.MongoClient(MongoDbAccessLink)
        cls.database = client[database]

    # Input a dictionary "data" into the specified "collection"
    @classmethod
    def insert(cls, collection, data):
        cls.collection = cls.database[collection]
        cls.collection.insert_one(data)

    @classmethod
    def read(cls, collection, query):
        return_dict=[]
        cls.collection = cls.database[collection]
        if query == "":
            x = cls.collection.find()
        else:
            x = cls.collection.find(query)
        for i in x:
            return_dict.append(i)
        return return_dict

        
    #@classmethod
    #def update(cls, objid, key, param, data):
    #    cls.database.collection.update(  { _id:objid} , { $set: { key.param : data  } }

