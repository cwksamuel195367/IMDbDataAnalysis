import pandas as pd

df=pd.read_csv('https://raw.githubusercontent.com/cwkteacher/Data/master/movie_metadata.csv')

print(df.head(5))
print(df.columns)

print(df['movie_title'])