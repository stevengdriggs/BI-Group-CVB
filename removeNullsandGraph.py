import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np

#for simplisity, I printed most of the statments so we could see what they do.

#you will need to change this to the file path that the file is saved.
printers=pd.read_csv('printerListwithCost.csv')

#removes any null values in the "Total Pages" column
printers=printers.dropna(axis=0,subset=['Total Pages'])

#get the descriptive stats and print them out to a csv file
printers.describe().to_csv('stats.csv')

#Here is my locaiton CSV, not sure if I still need this
location=pd.read_csv('IP List CVB.csv')

#gets you: a unique attribute, all the columns in the dataframe, and a unique row
#print(printers['Location IP'][0], printers.columns, printers.iloc[0])

#this gives the count of values in a specific column, in this case number of printers at each Location
printers['Location'].value_counts()

#this will get the mean of each of the columns grouped by Location
means=printers.groupby(['Location']).mean()

sorted_by_total_cost=printers.sort_values(['Total Cost'],ascending=False)
sorted_by_mono_cost=printers.sort_values(['Total Cost Mono'],ascending=False)
sorted_by_color_cost=printers.sort_values(['Total Cost Color'],ascending=False)

#now lets graph some stuff
sorted_by_total_cost['Total Cost Color'].T.plot.bar()
plt.show()

print(location['3rd Octet'],location['Branch'])

