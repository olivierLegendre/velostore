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
    def get_all_brand_list(self):
        """Récupère et affiche toutes les marques."""
        all_brands = self.bike_collection.distinct("brand.brand")
        for brand in all_brands:
            print(brand)
        return all_brands
    
    # Reqûtes internal parameters list 
    def get_all_bike_color(self):
        colors = self.bike_collection.find({}, {"config.color":1, "_id":0})
        unique_colors = set()
        for color in colors:
            if "config" in color and isinstance(color["config"], dict):
                unique_colors.add(color["config"]["color"])
        return unique_colors

    def get_all_bike_size(self):
        sizes = self.bike_collection.find({}, {"config.size":1, "_id":0})
        unique_sizes = set()
        for size in sizes:
            if "config" in size and isinstance(size["config"], dict):
                unique_sizes.add(size["config"]["size"])
        return unique_sizes
    
    def get_all_bike_destinations(self):
        destinations = self.bike_collection.find({}, {"brand.destination": 1, "_id": 0})
        unique_destinations = set()
        for destination in destinations:
            if "brand" in destination and isinstance(destination["brand"], dict):
                unique_destinations.add(destination["brand"]["destination"])
        print(unique_destinations)
        return unique_destinations

def main():
    """Fonction principale pour la classe BikeListEntity."""
    super_velo = BikeBrandListEntity()
    super_velo.get_all_bike_destinations()

if __name__ == '__main__':
    main()
