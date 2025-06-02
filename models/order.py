import utils_model as utils
import bike_item as bi
from datetime import date

class Order(utils.UtilsModel):
    """Classe pour gérer les opérations liées aux commandes."""
    def __init__(self, connector='sqlite'):
        """Initialise Order avec une entité.

        Args:
            entity (OrderEntity, optionnel): Une entité pour interagir avec les données de commandes.
        """
        super().__init__(connector)

    def get_order_by_id(self, order_id: int) -> dict:
        """Récupère une commande par son identifiant.

        Args:
            order_id (int): L'identifiant de la commande.

        Returns:
            dict: Les informations de la commande correspondante.
        """
        return self.entity.get_order_by_id(order_id)
    
    def get_item_list_by_id_order(self, id_order: int) -> list:
        """Récupère une liste d'articles par son identifiant.

        Args:
            item_list_id (int): L'identifiant de la liste d'articles.

        Returns:
            list: La liste d'articles correspondante.
        """
        return self.entity.get_item_list_by_id_order(id_order)
    
    def get_order_item_by_id_order(self, id_order: int) -> dict:
        """Récupère un article de commande par son identifiant.

        Args:
            order_item_id (int): L'identifiant de l'article de commande.

        Returns:
            dict: Les informations de l'article de commande correspondant.
        """
        return self.entity.get_order_item_by_id_order(id_order)
    
    def add_order_item(self, id_bike: int, nb_unit: int, total_price: float) -> dict:
        """Ajoute un article à une commande.

        Args:
            id_bike (int): L'identifiant du vélo.
            nb_unit (int): Le nombre d'unités.
            total_price (float): Le prix total.

        Returns:
            dict: Les informations de l'article de commande ajouté.
        """
        return self.entity.add_order_item(id_bike, nb_unit, total_price)
    
    def add_order(self, id_user: int, date: str, total_price: float, status: int) -> dict:
        """Ajoute une commande.

        Args:
            id_user (int): L'identifiant de l'utilisateur.
            date (str): La date de la commande.
            total_price (float): Le prix total.
            status (int): Le statut de la commande.

        Returns:
            dict: Les informations de la commande ajoutée.
        """
        return self.entity.add_order(id_user, date, total_price, status)
    
    def add_order_in_item_list(self, id_order: int, id_order_item: int)-> dict:
        """Ajoute une commande dans une liste d'articles.

        Args:
            id_order (int): L'identifiant de la commande.
            id_order_item (int): L'identifiant de l'article de commande.

        Returns:
            dict: Les informations de l'ajout de la commande dans la liste d'articles.
        """
        return self.entity.add_order_in_item_list(id_order, id_order_item)
    
    def place_order_with_bike(self, id_user, brand, size, color, price_per_unit: float) -> int:
        """Passe une commande avec un vélo.

        Returns:
            int: L'identifiant de la commande passée.
        """
        if connector=='sqlite':
            # 1. Add the bike
            bike_item = bi.BikeItem()
            id_bike = bike_item.add_bike_item(brand, size, color, 1)
    
            # 2. Add the order
            today_date = date.today().isoformat()
            id_order = self.entity.add_order(id_user, today_date, price_per_unit, 1)
    
            # 3. Add the order item
            id_order_item = self.entity.add_order_item(id_bike, 1, price_per_unit)
    
            # 4. Insert into item_list table
            id_item_list = self.entity.add_order_in_item_list(id_order, id_order_item)
        if connector=='mongoDB':
            # 1. Add the bike
            bike_item = bi.BikeItem()
            id_bike = bike_item.get_bike_id_by_brand_config(brand, size ,color)

            # 2. Add the order
            id_order = self.entity.add_order(id_user, id_bike)
    
            return id_order
    
    def pay_order(self, id_order:int ) -> int:
        """we update the status of the order to 2 (payed)

        Args:
            id_order (int): _description_

        Returns:
            int: nb row affected, 1 is expected
        """
        return self.entity.update_order_status(id_order, 2)
    
def main():
    """Fonction principale pour la classe Order."""
    order = Order('sqlite')
    order.get_item_list_by_id_order(2)
    print(order.get_order_item_by_id_order(2))
    order.place_order_with_bike(2, 3, 2, 1, 2000)



if __name__ == '__main__':
    main()