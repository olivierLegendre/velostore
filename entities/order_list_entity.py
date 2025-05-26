import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/db")
import database as db

class OrderListEntity(db.VelostoreDatabase):
    def get_all_orders(self, expand=True):
        if expand:
            query = """
                SELECT
                    orders.id_order,
                    user.username,
                    orders.date,
                    orders.total_price,
                    order_status.status
                FROM orders
                JOIN user ON orders.id_user = user.id
                JOIN order_status ON orders.status = order_status.id
                ORDER BY orders.date DESC
            """
        else:
            query = "SELECT * FROM orders ORDER BY date DESC"

        self.cursor.execute(query)
        return super().list_change()

    def get_orders_by_user(self, user_id, expand=True):
        if expand:
            query = """
                SELECT
                    orders.id_order,
                    user.id,
                    orders.date,
                    orders.total_price,
                    order_status.status
                FROM orders
                JOIN user ON orders.id_user = user.id
                JOIN order_status ON orders.status = order_status.id
                WHERE user.id = ?
                ORDER BY date DESC
            """
        else:
            query = "SELECT * FROM orders WHERE id_user = ? ORDER BY date DESC"

        self.cursor.execute(query, (user_id,))
        return super().list_change()

    def get_order_by_status(self, status, expand=True):
        if expand:
            query = """
                SELECT
                    orders.id_order,
                    user.id AS user_id,
                    user.username,
                    orders.date,
                    orders.total_price,
                    order_status.status
                FROM orders
                JOIN user ON orders.id_order = user.id
                JOIN order_status ON orders.status = order_status.id
                WHERE order_status.status = ?
            """
        else:
            query = "SELECT * FROM orders WHERE status = ?"
            
        self.cursor.execute(query, (status,))
        return super().list_change()

    
    def get_orders_by_user_and_status(self, user_id, status, expand=True):
        if expand:
            query = """
                SELECT
                    orders.id_order,
                    user.id AS user_id,
                    user.username,
                    orders.date,
                    orders.total_price,
                    order_status.status
                FROM orders
                JOIN user ON orders.id_user = user.id
                JOIN order_status ON orders.status = order_status.id
                WHERE orders.id_user = ? AND order_status.status = ?
                ORDER BY orders.date DESC
            """
        else:
            query = """
                SELECT *
                FROM orders
                WHERE id_user = ? AND status = (
                    SELECT id FROM order_status WHERE status = ?
                )
                ORDER BY date DESC
            """

        self.cursor.execute(query, (user_id, status))
        return super().list_change()

    def get_pending_order_by_user(self,user_id):
        return self.get_orders_by_user_and_status(user_id, "en attente")
    
    



def main():
    orders_instance = OrderListEntity()
    #close_orders = orders_instance.get_close_order()

if __name__ == '__main__':
    main()
