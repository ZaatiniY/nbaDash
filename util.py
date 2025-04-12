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

def assignRegSlopeValue(df,Years,xColumn,yColumn,container):
    for year in Years:
        currDF = df.copy()
        seasonDF=currDF.loc[currDF['Season Year']==year]
        linearRegStats=linearRegCalc(seasonDF[xColumn],seasonDF[yColumn])
        container.append(round(linearRegStats[0],2))
    return container

def getCorrelationValues(DF,Years,XColName,YColName):
    corrValues=[]
    for year in Years:
        currSeasonDF=DF.loc[DF['Season Year']==year]
        coefMatrix=np.corrcoef(currSeasonDF[XColName],currSeasonDF[YColName])
        coefValue=round(coefMatrix[0,1],2)
        corrValues.append(coefValue)
    return corrValues
