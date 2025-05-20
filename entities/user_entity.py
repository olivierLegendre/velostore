import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/db")
import database as db

class UserEntity(db.VelostoreDatabase):
    def __init__(self):
        super().__init__()

    def test_function_user_entity(self):
        print('test fonction user entity')
    
    def create_tables(self):
        self.create_user_type_table()
        self.create_user_status_table()
        self.create_user_table()
    
    def create_user_type_table(self):
        self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS user_type (
                        id INTEGER PRIMARY KEY NOT NULL,
                        type INTEGER NOT NULL
                    )
                    """)
    def create_user_status_table(self):
        self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS user_status (
                        id INTEGER PRIMARY KEY NOT NULL,
                        status STRING NOT NULL
                    )
                    """)
    def create_user_table(self):
        self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS user (
                        id INTEGER PRIMARY KEY NOT NULL,
                        user_type INTEGER NOT NULL,
                        username STRING NOT NULL,
                        status BOOL NOT NULL,
                        mail STRING NOT NULL,
                        password STRING NOT NULL,
                        FOREIGN KEY(user_type) REFERENCES user_type(id)
                        FOREIGN KEY(status) REFERENCES user_status(id)
                    )
                    """)
    def delete_user_type_table(self):
        self.cursor.execute("""
                        DROP TABLE IF EXISTS user_type
                        """)
    def delete_user_status_table(self):
        self.cursor.execute("""
                        DROP TABLE IF EXISTS user_status
                        """)
    def delete_user_table(self):
        self.cursor.execute("""
                        DROP TABLE IF EXISTS user
                        """)

def main():
    user = UserEntity()
    user.create_tables()

if __name__ == '__main__':
    main()