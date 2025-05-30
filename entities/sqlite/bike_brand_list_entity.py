import os
import sys
from bson.objectid import ObjectId

# Ajoutez le chemin vers le répertoire contenant le module mongodb_database
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/../db")

import mongodb_database as db

class BikeListEntity(db.VelostoreDatabase):
    """Classe pour gérer les opérations de base de données liées aux vélos."""

    def __init__(self):
        """Initialise BikeListEntity."""
        super().__init__()
        self.bike_collection = self.mydb['Bike']

    def get_all_bike_list(self, bike_id):
        """Récupère un vélo par son identifiant."""
        bike_by_id = self.bike_collection.find_one({"_id": ObjectId(bike_id)})
        print(bike_by_id)
        return bike_by_id

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
    super_velo.get_all_brand_list()

if __name__ == '__main__':
    main()
