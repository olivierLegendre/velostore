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

    def get_bike_brand_list(self, expand=True):
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
            unique_colors.add(color["config"]["color"])
        print(unique_colors)
        return unique_colors

    def get_all_prices_list(self):
        all_prices = self.bike_collection.find({}, {"brand.price": 1, "_id": 0})
        prices_list = []
        for price in all_prices:
            prices_list.append(price["brand"]["price"])
        return prices_list

    def get_all_bike_size(self):
        sizes = self.bike_collection.find({}, {"config.size":1, "_id":0})
        unique_sizes = set()
        for size in sizes:
                unique_sizes.add(size["config"]["size"])
        return unique_sizes
    
    def get_all_destinations_list(self):
        destinations = self.bike_collection.find({}, {"brand.destination": 1, "_id": 0})
        unique_destinations = set()
        for destination in destinations:
                unique_destinations.add(destination["brand"]["destination"])
        return unique_destinations
    
    def get_all_bike_status(self):
        all_status = self.bike_collection.find({}, {"status": 1, "_id": 0})
        status_list = []
        for bike in all_status:
            status_list.append(bike["status"])
        return status_list
    
def main():
    """Fonction principale pour la classe BikeListEntity."""
    super_velo = BikeBrandListEntity()
    super_velo.get_all_prices_list()

if __name__ == '__main__':
    main()
