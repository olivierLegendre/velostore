import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/db")
import database as db

class BikeBrandEntity(db.VelostoreDatabase):
    """Classe pour gérer les opérations de base de données liées aux marques de vélos."""
    def __init__(self):
        """Initialise BikeBrandEntity."""
        super().__init__()
        
    def create_tables(self):
        """Crée les tables nécessaires dans la base de données."""
        self.create_bike_brand_table()
        
    def create_bike_brand_table(self):
        """Crée la table des marques de vélos."""
        self.cursor.execute("""
                        CREATE TABLE IF NOT EXISTS bike_brand (
                            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            brand STRING NOT NULL UNIQUE,
                            description STRING NOT NULL,
                            price INTEGER NOT NULL,
                            destination STRING NOT NULL,
                            img STRING,
                            FOREIGN KEY(destination) REFERENCES bike_destination(id)
                        )
                        """)

    
    # GET BRAND BY ID
    def get_brand_by_id(self, brand_id: int, expand: bool = True) -> dict:
        """Récupère une marque de vélo par son identifiant.

        Args:
            brand_id (int): L'identifiant de la marque de vélo.
            expand (bool, optionnel): Un indicateur pour déterminer si les détails doivent être étendus. Par défaut, True.

        Returns:
            dict: Les informations de la marque de vélo correspondante.
        """
        if expand:
            query = """
                SELECT
                    bike_brand.id,
                    bike_brand.brand,
                    bike_brand.description,
                    bike_brand.price,
                    bike_destination.destination as destination,
                    bike_brand.img
                FROM bike_brand
                JOIN bike_destination ON bike_brand.destination = bike_destination.id
                WHERE bike_brand.id = ?
            """
        else:
            query = """
                SELECT 
                    * 
                FROM bike_brand
                WHERE bike_brand.id = ?
            """

        self.cursor.execute(query, (brand_id,))
        return super().change_list_to_dict(self.cursor.fetchone())
    

    # ADD BRAND (FOR ADMIN)
    def add_brand(self, brand: int, description: int, price: int, destination_id: int, img: str = None) -> int:
        """Ajoute une nouvelle marque de vélo.

        Args:
            brand (str): Le nom de la marque.
            description (str): La description de la marque.
            price (int): Le prix de la marque.
            destination_id (int): L'identifiant de la destination.
            img (str, optionnel): L'URL de l'image de la marque. Par défaut, None.

        Returns:
            int: L'identifiant de la nouvelle marque ajoutée.
        """
        self.cursor.execute("""
            INSERT INTO bike_brand (brand, description, price, destination, img)
            VALUES (?, ?, ?, ?, ?)
        """, (brand, description, price, destination_id, img))
        self.connection.commit()
        return self.cursor.lastrowid
    
    
    # DELETE BRAND (FOR ADMIN)
    def delete_brand(self, brand_id: int):
        """Supprime une marque de vélo.

        Args:
            brand_id (int): L'identifiant de la marque de vélo à supprimer.
        """
        self.cursor.execute("DELETE FROM bike_brand WHERE id = ?", (brand_id,))
        self.connection.commit()

    

def main():
    """Fonction principale pour la classe BikeBrandEntity."""
    super_velo = BikeBrandEntity()
    super_velo.create_tables()
    

if __name__ == '__main__':
    main()