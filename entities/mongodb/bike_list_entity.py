import os
import sys
from pymongo import MongoClient
from bson.objectid import ObjectId

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/../db")

import mongodb_database as db

class BikeListEntity(db.MongoDBVelostoreDatabase):
    """Classe pour gérer les opérations de base de données liées aux vélos."""

    def __init__(self):
        """Initialise BikeEntity."""
        super().__init__()
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['velostore']
        self.bike_collection = self.db['Bike']
    
    def get_all_bike_list(self, bike_id):
        bike_by_id = self.bike_collection.find_one({"_id": ObjectId(bike_id)})
        print(bike_by_id)
        return bike_by_id
    
    def get_all_brand_list(self, expand=True):
        if expand:
            all_brand = self.bike_collection.find_one({"brand": "Trek"})
            print(all_brand)

def main():
    """Fonction principale pour la classe BikeListEntity."""
    super_velo = BikeListEntity()
    super_velo.get_all_brand_list()

if __name__ == '__main__':
    main()
