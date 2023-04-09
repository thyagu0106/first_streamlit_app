
import streamlit
streamlit.header('Aasini Achivements')
streamlit.title('Aasini-First Robotic projects')
streamlit.title('She won Best team award')
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
 
import pandas
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
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.header('Fruitvice Advice!')
# streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
