import utils_model as utils

class User(utils.UtilsModel):
    """Classe pour gérer les opérations liées aux utilisateurs."""
    def __init__(self, connector='sqlite'):
        """Initialise User avec une entité.

        Args:
            entity (UserEntity, optionnel): Une entité pour interagir avec les données d'utilisateurs.
        """
        super().__init__(connector)
        
    
    def get_user_by_id(self, user_id: int) -> dict:
        """Récupère un utilisateur par son identifiant.

        Args:
            user_id (int): L'identifiant de l'utilisateur.

        Returns:
            dict: Les informations de l'utilisateur correspondant.
        """
        user = self.entity.get_user_by_id(user_id)
        return user

    def login(self, user_id):
        return self.get_user_by_id(user_id)

def main():
    """Fonction principale pour la classe User."""
    user = User('sqlite')
    user_id = user. get_user_by_id(1) 

if __name__ == '__main__':
    main()