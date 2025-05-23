import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/entities")

import internal_parameters_entity as ipe

class InternalParameters():
    def __init__(self, entity=ipe.InternalParametersEntity()):
        self.entity = entity
        # self.cursor = super().cursor

    def get_bike_status_id(self, bike_status_id):
        bike_status = self.entity.get_bike_status_by_id(bike_status_id)
        return bike_status

    def get_bike_size_id(self, size_id):
        size = self.entity.get_bike_size_by_id(size_id)
        return size

    def get_destination_id(self, destination_id):
        destination = self.entity.get_destination_by_id(destination_id)
        return destination

    def get_bike_color_id(self, color_id):
        color = self.entity.get_bike_color_by_id(color_id)
        return color

    def get_order_status_id(self, order_status_id):
        order_status = self.entity.get_order_status_by_id(order_status_id)
        return order_status

    def get_user_type_id(self, user_type_id):
        user_type = self.entity.get_user_type_by_id(user_type_id)
        return user_type

    def get_user_status_id(self, user_status_id):
        user_status = self.entity.gget_user_status_by_id(user_status_id)
        return user_status

    def get_statistics_name_id(self, statistics_name_id):
        statistics_name = self.entity.get_statistics_name_by_id(statistics_name_id)
        return statistics_name

def main():
    internal_parameters_entity = ipe.InternalParametersEntity()
    parameters = InternalParameters(internal_parameters_entity)
    parameters.get_bike_size_id(2)  




if __name__ == '__main__':
    main()