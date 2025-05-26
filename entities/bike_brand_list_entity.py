import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/db")
import database as db

class BikeBrandListEntity(db.VelostoreDatabase):
    def get_all_bike_brand_list(self, expand=True):
        if expand:
            query = """
                SELECT
                    bike_brand.id,
                    bike_brand.brand,
                    bike_brand.description,
                    bike_brand.price,
                    bike_destination.destination,
                    bike_brand.img
                FROM
                    bike_brand
                JOIN bike_destination ON bike_brand.id = bike_destination.id
            """
        else:
            query = "SELECT * FROM bike_brand"
        self.cursor.execute(query)
        return super().list_change()
    

    def get_all_prices_list(self):
        self.cursor.execute("""SELECT id, price FROM bike_brand""")
        return super().list_change()
    
    def get_all_destinations_list(self):
        self.cursor.execute("""SELECT * FROM bike_destination""")
        return super().list_change()

def main():
    bike_brand_list = BikeBrandListEntity()
    test1 = bike_brand_list.get_all_bike_brand_list()
    #print(test1)


if __name__ == "__main__":
    main()
