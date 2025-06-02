import utils_model as utils

class BikeBrand(utils.UtilsModel):
    
    """Classe pour gérer les opérations liées aux marques de vélos
    """
    def __init__(self, connector='sqlite'):
        """Initialise BikeBrand avec une entité

        Args:
            entity (BikeBrandEntity, optional): Une entité pour interagir avec les données des marques de vélos.
        """
        super().__init__(connector)
        self.init_attributes()
    
    def init_attributes(self):
        self.id = None
        self.brand = None
        self.description = None
        self.price = None
        self.destination = None
        self.img = None
        
    def dict_to_object(self, brand: list):
        print(f"fans bb list to object : {brand}")
        if self.connector == 'sqlite':
            self.id = brand["id"]
            self.brand = brand["brand"]
            self.description = brand["description"]
            self.price = brand["price"]
            self.destination = brand["destination"]
            self.img = brand["img"]
        if self.connector == 'mongodb':
            self.id = brand["id"]
            self.brand = brand["brand"]
            self.description = brand["description"]
            self.price = brand["price"]
            self.destination = brand["destination"]
            self.img = brand["img"]
        return self
        
    
    def get_brand_by_id(self, brand_id: int) -> dict:
        """Récupère unemarque de vélo par son identifiant.

        Args:
            brand_id (int): L'identifiant de la marque de vélo.

        Returns:
            dict: Les informations de la marque de vélo correspondante.
        """
        brand = self.entity.get_brand_by_id(brand_id)
        self.dict_to_object(brand)
        return brand

def main():
    """Fonction pricipale pour la class BikeBrandList"""

    # bike_brand_entity = bbe.BikeBrandEntity()
    brand = BikeBrand('sqlite')
    brand = brand.get_brand_by_id(2)
    print(f"brand {brand}")

if __name__ == '__main__':
    main()