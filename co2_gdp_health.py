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
    """ 
    This function read excel file into a data frame then clean the data by
    deleting unwanted and empty columns and rows
    """
    data_frame = pd.read_excel(filename)
    #make country name as index
    data_frame.set_index('Country Name', inplace = True)
    #delete unwanted columns
    data_frame.drop(labels = ['Country Code', 'Indicator Name', \
                                    'Indicator Code'], axis = 1, inplace = True)
    #delete empty rows
    data_frame.dropna(axis = 0,how = 'all',thresh = None, subset = None, \
                                                                inplace = True)
    #delete empty columns                                                            
    data_frame.dropna(axis=1, how = 'all', thresh = None, subset = None, \
                                                                inplace = True)
    #transposed the cleaned data                                                           
    clean_df_transpose = data_frame.transpose()
    #set year as the index of the transposed data frame
    clean_df_transpose = clean_df_transpose.rename_axis('Year') 
    return data_frame, clean_df_transpose


def co2_emission_trend(df):
    """ 
    This function visualizes the increase in co2 emission of top five countries 
    that emit most co2 in the world according to the data of 2019
    """
    # Extract data top five countries
    top_five = df.loc[['China', 'United States', 'India', 'Japan', 'Germany']]
    #Extract data of corresponding years to draw the bar graph
    top_five_year =top_five.loc[:, ["2005", "2010", "2015", "2019"]]
    #Plotting bar graph
    top_five_year.plot(kind = 'bar')
    plt.title("CO2 EMISSION GROWTH OF TOP 5 COUNTRIES")
    plt.ylabel("CO2 EMISSION (Kilo tonnes)")
    plt.xlabel("COUNTRY")
    return


def gdp_growth_trend(df):
    """
    This function visualizes gdp growth trend of top 5 co2 emitting countries in
    the world
    """
    #Extract the gdp data of top 5 co2 emitting countries
    top_five = df.loc[['China', 'United States', 'India', 'Japan', 'Germany']]
    #Extract the data of corresponding years to draw the bar graph
    top_five_year =top_five.loc[:, ["2005", "2010", "2015", "2019"]]
    print(top_five_year)
    top_five_year.plot(kind = 'bar')
    plt.title("GDP GROWTH OF TOP CARBON EMITTING COUNTRIES")
    plt.ylabel("GDP")
    plt.xlabel("COUNTRY")
    return


def statistics_comparison():
    """ 
    This function find out the statistical properties(skewness, kurtosis 
    and median in addition to describe) of indicators (Mortality Rate, 
    Life expectancy, Health Expenditure(%of GDP)of top 5 countries in 
    co2 emission over past 10 years
    """                                                
    indicator_comparison = pd.read_excel("statistics1.xlsx")
    # use descibe to find out statistical properties of each indiactor group by 
    #country
    statistics_description = indicator_comparison.groupby('Country Name')[[\
   "Life expectancy", "Mortality rate", "Current health expenditure"]].describe()
    # find median of each indiactor group by country
    statistics_median = indicator_comparison.groupby('Country Name')[[\
    "Life expectancy","Mortality rate","Current health expenditure"]].median()
    # write the result into an excel file for further analysis
    statistics_description.to_excel("statistics_description.xlsx")
    statistics_median.to_excel("statistics_median.xlsx")
    # extract indicator data over 10 years corresponding to world
    world_indicators = indicator_comparison[indicator_comparison['Country Name']\
                                                                    == 'World']
    # extract indicator data over 10 years corresponding to China
    china_indicators = indicator_comparison[indicator_comparison['Country Name']\
                                                                    == 'China']
    # extract indicator data over 10 years corresponding to India 
    india_indicators = indicator_comparison[indicator_comparison['Country Name']\
                                                                    == 'India']
    #calculate skewness and kurtosis of indictors of world, China, India                                                                == 'India']
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
    return

    
def correlation_analysis(filename):
    """ 
    This function find out the correlation between indicators by pearson 
    correlation coefficient and draw the heat map
    """
    correlation_data = pd.read_excel(filename)
    pear_corr=correlation_data.corr(method = 'pearson')
    fig, ax = plt.subplots(figsize = (8,8))
    im = ax.imshow(pear_corr, cmap = 'spring', interpolation = 'nearest')
    fig.colorbar(im, orientation = 'vertical', fraction = 0.05)
    ax.set_xticks([0, 1, 2, 3, 4])
    ax.set_xticklabels(correlation_data.columns, rotation = 90, fontsize = 20)
    ax.set_yticks([0, 1, 2, 3, 4])
    ax.set_yticklabels(correlation_data.columns, rotation = 0, fontsize = 20)
    for i in range(len(correlation_data.columns)):
        for j in range(len(correlation_data.columns)):
            text = ax.text(j, i, round(pear_corr.to_numpy()[i, j], 2), ha= \
                                          "center", va="center", color="black")
    plt.show()
    return


if __name__ == "__main__":
    #call the function to clean and transpose the data
    co_2, co2_trans = read_clean_transpose('co2.xls')
    #call the function to draw co2 emission bar graph
    co2_emission_trend(co_2)
    #call the function to clean and transpose the data
    gdp_growth, gdp_growth_trans = read_clean_transpose('gdp.xls')
    #call the function to draw gdp growth bar chart
    gdp_growth_trend(gdp_growth)
    #call the function to analyse statistical properties
    statistics_comparison()
    #call the function to find out correlation and draw the heat map
    correlation_analysis('china_heat.xlsx')
    correlation_analysis('india_heat.xlsx')
    
    
    
    
    
    
    