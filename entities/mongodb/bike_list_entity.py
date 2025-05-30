import os
import sys
from pymongo import MongoClient
from bson.objectid import ObjectId

sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../db")))

import mongodb_database as db

class BikeListEntity(db.VelostoreDatabase):
    """Classe pour gérer les opérations de base de données liées aux vélos."""

    def __init__(self):
        """Initialise BikeEntity."""
        super().__init__()
        self.bike_collection = self.mydb['Bike']
    
    def get_all_bike_list(self):
        """Récupère et affiche tous les vélos."""
        all_bikes = list(self.bike_collection.find({}))
        for bike in all_bikes:
            print(bike)
        return all_bikes

    def get_all_brand_list(self, expand=True):
        """Récupère et affiche toutes les marques."""
        if expand:
            all_brands = self.bike_collection.distinct("brand")
            for brand in all_brands:
                print(brand)
            return all_brands

def main():
    """Fonction principale pour la classe BikeListEntity."""
    super_velo = BikeListEntity()
    super_velo.get_all_bike_list()

if __name__ == '__main__':
    main()
