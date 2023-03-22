#Looking at the Shiny Diamonds

#Import the pandas and numpy libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#read the diamonds CSV file
#build a DataFrame from the data
df = pd.read_csv('Lab 06 - Text Adventure/diamonds.csv')

carat = df.carat
clarity = df.clarity
for i in range(20):
    print(df.iloc[i].clarity)
plt.scatter(clarity, carat)
plt.show() #or plt.savefig("name.svg")