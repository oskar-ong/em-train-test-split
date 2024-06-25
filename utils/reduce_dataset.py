import pandas as pd 

file_path = 'data/raw/musicbrainz-20-A01.csv.dapo'

df= pd.read_csv(file_path)

columns_to_drop = df.columns[[3, 4, 5, 7, 9, 10, 11]]

df = df.drop(columns_to_drop, axis = 1)

df.set_index('TID', inplace=True)

df.to_csv('./data/interim/musicbrainz-reduced.csv')