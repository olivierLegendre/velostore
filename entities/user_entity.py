import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/db")
import database as db

class UserEntity(db.VelostoreDatabase):
    def __init__(self):
        super().__init__()
    
    def create_tables(self):
        self.create_user_table()
    
    def create_user_table(self):
        self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS user (
                        id INTEGER PRIMARY KEY NOT NULL,
                        user_type INTEGER NOT NULL,
                        username STRING NOT NULL,
                        status BOOL NOT NULL,
                        mail STRING NOT NULL UNIQUE,
                        password STRING NOT NULL UNIQUE,
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