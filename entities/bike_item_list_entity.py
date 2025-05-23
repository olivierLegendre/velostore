import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/db")
import database as db


class BikeItemListEntity(db.VelostoreDatabase):
    def get_all_bike_item(self):
        self.cursor.execute("""SELECT * FROM bike""",)
        columns = [desc[0] for desc in self.cursor.description] 
        rows = self.cursor.fetchall()
        return self.change_list_of_list_to_dict(rows, columns)

def main():
    pass

if __name__ == '__main__':
    main()