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
    
    def get_orders_by_user(self, user_id):
        self.cursor.execute("""
            SELECT * FROM orders WHERE id_user = ? ORDER BY date DESC
        """, (user_id,))
        return super().list_change()
    


def main():
    pass

if __name__ == '__main__':
    main()