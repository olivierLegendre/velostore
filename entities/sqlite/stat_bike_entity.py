import os
import sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/db")
import database as db

class StatBikeEntity(db.VelostoreDatabase):
    """Classe pour gérer les statistiques de vélos dans la base de données."""

    def __init__(self):
        """Initialise StatBikeEntity."""
        super().__init__()

    def create_tables(self):
        """Crée les tables nécessaires dans la base de données."""
        self.create_statistics_bike()

    def create_statistics_bike(self):
        """Crée la table des statistiques de vélos."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS statistics_bike (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                id_bike INTEGER NOT NULL,
                statistics_name INTEGER NOT NULL,
                statistics_counter INTEGER NOT NULL,
                FOREIGN KEY(statistics_name) REFERENCES statistics_name(id),
                FOREIGN KEY(id_bike) REFERENCES bike_brand(id)
            )
        """)

    def delete_statistics_bike(self):
        """Supprime la table des statistiques de vélos."""
        self.cursor.execute("""
            DROP TABLE IF EXISTS statistics_bike
        """)

    def delete_statistics_name(self):
        """Supprime la table des noms de statistiques."""
        self.cursor.execute("""
            DROP TABLE IF EXISTS statistics_name
        """)

    def get_statistics_by_id(self, statistics_id: int, expand: bool = True) -> dict:
        """Récupère une statistique de vélo par son identifiant.

        Args:
            statistics_id (int): L'identifiant de la statistique.
            expand (bool, optionnel): Un indicateur pour déterminer si les détails doivent être étendus. Par défaut, True.

        Returns:
            dict: Les informations de la statistique correspondante.
        """
        if expand:
            query = """
                SELECT
                    statistics_bike.id,
                    bike_brand.brand as brand,
                    statistics_name.name as name_stat,
                    statistics_bike.statistics_counter
                FROM statistics_bike
                JOIN bike_brand ON statistics_bike.id_bike = bike_brand.id
                JOIN statistics_name ON statistics_bike.statistics_name = statistics_name.id
                WHERE statistics_bike.id = ?
            """
        else:
            query = """
                SELECT
                    *
                FROM statistics_bike
                WHERE statistics_bike.id = ?
            """

        self.cursor.execute(query, (statistics_id,))
        return super().change_list_to_dict(self.cursor.fetchone())

def main():
    """Fonction principale pour la classe StatBikeEntity."""
    stats = StatBikeEntity()
    stats.create_tables()

if __name__ == '__main__':
    main()
