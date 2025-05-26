import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/db")
import database as db

class UserListEntity(db.VelostoreDatabase):
    def get_all_user_list(self, expand=False):
        if expand:
            query = """
                SELECT
                    user.id,
                    user_type.type,
                    user.username,
                    user_status.status,
                    user.mail,
                    user.password
                FROM user
                JOIN user_type ON user.id = user_type.id
                JOIN user_status ON user.id = user_status.id
            """
        else:
            query = "SELECT * FROM user"

        self.cursor.execute(query)
        return super().list_change()

def main():
    user_list = UserListEntity()
    print(user_list.get_all_user_list())

if __name__ == '__main__':
    main()