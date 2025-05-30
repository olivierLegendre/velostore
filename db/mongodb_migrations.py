import os
import sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "entities/mongodb")

import mongodb_database as db
from bson import ObjectId
from datetime import datetime
import bike_entity as be
import user_entity as ue
import order_entity as oe

class Migration(db.VelostoreDatabase):
    """Classe pour gérer la migration des données dans la base de données Velostore."""

    def __init__(self):
        """Initialise Migration avec les entités nécessaires."""
        super().__init__()
        self.bike_entity = be.BikeEntity()
        self.user_entity = ue.UserEntity()
        self.order_entity = oe.OrderEntity()

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
        self.order_entity.create_tables()

    def create_user_tables(self):
        """Crée les collections d'utilisateurs."""
        self.user_entity.create_tables()

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
        user_data = {
        "user_type": "utilisateur",
        "username": "jules100",
        "status": "actif",
        "mail": "jules@gmail.com",
        "self.bike_entity.create_tables()word": "vl4e5swer5@"
    }
        user_id = self.user_entity.create_user(user_data)
        print(f"User crée id: {user_id}")

    def add_orders(self):
        order_data = {
        "_id": ObjectId(),
        "user": {
            "id_user": ObjectId("665612a5cbe5f12c8a4f1234"),
            "Username": "jules100",
            "Mail": "jules@gmail.com"
        },
        "bikes": [
            {
                "id_bike": ObjectId("665613f1cbe5f12c8a4f1235"),
                "brand": {
                    "brand": "Giant",
                    "Description": "Mountain Bike with suspension",
                    "Price": 500
                },
                "config": {
                    "Size": "M",
                    "Color": "Red"
                },
                "nb_unit": 1,
                "price": 500
            }
        ],
        "Date": datetime(2025, 5, 1),
        "Total_price": 500,
        "Status": "payé"
    }
        order_id = self.order_entity.create_order(order_data)
        print(f"Order crée id: {order_id}")

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
