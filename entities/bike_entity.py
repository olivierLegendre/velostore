import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/db")
import database as db

class BikeEntity(db.VelostoreDatabase):
    def __init__(self):
        super().__init__()
        
    def test_function_bike_entity(self):
        print("test_function_bike_entity")
        
    def create_tables(self):
        self.create_bike_status_table()
        self.create_bike_size_table()
        self.create_bike_category_table()
        self.create_bike_color_table()
        self.create_bike_table()
        
    def create_bike_status_table(self):
        self.cursor.execute("""
                        CREATE TABLE IF NOT EXISTS bike_status (
                            id INTEGER PRIMARY KEY NOT NULL,
                            status STRING NOT NULL
                        )
                        """)
        
    def create_bike_size_table(self):
        self.cursor.execute("""
                        CREATE TABLE IF NOT EXISTS bike_size (
                            id INTEGER PRIMARY KEY NOT NULL,
                            size STRING NOT NULL
                        )
                        """)
        
    def create_bike_category_table(self):
        self.cursor.execute("""
                        CREATE TABLE IF NOT EXISTS bike_category (
                            id INTEGER PRIMARY KEY NOT NULL,
                            category STRING NOT NULL
                        )
                        """)
        
    def create_bike_color_table(self):
        self.cursor.execute("""
                        CREATE TABLE IF NOT EXISTS bike_color (
                            id INTEGER PRIMARY KEY NOT NULL,
                            color STRING NOT NULL
                        )
                        """)
        
    def create_bike_type_table(self):
        self.cursor.execute("""
                        CREATE TABLE IF NOT EXISTS bike_type (
                            id INTEGER PRIMARY KEY NOT NULL,
                            type STRING NOT NULL
                        )
                        """)
        
    def create_bike_table(self):
        self.cursor.execute("""
                        CREATE TABLE IF NOT EXISTS bike (
                            id INTEGER PRIMARY KEY NOT NULL,
                            type INTEGER NOT NULL,
                            color INTEGER NOT NULL,
                            category INTEGER NOT NULL,
                            status INTEGER NOT NULL,
                            size INTEGER NOT NULL,
                            description STRING NOT NULL,
                            price INTEGER NOT NULL,
                            img STRING,
                            FOREIGN KEY(type) REFERENCES bike_type(id),
                            FOREIGN KEY(color) REFERENCES bike_color(id),
                            FOREIGN KEY(category) REFERENCES bike_category(id),
                            FOREIGN KEY(status) REFERENCES bike_status(id),
                            FOREIGN KEY(size) REFERENCES bike_size(id)
                        )
                        """)

    # def create_table_bike(self):
    #     self.cursor.execute("""
    #                     CREATE TABLE IF NOT EXISTS bike (
    #                         blablabla
    #                     )
    #                     """)
    
    def delete_bike_status_table(self):
        self.cursor.execute("""
                        DROP TABLE IF EXISTS bike_status
                        """)

def main():
    super_velo = BikeEntity()
    super_velo.create_tables()
    

if __name__ == '__main__':
    main()