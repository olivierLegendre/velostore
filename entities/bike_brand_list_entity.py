import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/db")
import database as db


class BikeBrandListEntity(db.VelostoreDatabase):
    def get_all_bike_brand(self):
        self.cursor.execute("""
                        SELECT * FROM bike_brand
                        """,
                        )
        return self.cursor.fetchall()

def main():
    pass

if __name__ == '__main__':
    main()