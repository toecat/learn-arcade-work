#Diamonds are a Data Scientist's Best Friend
#import the pandas and numpy libraries
import numpy as np
import pandas as pd
#read the diamonds CSV file
#build a DataFrame from the data
df = pd.read_csv('Lab 06 - Text Adventure/diamonds.csv')
print(df.head(10))
print()
#calculate the total value of the diamonds
sum = df.price.sum()
print("Total $ Value of Diamonds: ${:0,.2f}".format( sum))
#calculate the mean price of the diamonds
mean = df.price.mean()
print("Mean $ Value of Diamonds: ${:0,.2f}".format(mean))
#summarize the data
descrip = df.carat.describe()
print()
print(descrip)
descrip = df.describe(include='object')
print()
print(descrip)