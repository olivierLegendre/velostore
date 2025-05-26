import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/entities")

import internal_parameters_list_entity as iple

class InternalParametersList():
    """Classe pour gérer les listes de paramètres internes
    """
    def __init__(self, entity=iple.InternalParametersListEntity()):
        """Initialise une instance de InternalParametersList.

        Args:
            entity (InternalParametersListEntity, optional): Une entité contenant les paramètres internes.
        """
        self.entity = entity
    
    def get_bike_status_list(self) -> list:
        """Récupère la liste des status de vélo.

        Returns:
            list: Une liste des status de vélo.
        """
        status_list = self.entity.get_all_bike_status()
        return status_list

    def get_bike_size_list(self) -> list:
        """Récupère la liste des tailles de vélo

        Returns:
            list: Une liste des tailles de vélo.
        """
        size_list = self.entity.get_all_bike_size()
        return size_list

    def get_bike_destination_list(self) -> list:
        destination_list = self.entity.get_all_bike_destination()
        return destination_list

    def get_bike_color_list(self) -> list:
        """Récupère la liste des couleurs de vélo.

        Returns:
            list: Une liste des couleurs de vélo.
        """
        color_list = self.entity.get_all_bike_color()
        return color_list

    def get_order_status_list(self) -> list:
        """
        Récupère la liste des statuts de commande.

        Returns:
            list: Une liste des statuts de commande.
        """
        order_status_list = self.entity.get_all_order_status()
        return order_status_list

    def get_user_type_list(self) -> list:
        """
        Récupère la liste des types d'utilisateur.

        Returns:
            list: Une liste des types d'utilisateur.
        """
        user_type_list = self.entity.get_all_user_type()
        return user_type_list

    def get_user_status_list(self) -> list:
        """
        Récupère la liste des statuts d'utilisateur.

        Returns:
            list: Une liste des statuts d'utilisateur.
        """
        user_status_list = self.entity.get_all_user_status()
        return user_status_list

    def get_statistics_name_list(self) -> list:
        """
        Récupère la liste des noms de statistiques.

        Returns:
            list: Une liste des noms de statistiques.
        """
        statistics_name_list = self.entity.get_all_statistics_name()
        return statistics_name_list


def main():
    """Fonction pricipale pour la class InternalParametersList
    """
    internal_parameters_list_entity = iple.InternalParametersListEntity()
    internal_parameters_list = InternalParametersList(internal_parameters_list_entity)
    print(internal_parameters_list.get_bike_color_list())

if __name__ == '__main__':
    main()