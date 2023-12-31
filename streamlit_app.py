import streamlit;
import pandas;
import requests;
import snowflake.connector
from urllib.error import URLError

streamlit.title("My Parents' new healthy diner");
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast');

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice);
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json());
    return fruityvice_normalized;
  
streamlit.header("Fruityvice Fruit Advice!")
#streamlit.text(fruityvice_response.json())

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?');
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else:
    streamlit.write('The user entered ', fruit_choice);
    back_from_def=get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_def);
except URLerror as e:
  streamlit.error()



def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * from fruit_load_list")
        my_data_rows = my_cur.fetchall()
        return my_data_rows

streamlit.header("The fruit load list contains:")
if streamlit.button("Get Fruit list"):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list();
    my_cnx.close();
    streamlit.dataframe(my_data_rows)


def add_fruit_to_list(fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values ('"+fruit+"')")
        return 'Thanks for adding '+ add_fruit;


add_fruit = streamlit.text_input('Which fruit would you like to add?','jackfruit');
if streamlit.button("Add a fruit to list"):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_def = add_fruit_to_list(add_fruit)
    my_cnx.close();
    streamlit.write(back_from_def);
    
    
   







