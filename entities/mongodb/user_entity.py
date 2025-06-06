import os
import sys
from bson.objectid import ObjectId

sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../db")))

import mongodb_database as db

class UserEntity(db.VelostoreDatabase):
    """Classe pour gérer les opérations de base de données liées aux user."""

    def __init__(self):
        """Initialise UserEntity."""
        super().__init__()
        self.user_collection = self.mydb['User']

    def create_tables(self):
        """Crée les collections nécessaires dans la base de données."""
        self.get_or_create_collection()

    def get_or_create_collection(self, collection_name="User"):
        
        schema = {
            "bsonType": "object",
            "required": ["username", "password"],
            "properties": {
                "user_type": {"bsonType": "string"},
                "username": {"bsonType": "string"},
                "status": {"bsonType": "string"},
                "mail": {"bsonType": "string"},
                "password": {"bsonType": "string"},
            }
        }

        validator = {"$jsonSchema": schema}

        """Récupère ou crée une collection dans la base de données."""
        if collection_name not in self.mydb.list_collection_names():
            self.mydb.create_collection(collection_name, validator=validator)
            print("Collection 'user' créée avec validation JSON Schema.")
        return self.mydb[collection_name]

    # Requête CRUD
    def add_data_user(self, user_data):
        result_many = self.user_collection.insert_many(user_data)
        return result_many.inserted_ids
    
    def create_user(self, user_data):
        result = self.user_collection.insert_one(user_data)
        return result.inserted_id

    def get_user_by_id(self, user_id):
        return self.user_collection.find_one({"_id": ObjectId(user_id)})

    def update_user(self, user_id, update_data):
        result = self.user_collection.update_one({"_id": ObjectId(user_id)}, {"$set": update_data})
        return result.modified_count

    def delete_user(self, user_id):
        result = self.user_collection.delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count


def main():
    """Fonction principale pour la classe UserEntity."""
    super_user = UserEntity()
    print(super_user.get_user_by_id('6839adabf458c2b2f4c45602'))

if __name__ == '__main__':
    main()
