import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/entities")

import order_list_entity as ole

class OrderList():
    """CLasse pour gérer les listes de commandes
    """
    def __init__(self, entity=ole.OrderListEntity()):
        """Initialise OrderList avec une entité.

        Args:
            entity (OrderListEntity, optionnel): Une entité pour interagir avec les données de commandes.
        """
        self.entity = entity
    
    def get_all_orders_list(self, expand: bool = True) -> list:
        """Récupère la liste de toutes les commandes.

        Args:
            expand (bool, optionnel): Un indicateur pour déterminer si la liste doit être étendue. Par défaut, True.

        Returns:
            list: Une liste de toutes les commandes.
        """
        return self.entity.get_all_orders(expand)

    def get_orders_by_user_list(self,id, expand: bool = True) -> list:
        """Récupère la liste des commandes d'un utilisateur.

        Args:
            user_id (int): L'identifiant de l'utilisateur.
            expand (bool, optionnel): Un indicateur pour déterminer si la liste doit être étendue. Par défaut, True.

        Returns:
            list: Une liste des commandes de l'utilisateur.
        """
        return self.entity.get_orders_by_user(id, expand)
    
    def get_orders_by_status_list(self, status: str, expand: bool = True) -> list:
        """Récupère la liste des commandes par statut.

        Args:
            status (str): Le statut des commandes.
            expand (bool, optionnel): Un indicateur pour déterminer si la liste doit être étendue. Par défaut, True.

        Returns:
            list: Une liste des commandes correspondant au statut.
        """
        return self.entity.get_order_by_status(status, expand)
    
    def get_pending_order(self) -> list:
        """Récupère les commandes en attente.

        Returns:
            list: Une liste des commandes en attente.
        """
        return self.entity.get_pending_order()
    
    def get_orders_by_user_and_status(self, user_id: int, status: str, expand: bool = True) -> list:
        """Récupère la liste des commandes d'un utilisateur par statut.

        Args:
            user_id (int): L'identifiant de l'utilisateur.
            status (str): Le statut des commandes.
            expand (bool, optionnel): Un indicateur pour déterminer si la liste doit être étendue. Par défaut, True.

        Returns:
            list: Une liste des commandes de l'utilisateur correspondant au statut.
        """
        return self.entity.get_orders_by_user_and_status(user_id, status)
    
    def get_pending_order_by_user(self,user_id: int) -> list:
        """Récupère les commandes en attente d'un utilisateur.

        Args:
            user_id (int): L'identifiant de l'utilisateur.

        Returns:
            list: Une liste des commandes en attente de l'utilisateur.
        """
        return self.entity.get_pending_order_by_user(user_id)
    
    def get_closed_order_by_user(self, user_id: int) -> list:
        """Récupère les commandes fermée d'un utilisateur

        Args:
            user_id (int): L'identifiant de l'utilisateur.

        Returns:
            list: Une liste des commandes deja payées
        """
        return self.entity.get_closed_order_by_user(user_id)

def main():
    """Fonction principale pour la classe OrderList."""
    order_list_entity = ole.OrderListEntity()
    order_list = OrderList(order_list_entity)
    order_list.get_all_orders_list()  
    # print(order_list.get_pending_order())
    print(order_list.get_pending_order_by_user(11))

if __name__ == '__main__':
    main()