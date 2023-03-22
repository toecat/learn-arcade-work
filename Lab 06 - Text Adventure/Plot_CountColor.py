#Looking at the Shiny Diamonds

#import the pandas and numpy libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#read the diamonds CSV file
#build a DataFrame from the data
df = pd.read_csv('Lab 06 - Text Adventure/diamonds.csv')

#count the number of each textual type of color
colorindexes = df['color'].value_counts().index.tolist()
colorcount = df['color'].value_counts().values.tolist()

print(colorindexes)
print(colorcount)

plt.bar(colorindexes, colorcount)
plt.show() #or plt.savefig("name.png")