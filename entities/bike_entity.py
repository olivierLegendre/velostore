import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))
import database as db

class BikeEntity(db.VelostoreDatabase):
    def __init__(self):
        super().__init__()
        
    def test_function_bike_entity(self):
        print("test_function_bike_entity")

def main():
    super_velo = BikeEntity()
    super_velo.test_function()

if __name__ == '__main__':
    main()