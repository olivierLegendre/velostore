import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/entities")

import bike_item_list_entity as bile

class BikeItemList():
    def __init__(self, entity=bile.BikeItemListEntity()):
        self.entity = entity
        return
    
    def get_bike_list_brand(self):
        brand = self.entity.get_all_bike_item()
        print(brand)


def main():
    bike_item_list_entity = bile.BikeItemListEntity()
    bike_item = BikeItemList(bike_item_list_entity)
    all_bike_item = bike_item.get_bike_list_brand()

if __name__ == '__main__':
    main()