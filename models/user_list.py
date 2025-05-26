import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/entities")

import user_list_entity as ule

class UsersList():
    """Classe pour gérer les listes d'utilisateurs."""
    def __init__(self, entity=ule.UserListEntity()):
        """Initialise UsersList avec une entité.

        Args:
            entity (UserListEntity, optionnel): Une entité pour interagir avec les données d'utilisateurs.
        """
        self.entity = entity

    def get_user_list(self, expand: bool = True) -> list:
        """Récupère la liste de tous les utilisateurs.

        Args:
            expand (bool, optionnel): Un indicateur pour déterminer si la liste doit être étendue. Par défaut, True.

        Returns:
            list: Une liste de tous les utilisateurs.
        """
        users = self.entity.get_all_user_list(expand)
        return users

def main():
    """Fonction principale pour la classe UsersList."""
    user_list_entity = ule.UserListEntity()
    user = UsersList(user_list_entity)
    all_users = user.get_user_list()

if __name__ == '__main__':
    main()