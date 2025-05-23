import sqlite3

class VelostoreDatabase():
    def __init__(self):
        self.connection_db()

    def connection_db(self) -> None:
        """create a connection and a cursor object
        """
        with sqlite3.connect("db/velostore.db") as connection:
            self.connection = connection
            self.cursor = connection.cursor()
        
    def create_tables(self) -> None:
        """create all tables if they dont exist
            you can reset the whole "game" by deleting the water_world.db
        """
        #create file wator_world.db s'il n'existe pas
        file_path = "db/velostor.db"

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
      
    def create_bike_tables(self):
        #create
        pass
        
    def test_function(self):
        print("test function import")

    def change_list_to_dict(self, list):
        column_names = [description[0] for description in self.cursor.description]
        return dict(zip(column_names, list))
    
    def change_list_of_list_to_dict(self, list, columns):
        new_dict = {}
        for element in list:
            row_dict = {columns[i]: element[i] for i in range(len(columns))}
            new_dict[row_dict['id']] = row_dict

        return new_dict
            
