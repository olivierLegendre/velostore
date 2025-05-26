import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/entities")

import user_list_entity as ule

class UsersList():
    def __init__(self, entity=ule.UserListEntity()):
        self.entity = entity

    def get_user_list(self, expand=True):
        users = self.entity.get_all_user_list(expand)
        return users

def main():
    user_list_entity = ule.UserListEntity()
    user = UsersList(user_list_entity)
    all_users = user.get_user_list()

if __name__ == '__main__':
    main()