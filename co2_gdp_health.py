# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 17:22:17 2023

@author: ASWANY SHAJI
"""

import pandas as pd
import matplotlib.pyplot as plt

def read_clean_transpose(filename):
    data_frame = pd.read_excel(filename)
    data_frame.iloc[3:]
    data_frame.set_index('Country Name', inplace =True)
    data_frame.drop(labels = ['Country Code', 'Indicator Name', 'Indicator Code'], axis = 1, inplace = True)
    data_frame.dropna(axis=0,how='all',thresh=None, subset=None, inplace=True)
    data_frame.dropna(axis=1,how='all',thresh=None, subset=None, inplace=True)
    clean_df_transpose = data_frame.transpose()
    #clean_df_transpose.rename(columns={'index':'Year'}, inplace = True)
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
    
    


if __name__ == "__main__":

    co_2, co2_trans = read_clean_transpose('co2.xls')
    print(co_2)
    print(co2_trans)
   # co2_trans.to_excel("trans2.xlsx")
    co2_emission_trend(co_2)
    gdp_growth, gdp_growth_trans = read_clean_transpose('gdp.xls')
    gdp_growth_trend(gdp_growth)
    
    
    
    
    
    
    