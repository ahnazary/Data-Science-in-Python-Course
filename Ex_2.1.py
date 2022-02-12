import os

import pandas as pd
import scipy.stats as stats

projectPath = os.path.abspath(os.path.dirname(__file__))
path = projectPath + "/NISPUF17.csv"

df = pd.read_csv(path)


# function for question 1
def proportion_of_education():
    newDF = df['EDUC1']
    result = {}
    result["less than high school"] = len(newDF.where(df['EDUC1'] == 1).dropna()) / len(
        newDF.where((df['EDUC1'] >= 1) & (df['EDUC1'] <= 4)).dropna())
    result["high school"] = len(newDF.where(df['EDUC1'] == 2).dropna()) / len(
        newDF.where((df['EDUC1'] >= 1) & (df['EDUC1'] <= 4)).dropna())
    result["more than high school but not college"] = len(newDF.where(df['EDUC1'] == 3).dropna()) / len(
        newDF.where((df['EDUC1'] >= 1) & (df['EDUC1'] <= 4)).dropna())
    result["college"] = len(newDF.where(df['EDUC1'] == 4).dropna()) / len(
        newDF.where((df['EDUC1'] >= 1) & (df['EDUC1'] <= 4)).dropna())
    return result


# print(proportion_of_education())

# function for question 2
def average_influenza_doses():
    newDF = df[['P_NUMFLU', 'CBF_01']].dropna()
    result = (
        newDF.where(newDF['CBF_01'] == 1)['P_NUMFLU'].dropna().mean(),
        newDF.where(newDF['CBF_01'] == 2)['P_NUMFLU'].dropna().mean()
    )
    return result


# print(average_influenza_doses())

# function fro question 3
def chickenpox_by_sex():
    newDF = df[['HAD_CPOX', 'P_NUMVRC', 'SEX']].dropna()
    result = {}
    result['male'] = (
                len(newDF.where((newDF['SEX'] == 1) & (newDF['P_NUMVRC'] >= 1) & (newDF['HAD_CPOX'] == 1)).dropna()) /
                len(newDF.where((newDF['SEX'] == 1) & (newDF['P_NUMVRC'] >= 1) & (newDF['HAD_CPOX'] == 2)).dropna()))
    result["female"] = (
                len(newDF.where((newDF['SEX'] == 2) & (newDF['P_NUMVRC'] >= 1) & (newDF['HAD_CPOX'] == 1)).dropna()) /
                len(newDF.where((newDF['SEX'] == 2) & (newDF['P_NUMVRC'] >= 1) & (newDF['HAD_CPOX'] == 2)).dropna()))

    return result


# print(chickenpox_by_sex())

def corr_chickenpox():
    newDF = df[['HAD_CPOX', 'P_NUMVRC']].where((df['HAD_CPOX'] < 3)).dropna()
    corr, pval = stats.pearsonr(newDF["HAD_CPOX"], newDF["P_NUMVRC"])
    print(corr, pval)
    return float(corr)


print(corr_chickenpox())
