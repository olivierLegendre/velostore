import os
import sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/entities")

import user_entity as ue

class User():
    """Classe pour gérer les opérations liées aux utilisateurs."""
    def __init__(self, entity=ue.UserEntity()):
        """Initialise User avec une entité.

        Args:
            entity (UserEntity, optionnel): Une entité pour interagir avec les données d'utilisateurs.
        """
        self.entity = entity
        
    
    def get_user_by_id(self, user_id: int) -> dict:
        """Récupère un utilisateur par son identifiant.

        Args:
            user_id (int): L'identifiant de l'utilisateur.

        Returns:
            dict: Les informations de l'utilisateur correspondant.
        """
        user = self.entity.get_user_by_id(user_id)
        return user


def main():
    """Fonction principale pour la classe User."""
    user_entity = ue.UserEntity()
    user = User(user_entity)
    user_id = user. get_user_by_id(1) 

if __name__ == '__main__':
    main()