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
# # print(test)
# import numpy as np 
# x=np.array([1,3,5,7,9])
# y=np.array([2,4,4,8,10])

# correlation_matrix=np.corrcoef(x,y)

# print(correlation_matrix)
from getData import gitAdvData
import numpy as np
import util


advDF=gitAdvData()
years=util.uniqueYears(advDF['Season Year'])
correlationsORB=util.getCorrelationValues(advDF,years,'ORtg','ORB%')
correlationsDRB=util.getCorrelationValues(advDF,years,'DRtg','DRB%')
print(correlationsORB)
print(correlationsDRB)

