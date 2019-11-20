import pandas as pd
import datetime as dt

"""
This program is designated to clean the meter reports spreadsheet and convert it into a csv file that has the data only. 
Looks pretty good and works ok, needs some tweaks probably
"""

passed=False
print(f'This is a specified cleaning script for Cache Valley Bank reports as given to us by Lee Olsen Company')
while passed !=True:
    sourceFile=input("What is the name of your file you want?\n"
                     "Don't forget the extension (.xlsx or .csv)\n")
    try:
        if sourceFile[-3:]=='csv':
            meter=pd.read_csv(f'{sourceFile}')
            passed = True
        elif sourceFile[-4:]=='xlsx':
            meter=pd.read_excel(f'{sourceFile}')
            passed = True
        else:
            print(f'{sourceFile} is not a valid name. Please use .xlsx or .csv files.\n'
                  f'Please try again.')
    except FileNotFoundError:
        print(f'{sourceFile} is not found. Please check your working directory and verify the spelling of the file')


#this stores the date the report was run
date=meter.head(1).loc[0][1]

#starting date
reportStartDate=meter.loc[4][1].split('-')[0].split(' ')[0]
#converts it to date time
reportStartDate=dt.datetime.strptime(reportStartDate,'%m/%d/%Y')
#ending date
reportEndDate=meter.loc[4][1].split('-')[0].split(' ')[2]
#converts to datetime
reportEndDate=dt.datetime.strptime(reportEndDate,'%m/%d/%Y')

#find where the data actuall starts
headerRows=0
for x in range(len(meter)):
    if meter.loc[x][0]=="Account":
        headerRows=x
        break


#the first {headerRows} of rows are header info, for the analysis we don't need them.
costData=meter.drop(range(0,headerRows))

#this should make the first row the new headers
costData.columns=meter.loc[headerRows]

#removes the top row I am not a professional, but this is not changing the index,
#you still need to start at row headerRows+1 to reference stuff
costData=costData.drop(headerRows)

#this gets rid of the last row (there is a total column)
#Use a.empty, a.bool(), a.item(), a.any() or a.all().
if str(costData.loc[costData.tail(1).index]['Account'].item())=='nan':
    costData=costData.drop(costData.tail(1).index)
else:
    pass

#default name is start date-end date
#read it out to a new file
costData.to_csv(str(reportStartDate.strftime('%b-%d-%y')+ ' to ' +reportEndDate.strftime('%b-%d-%y') + '.csv'))

