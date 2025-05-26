import database as db
import os
import sys
import random
from faker import Faker

fake = Faker()
num_records = 20

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/entities")
import bike_item_entity as be
import bike_brand_entity as bbe
import order_entity as oe
import user_entity as ue
import stat_bike_entity as sbe
import internal_parameters_entity as ipe

class Migration(db.VelostoreDatabase):
    """Classe pour gérer la migration des données dans la base de données Velostore."""

    def __init__(self):
        """Initialise Migration avec les entités nécessaires."""
        super().__init__()
        self.bike_item_entity = be.BikeItemEntity()
        self.bike_brand_entity = bbe.BikeBrandEntity()
        self.order_entity = oe.OrderEntity()
        self.user_entity = ue.UserEntity()
        self.stat_bike_entity = sbe.StatBikeEntity()
        self.internal_parameters_entity = ipe.InternalParametersEntity()

    def setup(self):
        """Configure les tables et ajoute des données statiques."""
        self.create_bike_tables()
        self.create_bike_brand_tables()
        self.create_order_tables()
        self.create_user_tables()
        self.create_stat_tables()
        self.create_internal_parameters_tables()
        self.add_statics_data()

    def create_bike_tables(self):
        """Crée les tables de vélos."""
        self.bike_item_entity.create_tables()

    def create_bike_brand_tables(self):
        """Crée les tables de marques de vélos."""
        self.bike_brand_entity.create_tables()

    def create_order_tables(self):
        """Crée les tables de commandes."""
        self.order_entity.create_tables()

    def create_user_tables(self):
        """Crée les tables d'utilisateurs."""
        self.user_entity.create_tables()

    def create_stat_tables(self):
        """Crée les tables de statistiques."""
        self.stat_bike_entity.create_tables()

    def create_internal_parameters_tables(self):
        """Crée les tables de paramètres internes."""
        self.internal_parameters_entity.create_tables()

    def add_statics_data(self):
        """Ajoute des données statiques aux tables."""
        self.add_bike_status()
        self.add_bike_size()
        self.add_bike_destination()
        self.add_bike_color()
        self.add_order_status()
        self.add_user_status()
        self.add_user_type()
        self.add_stats_name()

    def add_dynamics_data(self):
        """Ajoute des données dynamiques aux tables."""
        self.add_user()
        self.add_orders()
        self.add_bike_brand()
        self.add_bike()
        self.add_order_item()
        self.add_item_list()
        self.add_statistics_bike()

    def add_bike_status(self):
        """Ajoute des statuts de vélo à la table bike_status."""
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
        """Ajoute des tailles de vélo à la table bike_size."""
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
        """Ajoute des destinations de vélo à la table bike_destination."""
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
        """Ajoute des couleurs de vélo à la table bike_color."""
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
        """Ajoute des statuts de commande à la table order_status."""
        status_order_list = [
            ("en attente",),
            ("payé",),
            ("livré",)
        ]
        self.cursor.executemany(
            "INSERT OR IGNORE INTO order_status (status) VALUES (?)", status_order_list
        )
        self.connection.commit()
        print(
            "Total",
            self.cursor.rowcount,
            "Records inserted successfully into order_status table",
        )

    def add_user_status(self):
        """Ajoute des statuts d'utilisateur à la table user_status."""
        status_user_list = [
            ("actif",),
            ("inactif",)
        ]
        self.cursor.executemany(
            "INSERT OR IGNORE INTO user_status (status) VALUES (?)", status_user_list
        )
        self.connection.commit()
        print(
            "Total",
            self.cursor.rowcount,
            "Records inserted successfully into user_status table",
        )

    def add_user_type(self):
        """Ajoute des types d'utilisateur à la table user_type."""
        user_type_list = [
            ("utilisateur",),
            ("admin",)
        ]
        self.cursor.executemany(
            "INSERT OR IGNORE INTO user_type (type) VALUES (?)", user_type_list
        )
        self.connection.commit()
        print(
            "Total",
            self.cursor.rowcount,
            "Records inserted successfully into user_type table",
        )

    def add_stats_name(self):
        """Ajoute des noms de statistiques à la table statistics_name."""
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
        """Ajoute des utilisateurs à la table user."""
        self.cursor.execute("SELECT id FROM user_type")
        user_type_ids = [row[0] for row in self.cursor.fetchall()]

        self.cursor.execute("SELECT id FROM user_status")
        status_ids = [row[0] for row in self.cursor.fetchall()]

        user_list = []

        for _ in range(num_records):
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
        """Ajoute des commandes à la table orders."""
        self.cursor.execute("SELECT id FROM user")
        user_ids = [row[0] for row in self.cursor.fetchall()]

        self.cursor.execute("SELECT id FROM order_status")
        order_status_ids = [row[0] for row in self.cursor.fetchall()]

        orders_list = []

        for _ in range(num_records):
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
        """Ajoute des listes d'articles à la table item_list."""
        self.cursor.execute("SELECT id_order FROM orders")
        orders_ids = [row[0] for row in self.cursor.fetchall()]

        self.cursor.execute("SELECT id_order_item FROM order_item")
        order_item_ids = [row[0] for row in self.cursor.fetchall()]

        item_list_list = []

        for _ in range(num_records):
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
        """Ajoute des articles de commande à la table order_item."""
        self.cursor.execute("SELECT id FROM bike")
        bike_ids = [row[0] for row in self.cursor.fetchall()]

        order_item_list = []

        for _ in range(num_records):
            id_bike = random.choice(bike_ids)
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
        """Ajoute des vélos à la table bike."""
        self.cursor.execute("SELECT id FROM bike_brand")
        bike_brand_ids = [row[0] for row in self.cursor.fetchall()]

        self.cursor.execute("SELECT id FROM bike_size")
        bike_size_ids = [row[0] for row in self.cursor.fetchall()]

        self.cursor.execute("SELECT id FROM bike_color")
        bike_color_ids = [row[0] for row in self.cursor.fetchall()]

        self.cursor.execute("SELECT id FROM bike_status")
        bike_status_ids = [row[0] for row in self.cursor.fetchall()]

        bike_list = []

        for _ in range(num_records):
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
        """Ajoute des statistiques de vélo à la table statistics_bike."""
        self.cursor.execute("SELECT id FROM bike_brand")
        bike_brand_ids = [row[0] for row in self.cursor.fetchall()]

        self.cursor.execute("SELECT id FROM statistics_name")
        statistics_name_ids = [row[0] for row in self.cursor.fetchall()]

        statistics_bike_list = []

        for _ in range(num_records):
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
        """Ajoute des marques de vélo à la table bike_brand."""
        bike_brand_list = [
            ("Rockrider", "Un vélo qui sert à grimper des montagnes", 300, 3, "url"),
            ("B’Twin", "Vélo urbain confortable idéal pour les trajets quotidiens en ville", 250, 1, "url"),
            ("Giant", "Vélo de route léger et performant, parfait pour les longues distances", 1200, 2, "url"),
            ("Cannondale", "Vélo tout-terrain robuste conçu pour les pistes accidentées", 850, 4, "url"),
            ("Electra", "Vélo cruiser au design rétro pour des balades détendues", 400, 2, "url"),
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
    """Fonction principale pour la classe Migration."""
    initial_setup = Migration()
    initial_setup.setup()
    initial_setup.add_dynamics_data()

if __name__ == "__main__":
    main()
