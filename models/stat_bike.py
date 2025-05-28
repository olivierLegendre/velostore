import utils_model as utils

class StatBike(utils.UtilsModel):
    """Classe pour gérer les statistiques liées aux vélos."""
    def __init__(self, connector='sqlite'):
        """Initialise StatBike avec une entité.

        Args:
            entity (StatBikeEntity, optionnel): Une entité pour interagir avec les données de statistiques de vélos.
        """
        super().__init__(connector)
        
    
    def get_stat_by_id(self, stat_id: int)-> dict:
        """Récupère une statistique de vélo par son identifiant.

        Args:
            stat_id (int): L'identifiant de la statistique.

        Returns:
            dict: Les informations de la statistique correspondante.
        """
        stat = self.entity.get_statistics_by_id(stat_id)
        return stat


def main():
    """Fonction principale pour la classe StatBike."""
    stat = StatBike('sqlite')
    stat_id = stat. get_stat_by_id(1) 

if __name__ == '__main__':
    main()