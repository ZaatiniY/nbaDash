def makeORBSelection(relevantYears,menuItems):
    menuOptions=[]
    for year in relevantYears:
        menuOptions.append({item:year for item in menuItems})
    return menuOptions

relevantYears=['01','02','03']
test=makeORBSelection(relevantYears,menuItems=['label','value'])
print(test)