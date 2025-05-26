import os, sys
from datetime import date
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/entities")

import order_entity as oe
import bike_item as bi


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
    
    def place_order_with_bike(self, id_user, brand_id, size_id, color_id, price_per_unit):
        # 1. Add the bike
        bike_item = bi.BikeItem()
        id_bike = bike_item.add_bike_item(brand_id, size_id, color_id, 1)

        # 2. Add the order
        today_date = date.today().isoformat()
        id_order = self.entity.add_order(id_user, today_date, price_per_unit, 1)

        # 3. Add the order item
        id_order_item = self.entity.add_order_item(id_bike, 1, price_per_unit)

        return 
    
def main():
    order_entity= oe.OrderEntity()
    order = Order(order_entity)
    order.get_id(2)
    order.get_item_list_by_id(2)
    order.get_order_item_by_id(2)
    order.place_order_with_bike(1, 1, 1, 1, 10)



if __name__ == '__main__':
    main()