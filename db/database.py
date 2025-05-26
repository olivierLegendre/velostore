import sqlite3

class VelostoreDatabase():
    """Classe pour gérer la base de données Velostore."""

    def __init__(self):
        """Initialise la connexion à la base de données."""
        self.connection_db()

    def connection_db(self) -> None:
        """Crée une connexion et un objet curseur pour la base de données.
        """
        with sqlite3.connect("db/velostore.db", check_same_thread=False) as connection:
            self.connection = connection
            self.cursor = connection.cursor()

    def create_tables(self) -> None:
        """Crée toutes les tables si elles n'existent pas.

        Vous pouvez réinitialiser toute la base de données en supprimant le fichier velostore.db.
        """
        # Crée le fichier velostore.db s'il n'existe pas
        file_path = "db/velostore.db"

        try:
            with open(file_path, 'x') as file:
                file.write("")
        except FileExistsError:
            print(f"The file '{file_path}' already exists")

    def create_table_one(self):
        """Crée une table de vélos."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS bike (
                blablabla
            )
        """)

    def create_bike_tables(self):
        """Crée les tables de vélos."""
        pass

    def test_function(self):
        """Fonction de test."""
        print("test function import")

    def change_list_to_dict(self, list: list) -> dict:
        """Convertit une liste en dictionnaire.

        Args:
            list (list): La liste à convertir.

        Returns:
            dict: Le dictionnaire résultant.
        """
        column_names = [description[0] for description in self.cursor.description]
        return dict(zip(column_names, list))

    def list_change(self) -> dict:
        """Convertit une liste de résultats en dictionnaire.

        Returns:
            dict: Le dictionnaire résultant.
        """
        new_dict_list = []
        result = self.cursor.fetchall()
        ids_list = [row[0] for row in result]
        for element in result:
            new_dict_list.append(self.change_list_to_dict(element))
        return dict(zip(ids_list, new_dict_list))
