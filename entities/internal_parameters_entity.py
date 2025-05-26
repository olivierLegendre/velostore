import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/db")
import database as db

class InternalParametersEntity(db.VelostoreDatabase):
    def __init__(self):
        super().__init__()
        
    def create_tables(self):
        self.create_bike_status_table()
        self.create_bike_size_table()
        self.create_bike_destination_table()
        self.create_bike_color_table()
        self.create_order_status_table()
        self.create_user_type_table()
        self.create_user_status_table()
        self.create_statistics_name()

    #CREATE TABLES  
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
        
    def create_order_status_table(self):
        self.cursor.execute("""
                        CREATE TABLE IF NOT EXISTS order_status (
                            id INTEGER PRIMARY KEY NOT NULL UNIQUE,
                            status STRING NOT NULL UNIQUE
                        )
                        """)
        
    def create_user_type_table(self):
        self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS user_type (
                        id INTEGER PRIMARY KEY NOT NULL,
                        type INTEGER NOT NULL UNIQUE
                    )
                    """)
        
    def create_user_status_table(self):
        self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS user_status (
                        id INTEGER PRIMARY KEY NOT NULL,
                        status STRING NOT NULL UNIQUE
                    )
                    """)
        
    def create_statistics_name(self):
        self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS statistics_name (
                        id INTEGER PRIMARY KEY NOT NULL,
                        name STRING NOT NULL UNIQUE
                    )
                    """)

    #CREATE FUNCTION GET INITIAL PARAMETERS BY ID   
    def get_bike_status_by_id(self, bike_status_id):
        self.cursor.execute("""
                        SELECT * FROM bike_status WHERE ID = ?
                        """,
                        (bike_status_id,))
        return self.cursor.fetchone()
    
    def get_bike_size_by_id(self, size_id):
        self.cursor.execute("""
                        SELECT * FROM bike_size WHERE ID = ?
                        """,
                        (size_id,))
        return self.cursor.fetchone()
    
    def get_bike_destination_by_id(self, destination_id):
        self.cursor.execute("""
                        SELECT * FROM bike_destination WHERE ID = ?
                        """,
                        (destination_id,))
        return self.cursor.fetchone()
    
    def get_bike_color_by_id(self, color_id):
        self.cursor.execute("""
                        SELECT * FROM bike_color WHERE ID = ?
                        """,
                        (color_id,))
        return self.cursor.fetchone()
    
    def get_order_status_by_id(self, order_status_id):
        self.cursor.execute("""
                        SELECT * FROM order_status WHERE ID = ?
                        """,
                        (order_status_id,))
        return self.cursor.fetchone()
    
    def get_user_type_by_id(self, user_type_id):
        self.cursor.execute("""
                        SELECT * FROM user_type WHERE ID = ?
                        """,
                        (user_type_id,))
        return self.cursor.fetchone()
    
    def get_user_status_by_id(self, user_status_id):
        self.cursor.execute("""
                        SELECT * FROM user_status WHERE ID = ?
                        """,
                        (user_status_id,))
        return self.cursor.fetchone()
    
    def get_statistics_name_by_id(self, statistics_name_id):
        self.cursor.execute("""
                        SELECT * FROM statistics_name WHERE ID = ?
                        """,
                        (statistics_name_id,))
        return self.cursor.fetchone()
    


def main():
    internal_parameters = InternalParametersEntity()
    internal_parameters.create_tables()
    

if __name__ == '__main__':
    main()