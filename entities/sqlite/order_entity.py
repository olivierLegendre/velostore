import os
import sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/../db")
import sqlite_database as db

class OrderEntity(db.VelostoreDatabase):
    """Classe pour gérer les opérations de base de données liées aux commandes."""

    def __init__(self):
        """Initialise OrderEntity."""
        super().__init__()

    def create_tables(self):
        """Crée les tables nécessaires dans la base de données."""
        self.create_orders_table()
        self.create_item_list_table()
        self.create_order_item_table()

    def create_orders_table(self):
        """Crée la table des commandes."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id_order INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                id_user INTEGER NOT NULL,
                date DATE NOT NULL,
                total_price INTEGER NOT NULL,
                status INTEGER NOT NULL,
                FOREIGN KEY(status) REFERENCES order_status(id),
                FOREIGN KEY(id_user) REFERENCES user(id)
            )
        """)

    def create_item_list_table(self):
        """Crée la table des listes d'articles."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS item_list (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                id_order INTEGER NOT NULL,
                id_order_item INTEGER NOT NULL,
                FOREIGN KEY(id_order) REFERENCES orders(id_order),
                FOREIGN KEY(id_order_item) REFERENCES order_item(id_order_item)
            )
        """)

    def create_order_item_table(self):
        """Crée la table des articles de commande."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS order_item (
                id_order_item INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                id_bike INTEGER NOT NULL,
                nb_unit STRING NOT NULL,
                total_price INTEGER NOT NULL,
                FOREIGN KEY(id_bike) REFERENCES bike(id)
            )
        """)

    def delete_order_status_table(self):
        """Supprime la table des statuts de commande."""
        self.cursor.execute("""
            DROP TABLE IF EXISTS order_status
        """)

    def delete_orders_table(self):
        """Supprime la table des commandes."""
        self.cursor.execute("""
            DROP TABLE IF EXISTS orders
        """)

    def delete_item_list_table(self):
        """Supprime la table des listes d'articles."""
        self.cursor.execute("""
            DROP TABLE IF EXISTS item_list
        """)

    def delete_order_item_table(self):
        """Supprime la table des articles de commande."""
        self.cursor.execute("""
            DROP TABLE IF EXISTS order_item
        """)

    def get_order_by_id(self, order_id: int, expand: bool = True) -> dict:
        """Récupère une commande par son identifiant.

        Args:
            order_id (int): L'identifiant de la commande.
            expand (bool, optionnel): Un indicateur pour déterminer si les détails doivent être étendus. Par défaut, True.

        Returns:
            dict: Les informations de la commande correspondante.
        """
        if expand:
            self.cursor.execute(
                """
                SELECT
                    orders.id_order,
                    user.username,
                    orders.date,
                    orders.total_price,
                    order_status.status
                FROM orders
                JOIN user ON orders.id_user = user.id
                JOIN order_status ON orders.status = order_status.id
                WHERE orders.id_order = ?
                """,
                (order_id,),
            )
            result = self.cursor.fetchone()
            if result:
                return super().change_list_to_dict(result)
            else:
                return None
        else:
            self.cursor.execute(
                """
                SELECT
                    *
                FROM orders
                WHERE orders.id_order = ?
                """,
                (order_id,),
            )
            result = self.cursor.fetchone()
            if result:
                return super().change_list_to_dict(result)
            else:
                return None

    def get_item_list_by_id_order(self, id_order: int, expand: bool = True) -> dict:
        """Récupère une liste d'articles par son identifiant.

        Args:
            item_list_id (int): L'identifiant de la liste d'articles.
            expand (bool, optionnel): Un indicateur pour déterminer si les détails doivent être étendus. Par défaut, True.

        Returns:
            dict: Les informations de la liste d'articles correspondante.
        """
        if expand:
            query = """
                SELECT
                    item_list.id,
                    orders.id_order as id_order,
                    order_item.id_order_item as id_order_item
                FROM item_list
                JOIN orders ON item_list.id_order = orders.id_order
                JOIN order_item ON item_list.id_order_item = order_item.id_order_item
                WHERE item_list.id_order = ?
            """
        else:
            query = """
                SELECT
                    *
                FROM item_list
                WHERE item_list.id_order = ?
            """

        self.cursor.execute(query, (id_order,))
        return super().change_list_to_dict(self.cursor.fetchone())

    def get_order_item_by_id_order(self, order_id: int, expand: bool = True) -> dict:
        """Récupère un article de commande par son identifiant.

        Args:
            order_item_id (int): L'identifiant de l'article de commande.
            expand (bool, optionnel): Un indicateur pour déterminer si les détails doivent être étendus. Par défaut, True.

        Returns:
            dict: Les informations de l'article de commande correspondant.
        """
        if expand:
            query = """
                SELECT
                    *
                FROM order_item oi
                JOIN item_list il ON il.id_order_item = oi.id_order_item
                JOIN bike ON bike.id = oi.id_bike
                JOIN bike_brand bb ON bb.id = bike.brand
                JOIN bike_color bc ON bc.id =bike.color
                JOIN bike_size bs ON bs.id = bike.size
                WHERE il.id_order = ?
            """
        else:
            query = """
                SELECT
                    *
                FROM order_item oi
                JOIN item_list il ON il.id_order_item = oi.id_order_item
                JOIN bike ON bike.id = oi.id_bike
                WHERE il.id_order = ?
            """

        self.cursor.execute(query, (order_id,))
        return super().list_change()

    def add_order_item(self, id_bike: int, nb_unit: int, total_price: float) -> int:
        """Ajoute un article à une commande.

        Args:
            id_bike (int): L'identifiant du vélo.
            nb_unit (int): Le nombre d'unités.
            total_price (float): Le prix total.

        Returns:
            int: L'identifiant du nouvel article de commande ajouté.
        """
        self.cursor.execute("""
            INSERT INTO order_item (id_bike, nb_unit, total_price)
            VALUES (?, ?, ?)
        """, (id_bike, nb_unit, total_price))
        self.connection.commit()
        return self.cursor.lastrowid

    def add_order(self, id_user: int, date: str, total_price: float, status: int) -> int:
        """Ajoute une commande.

        Args:
            id_user (int): L'identifiant de l'utilisateur.
            date (str): La date de la commande.
            total_price (float): Le prix total.
            status (int): Le statut de la commande.

        Returns:
            int: L'identifiant de la commande ajoutée.
        """
        # Check if the order already exists
        self.cursor.execute("""
            SELECT id_order, total_price FROM orders WHERE id_user = ? AND status = "en attente"
        """, (id_user,))
        result = self.cursor.fetchone()
        if result:
            # Order exists, update it
            id_order, old_total_price = result
            new_total_price = old_total_price + total_price
            self.cursor.execute("""
                UPDATE orders
                SET total_price = ?, status = ?
                WHERE id_order = ?
            """, (new_total_price, status, id_order))
            self.connection.commit()
            return id_order
        # Insert new one
        self.cursor.execute("""
            INSERT INTO orders (id_user, date, total_price, status)
            VALUES (?, ?, ?, ?)
        """, (id_user, date, total_price, status))
        self.connection.commit()
        return self.cursor.lastrowid

    def update_order_status(self, order_id: int, new_status: int) -> int:
        """Met à jour le statut d'une commande.

        Args:
            order_id (int): L'identifiant de la commande.
            new_status (int): Le nouveau statut de la commande.

        Returns:
            int: Le nombre de lignes mises à jour.
        """
        self.cursor.execute("""
            UPDATE orders
            SET status = ?
            WHERE id_order = ?
        """, (new_status, order_id))
        self.connection.commit()
        return self.cursor.rowcount

    def add_order_in_item_list(self, id_order: int, id_order_item: int) -> int:
        """Ajoute une commande dans une liste d'articles.

        Args:
            id_order (int): L'identifiant de la commande.
            id_order_item (int): L'identifiant de l'article de commande.

        Returns:
            int: L'identifiant de l'ajout de la commande dans la liste d'articles.
        """
        self.cursor.execute("""
            INSERT INTO item_list (id_order, id_order_item)
            VALUES (?, ?)
        """, (id_order, id_order_item))
        self.connection.commit()
        return self.cursor.lastrowid

def main():
    """Fonction principale pour la classe OrderEntity."""
    order = OrderEntity()
    order.create_tables()

if __name__ == "__main__":
    main()
