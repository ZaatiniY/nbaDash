import graph
import pandas as pd 
import util

# def makeORBSelection(relevantYears,menuItems):
#     menuOptions=[]
#     for year in relevantYears:
#         menuOptions.append({item:year for item in menuItems})
#     return menuOptions

# relevantYears=['01','02','03']
# test=makeORBSelection(relevantYears,menuItems=['label','value'])
# print(test)

def makeRBCorrelations():
    advDF=graph.gitAdvData()
    relevantYears = util.uniqueYears(advDF['Season Year'])
    input(relevantYears)
    DRBSlopes=[]
    ORBSlopes=[]
    for year in relevantYears:
        print(year)
        currDF = advDF.copy()
        currDF=currDF.loc[advDF['Season Year']==year]
        input(DRBSlopes)
        input(ORBSlopes)
        DRBSlopes=util.assignRegSlopeValue(currDF,'DRtg','DRB%',DRBSlopes)
        ORBSlopes=util.assignRegSlopeValue(currDF,'ORtg','ORB%',ORBSlopes)
        print(DRBSlopes)
        print(ORBSlopes)

makeRBCorrelations()