import utils_model as utils
import bike_brand as bb

class BikeBrandList(utils.UtilsModel):
    """Gère les opérations liées aux listes de marques de vélos."""
    
    def __init__(self, connector='sqlite'):
        """Initialisation de BikeBrandList avec une entité

        Args:
            entity (BikeBrandListEntity, optional): Une entité pour interagir avec les données de marques de vélos.
        """
        super().__init__(connector)
        
    def get_object_list(self, bike_brand_list_dict: list):
        self.bike_brand_object_list = dict()
        for id, bike_brand in bike_brand_list_dict.items():
            self.bike_brand_object_list[id] = bb.BikeBrand(self.connector).dict_to_object(bike_brand)
            
    def get_bike_brand_object_list(self):
        self.get_object_list(self.get_bike_brand_list(True))
        return self.bike_brand_object_list
    
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
        """Récupère la liste de tous les prix.

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
    brand = BikeBrandList('sqlite')
    print(brand.get_bike_brand_list())

if __name__ == '__main__':
    main()
