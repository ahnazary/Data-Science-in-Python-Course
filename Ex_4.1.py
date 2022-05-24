import pandas as pd
import re

# pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

mlb = pd.read_csv('mlb.csv')
nba = pd.read_csv('nba.csv')
nfl = pd.read_csv('nfl.csv')
nhl = pd.read_csv('nhl.csv')
cities = pd.read_csv('wikipedia_data.csv')


nhl.drop(nhl.index[0], inplace=True)


nhl['Metropolitan area'] = nhl['team'].apply(lambda x: (re.split(' [^ ]*$', x)[0]).replace('*', ""))
nhl['team'] = nhl['team'].apply(lambda x: re.split('^.* ', x)[-1].replace('*', ""))

nhl.at['San Francisco Bay Area'] = 'San Jose'
print(cities)
cities.at[9, 'Metropolitan area'] = 'Minnesota'
cities.at[9, 'NHL'] = 'Minnesota Wild'

nhl.set_index('Metropolitan area', inplace=True)
cities.set_index('Metropolitan area', inplace=True)


newDf = cities.merge(nhl, how='inner', left_index=True, right_index=True)

newDf = newDf[newDf.year == 2018]

# print(newDf[['team', 'NHL', 'W', 'L']], newDf[['team', 'NHL', 'W', 'L']].shape)
