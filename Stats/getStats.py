import pandas as pd
import pprint as pp
import json

printers=pd.read_csv('CleanedData/removedNullsPrinter.csv')
print(printers)

#get some stats
printers.describe()

stats=printers.describe()
#write out those stats to a csv an exsisting one or creates on with the given name
stats.to_csv('CleanedData/stats.csv')

#gets the stats for a specific column
ModelStats=printers.groupby(['Model']).describe()

#gets the stats for specific columns
columns=['Model','Location','Manufacturer','Is Managed']
bigStats={}
for x in printers.columns:
    name=''
    if x in columns:
        name+=(x+'Stats').replace(' ','')
        bigStats[name]=printers.groupby([x]).describe()
#then writes each of those to a csv file
for x in bigStats:
    print(x)
    bigStats[x].to_csv(x+'.csv')

pp.pprint(bigStats)



"""
we want to find stats for:
Model
Location
Manufacturer
Is Managed

columns=['Model','Location','Manufacturer','Is Managed']
goodStats={}
for x in printers.columns:
    if x in columns:
        printers.groupby([x]).sum()['Total Cost']
        printers.groupby([x]).mean()['Total Cost']
        printers.groupby([x]).sum()['Total Cost'] 
"""
