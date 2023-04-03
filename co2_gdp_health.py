# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 17:22:17 2023

@author: ASWANY SHAJI
"""

import pandas as pd
import matplotlib.pyplot as plt

def read_transpose_clean(filename):
    data_frame = pd.read_excel(filename)
    # Set the Index on Country Name - previously was numeric.
    data_frame_transpose = data_frame.set_index('Country Name')
    # Transpose the index and columns
    data_frame_transpose = data_frame_transpose.transpose()
    # Reset the index, sets, 'index' as a column
    data_frame_transpose = data_frame_transpose.reset_index()
    # Rename the 'index' column to year
    data_frame_transpose = data_frame_transpose.rename(columns={'index':'Year'})
    # Set the DataFrame Index to newly named 'Year'
    data_frame_transpose = data_frame_transpose.set_index('Year')
    return data_frame, data_frame_transpose

def clean_data(df):
    df.drop(labels = ['Country Code', 'Indicator Name', 'Indicator Code'], axis = 0, inplace = True)
    df.dropna(axis=0,how='all',thresh=None, subset=None, inplace=True)
    df.dropna(axis=1,how='all',thresh=None, subset=None, inplace=True)
    return df

if __name__ == "__main__" :
    
    df1, df1_t = read_transpose_clean('co2_emission.xls')
    clean_df = clean_data(df1_t)
    clean_df.to_excel('clean2.xlsx')
    