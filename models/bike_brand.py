import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/entities")

import bike_brand_entity as bbe

class BikeBrand():
    def __init__(self, entity=bbe.BikeItemEntity()):
        self.entity = entity

def main():
    pass

if __name__ == '__main__':
    main()