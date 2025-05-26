import streamlit as st
import pandas as pd
import components

st.set_page_config(
    page_title = "Velostore: Vos commandes",
    page_icon="🚲"
)

st.write("# Vos Commandes 🚲")

def get_bike_one():
    bike = dict()
    bike["brand"] = "rockrider"
    bike["description"] = "Oh, le joli velo"
    bike["price"] = 150
    bike["img"] = "A30M.jpg"
    bike["destination"] = "vtt"
    return bike

def get_bike_two():
    bike = dict()
    bike["brand"] = "elios"
    bike["description"] = "Plus detente"
    bike["price"] = 120
    bike["img"] = "A30M.jpg"
    bike["destination"] = "route"
    return bike

def get_item_one():
    # bike = st.session_state.bike_item
    bike = get_bike_one()
    nb_unit = 2
    # total_price = bike.brand.price * nb_unit
    total_price = 300
    order_item = dict()
    order_item["bike"] = bike
    order_item["nb_unit"] = nb_unit
    order_item["total_price"] = total_price
    return order_item

def get_item_two():
    # bike = st.session_state.bike_item
    bike = get_bike_two()
    nb_unit = 1
    # total_price = bike.brand.price * nb_unit
    total_price = 120
    order_item = dict()
    order_item["bike"] = bike
    order_item["nb_unit"] = nb_unit
    order_item["total_price"] = total_price
    return order_item
    
def get_order():
    date = "2025/05/21"
    total_price = 300
    order_item_list = list()
    order_item_list.append(get_item_one())
    order_item_list.append(get_item_two())
    order = dict()
    order["date"] = date
    order["total_price"] = total_price
    order["order_item_list"] = order_item_list
    return order

def get_old_orders():
    old_orders = list()
    date = "2024/05/21"
    total_price = 300
    order_item_list = list()
    order_item_list.append(get_item_one())
    order_item_list.append(get_item_two())
    order = dict()
    order["date"] = date
    order["total_price"] = total_price
    order["order_item_list"] = order_item_list
    date = "2024/05/18"
    total_price = 200
    order_item_list = list()
    order_item_list.append(get_item_two())
    order_item_list.append(get_item_one())
    order2 = dict()
    order2["date"] = date
    order2["total_price"] = total_price
    order2["order_item_list"] = order_item_list
    old_orders.append(order)
    old_orders.append(order2)
    return old_orders
    


def main():
    components.display_sidebar()
    components.display_pending_order()
    components.display_closed_order()

if __name__ == '__main__':
    main()