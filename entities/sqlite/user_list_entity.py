import os
import sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/db")
import database as db

class UserListEntity(db.VelostoreDatabase):
    """Classe pour gérer les listes d'utilisateurs dans la base de données."""

    def get_all_user_list(self, expand: bool = False) -> list:
        """Récupère la liste de tous les utilisateurs.

        Args:
            expand (bool, optionnel): Un indicateur pour déterminer si les détails doivent être étendus. Par défaut, False.

        Returns:
            list: Une liste de tous les utilisateurs.
        """
        if expand:
            query = """
                SELECT
                    user.id,
                    user_type.type,
                    user.username,
                    user_status.status,
                    user.mail,
                    user.password
                FROM user
                JOIN user_type ON user.id = user_type.id
                JOIN user_status ON user.id = user_status.id
            """
        else:
            query = "SELECT * FROM user"

        self.cursor.execute(query)
        return super().list_change()

def main():
    """Fonction principale pour la classe UserListEntity."""
    user_list = UserListEntity()
    print(user_list.get_all_user_list())

if __name__ == '__main__':
    main()
