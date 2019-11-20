import pandas as pd
#import matplotlib.pyplot as plt
#import numpy as np

#for simplisity, I printed most of the statments so we could see what they do.

#you will need to change this to the file path that the file is saved.
printers=pd.read_csv('printers.csv')
location=pd.read_csv('IP List CVB.csv')

locIP=[]

printers["IP Address"]

#there was a weird empty last entry. this deletes it
printers.drop(printers.tail(1).index,inplace=True)

#creates a column named "Location IP", and then assigns the 3 octet in the IP address column to that value
#we will take this and we will link this to another table
def labelLocalIP(row):
    return row.split('.')[2]
printers['Location IP']=printers['IP Address'].apply(lambda row: labelLocalIP(row))

#gets you: a unique attribute, all the columns in the dataframe, and a unique row
#print(printers['Location IP'][0], printers.columns, printers.iloc[0])

#this gives the count of values in a specific column, in this case Location IP
#print(printers['Location IP'].value_counts())

#write out to a csv
#printers.to_csv('Matt.csv')


print(location['3rd Octet'],location['Branch'])

