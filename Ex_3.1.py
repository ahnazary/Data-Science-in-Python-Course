import pandas as pd
import numpy as np
import matplotlib as plt

# Filter all warnings. If you would like to see the warnings, please comment the two lines below.
import warnings

warnings.filterwarnings('ignore')

pd.set_option('display.max_columns', None)


# pd.set_option('display.max_rows', None)


def answer_one():
    global ScimEn, GDP, Energy
    Energy = pd.read_excel('Energy Indicators.xls')
    Energy.rename({'Unnamed: 0': 'Country'})
    Energy = Energy.drop(Energy.index[0:17]).drop(Energy.index[243:]).drop(['Unnamed: 0', 'Unnamed: 2'], axis=1)
    Energy.rename(
        columns={'Unnamed: 1': "Country", 'Unnamed: 3': "Energy Supply", 'Unnamed: 4': "Energy Supply per Capita",
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

    ScimEn = pd.read_excel('scimagojr country rank 1996-2021.xlsx')
    ScimEn = ScimEn[
        ['Rank', 'Country', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document',
         'H index']]
    # print(ScimEn)

    tempDict = {"Korea, Rep.": "South Korea",
                "Iran, Islamic Rep.": "Iran",
                "Hong Kong SAR, China": "Hong Kong"}
    GDP = pd.read_csv('API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4019306.csv', skiprows=[0, 1, 2, 3])
    GDP = GDP.replace({'Country Name': tempDict})
    GDP = GDP[['Country Name', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]
    GDP.rename(columns={'Country Name': 'Country'}, inplace=True)
    # print(GDP)

    result = ScimEn.merge(Energy, on='Country', how='left').merge(GDP, on='Country', how='left').iloc[0:15]
    result.set_index('Country', inplace=True)
    return result


answer_one()


# print(type(answer_one()) == pd.DataFrame)
# print(answer_one().shape == (15, 20))


def answer_two():
    allEntries = ScimEn.merge(Energy, on='Country', how='inner').merge(GDP, on='Country', how='inner')
    allEntries.set_index('Country', inplace=True)
    return (allEntries.shape[0] - answer_one().shape[0]) + 2


# print(answer_two())

def answer_three():
    result = answer_one()[['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]
    return result.mean(axis=1, skipna=True).sort_values(ascending=False)


# print(type(answer_three()) == pd.Series)

def answer_four():
    sixthLargest = answer_three().index[5]
    return answer_one().loc[sixthLargest][19] - answer_one().loc[sixthLargest][10]


def answer_five():
    return answer_one()['Energy Supply per Capita'].mean()


# print(answer_five())

def answer_six():
    temp = answer_one()['% Renewable'].sort_values(ascending=False)
    return (temp.index[0], temp[0])


# print(answer_six())

def answer_seven():
    res = (answer_one()['Self-citations'] / answer_one()['Citations']).sort_values(ascending=False)
    return (res.index[0], res[0])


# print(answer_seven())

def answer_eight():
    res = (answer_one()['Energy Supply'] / answer_one()['Energy Supply per Capita']).sort_values(ascending=False)
    print(res)
    return res.index[2]

# print(answer_eight())

def answer_nine():
    Top15 = answer_one()
    se = Top15['Citable documents'] / (Top15['Energy Supply'] / Top15['Energy Supply per Capita'])
    ans = se.corr(Top15['Energy Supply per Capita'])
    return ans

# print(answer_nine())

def answer_ten():
    tempDf = answer_one()
    med = tempDf['% Renewable'].median()
    tempDf['newcol'] = tempDf['% Renewable'].apply(lambda x: 1 if x >= med else 0)
    tempRank = tempDf['Rank']
    for index in tempRank.index:
        tempRank[index] = tempDf['newcol'].loc[index]
    return tempRank
# print(answer_ten())

def answer_eleven():
    ContinentDict = {'China': 'Asia',
                     'United States': 'North America',
                     'Japan': 'Asia',
                     'United Kingdom': 'Europe',
                     'Russian Federation': 'Europe',
                     'Canada': 'North America',
                     'Germany': 'Europe',
                     'India': 'Asia',
                     'France': 'Europe',
                     'South Korea': 'Asia',
                     'Italy': 'Europe',
                     'Spain': 'Europe',
                     'Iran': 'Asia',
                     'Australia': 'Australia',
                     'Brazil': 'South America'}
    Top15 = answer_one()
    df = pd.DataFrame(list(ContinentDict.items()), columns=['Country', 'Continent']).set_index('Country')
    print(type(df))
    df = df.merge((Top15['Energy Supply'] / Top15['Energy Supply per Capita']).rename('popEst'), left_index=True, right_index=True)
    res = df.groupby(['Continent']).agg(size=('popEst', 'size'), sum=('popEst', 'sum'), mean= ('popEst', 'mean'),  std= ('popEst', 'std'))
    return res


print(answer_eleven())
