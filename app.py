# Importing necessary packages
import streamlit as st
import pandas as pd
from utils import api_extracter

# create an instance of class api_extracter
client = api_extracter()

# create a webpage browser title
st.set_page_config(page_title="IMDB Popular Movies",layout="wide")

# create a title for webpage
st.title("20 Most Popular Movies extracted from IMDB website")

# create a subheading mentioning your name
st.subheader("By Tejaswini Niwal")

# create  a button which when clicked,will display the content to the user
ip_button = st.button("20most popular movies")
if ip_button:
    # get the movies list data from client.get_data method
    data = client.get_data()
    # convert the data received into a dataframe
    df = pd.DataFrame(data,columns=["Movie Titles","Release Year","Rank"])
    # display above dataframe via st.dataframe
    st.dataframe(df)

   