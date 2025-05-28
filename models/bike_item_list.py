import sql_model as sql_m

class BikeItemList(sql_m.SqlModel):
    """Classe pour gérer les opérations liées aux listes d'articles de vélos.
    """
    def __init__(self, connector='sqlite'):
        """Initialise BikeItemList avec une entité.

        Args:
            entity (BikeItemListEntity, optional): Une entité pour interagir avec les données d'articles de vélos.
        """
        super().__init__(connector)
    
    def get_bike_item_list(self, expand: bool = True) -> list:
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
    bike_item = BikeItemList('sqlite')
    all_bike_item = bike_item.get_bike_item_list()

if __name__ == '__main__':
    main()