import os
import sys
from pymongo import MongoClient
from bson.objectid import ObjectId

sys.path.insert(1, r'c:\Users\coque\velostore\db')

import mongodb_database as db

class BikeEntity(db.MongoDBVelostoreDatabase):
    """Classe pour gérer les opérations de base de données liées aux vélos."""

    def __init__(self):
        """Initialise BikeEntity."""
        super().__init__()
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['velostore']
        self.bike_collection = self.db['Bike']

    def create_tables(self):
        """Crée les collections nécessaires dans la base de données."""
        self.get_or_create_collection()

    def get_or_create_collection(self, collection_name="Bike"):
        """Récupère ou crée une collection dans la base de données."""
        if collection_name not in self.db.list_collection_names():
            self.db.create_collection(collection_name)
        return self.db[collection_name]
    
    # Requête CRUD
    def create_bike(self, bike_data):
        result = self.bike_collection.insert_one(bike_data)
        return result.inserted_id
    
    def read_bike_by_id(self, bike_id):
        return self.bike_collection.find_one({"_id": ObjectId(bike_id)})
    
    def update_bike(self, bike_id, update_data):
        result = self.bike_collection.update_one({"_id": ObjectId(bike_id)}, {"$set": update_data})
        return result.modified_count

    def delete_bike(self, bike_id):
        result = self.bike_collection.delete_one({"_id": ObjectId(bike_id)})
        return result.deleted_count

    def get_brand_by_id(self, bike_id):
        bike = self.bike_collection.find_one({"_id": ObjectId(bike_id)}, {"brand": 1, "_id": 0})
        return bike.get("brand") if bike else None

def main():
    """Fonction principale pour la classe BikeEntity."""
    super_velo = BikeEntity()
    super_velo.create_tables()

if __name__ == '__main__':
    main()
