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
                        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
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

    # GET USER BY ID
    def get_user_by_id(self, user_id, expand=True):
        if expand:
            query = """
                SELECT
                    user.id,
                    user_type.type as type,
                    user.username,
                    user_status.status as status,
                    user.mail,
                    user.password
                FROM user
                JOIN user_type ON user.user_type = user_type.id
                JOIN user_status ON user.status = user_status.id
                WHERE user.id = ?
            """
        else:
            query = """
                SELECT 
                    * 
                FROM user
                WHERE user.id = ?
            """

        self.cursor.execute(query, (user_id,))
        return super().change_list_to_dict(self.cursor.fetchone())

    def get_id_by_login_password(self, username, password):
        query = """
            SELECT id
            FROM user
            WHERE username = ? AND password = ?
        """
        self.cursor.execute(query, (username, password))
        result = self.cursor.fetchone()
        if result:
            return result[0]  
        else:
            return None 

    
    def get_type_id_user(self, user_id):
        query = """
            SELECT user.user_type
            FROM user
            WHERE id = ?
            """
        self.cursor.execute(query, (user_id,))
        return super().change_list_to_dict(self.cursor.fetchone())

def main():
    user = UserEntity()
    user.create_tables()
    #print(user.get_login_user_by_id(1))
    #print(user.get_type_id_user(5))


if __name__ == "__main__":
    main()
