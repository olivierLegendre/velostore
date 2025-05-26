import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/entities")

import bike_brand_entity as bbe

class BikeBrand():
    """Classe pour gérer les opérations liées aux marques de vélos
    """
    def __init__(self, entity=bbe.BikeBrandEntity()):
        """Initialise BikeBrand avec une entité

        Args:
            entity (BikeBrandEntity, optional): Une entité pour interagir avec les données des marques de vélos.
        """
        self.entity = entity
        
    
    def get_brand_by_id(self, brand_id: int) -> dict:
        """Récupère unemarque de vélo par son identifiant.

        Args:
            brand_id (int): L'identifiant de la marque de vélo.

        Returns:
            dict: Les informations de la marque de vélo correspondante.
        """
        brand_id = self.entity.get_brand_by_id(brand_id)
        return brand_id

def main():
    """Fonction pricipale pour la class BikeBrandList"""

    bike_brand_entity = bbe.BikeBrandEntity()
    brand = BikeBrand(bike_brand_entity)
    brand_id = brand.get_brand_by_id(2)  

if __name__ == '__main__':
    main()