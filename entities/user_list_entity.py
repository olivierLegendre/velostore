import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/db")
import database as db

class UserListEntity(db.VelostoreDatabase):
    def get_all_user_list(self):
        self.cursor.execute("""SELECT * FROM user""")
        return super().list_change()


def main():
    pass

if __name__ == '__main__':
    main()