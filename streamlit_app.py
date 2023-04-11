
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.header('Aasini Achivements')
streamlit.title('Aasini-First Robotic projects')
streamlit.title('She won Best Design,Amaze,Excellence awards')
streamlit.title('Aasini selected for State compitition')
streamlit.title('Aasini went to Iowa to compete')
streamlit.title('Aasini select for world compitition')
streamlit.title('Aasini going to Dallas for world Championship !!')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.header('🥑Breakfast Menu🥑')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal🍞')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg 🐔 ')
streamlit.header('Import your own fruit List')
 

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Cantaloupe','Lemon'])
fruits_to_show = my_fruit_list.loc[fruits_selected]


# Display the table on the page.
streamlit.dataframe(my_fruit_list)
streamlit.header('Selected Fruits...')
streamlit.dataframe(fruits_to_show)

# import Python packasge


# streamlit.text(fruityvice_response.json())
streamlit.header('Fruitvice Fruit Advice!')
try:
 fruit_choice = streamlit.text_input('What fruit would you like information about?')
 if not fruit_choice:
  streamlit.error("Please select a fruit of your choice to get information!")
 else:
  streamlit.write('The user entered ', fruit_choice)
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)    
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  streamlit.dataframe(fruityvice_normalized)
  
 except URLError as e:
  streamlit.error()
  
streamlit.stop()


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
my_fruit = my_cnx.cursor()
my_fruit.execute("SELECT * from fruit_load_list")
my_data_row = my_fruit.fetchall()
streamlit.text("Fruit List:")
streamlit.dataframe(my_data_row)

# import streamlit as st

add_my_fruit = streamlit.text_input('What fruit would like to add?', 'Koyya')
streamlit.write('Added fruit is', add_my_fruit)
my_cur.execute("insert into fruit_load_list values ('add_my_fruit')")
