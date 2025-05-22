import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/db")
import database as db

class BikeBrandEntity(db.VelostoreDatabase):
    def __init__(self):
        super().__init__()
        
    def create_tables(self):
        self.create_bike_brand_table()
        
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
        
    def get_brand_by_id(self, brand_id):
        self.cursor.execute("""
                        SELECT * FROM bike_brand WHERE ID = ?
                        """,
                        (brand_id,))
        return self.cursor.fetchone()

def main():
    super_velo = BikeBrandEntity()
    super_velo.create_tables()
    

if __name__ == '__main__':
    main()