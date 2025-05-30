import os
import sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "../../entities/mongodb")

import mongodb_database as db
import bike_entity as be

class Migration(db.VelostoreDatabase):
    """Classe pour gérer la migration des données dans la base de données Velostore."""

    def __init__(self):
        """Initialise Migration avec les entités nécessaires."""
        super().__init__()
        self.bike_entity = be.BikeEntity()

    def setup(self):
        """Configure les collections et ajoute des données statiques."""
        self.create_bike_tables()
        self.create_order_tables()
        self.create_user_tables()

    def create_bike_tables(self):
        """Crée la collection de vélos."""
        self.bike_entity.create_tables()

    def create_order_tables(self):
        """Crée les collections de commandes."""
        pass

    def create_user_tables(self):
        """Crée les collections d'utilisateurs."""
        pass

    def add_dynamics_data(self):
        """Ajoute des données dynamiques aux collections."""
        self.add_bike()
        self.add_user()
        self.add_orders()
        self.add_bike_brand()
        self.add_order_item()
        self.add_item_list()

    def add_bike(self):
        bike_data = {"brand":{
            "brand": "Trek",
            "model": "Marlin 5",
            "year": 2022,
            "price": 599.99,
            "image": "image.url",
            "destination": "VTT"
        }, "config":{
            "size": "M",
            "color": "bleu"
        }}
        bike_id = self.bike_entity.create_bike(bike_data)
        print(f"Vélo crée id: {bike_id}")

    def add_user(self):
        pass

    def add_orders(self):
        pass

    def add_item_list(self):
        pass

    def add_order_item(self):
        pass

    def add_bike_brand(self):
        pass

def main():
    """Fonction principale pour la classe Migration."""
    initial_setup = Migration()
    initial_setup.setup()
    initial_setup.add_dynamics_data()

if __name__ == "__main__":
    main()
