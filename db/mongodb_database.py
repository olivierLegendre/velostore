import pymongo 

class VelostoreDatabase():
    """Classe pour gérer la base de données Velostore."""

    def __init__(self):
        """Initialise la connexion à la base de données."""
        self.connection_db()

    def connection_db(self) -> None:
        """Crée une connexion et un objet curseur pour la base de données.
        """
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.myclient["velostore"]
        
    def list_change(self, entity_list):
        entity_dict = dict()
        ids_list = [row['_id'] for row in entity_list]
        return dict(zip(ids_list, entity_list))

        
def main():
    velostore_db = VelostoreDatabase()
    velostore_db.connection_db()

if __name__ == '__main__':
    main()


