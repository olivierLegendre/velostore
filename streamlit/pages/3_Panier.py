import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = "Velostore: Votre panier",
    page_icon="🚲"
)

st.write("# Votre Panier 🚲")

def get_one_bike():
    bike = dict()
    bike["brand"] = "rockrider"
    bike["description"] = "Oh, le joli velo"
    bike["price"] = 150
    bike["image"] = "A30M.jpg"
    bike["destination"] = "vtt"
    return bike

def get_one_item():
    # bike = st.session_state.bike_item
    bike = get_one_bike()
    nb_unit = 1
    # total_price = bike.brand.price * nb_unit
    total_price = 150
    order_item = dict()
    order_item["bike"] = bike
    order_item["nb_unit"] = nb_unit
    order_item["total_price"] = total_price
    return order_item
    
def get_order():
    date = "2025/05/21"
    total_price = 300
    order_item_list = list()
    order_item_list.append(get_one_item())
    order_item_list.append(get_one_item())
    order = dict()
    order["date"] = date
    order["total_price"] = total_price
    order["order_item_list"] = order_item_list
    return order
    
def display_order():
    order = get_order()
    df_order = create_order_dataframe(order)
    order_table = st.table(df_order)
    return order_table

def create_order_dataframe(order):
    bikes = [item.get("bike") for item in order["order_item_list"]]
    df_bike = pd.DataFrame(bikes)
    df_order_item = pd.DataFrame(order)
    df_order = pd.concat([df_order_item, df_bike], axis=1)
    df_order = df_order.drop(columns="order_item_list")
    return df_order

def main():
    display_order()

if __name__ == '__main__':
    main()