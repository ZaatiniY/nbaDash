import pandas
import numpy as np

#uniqueYears removes repeated years in a dataframe and returns a list of unique years that can be used in analysis
#Parameters:
#   seasonYearsColumns (Series) -> Series with unique or repeat containing years 
#Return: keep (list) -> final unique value from your input 
def uniqueYears(seasonYearsColumns):
    found = set()
    keep = []
    for year in seasonYearsColumns:
        if year not in found:
            found.add(year)
            keep.append(year)
    return keep



def calcAvgYearlyStat(targetDF, years, columnName):
    averagedData = list()
    for year in years:
        currYearFiltered = targetDF.loc[targetDF['Season Year']==year]
        sumOfStat = currYearFiltered[columnName].sum()
        numberOfDataPoints = len(currYearFiltered[columnName]) 
        averageValue = round(sumOfStat/numberOfDataPoints,1)
        averagedData.append(averageValue)
    return averagedData



def linearRegCalc(xValue,yValue):
    slope,y_int = np.polyfit(xValue,yValue,1)
    return (slope,y_int)

def assignRegSlopeValue(df,xColumn,yColumn,container):
    input(f"This is container - {container}")
    linearRegStats=linearRegCalc(df[xColumn],df[yColumn])
    input(container.append(linearRegStats[0]))
    return container.append(linearRegStats[0])
