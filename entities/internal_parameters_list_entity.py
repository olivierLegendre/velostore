import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/db")
import database as db


class InternalParametersListEntity(db.VelostoreDatabase):
    def get_all_bike_status(self):
        self.cursor.execute("""
                        SELECT * FROM bike_status
                        """,
                        )
        return self.cursor.fetchall()
    
    def get_all_bike_size(self):
        self.cursor.execute("""
                        SELECT * FROM bike_size
                        """,
                        )
        return self.cursor.fetchall()
    
    def get_all_bike_destination(self):
        self.cursor.execute("""
                        SELECT * FROM bike_destination
                        """,
                        )
        return self.cursor.fetchall()
    
    def get_all_bike_color(self):
        self.cursor.execute("""
                        SELECT * FROM bike_color
                        """,
                        )
        return self.cursor.fetchall()
    
    def get_all_order_status(self):
        self.cursor.execute("""
                        SELECT * FROM order_status
                        """,
                        )
        return self.cursor.fetchall()
    
    def get_all_user_type(self):
        self.cursor.execute("""
                        SELECT * FROM user_type
                        """,
                        )
        return self.cursor.fetchall()
    
    def get_all_user_status(self):
        self.cursor.execute("""
                        SELECT * FROM user_status
                        """,
                        )
        return self.cursor.fetchall()
    
    def get_all_statistics_name(self):
        self.cursor.execute("""
                        SELECT * FROM statistics_name
                        """,
                        )
        return self.cursor.fetchall()


def main():
    pass

if __name__ == '__main__':
    main()