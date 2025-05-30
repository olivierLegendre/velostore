import os
import sys
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../db")))
import mongodb_database as db
from bike_brand_list_entity import BikeBrandListEntity

class InternalParametersEntity(db.VelostoreDatabase):
    """Classe pour gérer les paramètres internes dans la base de données."""

    def __init__(self):
        """Initialise InternalParametersEntity."""
        super().__init__()
        self.bike_list_entity = BikeBrandListEntity()

    def get_all_bike_color(self):
        """Appel la fonction get_all_bike_color de bike list entity"""
        return self.bike_list_entity.get_all_bike_color()

    def get_all_bike_size(self):
        """Appel la fonction get_all_bike_size de bike list entity"""
        return self.bike_list_entity.get_all_bike_size()
    
    def get_all_bike_destinations(self):
        """Appel la fonction get_all_bike_destinations de bike list entity"""
        return self.bike_list_entity.get_all_bike_destinations()
        
def main():
    """Fonction principale pour la classe InternalParametersEntity."""
    internal_parameters = InternalParametersEntity()
    size = internal_parameters.get_all_bike_size()
    print(size)

if __name__ == '__main__':
    main()
