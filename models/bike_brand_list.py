import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/entities")

import bike_brand_list_entity as bbl

class BikeBrandList():
    def __init__(self, entity=bbl.BikeBrandListEntity()):
        self.entity = entity
        return
    
    def get_bike_list_brand(self):
        brand = self.entity.get_all_bike_brand()
        print(brand)


def main():
    bike_brand_list_entity = bbl.BikeBrandListEntity()
    brand = BikeBrandList(bike_brand_list_entity)
    all_brand = brand.get_bike_list_brand()  

if __name__ == '__main__':
    main()