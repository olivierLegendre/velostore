import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/entities")

import bike_item_entity as bie

class BikeItem():
    """Classe pour gérer les opérations liées aux articles de vélos
    """
    def __init__(self, entity=bie.BikeItemEntity()):
        """Initialise BikeItem avec une entité.

        Args:
            entity (BikeItem, optional): Une entité pour interagir avec les données d'articles de vélos.
        """
        self.entity = entity
    
    def get_bike_id(self, bike_id: int) -> dict:
        """Récupère un vélo par son identifiant.

        Args:
            bike_id (int): L'identifiant du vélo.

        Returns:
            dict: Les informations du vélo correspondant.
        """
        bike_id = self.entity.get_bike_by_id(bike_id)
        return bike_id
    
    def get_bike_parameters(self, parameters: dict) -> list:
        """Récupère des vélos en fonction de paramètres donnés

        Args:
            parameters (dict): Un dictionnaire de paramètres pour filtrer les vélos.

        Returns:
            list: Une liste de vélos correspondant aux paramètres.
        """
        bike_param = self.entity.get_bike_by_parameters(parameters)
        return bike_param

    def add_bike_item(self, brand_id: int, size_id: int, color_id:int, status_id:int) -> dict:
        """Ajoute un nouvel article de vélo.

        Args:
            brand_id (int): L'identifiant de la marque.
            size_id (int): L'identifiant de la taille.
            color_id (int): L'identifiant de la couleur.
            status_id (int): L'identifiant du stat.

        Returns:
            dict: Les informations de l'article de vélo ajouté
        """
        return self.entity.add_bike_item(brand_id, size_id, color_id, status_id)
       
def main():
    """Fonction pricipale pour la class BikeItem
    """
    bike_item_entity = bie.BikeItemEntity()
    # bike_entity.test_function_bike_entity()
    bicycle = BikeItem(bike_item_entity)
    bike_id = bicycle.get_bike_id(2)  
    bike_param = bicycle.get_bike_parameters({'brand': '2'})
    get_bike_id = bicycle.get_bike_id(2)
    bicycle.add_bike_item(1,1,1,1)



if __name__ == '__main__':
    main()