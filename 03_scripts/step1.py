import numpy as np
import pandas as pd

df = pd.read_csv("../01_data/IMDB top 1000.csv")
data_array = df[["Title", "Genre", "Rate"]].to_numpy()

print(data_array)
