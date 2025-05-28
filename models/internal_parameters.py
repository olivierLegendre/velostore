import sql_model as sql_m

class InternalParameters(sql_m.SqlModel):
    """
    Une classe pour gérer les paramètres internes.
    """
    def __init__(self, connector='sqlite'):
        """
        Initialise une instance de InternalParameters.

        Args:
            entity (InternalParametersEntity, optionnel): Une entité contenant les paramètres internes.
        """
        super().__init__(connector)

    def get_bike_status_id(self, bike_status_id: int) -> object:
        """
        Récupère le statut de vélo en fonction de son identifiant.

        Args:
            bike_status_id (int): L'identifiant du statut de vélo.

        Returns:
            object: Le statut de vélo correspondant à l'identifiant.
        """
        bike_status = self.entity.get_bike_status_by_id(bike_status_id)
        return bike_status

    def get_bike_size_id(self, size_id: int) -> object:
        """
        Récupère la taille de vélo en fonction de son identifiant.

        Args:
            size_id (int): L'identifiant de la taille de vélo.

        Returns:
            object: La taille de vélo correspondant à l'identifiant.
        """
        size = self.entity.get_bike_size_by_id(size_id)
        return size

    def get_destination_id(self, destination_id: int) -> object:
        """
        Récupère la destination de vélo en fonction de son identifiant.

        Args:
            destination_id (int): L'identifiant de la destination de vélo.

        Returns:
            object: La destination de vélo correspondant à l'identifiant.
        """
        destination = self.entity.get_destination_by_id(destination_id)
        return destination

    def get_bike_color_id(self, color_id: int) -> object:
        """
        Récupère la couleur de vélo en fonction de son identifiant.

        Args:
            color_id (int): L'identifiant de la couleur de vélo.

        Returns:
            object: La couleur de vélo correspondant à l'identifiant.
        """
        color = self.entity.get_bike_color_by_id(color_id)
        return color

    def get_order_status_id(self, order_status_id: int) -> object:
        """
        Récupère le statut de commande en fonction de son identifiant.

        Args:
            order_status_id (int): L'identifiant du statut de commande.

        Returns:
            object: Le statut de commande correspondant à l'identifiant.
        """
        order_status = self.entity.get_order_status_by_id(order_status_id)
        return order_status

    def get_user_type_id(self, user_type_id: int) -> object:
        """
        Récupère le type d'utilisateur en fonction de son identifiant.

        Args:
            user_type_id (int): L'identifiant du type d'utilisateur.

        Returns:
            object: Le type d'utilisateur correspondant à l'identifiant.
        """
        user_type = self.entity.get_user_type_by_id(user_type_id)
        return user_type

    def get_user_status_id(self, user_status_id: int) -> object:
        """
        Récupère le statut d'utilisateur en fonction de son identifiant.

        Args:
            user_status_id (int): L'identifiant du statut d'utilisateur.

        Returns:
            object: Le statut d'utilisateur correspondant à l'identifiant.
        """
        user_status = self.entity.gget_user_status_by_id(user_status_id)
        return user_status

    def get_statistics_name_id(self, statistics_name_id: int) -> object:
        """
        Récupère le nom de statistique en fonction de son identifiant.

        Args:
            statistics_name_id (int): L'identifiant du nom de statistique.

        Returns:
            object: Le nom de statistique correspondant à l'identifiant.
        """
        statistics_name = self.entity.get_statistics_name_by_id(statistics_name_id)
        return statistics_name

def main():
    parameters = InternalParameters('sqlite')
    parameters.get_bike_size_id(2)  




if __name__ == '__main__':
    main()