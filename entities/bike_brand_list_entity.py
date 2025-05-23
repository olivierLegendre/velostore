import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/db")
import database as db

class BikeBrandListEntity(db.VelostoreDatabase):
    def get_all_bike_brand_list(self):
        self.cursor.execute("""SELECT * FROM bike_brand""")
        return super().list_change()
    

    def get_all_prices_list(self):
        self.cursor.execute("""SELECT id, price FROM bike_brand""")
        return super().list_change()
    
    def get_all_destinations_list(self):
        self.cursor.execute("""SELECT * FROM bike_destination""")
        return super().list_change()

def main():
    pass


if __name__ == "__main__":
    main()
