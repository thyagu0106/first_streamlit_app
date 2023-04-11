
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

# Create the repeatable code block (Function)
def get_fruityvice_data(this_fruit_choice):
	fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
	fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
	return fruityvice_normalized


try:
	fruit_choice = streamlit.text_input('What fruit would you like information about?')
	if not fruit_choice:
		streamlit.error("Please select a fruit of your choice to get information!")
	else:
		back_from_function = get_fruityvice_data(fruit_choice)
		streamlit.dataframe(back_from_function)
except URLError as e:
	streamlit.error()
  
#streamlit.stop()
#Snowflake Related functions
def get_fruit_load_list():
	with my_cnx.cursor() as my_cur:
		my_cur.execute("select * from fruit_load_list")
		return my_cur.fetchall()
# Add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
	my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
	my_data_rows = get_fruit_load_list()
	streamlit.dataframe(my_data_rows)
	
# Allow End users to add fruit to the list
def insert_row_snowflake(new_fruit):
	with my_cnx.cursor() as my_cur:
		my_cur.execute("insert into fruit_load_list values ('add_my_fruit')")
		return "Thanks for adding " + new_fruit
		

add_my_fruit = streamlit.text_input('What fruit would like to add?')
if stremlit.button("Add a Fruit to the list'):
		   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
		   back_from_function = insert_row_snowflake(add_my_fruit)
		   stremlit.text(back_from_function)
		   
		   

