import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/entities")

import order_entity as oe

class Order():
    def __init__(self, entity=oe.OrderEntity()):
        self.entity = entity

    def get_id(self, order_id):
        return self.entity.get_order_by_id(order_id)
    
    def get_item_list_by_id(self, item_list_id):
        return self.entity.get_item_list_by_id(item_list_id)
    
    def get_order_item_by_id(self, order_item_id):
        return self.entity.get_item_list_by_id(order_item_id)
    
    def add_order_item(self, id_bike, nb_unit, total_price):
        return self.entity.add_order_item(id_bike, nb_unit, total_price)
    
    def add_order(self, id_user, date, total_price, status):
        return self.entity.add_order(id_user, date, total_price, status)


def main():
    order_entity= oe.OrderEntity()
    order = Order(order_entity)
    order.get_id(2)
    order.get_item_list_by_id(2)
    order.get_order_item_by_id(2)



if __name__ == '__main__':
    main()