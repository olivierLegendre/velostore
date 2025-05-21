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
        self.create_bike_destination_table()
        self.create_bike_color_table()
        self.create_bike_brand_table()
        self.create_bike_table()
        
    def create_bike_status_table(self):
        self.cursor.execute("""
                        CREATE TABLE IF NOT EXISTS bike_status (
                            id INTEGER PRIMARY KEY NOT NULL,
                            status STRING NOT NULL UNIQUE
                        )
                        """)
        
    def create_bike_size_table(self):
        self.cursor.execute("""
                        CREATE TABLE IF NOT EXISTS bike_size (
                            id INTEGER PRIMARY KEY NOT NULL,
                            size STRING NOT NULL UNIQUE
                        )
                        """)
        
    def create_bike_destination_table(self):
        self.cursor.execute("""
                        CREATE TABLE IF NOT EXISTS bike_destination (
                            id INTEGER PRIMARY KEY NOT NULL,
                            destination STRING NOT NULL UNIQUE
                            
                        )
                        """)
        
    def create_bike_color_table(self):
        self.cursor.execute("""
                        CREATE TABLE IF NOT EXISTS bike_color (
                            id INTEGER PRIMARY KEY NOT NULL,
                            color STRING NOT NULL UNIQUE 
                        )
                        """)
        
    def create_bike_brand_table(self):
        self.cursor.execute("""
                        CREATE TABLE IF NOT EXISTS bike_brand (
                            id INTEGER PRIMARY KEY NOT NULL,
                            brand STRING NOT NULL UNIQUE,
                            description STRING NOT NULL,
                            price INTEGER NOT NULL,
                            destination STRING NOT NULL,
                            img STRING,
                            FOREIGN KEY(destination) REFERENCES bike_destination(id)
                        )
                        """)
        
    def create_bike_table(self):
        self.cursor.execute("""
                        CREATE TABLE IF NOT EXISTS bike (
                            id INTEGER PRIMARY KEY NOT NULL,
                            brand INTEGER NOT NULL,
                            size INTEGER NOT NULL,
                            color INTEGER NOT NULL,
                            status INTEGER NOT NULL,
                            FOREIGN KEY(brand) REFERENCES bike_brand(id),
                            FOREIGN KEY(status) REFERENCES bike_status(id),
                            FOREIGN KEY(size) REFERENCES bike_size(id),
                            FOREIGN KEY(color) REFERENCES bike_color(id)
                        )
                        """)
    def get_bike_by_id(self, bike_id):
        self.cursor.execute("""
                        SELECT * FROM bike WHERE ID = ?
                        """,
                        (bike_id,))
        return self.cursor.fetchone()
    
    def get_bike_by_parameters(self, parameters):
        query = "SELECT * FROM bike WHERE "
        conditions = []
        values = []

        for key, value in parameters.items():
            if key in ['id', 'brand', 'size', 'color', 'status']:
                conditions.append(f"{key} = ?")
                values.append(value)

        if not conditions:
            raise ValueError("No valid parameters provided for the query.")
        # pour joindre les 2 param (clé valeur) à vérifier
        query += " AND ".join(conditions)

        # debug
        #print("Generated SQL Query:", query)
        #print("Values:", values)

        self.cursor.execute(query, tuple(values))
        return self.cursor.fetchone()


    def delete_bike_status_table(self):
        self.cursor.execute("""
                        DROP TABLE IF EXISTS bike_status
                        """)

def main():
    super_velo = BikeEntity()
    super_velo.create_tables()
    

if __name__ == '__main__':
    main()