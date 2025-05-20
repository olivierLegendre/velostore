import sqlite3

class VelostoreDatabase():
    def __init__(self):
        self.connection_db()

    def connection_db(self) -> None:
        """create a connection and a cursor object
        """
        with sqlite3.connect("velostore.db") as connection:
            self.connection = connection
            self.cursor = connection.cursor()
        
    def create_tables(self) -> None:
        """create all tables if they dont exist
            you can reset the whole "game" by deleting the water_world.db
        """
        #create file wator_world.db s'il n'existe pas
        file_path = "velostor.db"

        try:
            with open(file_path, 'x') as file:
                file.write("")
        except FileExistsError:
            print(f"The file '{file_path}' already exists")
            
        # self.create_table_one()
        # self.create_table_two()
        # self.create_table_three()
        
    def create_table_one(self):
        self.cursor.execute("""
                        CREATE TABLE IF NOT EXISTS bike (
                            blablabla
                        )
                        """)
        
    def test_function(self):
        print("test function import")