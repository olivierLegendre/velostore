import database as db
import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/entities")
import bike_entity as be
import order_entity as oe
import user_entity as ue
import stat_bike_entity as sbe

class Migration(db.VelostoreDatabase):
    def __init__(self):
        super().__init__()
        self.bike_entity = be.BikeEntity()
        self.order_entity = oe.OrderEntity()
        self.user_entity = ue.UserEntity()
        self.stat_bike_entity = sbe.StatBikeEntity()

    def setup(self):
        self.create_bike_tables()
        self.create_order_tables()
        self.create_user_tables()
        self.create_stat_tables()
        self.add_statics_data()

    def create_bike_tables(self):
        self.bike_entity.create_tables()

    def create_order_tables(self):
        self.order_entity.create_tables()

    def create_user_tables(self):
        self.user_entity.create_tables()
    
    def create_stat_tables(self):
        self.stat_bike_entity.create_tables()

    def add_statics_data(self):
        self.add_bike_status()
        self.add_bike_size()
        self.add_bike_destination()
        self.add_bike_color()
        self.add_bike_brand()
        self.add_order_status()
        self.add_user_status()
        self.add_user_type()
        self.add_stats_name()
    

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

    def add_bike_destination(self):
        destination_list = [
            ("route",),
            ("course",),
            ("VTT",),
            ("BMX",),
        ]
        self.cursor.executemany(
            "INSERT OR IGNORE INTO bike_destination (destination) VALUES (?)", destination_list
        )
        self.connection.commit()
        print(
            "Total",
            self.cursor.rowcount,
            "Records inserted successfully into bike_destination table",
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

    def add_bike_brand(self):
        brand_list = [
            ("Rockrider",),
            ("Elops",),
            ("Btwin",),
            ("Stilus",),
        ]
        self.cursor.executemany(
            "INSERT OR IGNORE INTO bike_brand (brand) VALUES (?)", brand_list
        )
        self.connection.commit()
        print(
            "Total",
            self.cursor.rowcount,
            "Records inserted successfully into bike_brand table",
        )

    def add_order_status(self):
        status_order__list = [
            ("en attente",),
            ("payé",),
            ("livré",)
        ]
        self.cursor.executemany(
            "INSERT OR IGNORE INTO order_status (status) VALUES (?)", status_order__list
        )
        self.connection.commit()
        print(
            "Total",
            self.cursor.rowcount,
            "Records inserted successfully into order_status table",
        )

    def add_user_status(self):
        status_user__list = [
            ("actif",),
            ("inactif",)
        ]
        self.cursor.executemany(
            "INSERT OR IGNORE INTO user_status (status) VALUES (?)", status_user__list
        )
        self.connection.commit()
        print(
            "Total",
            self.cursor.rowcount,
            "Records inserted successfully into user_status table",
        )


    def add_user_type(self):
        status_user__type = [
            ("utilisateur",),
            ("admin",)
        ]
        self.cursor.executemany(
            "INSERT OR IGNORE INTO user_type (type) VALUES (?)", status_user__type
        )
        self.connection.commit()
        print(
            "Total",
            self.cursor.rowcount,
            "Records inserted successfully into user_type table",
        )


    def add_stats_name(self):
        stats_name_list = [
            ("Nombre de clique par vélo",)
        ]
        self.cursor.executemany(
            "INSERT OR IGNORE INTO statistics_name (name) VALUES (?)", stats_name_list
        )
        self.connection.commit()
        print(
            "Total",
            self.cursor.rowcount,
            "Records inserted successfully into statistics_name table",
        )


def main():
    initial_setup = Migration()
    initial_setup.setup()


if __name__ == "__main__":
    main()
