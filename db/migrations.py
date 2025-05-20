import database as db
import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/entities")
import bike_entity as be


class Migration(db.VelostoreDatabase):
    def __init__(self):
        super().__init__()
        self.bike_entity = be.BikeEntity()

    def setup(self):
        self.create_bike_tables()
        self.add_statics_data()

    def create_bike_tables(self):
        self.bike_entity.create_tables()

    def create_order_tables(self):
        pass

    def create_user_tables(self):
        pass

    def add_statics_data(self):
        self.add_bike_status()
        self.add_bike_size()
        self.add_bike_category()
        self.add_bike_color()
        self.add_bike_type()

    def add_bike_status(self):
        status_list = [
            ("disponible",),
            ("non disponible",),
        ]
        self.cursor.executemany(
            "INSERT OR IGNORE INTO bike_status (status) VALUES (?)", status_list
        )
        self.connection.commit()
        print(
            "Total",
            self.cursor.rowcount,
            "Records inserted successfully into bike_status table",
        )

    def add_bike_size(self):
        size_list = [
            ("S",),
            ("M",),
            ("L",),
            ("XL",),
        ]
        self.cursor.executemany(
            "INSERT OR IGNORE INTO bike_size (size) VALUES (?)", size_list
        )
        self.connection.commit()
        print(
            "Total",
            self.cursor.rowcount,
            "Records inserted successfully into bike_size table",
        )

    def add_bike_category(self):
        category_list = [
            ("route",),
            ("course",),
            ("VTT",),
            ("BMX",),
        ]
        self.cursor.executemany(
            "INSERT OR IGNORE INTO bike_category (category) VALUES (?)", category_list
        )
        self.connection.commit()
        print(
            "Total",
            self.cursor.rowcount,
            "Records inserted successfully into bike_category table",
        )

    def add_bike_color(self):
        color_list = [
            ("bleu",),
            ("rouge",),
            ("vert",),
            ("noir",),
            ("rose",),
            ("blanc",),
        ]
        self.cursor.executemany(
            "INSERT OR IGNORE INTO bike_color (color) VALUES (?)", color_list
        )
        self.connection.commit()
        print(
            "Total",
            self.cursor.rowcount,
            "Records inserted successfully into bike_color table",
        )

    def add_bike_type(self):
        type_list = [
            ("Rockrider",),
            ("Elops",),
            ("Btwin",),
            ("Stilus",),
        ]
        self.cursor.executemany(
            "INSERT OR IGNORE INTO bike_type (type) VALUES (?)", type_list
        )
        self.connection.commit()
        print(
            "Total",
            self.cursor.rowcount,
            "Records inserted successfully into bike_type table",
        )


def main():
    initial_setup = Migration()
    initial_setup.setup()


if __name__ == "__main__":
    main()
