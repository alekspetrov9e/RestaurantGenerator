import streamlit as st
import langchain_tutorial


st.title("Restaurant Name Generator")

cuisine = (
    st.sidebar.selectbox("Pick a Cuisine",
                     ("Indian","Italian", "Bulgarian",
                      "French", "Mexican", "Japanese",
                      "German")))



if cuisine:
    response = langchain_tutorial.generate_restaurant_name_and_items(cuisine)
    st.header(response["restaurant_name"].strip())
    menu_items = response["menu_items"].strip().split(",")
    st.write("Menu Items")

    for item in menu_items:
        st.write("-", item)