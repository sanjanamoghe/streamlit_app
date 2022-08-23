import streamlit
import pandas

streamlit.title('Welcome to the Healthy Diner!')
streamlit.header('Menu')
streamlit.text('🥑 Avocado smoothie')
streamlit.text('🐔 Chicken salad')
streamlit.text('🐔 Egg White Omlette')
streamlit.text('🥗 Caesar salad')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show=fruits_selected.loc[fruits_selected]

streamlit.dataframe(my_fruit_list)
