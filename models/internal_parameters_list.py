import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/entities")

import internal_parameters_list_entity as iple

class InternalParametersList():
    def __init__(self, entity=iple.InternalParametersListEntity()):
        self.entity = entity
        return
    
    def get_bike_status_list(self):
        status_list = self.entity.get_all_bike_status()
        print(status_list)

    def get_bike_size_list(self):
        size_list = self.entity.get_all_bike_size()
        print(size_list)

    def get_bike_destination_list(self):
        destination_list = self.entity.get_all_bike_destination()
        print(destination_list)

    def get_bike_color_list(self):
        color_list = self.entity.get_all_bike_color()
        print(color_list)

    def get_order_status_list(self):
        order_status_list = self.entity.get_all_order_status()
        print(order_status_list)

    def get_user_type_list(self):
        user_type_list = self.entity.get_all_user_type()
        print(user_type_list)

    def get_user_status_list(self):
        user_status_list = self.entity.get_all_user_status()
        print(user_status_list)

    def get_statistics_name_list(self):
        statistics_name_list = self.entity.get_all_statistics_name()
        print(statistics_name_list)


def main():
    internal_parameters_list_entity = iple.InternalParametersListEntity()
    internal_parameters_list = InternalParametersList(internal_parameters_list_entity)
    all_color = internal_parameters_list.get_bike_color_list()

if __name__ == '__main__':
    main()