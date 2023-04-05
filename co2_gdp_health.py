# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 17:22:17 2023

@author: ASWANY SHAJI
"""

import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

def read_clean_transpose(filename):
    data_frame = pd.read_excel(filename)
    data_frame.set_index('Country Name', inplace =True)
    data_frame.drop(labels = ['Country Code', 'Indicator Name', 'Indicator Code'], axis = 1, inplace = True)
    data_frame.dropna(axis=0,how='all',thresh=None, subset=None, inplace=True)
    data_frame.dropna(axis=1,how='all',thresh=None, subset=None, inplace=True)
    clean_df_transpose = data_frame.transpose()
    clean_df_transpose = clean_df_transpose.rename_axis('Year') 
    return data_frame, clean_df_transpose

def co2_emission_trend(df):
    top_five = df.loc[['China', 'United States', 'India', 'Japan', 'Germany']]
    top_five_year =top_five.loc[:, ["2005", "2010", "2015", "2019"]]
    print(top_five_year)
    top_five_year.plot(kind ='bar',)
    plt.title("CO2 EMISSION TREND OF TOP 5 COUNTRIES")
    plt.ylabel("CO2 EMISSION (Kilo tonnes)")
    plt.xlabel("COUNTRY")
    
def gdp_growth_trend(df):
    top_five = df.loc[['China', 'United States', 'India', 'Japan', 'Germany']]
    top_five_year =top_five.loc[:, ["2005", "2010", "2015", "2019"]]
    print(top_five_year)
    top_five_year.plot(kind ='bar',)
    plt.title("GDP GROWTH TREND OF TOP CARBON EMITTING COUNTRIES")
    plt.ylabel("GDP GROWTH")
    plt.xlabel("COUNTRY")
    

def statistics_comparison():
    indicator_comparison = pd.read_excel("statistics1.xlsx")
    statistics_description = indicator_comparison.groupby('Country Name')[["Life expectancy","Mortality rate","Current health expenditure"]].describe()
    statistics_median = indicator_comparison.groupby('Country Name')[["Life expectancy","Mortality rate","Current health expenditure"]].median()
    statistics_description.to_excel("statistics_description.xlsx")
    world_indicators = indicator_comparison[indicator_comparison['Country Name'] == 'World']
    china_indicators = indicator_comparison[indicator_comparison['Country Name'] == 'China']
    india_indicators = indicator_comparison[indicator_comparison['Country Name'] == 'India']

    print(stats.skew(world_indicators["Life expectancy"]))
    print(stats.skew(world_indicators["Current health expenditure"]))
    print(stats.skew(world_indicators["Mortality rate"]))
    print(stats.skew(china_indicators["Life expectancy"]))
    print(stats.skew(china_indicators["Current health expenditure"]))
    print(stats.skew(china_indicators["Mortality rate"]))
    print(stats.skew(india_indicators["Life expectancy"]))
    print(stats.skew(india_indicators["Current health expenditure"]))
    print(stats.skew(india_indicators["Mortality rate"]))
    print(stats.kurtosis(world_indicators["Life expectancy"]))
    print(stats.kurtosis(world_indicators["Current health expenditure"]))
    print(stats.kurtosis(world_indicators["Mortality rate"]))
    print(stats.kurtosis(china_indicators["Life expectancy"]))
    print(stats.kurtosis(china_indicators["Current health expenditure"]))
    print(stats.kurtosis(china_indicators["Mortality rate"]))
    print(stats.kurtosis(india_indicators["Life expectancy"]))
    print(stats.kurtosis(india_indicators["Current health expenditure"]))
    print(stats.kurtosis(india_indicators["Mortality rate"]))
    
def correlation_analysis(filename):
    correlation_data = pd.read_excel(filename)
    pear_corr=correlation_data.corr(method='pearson')
    fig, ax = plt.subplots(figsize=(8,8))
    im = ax.imshow(pear_corr, cmap = 'spring', interpolation='nearest')
    fig.colorbar(im, orientation='vertical', fraction = 0.05)
    ax.set_xticks([0, 1, 2, 3, 4])
    ax.set_xticklabels(correlation_data.columns, rotation=90, fontsize=20)
    ax.set_yticks([0, 1, 2, 3, 4])
    ax.set_yticklabels(correlation_data.columns, rotation=0, fontsize=20)
    for i in range(len(correlation_data.columns)):
        for j in range(len(correlation_data.columns)):
            text = ax.text(j, i, round(pear_corr.to_numpy()[i, j], 2), ha="center", va="center", color="black")
    plt.show()

if __name__ == "__main__":

    co_2, co2_trans = read_clean_transpose('co2.xls')
    print(co_2)
    print(co2_trans)
   # co2_trans.to_excel("trans2.xlsx")
    co2_emission_trend(co_2)
    gdp_growth, gdp_growth_trans = read_clean_transpose('gdp.xls')
    gdp_growth_trend(gdp_growth)
    statistics_comparison()
    correlation_analysis('china_heat.xlsx')
    correlation_analysis('india_heat.xlsx')
    
    
    
    
    
    
    