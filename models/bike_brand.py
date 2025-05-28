import sql_model as sql_m

class BikeBrand(sql_m.SqlModel):
    
    """Classe pour gérer les opérations liées aux marques de vélos
    """
    def __init__(self, connector='sqlite'):
        """Initialise BikeBrand avec une entité

        Args:
            entity (BikeBrandEntity, optional): Une entité pour interagir avec les données des marques de vélos.
        """
        super().__init__(connector)
    
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