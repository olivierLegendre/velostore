import os
import sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/entities/mongodb")

import mongodb_database as db
from bson import ObjectId
from datetime import datetime
import bike_brand_entity as be
import user_entity as ue
import order_entity as oe

class Migration(db.VelostoreDatabase):
    """Classe pour gérer la migration des données dans la base de données Velostore."""

    def __init__(self):
        """Initialise Migration avec les entités nécessaires."""
        super().__init__()
        self.bike_brand_entity = be.BikeBrandEntity()
        self.user_entity = ue.UserEntity()
        self.order_entity = oe.OrderEntity()

    def setup(self):
        """Configure les collections et ajoute des données statiques."""
        self.create_bike_tables()
        self.create_order_tables()
        self.create_user_tables()

    def create_bike_tables(self):
        """Crée la collection de vélos."""
        self.bike_brand_entity.create_tables()

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
        bike_id = self.bike_brand_entity.create_bike(bike_data)
        print(f"Vélo crée id: {bike_id}")

    def add_user(self):
        user_data = [
            {
                "user_type": "utilisateur",
                "username": "jules100",
                "status": "actif",
                "mail": "jules@gmail.com",
                "password": "vl4e5swer5@"
            },
            {
                "user_type": "utilisateur",
                "username": "emma200",
                "status": "actif",
                "mail": "emma200@gmail.com",
                "password": "P@ssword2024"
            },
            {
                "user_type": "utilisateur",
                "username": "lucas_dev",
                "status": "inactif",
                "mail": "lucas.dev@mail.com",
                "password": "devL1234@"
            },
            {
                "user_type": "utilisateur",
                "username": "sophie_x",
                "status": "actif",
                "mail": "sophie.x@example.com",
                "password": "s0Ph!e456"
            },
            {
                "user_type": "utilisateur",
                "username": "maxime99",
                "status": "suspendu",
                "mail": "maxime99@hotmail.com",
                "password": "MaX_789$"
            },
            {
                "user_type": "utilisateur",
                "username": "lea_moon",
                "status": "actif",
                "mail": "lea.moon@outlook.fr",
                "password": "leaMoon#1"
            },
            {
                "user_type": "utilisateur",
                "username": "tommy_t",
                "status": "actif",
                "mail": "tommy_t@gmail.com",
                "password": "TomT123@"
            },
            {
                "user_type": "utilisateur",
                "username": "noemie_45",
                "status": "inactif",
                "mail": "noemie45@yahoo.fr",
                "password": "NoeMIE_98%"
            },
            {
                "user_type": "utilisateur",
                "username": "adrien.k",
                "status": "actif",
                "mail": "adrien.k@protonmail.com",
                "password": "adr1enK#56"
            },
            {
                "user_type": "utilisateur",
                "username": "claire.z",
                "status": "actif",
                "mail": "claire.z@gmail.com",
                "password": "cl@ireZ2025"
            }
        ]   
        self.user_entity.add_data_user(user_data)

    def add_orders(self):
        order_data = [
            {
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
            },
            {
                "_id": ObjectId(),
                "user": {
                    "id_user": ObjectId("665612a5cbe5f12c8a4f1236"),
                    "Username": "emma200",
                    "Mail": "emma200@gmail.com"
                },
                "bikes": [
                    {
                        "id_bike": ObjectId("665613f1cbe5f12c8a4f1237"),
                        "brand": {
                            "brand": "Trek",
                            "Description": "Road bike for long-distance riding",
                            "Price": 700
                        },
                        "config": {
                            "Size": "L",
                            "Color": "Blue"
                        },
                        "nb_unit": 2,
                        "price": 1400
                    }
                ],
                "Date": datetime(2025, 5, 3),
                "Total_price": 1400,
                "Status": "livré"
            },
            {
                "_id": ObjectId(),
                "user": {
                    "id_user": ObjectId("665612a5cbe5f12c8a4f1238"),
                    "Username": "lucas_dev",
                    "Mail": "lucas.dev@mail.com"
                },
                "bikes": [
                    {
                        "id_bike": ObjectId("665613f1cbe5f12c8a4f1239"),
                        "brand": {
                            "brand": "Decathlon",
                            "Description": "Urban bike for daily commutes",
                            "Price": 350
                        },
                        "config": {
                            "Size": "S",
                            "Color": "Black"
                        },
                        "nb_unit": 1,
                        "price": 350
                    },
                    {
                        "id_bike": ObjectId("665613f1cbe5f12c8a4f1240"),
                        "brand": {
                            "brand": "Orbea",
                            "Description": "Electric bike with long battery life",
                            "Price": 1200
                        },
                        "config": {
                            "Size": "M",
                            "Color": "White"
                        },
                        "nb_unit": 1,
                        "price": 1200
                    }
                ],
                "Date": datetime(2025, 5, 5),
                "Total_price": 1550,
                "Status": "livré"
            },
            {
                "_id": ObjectId(),
                "user": {
                    "id_user": ObjectId("665612a5cbe5f12c8a4f1239"),
                    "Username": "sophie_x",
                    "Mail": "sophie.x@example.com"
                },
                "bikes": [
                    {
                        "id_bike": ObjectId("665613f1cbe5f12c8a4f1241"),
                        "brand": {
                            "brand": "BMC",
                            "Description": "Hybrid bike for trails and roads",
                            "Price": 600
                        },
                        "config": {
                            "Size": "M",
                            "Color": "Green"
                        },
                        "nb_unit": 1,
                        "price": 600
                    }
                ],
                "Date": datetime(2025, 5, 6),
                "Total_price": 600,
                "Status": "payé"
            },
            {
                "_id": ObjectId(),
                "user": {
                    "id_user": ObjectId("665612a5cbe5f12c8a4f1242"),
                    "Username": "maxime99",
                    "Mail": "maxime99@hotmail.com"
                },
                "bikes": [
                    {
                        "id_bike": ObjectId("665613f1cbe5f12c8a4f1243"),
                        "brand": {
                            "brand": "Scott",
                            "Description": "Sport BMX bike",
                            "Price": 450
                        },
                        "config": {
                            "Size": "S",
                            "Color": "Yellow"
                        },
                        "nb_unit": 2,
                        "price": 900
                    }
                ],
                "Date": datetime(2025, 5, 7),
                "Total_price": 900,
                "Status": "en attente"
            }
        ]
        self.order_entity.add_data_order(order_data)

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
