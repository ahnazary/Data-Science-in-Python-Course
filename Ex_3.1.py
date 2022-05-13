import pandas as pd
import numpy as np

# Filter all warnings. If you would like to see the warnings, please comment the two lines below.
import warnings

warnings.filterwarnings('ignore')
# pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df = pd.read_excel('Energy Indicators.xls')
df.rename({'Unnamed: 0': 'Country'})
df = df.drop(df.index[0:17]).drop(df.index[243:]).drop(['Unnamed: 0', 'Unnamed: 2'], axis=1)
df.rename(columns={'Unnamed: 1': "Country", 'Unnamed: 3': "Energy Supply", 'Unnamed: 4': "Energy Supply per Capita",
                   'Unnamed: 5': "% Renewable"}, inplace=True, errors='raise')
tempDict = {"Republic of Korea": "South Korea",
            "United States of America": "United States",
            "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
            "China, Hong Kong Special Administrative Region": "Hong Kong"}
df = df.replace(to_replace='...', value=np.NAN).replace({'Country': tempDict}).replace(to_replace='Switzerland17',
                value='Switzerland').replace(to_replace='Bolivia (Plurinational State of)', value='Bolivia')
# df = df['Energy Supply']*1000000

print(df)
