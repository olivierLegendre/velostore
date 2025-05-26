import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/entities")

import bike_brand_list_entity as bbl

class BikeBrandList():
    """Gère les opérations liées aux listes de marques de vélos."""
    
    def __init__(self, entity=bbl.BikeBrandListEntity()):
        """Initialisation de BikeBrandList avec une entité

        Args:
            entity (BikeBrandListEntity, optional): Une entité pour interagir avec les données de marques de vélos.
        """
        self.entity = entity
    
    def get_bike_brand_list(self, expand: bool = True) -> list:
        """Récupère la liste des marques de vélos.

        Args:
            expand (bool, optional): Indicateur pour déterminier si la liste doit être étendue. True par défaut.

        Returns:
            list: Une liste des marques de vélos.
        """
        brand = self.entity.get_all_bike_brand_list(expand)
        return brand

    def get_all_prices_list(self) -> list:
        """Réupère la liste de tous les prix.

        Returns:
            list: Une liste de prix.
        """
        prices = self.entity.get_all_prices_list()
        return prices

    def get_all_destinations_list(self) -> list:
        """Récupère la liste de tous les types de vélos

        Returns:
            list: Une liste des destinations
        """
        destinations = self.entity.get_all_destinations_list()
        return destinations

def main():
    """Fonction pricipale pour la class BikeBrandList
    """
    bike_brand_list_entity = bbl.BikeBrandListEntity()
    brand = BikeBrandList(bike_brand_list_entity)
    print(brand.get_bike_brand_list())
    all_destinations = brand.get_all_destinations_list()

if __name__ == '__main__':
    main()