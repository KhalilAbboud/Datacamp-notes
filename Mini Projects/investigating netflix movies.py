# ===============================PROJECT 1:===============================
# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Start coding here! Use as many cells as you like

#filtering the 90s movies:
movies_from_90s = netflix_df[(netflix_df['release_year'] >= 1990) & 
                          (netflix_df['release_year'] < 2000)]

print(movies_from_90s)

#most frqnt duration, i bet like 92 93 minutes, anyway:
duration = movies_from_90s['duration'].mode()[0]

print(duration)

# output was 94 !!! almost got it

#count the quoteonquote 'short movies', less than 90 minutes

short_action_movies = netflix_df[(netflix_df['release_year'] >= 1990) & 
                          (netflix_df['release_year'] < 2000) & (netflix_df['genre'] == 'Action') & (netflix_df['duration'] < 90)]

short_movie_count = len(short_action_movies)
print(short_movie_count)
