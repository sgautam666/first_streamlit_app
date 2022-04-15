import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Bluberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boild Free-Range Egg')
streamlit.text('Avocado Toast')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Fruit pick lists
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# display the table on the page
streamlit.header('Build Your Own Fruit Smoothie')
streamlit.dataframe(my_fruit_list)
