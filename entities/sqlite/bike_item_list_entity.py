import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/../db")
import sqlite_database as db

class BikeItemListEntity(db.VelostoreDatabase):
    """Classe pour gérer les listes d'articles de vélos dans la base de données."""    """Classe pour gérer les listes d'articles de vélos dans la base de données."""
    def get_all_bike_item(self, expand: bool = True) -> list:
        """Récupère la liste de tous les articles de vélos.

        Args:
            expand (bool, optionnel): Un indicateur pour déterminer si la liste doit être étendue. Par défaut, True.

        Returns:
            list: Une liste de tous les articles de vélos.
        """
        if expand:
            query = """
                SELECT 
                    bike_item.id,
                    bike_item.brand,
                    bike_size.size,
                    bike_color.color,
                    bike_status.status
                FROM
                    bike_item
                JOIN bike_size ON bike_item.id = bike_size.id
                JOIN bike_color ON bike_item.id = bike_color.id
                JOIN bike_status ON bike_item.id = bike_status.id
                """
        else:
            query = "SELECT * FROM bike"
        self.cursor.execute(query)
        return super().list_change()

def main():
    """Fonction principale pour la classe BikeItemListEntity."""
    pass

if __name__ == '__main__':
    main()