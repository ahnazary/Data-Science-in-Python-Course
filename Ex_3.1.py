import pandas as pd
import numpy as np

# Filter all warnings. If you would like to see the warnings, please comment the two lines below.
import warnings

warnings.filterwarnings('ignore')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

def answer_one():
    Energy = pd.read_excel('Energy Indicators.xls')
    Energy.rename({'Unnamed: 0': 'Country'})
    Energy = Energy.drop(Energy.index[0:17]).drop(Energy.index[243:]).drop(['Unnamed: 0', 'Unnamed: 2'], axis=1)
    Energy.rename(columns={'Unnamed: 1': "Country", 'Unnamed: 3': "Energy Supply", 'Unnamed: 4': "Energy Supply per Capita",
                           'Unnamed: 5': "% Renewable"}, inplace=True, errors='raise')
    tempDict = {"Republic of Korea": "South Korea",
                "United States of America": "United States",
                "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
                "China, Hong Kong Special Administrative Region": "Hong Kong",
                "Iran (Islamic Republic of)": 'Iran'}
    Energy = Energy.replace(to_replace='...', value=np.NAN).replace({'Country': tempDict}).replace(
        to_replace='Switzerland17',
        value='Switzerland').replace(to_replace='Bolivia (Plurinational State of)', value='Bolivia')
    Energy['Energy Supply'] = Energy['Energy Supply'].apply(lambda x: x * 1000000)
    # print(Energy)

    ScimEn = pd.read_excel('scimagojr country rank 1996-2021.xlsx')
    ScimEn = ScimEn[['Rank', 'Country', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index']]
    # print(ScimEn)

    tempDict = {"Korea, Rep.": "South Korea",
                "Iran, Islamic Rep.": "Iran",
                "Hong Kong SAR, China": "Hong Kong"}
    GDP = pd.read_csv('API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4019306.csv', skiprows=[0,1,2,3])
    GDP = GDP.replace({'Country Name': tempDict})
    GDP = GDP[['Country Name', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]
    GDP.rename(columns={'Country Name': 'Country'}, inplace=True)
    # print(GDP)

    result = ScimEn.merge(Energy, on='Country', how='left').merge(GDP, on='Country', how='left').iloc[0:15]
    result.set_index('Country', inplace=True)
    return result

print(answer_one())
print(type(answer_one()) == pd.DataFrame)
print(answer_one().shape == (15,20))