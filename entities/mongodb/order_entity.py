import os
import sys
from bson.objectid import ObjectId

sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../db")))

import mongodb_database as db
from bson import ObjectId
from datetime import datetime

class OrderEntity(db.VelostoreDatabase):
    """Classe pour gérer les opérations de base de données liées aux vélos."""

    def __init__(self):
        """Initialise OrderEntity."""
        super().__init__()
        self.order_collection = self.mydb['Order']

    def create_tables(self):
        """Crée les collections nécessaires dans la base de données."""
        self.get_or_create_collection()

    def get_or_create_collection(self, collection_name="Order"):
        """Récupère ou crée une collection dans la base de données."""
        if collection_name not in self.mydb.list_collection_names():
            self.mydb.create_collection(collection_name)
        return self.mydb[collection_name]

    # Requête CRUD
    def create_order(self, order_data):
        result = self.order_collection.insert_one(order_data)
        return result.inserted_id

    def get_order_by_id(self, order_id):
        return self.order_collection.find_one({"_id": ObjectId(order_id)})

    def update_order(self, order_id, update_data):
        result = self.order_collection.update_one({"_id": ObjectId(order_id)}, {"$set": update_data})
        return result.modified_count

    def delete_order(self, order_id):
        result = self.order_collection.delete_one({"_id": ObjectId(order_id)})
        return result.deleted_count
    
    def create_one_order(order_collection, user_collection, bike_collection, id_user, id_bike, nb_unit, bike_price):
        # récuper les infos dans collection user
        user = user_collection.find_one({"_id": ObjectId(id_user)}, {"Username": 1, "Mail": 1})

        # récuper infos collection bike
        bike = bike_collection.find_one({"_id": ObjectId(id_bike)}, {"brand": 1}, {"config": 1} )
        brand_info = bike.get("brand")
        config_info = bike.get("config")

        bike_entry = {
            "id_bike": ObjectId(id_bike),
            "brand": {
                "brand": brand_info.get("Brand"),
                "Description": brand_info.get("Description"),
                "Price": brand_info.get("Price")
            },
            "config": {
                "Size": config_info.get("Size"),
                "Color": config_info.get("Color")
            },
            "nb_unit": nb_unit,
            "price": bike_price
        }

        total_price = bike_price * nb_unit

        # compiler infos dans order collection
        order = {
            "user": {
                "id_user": ObjectId(id_user),
                "Username": user.get("Username"),
                "Mail": user.get("Mail")
            },
            "bikes": [bike_entry],
            "Date": datetime.now(),
            "Total_price": total_price,
            "Status": "en attente" 
        }

        result = order_collection.insert_one(order)
        return result.inserted_id


    def get_pending_order_by_user(order_collection, id_user):
        list_order = list(order_collection.find({"user.id_user": ObjectId(id_user),"Status":"en attente"}))
        return list_order

    def get_closed_order_by_user(order_collection, id_user):
        list_order = list(order_collection.find({"user.id_user": ObjectId(id_user),"Status":"livré"}))
        return list_order

    def update_order_status(collection, order_id, new_status):
        result = collection.update_one(
            {"_id": ObjectId(order_id)},
            {"$set": {"Status": new_status}}
        )
        return result.modified_count

    def get_orders_by_user_id(collection, user_id):
        return list(collection.find({"user.id_user": ObjectId(user_id)}))


    def read_order_by_id(collection, order_id):
        return collection.find_one({"_id": ObjectId(order_id)})



def main():
    """Fonction principale pour la classe BikeEntity."""
    super_order = OrderEntity()
    print(super_order.get_order_by_id('6839afb0131a0684c0ade292'))

if __name__ == '__main__':
    main()
