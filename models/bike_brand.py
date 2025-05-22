import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/entities")

import bike_brand_entity as bbe

class BikeBrand():
    def __init__(self, entity=bbe.BikeBrandEntity()):
        self.entity = entity
        return
    
    def get_brand_by_id(self, brand_id):
        brand_id = self.entity.get_brand_by_id(brand_id)
        print(brand_id)

def main():
    bike_brand_entity = bbe.BikeBrandEntity()
    brand = BikeBrand(bike_brand_entity)
    brand_id = brand.get_brand_by_id(2)  

if __name__ == '__main__':
    main()