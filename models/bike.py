import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/entities")

import bike_entity as be

class Bike():
    def __init__(self, entity=be.BikeEntity()):
        self.entity = entity


def main():
    bike_entity = be.BikeEntity()
    bike_entity.test_function_bike_entity()
    bicycle = Bike(bike_entity)

if __name__ == '__main__':
    main()