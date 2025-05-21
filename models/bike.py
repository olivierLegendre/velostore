import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/entities")

import bike_entity as be

class Bike():
    def __init__(self, entity=be.BikeEntity()):
        self.entity = entity
        # self.cursor = super().cursor
        return
    
    def get_bike_id(self, bike_id):
        bike_id = self.entity.get_bike_by_id(bike_id)
        print(bike_id)
    
    def get_bike_parameters(self, parameters):
        bike_param = self.entity.get_bike_by_parameters(parameters)
        print(bike_param)

def main():
    bike_entity = be.BikeEntity()
    # bike_entity.test_function_bike_entity()
    bicycle = Bike(bike_entity)
    bike_id = bicycle.get_bike_id(2)  
    bike_param = bicycle.get_bike_parameters({'brand': 'Amy Jackson'})



if __name__ == '__main__':
    main()