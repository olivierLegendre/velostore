import os
import sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/db")
import database as db

class InternalParametersEntity(db.VelostoreDatabase):
    """Classe pour gérer les paramètres internes dans la base de données."""

    def __init__(self):
        """Initialise InternalParametersEntity."""
        super().__init__()

    def create_tables(self):
        """Crée toutes les tables nécessaires dans la base de données."""
        self.create_bike_status_table()
        self.create_bike_size_table()
        self.create_bike_destination_table()
        self.create_bike_color_table()
        self.create_order_status_table()
        self.create_user_type_table()
        self.create_user_status_table()
        self.create_statistics_name()

    def create_bike_status_table(self):
        """Crée la table des statuts de vélo."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS bike_status (
                id INTEGER PRIMARY KEY NOT NULL,
                status STRING NOT NULL UNIQUE
            )
        """)

    def create_bike_size_table(self):
        """Crée la table des tailles de vélo."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS bike_size (
                id INTEGER PRIMARY KEY NOT NULL,
                size STRING NOT NULL UNIQUE
            )
        """)

    def create_bike_destination_table(self):
        """Crée la table des destinations de vélo."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS bike_destination (
                id INTEGER PRIMARY KEY NOT NULL,
                destination STRING NOT NULL UNIQUE
            )
        """)

    def create_bike_color_table(self):
        """Crée la table des couleurs de vélo."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS bike_color (
                id INTEGER PRIMARY KEY NOT NULL,
                color STRING NOT NULL UNIQUE
            )
        """)

    def create_order_status_table(self):
        """Crée la table des statuts de commande."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS order_status (
                id INTEGER PRIMARY KEY NOT NULL UNIQUE,
                status STRING NOT NULL UNIQUE
            )
        """)

    def create_user_type_table(self):
        """Crée la table des types d'utilisateur."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_type (
                id INTEGER PRIMARY KEY NOT NULL,
                type INTEGER NOT NULL UNIQUE
            )
        """)

    def create_user_status_table(self):
        """Crée la table des statuts d'utilisateur."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_status (
                id INTEGER PRIMARY KEY NOT NULL,
                status STRING NOT NULL UNIQUE
            )
        """)

    def create_statistics_name(self):
        """Crée la table des noms de statistiques."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS statistics_name (
                id INTEGER PRIMARY KEY NOT NULL,
                name STRING NOT NULL UNIQUE
            )
        """)

    def get_bike_status_by_id(self, bike_status_id: int) -> dict:
        """Récupère un statut de vélo par son identifiant.

        Args:
            bike_status_id (int): L'identifiant du statut de vélo.

        Returns:
            dict: Les informations du statut de vélo correspondant.
        """
        self.cursor.execute("""
            SELECT * FROM bike_status WHERE ID = ?
        """, (bike_status_id,))
        return self.cursor.fetchone()

    def get_bike_size_by_id(self, size_id: int) -> dict:
        """Récupère une taille de vélo par son identifiant.

        Args:
            size_id (int): L'identifiant de la taille de vélo.

        Returns:
            dict: Les informations de la taille de vélo correspondante.
        """
        self.cursor.execute("""
            SELECT * FROM bike_size WHERE ID = ?
        """, (size_id,))
        return self.cursor.fetchone()

    def get_bike_destination_by_id(self, destination_id: int) -> dict:
        """Récupère une destination de vélo par son identifiant.

        Args:
            destination_id (int): L'identifiant de la destination de vélo.

        Returns:
            dict: Les informations de la destination de vélo correspondante.
        """
        self.cursor.execute("""
            SELECT * FROM bike_destination WHERE ID = ?
        """, (destination_id,))
        return self.cursor.fetchone()

    def get_bike_color_by_id(self, color_id: int) -> dict:
        """Récupère une couleur de vélo par son identifiant.

        Args:
            color_id (int): L'identifiant de la couleur de vélo.

        Returns:
            dict: Les informations de la couleur de vélo correspondante.
        """
        self.cursor.execute("""
            SELECT * FROM bike_color WHERE ID = ?
        """, (color_id,))
        return self.cursor.fetchone()

    def get_order_status_by_id(self, order_status_id: int) -> dict:
        """Récupère un statut de commande par son identifiant.

        Args:
            order_status_id (int): L'identifiant du statut de commande.

        Returns:
            dict: Les informations du statut de commande correspondant.
        """
        self.cursor.execute("""
            SELECT * FROM order_status WHERE ID = ?
        """, (order_status_id,))
        return self.cursor.fetchone()

    def get_user_type_by_id(self, user_type_id: int) -> dict:
        """Récupère un type d'utilisateur par son identifiant.

        Args:
            user_type_id (int): L'identifiant du type d'utilisateur.

        Returns:
            dict: Les informations du type d'utilisateur correspondant.
        """
        self.cursor.execute("""
            SELECT * FROM user_type WHERE ID = ?
        """, (user_type_id,))
        return self.cursor.fetchone()

    def get_user_status_by_id(self, user_status_id: int) -> dict:
        """Récupère un statut d'utilisateur par son identifiant.

        Args:
            user_status_id (int): L'identifiant du statut d'utilisateur.

        Returns:
            dict: Les informations du statut d'utilisateur correspondant.
        """
        self.cursor.execute("""
            SELECT * FROM user_status WHERE ID = ?
        """, (user_status_id,))
        return self.cursor.fetchone()

    def get_statistics_name_by_id(self, statistics_name_id: int) -> dict:
        """Récupère un nom de statistique par son identifiant.

        Args:
            statistics_name_id (int): L'identifiant du nom de statistique.

        Returns:
            dict: Les informations du nom de statistique correspondant.
        """
        self.cursor.execute("""
            SELECT * FROM statistics_name WHERE ID = ?
        """, (statistics_name_id,))
        return self.cursor.fetchone()

def main():
    """Fonction principale pour la classe InternalParametersEntity."""
    internal_parameters = InternalParametersEntity()
    internal_parameters.create_tables()

if __name__ == '__main__':
    main()
