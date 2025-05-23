import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/entities")

import stat_bike_entity as sbe

class StatBike():
    def __init__(self, entity=sbe.StatBikeEntity()):
        self.entity = entity
        
    
    def get_stat_by_id(self, stat_id):
        stat = self.entity.get_statistics_by_id(stat_id)
        return stat


def main():
    stat_bike_entity = sbe.StatBikeEntity()
    stat = StatBike(stat_bike_entity)
    stat_id = stat. get_stat_by_id(1) 

if __name__ == '__main__':
    main()