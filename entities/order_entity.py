import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/db")
import database as db

class OrderEntity(db.VelostoreDatabase):
    def __init__(self):
        super().__init__()

    def create_tables(self):
        self.create_orders_table()
        self.create_item_list_table()
        self.create_order_item_table()

    def create_orders_table(self):
        self.cursor.execute("""
                        CREATE TABLE IF NOT EXISTS orders (
                            id_order INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            id_user INTEGER NOT NULL,
                            date DATE NOT NULL,
                            total_price INTEGER NOT NULL,
                            status INTEGER NOT NULL,
                            FOREIGN KEY(status) REFERENCES order_status(id),
                            FOREIGN KEY(id_user) REFERENCES user(id)
                        )
                        """)

    def create_item_list_table(self):
        self.cursor.execute("""
                        CREATE TABLE IF NOT EXISTS item_list (
                            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            id_order INTEGER NOT NULL,
                            id_order_item INTEGER NOT NULL,
                            FOREIGN KEY(id_order) REFERENCES order_table(id_order)
                            FOREIGN KEY(id_order_item) REFERENCES order_item_table(id_order_item)
                        )
                        """)

    def create_order_item_table(self):
        self.cursor.execute("""
                        CREATE TABLE IF NOT EXISTS order_item (
                            id_order_item INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            id_bike INTEGER NOT NULL,
                            nb_unit STRING NOT NULL,
                            total_price INTEGER NOT NULL,
                            FOREIGN KEY(id_bike) REFERENCES bike(id)
                        )
                        """)

    def delete_order_status_table(self):
        self.cursor.execute("""
                        DROP TABLE IF EXISTS order_status
                        """)

    def delete_orders_table(self):
        self.cursor.execute("""
                        DROP TABLE IF EXISTS orders
                        """)

    def delete_item_list_table(self):
        self.cursor.execute("""
                        DROP TABLE IF EXISTS item_list
                        """)

    def delete_order_item_table(self):
        self.cursor.execute("""
                        DROP TABLE IF EXISTS order_item
                        """)
        
    def get_order_by_id(self, order_id, expand=True):
        if expand:
            self.cursor.execute(
                """
                SELECT
                    orders.id_order,
                    user.username,
                    orders.date,
                    orders.total_price,
                    order_status.status
                FROM orders
                JOIN user ON orders.id_user = user.id
                JOIN order_status ON orders.status = order_status.id
                WHERE orders.id_order = ?
            """,
                (order_id,),
            )
            result = self.cursor.fetchone()
            if result:
                return super().change_list_to_dict(result)
            else:
                return None
        else:
            self.cursor.execute(
                """
                SELECT
                    *
                FROM orders
                WHERE orders.id_order = ?
            """,
                (order_id,),
            )
            result = self.cursor.fetchone()
            if result:
                return super().change_list_to_dict(result)
            else:
                return None

    # GET ITEM LIST BY ID
    def get_item_list_by_id(self, item_list_id, expand=True):
        if expand:
            query = """
                SELECT
                    item_list.id,
                    orders.id_order as id_order,
                    order_item.id_order_item as id_order_item
                FROM item_list
                JOIN orders ON item_list.id_order = orders.id_order
                JOIN order_item ON item_list.id_order_item = order_item.id_order_item
                WHERE item_list.id = ?
            """
        else:
            query = """
                SELECT 
                    * 
                FROM item_list
                WHERE item_list.id = ?
            """

        self.cursor.execute(query, (item_list_id,))
        return super().change_list_to_dict(self.cursor.fetchone())
    
    # GET ORDER ITEM BY ID
    def get_order_item_by_id(self, order_item_id, expand=True):
        if expand:
            query = """
                SELECT
                    order_item.id_order_item,
                    bike.id as id_bike,
                    order_item.nb_unit,
                    order_item.total_price
                FROM order_item
                JOIN bike ON order_item.id_bike = bike.id
                WHERE order_item.id_order_item = ?
            """
        else:
            query = """
                SELECT 
                    * 
                FROM order_item
                WHERE order_item.id_order_item = ?
            """

        self.cursor.execute(query, (order_item_id,))
        return super().change_list_to_dict(self.cursor.fetchone())
    
    # ADD ORDER ITEM
    def add_order_item(self, id_bike, nb_unit, total_price):
        self.cursor.execute("""
            INSERT INTO order_item (id_bike, nb_unit, total_price)
            VALUES (?, ?, ?)
        """, (id_bike, nb_unit, total_price))
        self.connection.commit()
        return self.cursor.lastrowid    

    # ADD ORDER
    def add_order(self, id_user, date, total_price, status):
        # Check if the order already exists
        self.cursor.execute("""
            SELECT id_order, total_price FROM orders WHERE id_user = ? AND date = ?
        """, (id_user, date))
        result = self.cursor.fetchone()
        if result:
            # Order exists, update it
            id_order, old_total_price = result
            new_total_price = old_total_price + total_price
            self.cursor.execute("""
                UPDATE orders
                SET total_price = ?, status = ?
                WHERE id_order = ?
            """, (new_total_price, status, id_order))
            self.connection.commit()
            return id_order
        # insert new one
        self.cursor.execute("""
            INSERT INTO orders (id_user, date, total_price, status)
            VALUES (?, ?, ?, ?)
        """, (id_user, date, total_price, status))
        self.connection.commit()
        return self.cursor.lastrowid

    # UPDATE ORDER STATUS
    def update_order_status(self, order_id, new_status):
        self.cursor.execute("""
            UPDATE orders
            SET status = ?
            WHERE id_order = ?
        """, (new_status, order_id))
        self.connection.commit()
        return self.cursor.rowcoun

    
    # Insert into item_list table
    def add_order_in_item_list(self, id_order, id_order_item):
        self.cursor.execute("""
            INSERT INTO item_list (id_order, id_order_item)
            VALUES (?, ?)
        """, (id_order, id_order_item))
        self.connection.commit()
        return self.cursor.lastrowid

def main():
    order = OrderEntity()
    order.create_tables()


if __name__ == "__main__":
    main()
