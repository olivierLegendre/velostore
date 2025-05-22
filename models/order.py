import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/entities")

import order_entity as oe

class Order():
    def __init__(self, entity=oe.OrderEntity()):
        self.entity = entity

    def get_id(self, order_id):
        order_id = self.entity.get_order_by_id(order_id)
        print(order_id)
        return order_id


def main():
    order_entity= oe.OrderEntity()
    order = Order(order_entity)
    order_id = order.get_id(2) 

if __name__ == '__main__':
    main()