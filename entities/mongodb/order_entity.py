import os
import sys
from bson.objectid import ObjectId

sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../db")))

import mongodb_database as db
from bson import ObjectId
from datetime import datetime

class OrderEntity(db.VelostoreDatabase):
    """Classe pour gérer les opérations de base de données liées aux orders."""

    def __init__(self):
        """Initialise OrderEntity."""
        super().__init__()
        self.order_collection = self.mydb['Order']
        self.user_collection = self.mydb['User']
        self.bike_collection = self.mydb['Bike']

    def create_tables(self):
        """Crée les collections nécessaires dans la base de données."""
        self.get_or_create_collection()

    
    def get_or_create_collection(self, collection_name="Order"):

        schema = {
            "bsonType": "object",
            "required": ["user", "bikes", "date", "total_price", "status"],
            "properties": {
                "user": {
                    "bsonType": "object",
                    "required": ["id_user", "username", "mail"],
                    "properties": {
                        "id_user": {"bsonType": "objectId"},
                        "username": {"bsonType": "string"},
                        "mail": {"bsonType": "string"}
                    }
                },
                "bikes": {
                    "bsonType": "array",
                    "items": {
                        "bsonType": "object",
                        "required": ["id_bike", "brand", "config", "nb_unit", "price"],
                        "properties": {
                            "id_bike": {"bsonType": "objectId"},
                            "brand": {
                                "bsonType": "object",
                                "required": ["brand", "price"],
                                "properties": {
                                    "brand": {"bsonType": "string"},
                                    "price": {"bsonType": "double"}
                                }
                            },
                            "config": {
                                "bsonType": "object",
                                "required": ["size", "color"],
                                "properties": {
                                    "size": {"bsonType": "string"},
                                    "color": {"bsonType": "string"}
                                }
                            },
                            "nb_unit": {"bsonType": "int"},
                            "price": {"bsonType": "double"}
                        }
                    }
                },
                "date": {"bsonType": "date"},
                "total_price": {"bsonType": "double"},
                "status": {"bsonType": "string"}
            }
        }

        validator = {"$jsonSchema": schema}

        """Récupère ou crée une collection dans la base de données."""
        if collection_name not in self.mydb.list_collection_names():
            self.mydb.create_collection(collection_name, validator=validator)
            print("Collection 'order' créée avec validation JSON Schema.")
        return self.mydb[collection_name]

    # Requête CRUD
    def add_data_order(self, order_data):
        result_many = self.order_collection.insert_many(order_data)
        return result_many.inserted_ids    

    def create_order(self, order_data):
        result = self.order_collection.insert_one(order_data)
        return result.inserted_id
        
    def create_one_order(self, id_user: str, bike_list: list) -> ObjectId :
        """
        Crée une commande contenant un ou plusieurs vélos pour un utilisateur donné.

        Paramètres :
        - id_user : str — ID de l'utilisateur sous forme de chaîne.
        - bike_list : liste de dictionnaires — Chaque dictionnaire doit contenir :
            - 'id_bike' : str — ID du vélo
            - 'nb_unit' : int — Nombre d'unités commandées

        Retour :
        - ID de la commande insérée dans la collection 'orders'
        """
        # récuper les infos dans collection user
        user = self.user_collection.find_one({"_id": ObjectId(id_user)}, {"username": 1, "mail": 1})

        total_price = 0
        bikes_list = []

        for item in bike_list:
            id_bike = item["id_bike"]
            nb_unit = item["nb_unit"]
            
            # récuper infos collection bike
            bike = self.bike_collection.find_one({"_id": ObjectId(id_bike)}, {"brand": 1, "config": 1} )
            brand_info = bike.get("brand")
            config_info = bike.get("config")
            bike_price = brand_info.get("price")
            bike_price_total = bike_price * nb_unit
    
            bike_entry = {
                "id_bike": ObjectId(id_bike),
                "brand": {
                    "brand": brand_info.get("brand"),
                    "price": bike_price
                },
                "config": {
                    "size": config_info.get("size"),
                    "color": config_info.get("color")
                },
                "nb_unit": nb_unit,
                "price" : bike_price_total
            }
    
            total_price += bike_price_total
            bikes_list.append(bike_entry)

        # compiler infos dans order collection
        order = {
            "user": {
                "id_user": ObjectId(id_user),
                "username": user.get("username"),
                "mail": user.get("mail")
            },
            "bikes": bikes_list,
            "date": datetime.now(),
            "total_price": total_price,
            "status": "en attente" 
        }

        result = self.order_collection.insert_one(order)
        return result.inserted_id
 
    def get_order_item_by_id_order(self, order_id):
        return self.order_collection.find_one({"_id": ObjectId(order_id)}, {"bikes": 1})
    
    def get_order_by_id(self, order_id):
        return self.order_collection.find_one({"_id": ObjectId(order_id)})

    def update_order(self, order_id, update_data):
        result = self.order_collection.update_one({"_id": ObjectId(order_id)}, {"$set": update_data})
        return result.modified_count
    
    def update_order_status(self, order_id, new_status):
        if new_status == 2:
            result = self.order_collection.update_one(
            {"_id": ObjectId(order_id)},
            {"$set": {"Status": "payé"}}
        )
        else :
            result = self.order_collection.update_one(
                {"_id": ObjectId(order_id)},
                {"$set": {"Status": new_status}}
            )
        return result.modified_count

    def pay_order(self, order_id):
        result = self.order_collection.update_one(
            {"_id": ObjectId(order_id)},
            {"$set": {"Status": "payé"}}
        )
        return result.modified_count
    
    def delete_order(self, order_id):
        result = self.order_collection.delete_one({"_id": ObjectId(order_id)})
        return result.deleted_count
    


def main():
    """Fonction principale pour la classe OrderEntity."""
    order = OrderEntity()
    print(order.get_order_item_by_id_order('683b1cdb9f09c38f306a56aa'))
    dict_bike = [{"id_bike" : "683d5ae1da74fc36dd28214b","nb_unit" : 2}]
    order.create_one_order("683d5ae1da74fc36dd28214e", dict_bike)
    

if __name__ == '__main__':
    main()
