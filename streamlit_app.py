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
streamlit.dataframe(my_fruit_list)
