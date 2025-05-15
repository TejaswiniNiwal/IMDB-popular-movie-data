# Importing necessary libraries
import csv,requests
import pandas as pd
import streamlit as st


class api_extracter:
    # create instance attributes
    def __init__(self):
        self.api_key = st.secrets["API_KEY"]
    
    def get_data(self):

        url = "https://imdb232.p.rapidapi.com/api/title/get-most-popular"

        querystring = {"limit":"20","topMeterTitlesType":"ALL"}

        headers = {
            "x-rapidapi-key": self.api_key,
            "x-rapidapi-host": "imdb232.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        api_data = response.json()

        nodes = api_data.get('data',{}).get('topMeterTitles',{}).get('edges',{})
        popular_movie_data = []
        for nd in nodes:
            node = nd.get('node',{})
            title = node.get('titleText',{}).get('text',{})
            year = node.get('releaseYear',{}).get('year',{})
            ranks = node.get('meterRanking',{}).get('currentRank',{})
            #print(title,year,ranks)
            popular_movie_data.append([title,year,ranks])
        
        return popular_movie_data
    
    def save_data(self):
        with open("Top_movies.csv","w",encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Movie Titles","Release Year","Rank"]) # represents the column names
            writer.writerows(popular_movie_data) # represents rows of data being inserted
        print("File is saved successfully")