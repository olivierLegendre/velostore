import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/db")
import database as db

class BikeBrandListEntity(db.VelostoreDatabase):
    """Classe pour gérer les listes de marques de vélos dans la base de données."""
    def get_all_bike_brand_list(self, expand: bool = True) -> list:
        """Récupère la liste de toutes les marques de vélos.

        Args:
            expand (bool, optionnel): Un indicateur pour déterminer si la liste doit être étendue. Par défaut, True.

        Returns:
            list: Une liste de toutes les marques de vélos.
        """
        if expand:
            query = """
                SELECT
                    bike_brand.id,
                    bike_brand.brand,
                    bike_brand.description,
                    bike_brand.price,
                    bike_destination.destination,
                    bike_brand.img
                FROM
                    bike_brand
                JOIN bike_destination ON bike_brand.id = bike_destination.id
            """
        else:
            query = "SELECT * FROM bike_brand"
        self.cursor.execute(query)
        return super().list_change()
    

    def get_all_prices_list(self) -> list:
        """Récupère la liste de tous les prix des marques de vélos.

        Returns:
            list: Une liste des prix des marques de vélos.
        """
        self.cursor.execute("""SELECT id, price FROM bike_brand""")
        return super().list_change()
    
    def get_all_destinations_list(self) -> list:
        """Récupère la liste de toutes les destinations de vélos.

        Returns:
            list: Une liste des destinations de vélos.
        """
        self.cursor.execute("""SELECT * FROM bike_destination""")
        return super().list_change()

def main():
    """Fonction principale pour la classe BikeBrandListEntity."""
    bike_brand_list = BikeBrandListEntity()
    test1 = bike_brand_list.get_all_bike_brand_list()
    #print(test1)


if __name__ == "__main__":
    main()
