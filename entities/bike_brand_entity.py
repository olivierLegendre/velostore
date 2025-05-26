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

    
    # GET BRAND BY ID
    def get_brand_by_id(self, brand_id, expand=True):
        if expand:
            query = """
                SELECT
                    bike_brand.id,
                    bike_brand.brand,
                    bike_brand.description,
                    bike_brand.price,
                    bike_destination.destination as destination,
                    bike_brand.img
                FROM bike_brand
                JOIN bike_destination ON bike_brand.destination = bike_destination.id
                WHERE bike_brand.id = ?
            """
        else:
            query = """
                SELECT 
                    * 
                FROM bike_brand
                WHERE bike_brand.id = ?
            """

        self.cursor.execute(query, (brand_id,))
        return super().change_list_to_dict(self.cursor.fetchone())
    

    # ADD BRAND (FOR ADMIN)
    def add_brand(self, brand, description, price, destination_id, img=None):
        self.cursor.execute("""
            INSERT INTO bike_brand (brand, description, price, destination, img)
            VALUES (?, ?, ?, ?, ?)
        """, (brand, description, price, destination_id, img))
        self.connection.commit()
        return self.cursor.lastrowid
    
    
    # DELETE BRAND (FOR ADMIN)
    def delete_brand(self, brand_id):
        self.cursor.execute("DELETE FROM bike_brand WHERE id = ?", (brand_id,))
        self.connection.commit()

    

def main():
    super_velo = BikeBrandEntity()
    super_velo.create_tables()
    

if __name__ == '__main__':
    main()