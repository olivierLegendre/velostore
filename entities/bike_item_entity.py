import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/db")
import database as db

class BikeItemEntity(db.VelostoreDatabase):
    def __init__(self):
        super().__init__()
        
    def create_tables(self):
        self.create_bike_table()
  
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

    def get_bike_expand_by_id(self, bike_id, expand=True):
        if expand:
            self.cursor.execute(
                """
                SELECT
                    bike.id,
                    bike_brand.brand as brand,
                    bike_size.size as size,
                    bike_color.color as color,
                    bike_status.status as status
                FROM bike
                JOIN bike_size ON bike.size = bike_size.id
                JOIN bike_color ON bike.color = bike_color.id
                JOIN bike_brand ON bike.brand = bike_brand.id
                JOIN bike_status ON bike.status = bike_status.id
                WHERE bike.id = ?
            """,
                (bike_id,),
            )
            return super().change_list_to_dict(self.cursor.fetchone())
        else:
            self.cursor.execute(
                """
                SELECT 
                    * 
                FROM bike 
                WHERE bike.id = ?
            """,
                (bike_id,),
            )
            return super().change_list_to_dict(self.cursor.fetchone())


    def delete_bike_status_table(self):
        self.cursor.execute("""
                        DROP TABLE IF EXISTS bike_status
                        """)

def main():
    super_velo = BikeItemEntity()
    super_velo.create_tables()
    

if __name__ == '__main__':
    main()