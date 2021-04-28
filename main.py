import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/cwkteacher/Data/master/movie_metadata.csv')

print(df.head(5))
print(df.columns)

print(df['movie_title'])

cols = ['movie_title', 'facenumber_in_poster']
print(df[cols])

#

rating = df[df['imdb_score'] > 7.5]
print(rating[['movie_title', 'imdb_score']])

