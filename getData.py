import pandas as pd

def gitAdvData():
    df = pd.read_csv('https://raw.githubusercontent.com/ZaatiniY/nbaDash/main/advanced_team_r.csv')
    input(df['Season Year'])
    return df

