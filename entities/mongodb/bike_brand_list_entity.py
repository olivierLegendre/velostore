import os
import sys
from pymongo import MongoClient
from bson.objectid import ObjectId

sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../db")))

import mongodb_database as db

class BikeBrandListEntity(db.VelostoreDatabase):
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

    # surement une façon plus simple de faire ou modifier naming brand dans dict brand
    def get_all_bike_brand_list(self):
        """Récupère et retourne une liste de toutes les marques de vélos."""
        brands = self.bike_collection.find({}, {"brand.brand": 1, "_id": 0})
        # set pour virer les doublons
        unique_brands = set()
        for brand in brands:
            if "brand" in brand and isinstance(brand["brand"], dict) and "brand" in brand["brand"]:
                unique_brands.add(brand["brand"]["brand"])
        print(unique_brands)
        return unique_brands
    
    # Reqûtes internal parameters list 
    def get_all_bike_color(self):
        colors = self.bike_collection.find({}, {"config.color":1, "_id":0})
        unique_colors = set()
        for color in colors:
            if "config" in color and isinstance(color["config"], dict) and "color" in color["config"]:
                unique_colors.add(color["config"]["color"])
        print(unique_colors)

    def get_all_bike_size(self):
        sizes = self.bike_collection.find({}, {"config.size":1, "_id":0})
        unique_sizes = set()
        for size in sizes:
            if "config" in size and isinstance(size["config"], dict) and "size" in size["config"]:
                unique_sizes.add(size["config"]["size"])
        print(unique_sizes)

def main():
    """Fonction principale pour la classe BikeListEntity."""
    super_velo = BikeBrandListEntity()
    super_velo.get_all_bike_size()

if __name__ == '__main__':
    main()
