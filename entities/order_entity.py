import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/db")
import database as db
from bike_entity import BikeEntity


class OrderEntity(db.VelostoreDatabase):
    def __init__(self):
        super().__init__()
        self.bike_entity = BikeEntity()

    def create_tables(self):
        self.create_orders_table()
        self.create_item_list_table()
        self.create_order_item_table()

    def create_orders_table(self):
        self.cursor.execute("""
                        CREATE TABLE IF NOT EXISTS orders (
                            id_order INTEGER PRIMARY KEY NOT NULL,
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
                            id INTEGER PRIMARY KEY NOT NULL,
                            id_order INTEGER NOT NULL,
                            id_order_item INTEGER NOT NULL,
                            FOREIGN KEY(id_order) REFERENCES order_table(id_order)
                            FOREIGN KEY(id_order_item) REFERENCES order_item_table(id_order_item)
                        )
                        """)

    def create_order_item_table(self):
        self.cursor.execute("""
                        CREATE TABLE IF NOT EXISTS order_item (
                            id_order_item INTEGER PRIMARY KEY NOT NULL,
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

    def get_bike_by_id(self, bike_id, expand=True):
        if expand:
            self.cursor.execute(
                """
                SELECT
                    bike.id,
                    bike_brand.brand as brand,
                    bike_size.size as size,
                    bike_color.color as color,
                    bike_status.status as status
                FROM bike
                JOIN bike_size ON bike.size = bike_size.id
                JOIN bike_color ON bike.color = bike_color.id
                JOIN bike_brand ON bike.brand = bike_brand.id
                JOIN bike_status ON bike.status = bike_status.id
                WHERE bike.id = ?
            """,
                (bike_id,),
            )
            return super().change_list_to_dict(self.cursor.fetchone())
        else:
            self.cursor.execute(
                """
                SELECT 
                    * 
                FROM bike 
                WHERE bike.id = ?
            """,
                (bike_id,),
            )
            return super().change_list_to_dict(self.cursor.fetchone())


def main():
    order = OrderEntity()
    order.create_tables()


if __name__ == "__main__":
    main()
