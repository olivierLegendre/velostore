import utils_model as utils

class UsersList(utils.UtilsModel):
    """Classe pour gérer les listes d'utilisateurs."""
    def __init__(self, connector='sqlite'):
        """Initialise UsersList avec une entité.

        Args:
            entity (UserListEntity, optionnel): Une entité pour interagir avec les données d'utilisateurs.
        """
        super().__init__(connector)

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
    user = UsersList('sqlite')
    all_users = user.get_user_list()

if __name__ == '__main__':
    main()