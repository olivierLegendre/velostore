import os
import sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/db")
import database as db

class InternalParametersListEntity(db.VelostoreDatabase):
    """Classe pour gérer les listes de paramètres internes dans la base de données."""

    def get_all_bike_status(self) -> list:
        """Récupère la liste de tous les statuts de vélo.

        Returns:
            list: Une liste de tous les statuts de vélo.
        """
        self.cursor.execute("""
            SELECT * FROM bike_status
        """)
        return self.cursor.fetchall()

    def get_all_bike_size(self) -> list:
        """Récupère la liste de toutes les tailles de vélo.

        Returns:
            list: Une liste de toutes les tailles de vélo.
        """
        self.cursor.execute("""
            SELECT * FROM bike_size
        """)
        return self.cursor.fetchall()

    def get_all_bike_destination(self) -> list:
        """Récupère la liste de toutes les destinations de vélo.

        Returns:
            list: Une liste de toutes les destinations de vélo.
        """
        self.cursor.execute("""
            SELECT * FROM bike_destination
        """)
        return self.cursor.fetchall()

    def get_all_bike_color(self) -> list:
        """Récupère la liste de toutes les couleurs de vélo.

        Returns:
            list: Une liste de toutes les couleurs de vélo.
        """
        self.cursor.execute("""
            SELECT * FROM bike_color
        """)
        return self.cursor.fetchall()

    def get_all_order_status(self) -> list:
        """Récupère la liste de tous les statuts de commande.

        Returns:
            list: Une liste de tous les statuts de commande.
        """
        self.cursor.execute("""
            SELECT * FROM order_status
        """)
        return self.cursor.fetchall()

    def get_all_user_type(self) -> list:
        """Récupère la liste de tous les types d'utilisateur.

        Returns:
            list: Une liste de tous les types d'utilisateur.
        """
        self.cursor.execute("""
            SELECT * FROM user_type
        """)
        return self.cursor.fetchall()

    def get_all_user_status(self) -> list:
        """Récupère la liste de tous les statuts d'utilisateur.

        Returns:
            list: Une liste de tous les statuts d'utilisateur.
        """
        self.cursor.execute("""
            SELECT * FROM user_status
        """)
        return self.cursor.fetchall()

    def get_all_statistics_name(self) -> list:
        """Récupère la liste de tous les noms de statistiques.

        Returns:
            list: Une liste de tous les noms de statistiques.
        """
        self.cursor.execute("""
            SELECT * FROM statistics_name
        """)
        return self.cursor.fetchall()

def main():
    """Fonction principale pour la classe InternalParametersListEntity."""
    pass

if __name__ == '__main__':
    main()
