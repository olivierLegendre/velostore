import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/entities")

import order_entity as oe

class Order():
    def __init__(self, entity=oe.OrderEntity()):
        self.entity = entity
        return

    def get_id(self, bike_id):
        bike_id = self.entity.get_bike_id(bike_id)
        print(bike_id)


def main():
    order_entity= oe.OrderEntity()
    order = Order(order_entity)
    bike_id = order.get_id(2) 

if __name__ == '__main__':
    main()