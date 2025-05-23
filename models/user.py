import os
import sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/entities")

import user_entity as ue

class User():
    def __init__(self, entity=ue.UserEntity()):
        self.entity = entity
        
    
    def get_user_by_id(self, user_id):
        user = self.entity.get_user_by_id(user_id)
        print(user)
        return user


def main():
    user_entity = ue.UserEntity()
    user = User(user_entity)
    user_id = user. get_user_by_id(1) 

if __name__ == '__main__':
    main()