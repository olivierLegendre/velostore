import os
import sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/../db")
import sqlite_database as db

class UserEntity(db.VelostoreDatabase):
    """Classe pour gérer les opérations de base de données liées aux utilisateurs."""

    def __init__(self):
        """Initialise UserEntity."""
        super().__init__()

    def create_tables(self):
        """Crée les tables nécessaires dans la base de données."""
        self.create_user_table()

    def create_user_table(self):
        """Crée la table des utilisateurs."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                user_type INTEGER NOT NULL,
                username STRING NOT NULL,
                status BOOL NOT NULL,
                mail STRING NOT NULL UNIQUE,
                password STRING NOT NULL UNIQUE,
                FOREIGN KEY(user_type) REFERENCES user_type(id),
                FOREIGN KEY(status) REFERENCES user_status(id)
            )
        """)

    def delete_user_type_table(self):
        """Supprime la table des types d'utilisateur."""
        self.cursor.execute("""
            DROP TABLE IF EXISTS user_type
        """)

    def delete_user_status_table(self):
        """Supprime la table des statuts d'utilisateur."""
        self.cursor.execute("""
            DROP TABLE IF EXISTS user_status
        """)

    def delete_user_table(self):
        """Supprime la table des utilisateurs."""
        self.cursor.execute("""
            DROP TABLE IF EXISTS user
        """)

    def get_user_by_id(self, user_id: int, expand: bool = True) -> dict:
        """Récupère un utilisateur par son identifiant.

        Args:
            user_id (int): L'identifiant de l'utilisateur.
            expand (bool, optionnel): Un indicateur pour déterminer si les détails doivent être étendus. Par défaut, True.

        Returns:
            dict: Les informations de l'utilisateur correspondant.
        """
        if expand:
            query = """
                SELECT
                    user.id,
                    user_type.type as type,
                    user.username,
                    user_status.status as status,
                    user.mail,
                    user.password
                FROM user
                JOIN user_type ON user.user_type = user_type.id
                JOIN user_status ON user.status = user_status.id
                WHERE user.id = ?
            """
        else:
            query = """
                SELECT
                    *
                FROM user
                WHERE user.id = ?
            """

        self.cursor.execute(query, (user_id,))
        return super().change_list_to_dict(self.cursor.fetchone())

    def get_id_by_login_password(self, username: str, password: str) -> int:
        """Récupère l'identifiant d'un utilisateur par son nom d'utilisateur et son mot de passe.

        Args:
            username (str): Le nom d'utilisateur.
            password (str): Le mot de passe.

        Returns:
            int: L'identifiant de l'utilisateur correspondant.
        """
        query = """
            SELECT id
            FROM user
            WHERE username = ? AND password = ?
        """
        self.cursor.execute(query, (username, password))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

    def get_type_id_user(self, user_id: int) -> dict:
        """Récupère le type d'un utilisateur par son identifiant.

        Args:
            user_id (int): L'identifiant de l'utilisateur.

        Returns:
            dict: Les informations du type de l'utilisateur correspondant.
        """
        query = """
            SELECT user.user_type
            FROM user
            WHERE id = ?
        """
        self.cursor.execute(query, (user_id,))
        return super().change_list_to_dict(self.cursor.fetchone())

def main():
    """Fonction principale pour la classe UserEntity."""
    user = UserEntity()
    user.create_tables()

if __name__ == "__main__":
    main()
