
import numpy as np
import pandas as pd

anime = pd.read_csv("anime.csv")
items = np.array(anime.genre)

genres = input("Ps: keep the first letter as Capital \n Enter the genre: " )

val = [(genres in str(item)) for item in items]

X = anime.loc[val]
X_mod = X[['name', 'genre', 'type', 'episodes', 'rating']]

print(X_mod.head())
