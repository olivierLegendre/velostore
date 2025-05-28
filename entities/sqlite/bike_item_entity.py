import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/../db")
import sqlite_database as db

class BikeItemEntity(db.VelostoreDatabase):
    """Classe pour gérer les opérations de base de données liées aux articles de vélos."""
    def __init__(self):
        """Initialise BikeItemEntity."""
        super().__init__()
        
    def create_tables(self):
        """Crée les tables nécessaires dans la base de données."""
        self.create_bike_table()
  
    def create_bike_table(self):
        """Crée la table des vélos."""
        self.cursor.execute("""
                        CREATE TABLE IF NOT EXISTS bike (
                            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            brand INTEGER NOT NULL,
                            size INTEGER NOT NULL,
                            color INTEGER NOT NULL,
                            status INTEGER NOT NULL,
                            FOREIGN KEY(brand) REFERENCES bike_brand(id),
                            FOREIGN KEY(status) REFERENCES bike_status(id),
                            FOREIGN KEY(size) REFERENCES bike_size(id),
                            FOREIGN KEY(color) REFERENCES bike_color(id)
                        )
                        """)

    def get_bike_by_id(self, bike_id: int, expand: bool = False) -> dict:
        """Récupère un vélo par son identifiant.

        Args:
            bike_id (int): L'identifiant du vélo.
            expand (bool, optionnel): Un indicateur pour déterminer si les détails doivent être étendus. Par défaut, False.

        Returns:
            dict: Les informations du vélo correspondant.
        """
        if expand:
            self.cursor.execute(
                """
                SELECT
                    bike.id,
                    bike_brand.brand as brand,
                    bike_size.size as size,
                    bike_color.color as color,
                    bike_status.status as status
                FROM bike
                JOIN bike_size ON bike.size = bike_size.id
                JOIN bike_color ON bike.color = bike_color.id
                JOIN bike_brand ON bike.brand = bike_brand.id
                JOIN bike_status ON bike.status = bike_status.id
                WHERE bike.id = ?
            """,
                (bike_id,),
            )
            return super().change_list_to_dict(self.cursor.fetchone())
        else:
            self.cursor.execute(
                """
                SELECT 
                    * 
                FROM bike 
                WHERE bike.id = ?
            """,
                (bike_id,),
            )
            return super().change_list_to_dict(self.cursor.fetchone())

    def get_bike_by_parameters(self, parameters: dict) -> dict:
        """Récupère un vélo en fonction de paramètres donnés.

        Args:
            parameters (dict): Un dictionnaire de paramètres pour filtrer les vélos.

        Returns:
            dict: Les informations du vélo correspondant aux paramètres.

        Raises:
            ValueError: Si les paramètres sont invalides.
        """
        query = "SELECT * FROM bike WHERE "
        conditions = []
        values = []

        for key, value in parameters.items():
            if key in ['id', 'brand', 'size', 'color', 'status']:
                conditions.append(f"{key} = ?")
                values.append(value)

        if not conditions:
            raise ValueError("Paramètres invalides")
        # pour joindre les 2 param (clé valeur) à vérifier
        query += " AND ".join(conditions)

        self.cursor.execute(query, tuple(values))
        return self.cursor.fetchone()

    def delete_bike_status_table(self):
        """Supprime la table des statuts de vélo."""
        self.cursor.execute("""
                        DROP TABLE IF EXISTS bike_status
                        """)
        
    def add_bike_item(self, brand_id: int, size_id: int, color_id: int, status_id: int) -> int:
        """Ajoute un nouvel article de vélo.

        Args:
            brand_id (int): L'identifiant de la marque.
            size_id (int): L'identifiant de la taille.
            color_id (int): L'identifiant de la couleur.
            status_id (int): L'identifiant du statut.

        Returns:
            int: L'identifiant du nouvel article de vélo ajouté.
        """
        self.cursor.execute("""
            INSERT INTO bike (brand, size, color, status)
            VALUES (?, ?, ?, ?)
        """, (brand_id, size_id, color_id, status_id))
        self.connection.commit()
        return self.cursor.lastrowid 
    

def main():
    """Fonction principale pour la classe BikeItemEntity."""
    super_velo = BikeItemEntity()
    super_velo.create_tables()
    

if __name__ == '__main__':
    main()