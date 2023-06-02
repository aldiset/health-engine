from pymongo import MongoClient

from app.config.config import CONNECTION_MONGO

class MongoDB:
    def __init__(self, database_name):
        self.client = MongoClient(CONNECTION_MONGO)
        self.db = self.client[database_name]
    
    def create(self, collection_name, document):
        collection = self.db[collection_name]
        result = collection.insert_one(document)
        return result.inserted_id
    
    def read(self, collection_name, query):
        collection = self.db[collection_name]
        document = collection.find_one(query)
        return document
    
    def update(self, collection_name, query, update_data):
        collection = self.db[collection_name]
        result = collection.update_one(query, {"$set": update_data})
        return result.modified_count
    
    def delete(self, collection_name, query):
        collection = self.db[collection_name]
        result = collection.delete_one(query)
        return result.deleted_count
