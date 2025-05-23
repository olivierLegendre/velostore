import database as db
import os, sys
import random
from faker import Faker
fake = Faker()
num_records = 20

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/entities")
import bike_entity as be
import order_entity as oe
import user_entity as ue
import stat_bike_entity as sbe
import internal_parameters_entity as ipe

class Migration(db.VelostoreDatabase):
    def __init__(self):
        super().__init__()
        self.bike_entity = be.BikeEntity()
        self.order_entity = oe.OrderEntity()
        self.user_entity = ue.UserEntity()
        self.stat_bike_entity = sbe.StatBikeEntity()
        self.internal_parameters_entity = ipe.InternalParametersEntity()

    def setup(self):
        self.create_bike_tables()
        self.create_order_tables()
        self.create_user_tables()
        self.create_stat_tables()
        self.create_internal_parameters_tables()
        self.add_statics_data()


    def create_bike_tables(self):
        self.bike_entity.create_tables()

    def create_order_tables(self):
        self.order_entity.create_tables()

    def create_user_tables(self):
        self.user_entity.create_tables()
    
    def create_stat_tables(self):
        self.stat_bike_entity.create_tables()

    def create_internal_parameters_tables(self):
        self.internal_parameters_entity.create_tables()

    def add_statics_data(self):
        self.add_bike_status()
        self.add_bike_size()
        self.add_bike_destination()
        self.add_bike_color()
        self.add_order_status()
        self.add_user_status()
        self.add_user_type()
        self.add_stats_name()
    
    def add_dynamics_data(self):
        self.add_user()
        self.add_orders()
        self.add_bike_brand()
        self.add_bike()
        self.add_order_item()
        self.add_item_list()
        self.add_statistics_bike()
    

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

    def add_user(self): 
        self.cursor.execute("SELECT id FROM user_type")
        user_type_ids = [row[0] for row in self.cursor.fetchall()]

        self.cursor.execute("SELECT id FROM user_status")
        status_ids = [row[0] for row in self.cursor.fetchall()]

        
        user_list = []

        for i in range(num_records) :
            user_type = random.choice(user_type_ids)
            username = fake.user_name()
            status = random.choice(status_ids)
            mail = fake.email()
            password = fake.password()  

            user_list.append((user_type, username, status, mail, password))  

        self.cursor.executemany(
            "INSERT OR IGNORE INTO user (user_type, username, status, mail, password) VALUES (?, ?, ?, ?, ?)", user_list
        )
        self.connection.commit()
        print(
            "Total",
            self.cursor.rowcount,
            "Records inserted successfully into user table",
        )
       
    def add_orders(self): 
        self.cursor.execute("SELECT id FROM user")
        user_ids = [row[0] for row in self.cursor.fetchall()]
    
        self.cursor.execute("SELECT id FROM order_status")
        order_status_ids = [row[0] for row in self.cursor.fetchall()]
        
        
        orders_list = []

        for i in range(num_records) :
            id_user = random.choice(user_ids)
            date = fake.date()
            total_price = fake.pricetag()
            status = random.choice(order_status_ids)

            orders_list.append((id_user, date, total_price, status))  

        self.cursor.executemany(
            "INSERT OR IGNORE INTO orders (id_user, date, total_price, status) VALUES (?, ?, ?, ?)", orders_list
        )
        self.connection.commit()
        print(
            "Total",
            self.cursor.rowcount,
            "Records inserted successfully into orders table",
        )

    def add_item_list(self): 
        self.cursor.execute("SELECT id_order FROM orders")
        orders_ids = [row[0] for row in self.cursor.fetchall()]
    
        self.cursor.execute("SELECT id_order_item FROM order_item")
        order_item_ids = [row[0] for row in self.cursor.fetchall()]
    
        item_list_list = []

        for i in range(num_records) :
            id_order = random.choice(orders_ids) 
            id_order_item = random.choice(order_item_ids)

            item_list_list.append((id_order, id_order_item))  

        self.cursor.executemany(
            "INSERT OR IGNORE INTO item_list (id_order, id_order_item) VALUES (?, ?)", item_list_list
        )
        self.connection.commit()
        print(
            "Total",
            self.cursor.rowcount,
            "Records inserted successfully into item_list table",
        )

    def add_order_item(self):
        self.cursor.execute("SELECT id FROM bike")
        bike_ids = [row[0] for row in self.cursor.fetchall()]
     
        order_item_list = []

        for i in range(num_records) :
            id_bike =  random.choice(bike_ids)
            nb_unit = fake.randomize_nb_elements()
            total_price = fake.pricetag()

            order_item_list.append((id_bike, nb_unit, total_price))  

        self.cursor.executemany(
            "INSERT OR IGNORE INTO order_item (id_bike, nb_unit, total_price) VALUES (?, ?, ?)", order_item_list
        )
        self.connection.commit()
        print(
            "Total",
            self.cursor.rowcount,
            "Records inserted successfully into order_item table",
        )

    def add_bike(self): 
        self.cursor.execute("SELECT id FROM bike_brand")
        bike_brand_ids = [row[0] for row in self.cursor.fetchall()]

        self.cursor.execute("SELECT id FROM bike_size")
        bike_size_ids = [row[0] for row in self.cursor.fetchall()]

        self.cursor.execute("SELECT id FROM bike_color")
        bike_color_ids = [row[0] for row in self.cursor.fetchall()]

        self.cursor.execute("SELECT id FROM bike_status")
        bike_status_ids = [row[0] for row in self.cursor.fetchall()]

    
        bike_list = []

        for i in range(num_records) :
            brand = random.choice(bike_brand_ids) 
            size = random.choice(bike_size_ids)
            color = random.choice(bike_color_ids)
            status = random.choice(bike_status_ids)

            bike_list.append((brand, size, color, status))  

        self.cursor.executemany(
            "INSERT OR IGNORE INTO bike (brand, size, color, status) VALUES (?, ?, ?, ?)", bike_list
        )
        self.connection.commit()
        print(
            "Total",
            self.cursor.rowcount,
            "Records inserted successfully into bike table",
        )

    def add_statistics_bike(self): 
        self.cursor.execute("SELECT id FROM bike_brand")
        bike_brand_ids = [row[0] for row in self.cursor.fetchall()]

        self.cursor.execute("SELECT id FROM statistics_name")
        statistics_name_ids = [row[0] for row in self.cursor.fetchall()]


        statistics_bike_list = []

        for i in range(num_records) :
            id_bike = random.choice(bike_brand_ids)
            statistics_name = random.choice(statistics_name_ids)
            statistics_counter = 1000

            statistics_bike_list.append((id_bike, statistics_name, statistics_counter))  

        self.cursor.executemany(
            "INSERT OR IGNORE INTO statistics_bike (id_bike, statistics_name, statistics_counter) VALUES (?, ?, ?)", statistics_bike_list
        )
        self.connection.commit()
        print(
            "Total",
            self.cursor.rowcount,
            "Records inserted successfully into statistics_bike table",
        )


    def add_bike_brand(self):
        bike_brand_list = [
            ("Rockrider","Un vélo qui sert à grimper des montagnes",300,3,"url"),
            ("B’Twin","Vélo urbain confortable idéal pour les trajets quotidiens en ville",250,1,"url"),
            ("Giant","Vélo de route léger et performant, parfait pour les longues distances",1200,2,"url"),
            ("Cannondale","Vélo tout-terrain robuste conçu pour les pistes accidentées",850,4,"url"),
            ("Electra","Vélo cruiser au design rétro pour des balades détendues",400,2,"url"),
        ]
        self.cursor.executemany(
            "INSERT OR IGNORE INTO bike_brand (brand, description, price, destination, img) VALUES (?, ?, ?, ?, ?)", bike_brand_list
        )
        self.connection.commit()
        print(
            "Total",
            self.cursor.rowcount,
            "Records inserted successfully into bike_brand table",
        )


def main():
    initial_setup = Migration()
    initial_setup.setup()
    initial_setup.add_dynamics_data()


if __name__ == "__main__":
    main()
