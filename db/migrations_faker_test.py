import database as db
import os, sys
from faker import Faker

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/entities")
import bike_entity as be

class Migration_test(db.VelostoreDatabase):
    def __init__(self):
        super().__init__()
        self.bike_entity = be.BikeEntity()

    def setup(self):
        self.create_bike_tables()
        self.add_dynamics_test_data()

    def create_bike_tables(self):
        self.bike_entity.create_tables()

    def add_dynamics_test_data(self):
        self.add_dynamics_test_bike_brand()

    def add_dynamics_test(self):
        for i in range(10):
            fake = Faker()
            name = fake.name()
            address = fake.address()
            phone_number = fake.phone_number()
            date_of_birth = fake.date_of_birth()
            name2 = fake.name()
            color = fake.color_name() 

            self.cursor.executemany(
                "INSERT INTO bike_brand (brand, description, price, color, size, destination) VALUES (?, ?, ?, ?, ?, ?)",
                [(name, address, phone_number, color, date_of_birth, name2)]
            )

    def add_dynamics_test_bike_brand(self):
        for i in range(10):
            fake = Faker()
            name = fake.name()
            address = fake.address()
            phone_number = fake.phone_number()
            date_of_birth = fake.date_of_birth()
            color = fake.color_name() 

            self.cursor.executemany(
                "INSERT INTO bike_brand (brand, description, price, img, destination) VALUES (?, ?, ?, ?, ?)",
                [(name, address, phone_number, color, date_of_birth)]
            )

        self.connection.commit()
        print(
            "Total",
            self.cursor.rowcount,
            "Records inserted successfully into bike_brand table",
        )

def main():
    initial_setup = Migration_test()
    initial_setup.setup()

if __name__ == "__main__":
    main()
