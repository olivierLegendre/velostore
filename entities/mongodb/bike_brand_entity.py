import os
import sys
from bson.objectid import ObjectId

sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../db")))

import mongodb_database as db

class BikeBrandEntity(db.VelostoreDatabase):
    """Classe pour gérer les opérations de base de données liées aux vélos."""

    def __init__(self):
        """Initialise BikeBrandEntity."""
        super().__init__()
        self.bike_collection = self.mydb['Bike']

    def create_tables(self):
        """Crée les collections nécessaires dans la base de données."""
        self.get_or_create_collection()

    def get_or_create_collection(self, collection_name="Bike"):
        """Récupère ou crée une collection dans la base de données."""
        if collection_name not in self.mydb.list_collection_names():
            self.mydb.create_collection(collection_name)
        return self.mydb[collection_name]

    # Requête CRUD
    def create_bike(self, bike_data):
        result = self.bike_collection.insert_many(bike_data)
        return result.inserted_ids

    def get_bike_by_id(self, bike_id, expand=True):
        bike = self.bike_collection.find_one({"_id": ObjectId(bike_id)})
        return bike

    def update_bike(self, bike_id, update_data):
        result = self.bike_collection.update_one({"_id": ObjectId(bike_id)}, {"$set": update_data})
        return result.modified_count

    def delete_bike(self, bike_id):
        result = self.bike_collection.delete_one({"_id": ObjectId(bike_id)})
        return result.deleted_count

    def get_brand_by_id(self, bike_id, expand=True):
        bike = self.bike_collection.find_one({"_id": ObjectId(bike_id)}, {"brand": 1, "_id": 0})
        return bike.get("brand") if bike else None

def main():
    """Fonction principale pour la classe BikeEntity."""
    super_velo = BikeBrandEntity()
    super_velo.get_bike_by_id('6839748b4445c30a2120347d')

if __name__ == '__main__':
    main()
