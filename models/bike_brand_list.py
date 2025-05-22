import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/entities")

import bike_brand_list_entity as bbl

class BikeBrandList():
    def __init__(self, entity=bbl.BikeBrandListEntity()):
        self.entity = entity
    
    def get_bike_brand_list(self):
        brand = self.entity.get_all_bike_brand_list()
        print(brand)
        return brand

    def get_all_prices_list(self):
        prices = self.entity.get_all_prices_list()
        print(prices)
        return prices

def main():
    bike_brand_list_entity = bbl.BikeBrandListEntity()
    brand = BikeBrandList(bike_brand_list_entity)
    all_brand = brand.get_bike_brand_list()  
    all_prices = brand.get_all_prices_list()

if __name__ == '__main__':
    main()