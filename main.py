import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/cwkteacher/Data/master/movie_metadata.csv')

# fig = plt.figure()
# x = np.arange(6)
# y = np.arange(6)
# plt. plot(x, y)
# plt.xlabel("Number of Doughnuts eaten")
# plt.ylabel("Miles unicycled")
# plt.title("Correlation does not equal causation")
# fig.savefig("THE_PLOT.png")

fig = plt.figure(figsize=(11,8))

actor = df.groupby(['actor_1_name'])['actor_1_facebook_likes'].sum()
actor = actor.sort_values(ascending=False)
print(actor.head(10))
actor[:10].plot(kind="barh")
plt.xlabel("facebook Likes")
plt.ylabel("Actors")
plt.title("10 Actors with the Most Facebook Likes")
fig.savefig('actor.png')

fig = plt.figure()

# number of movies made by each director
num_movies = df['director_name'].value_counts()[:15]
print(num_movies)
num_movies.plot(kind="barh")
fig.savefig('num_movies')