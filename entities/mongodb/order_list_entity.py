import os
import sys
from bson.objectid import ObjectId

sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../db")))

import mongodb_database as db
from bson import ObjectId
from datetime import datetime

class OrderListEntity(db.VelostoreDatabase):
    """Classe pour gérer les opérations de base de données liées aux listes order."""

    def __init__(self):
        """Initialise OrderEntity."""
        super().__init__()
        self.order_collection = self.mydb['Order']

    def get_pending_order_by_user(self, id_user):
        list_order = list(self.order_collection.find({"user.id_user": ObjectId(id_user),"status":"en attente"}))
        return list_order

    def get_closed_order_by_user(self, id_user):
        list_order = list(self.order_collection.find({"user.id_user": ObjectId(id_user),"status":"livré"}))
        return list_order

    def get_orders_by_user_id(self, user_id):
        return list(self.order_collection.find({"user.id_user": ObjectId(user_id)}))



def main():
    """Fonction principale pour la classe OrderListEntity."""
    order_list = OrderListEntity()
    print(order_list.get_pending_order_by_user("665612a5cbe5f12c8a4f1242"))
    

if __name__ == '__main__':
    main()
