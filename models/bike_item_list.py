import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/entities")

import bike_item_list_entity as bile

class BikeItemList():
    """Classe pour gérer les opérations liées aux listes d'articles de vélos.
    """
    def __init__(self, entity=bile.BikeItemListEntity()):
        """Initialise BikeItemList avec une entité.

        Args:
            entity (BikeItemListEntity, optional): Une entité pour interagir avec les données d'articles de vélos.
        """
        self.entity = entity
    
    def get_bike_item_list(self, expand=True):
        """Récupère la liste des articles de vélos.

        Args:
            expand (bool, optional): Un indicateur pour déterminer si la liste doit être étendue. Defaults to True.

        Returns:
            list: Une liste d'articles de vélos.
        """
        items = self.entity.get_all_bike_item(expand)
        return items

def main():
    """Fonction principale pour la classe BikeItemList
    """
    bike_item_list_entity = bile.BikeItemListEntity()
    bike_item = BikeItemList(bike_item_list_entity)
    all_bike_item = bike_item.get_bike_item_list()

if __name__ == '__main__':
    main()