import streamlit
import pandas
import requests
import snowflake.connector

streamlit.header('Breakfast Menu')

streamlit.text('🐔 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥑🍞 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥣 🥗 Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')



my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

streamline.header("Fruityvice Fruit Advice!")
try:
   fruit_choice = streamline.text_input("What fruit would you like information about?")
   if not fruit_choice:
	streamline.error(“Please select a fruit to get information.”)
   else:
	back_from_function = get_fruityvice_data(fruit_choice)
	streamlet.dataframe(back_from_function)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_row)
fruit_choice = streamlit.text_input('What fruit would you like to add','Jackfruit')
streamlit.write('The user entered ', fruit_choice)

streamlit.write('Thanks for adding' , fruit_choice)
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
