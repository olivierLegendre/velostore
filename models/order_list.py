import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/entities")

import order_list_entity as ole

class OrderList():
    def __init__(self, entity=ole.OrderListEntity()):
        self.entity = entity
    
    def get_all_orders_list(self):
        return self.entity.get_all_orders()

    def get_orders_by_user_id(self,id):
        return self.entity.get_orders_by_user(id)
    
    def get_orders_by_status_list(self, status):
        return self.entity.get_order_by_status(status)

    def get_orders_by_user_and_status(self, user_id, status, expand=True):
        return self.entity.get_orders_by_user_and_status(user_id, status)
    
    def get_pending_order_by_user(self,user_id):
        return self.entity.get_pending_order_by_user(user_id)

def main():
    order_list_entity = ole.OrderListEntity()
    order_list = OrderList(order_list_entity)
    order_list.get_all_orders_list()  
    # print(order_list.get_pending_order())
    print(order_list.get_pending_order_by_user(11))
    
    



if __name__ == '__main__':
    main()