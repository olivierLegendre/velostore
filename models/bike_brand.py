import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/entities")

# import bike_brand_entity as bbe
import entity_manager as em

class BikeBrand():
    model_name = 'bike_brand'
    model_class_name = 'BikeBrand'
    entity_name = 'bike_brand_entity'
    entity_class_name = 'BikeBrandEntity'
    
    """Classe pour gérer les opérations liées aux marques de vélos
    """
    def __init__(self, connector='sqlite'):
        """Initialise BikeBrand avec une entité

        Args:
            entity (BikeBrandEntity, optional): Une entité pour interagir avec les données des marques de vélos.
        """
        entity_manager = em.EntityManager(connector)
        entity = entity_manager.get_entity(self.get_names())
        self.entity = entity
    
    
    def get_names(self):
        return dict(
            model_name = self.model_name,
            model_class_name = self.model_class_name,
            entity_name = self.entity_name,
            entity_class_name = self.entity_class_name,
        )
    
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

    # bike_brand_entity = bbe.BikeBrandEntity()
    brand = BikeBrand('sqlite')
    brand = brand.get_brand_by_id(2)
    print(f"brand {brand}")

if __name__ == '__main__':
    main()