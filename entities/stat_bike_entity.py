import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/db")
import database as db

class StatBikeEntity(db.VelostoreDatabase):
    def __init__(self):
        super().__init__()
    
    def create_tables(self):
        self.create_statistics_name()
        self.create_statistics_bike()

    def create_statistics_name(self):
        self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS statistics_name (
                        id INTEGER PRIMARY KEY NOT NULL,
                        name STRING NOT NULL UNIQUE
                    )
                    """)


    def create_statistics_bike(self):
        self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS statistics_bike (
                        id INTEGER PRIMARY KEY NOT NULL,
                        id_bike INTEGER NOT NULL,
                        statistics_name INTEGER NOT NULL,
                        statistics_counter INTEGER NOT NULL,
                        FOREIGN KEY(statistics_name) REFERENCES statistics_name(id),
                        FOREIGN KEY(id_bike) REFERENCES bike_brand(id)
                    )
                    """)

def main():
    stats = StatBikeEntity()
    stats.create_tables()

if __name__ == '__main__':
    main()