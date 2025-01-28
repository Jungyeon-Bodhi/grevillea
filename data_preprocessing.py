#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 21:12:49 2025

@author: Bodhi Global Analysis (Jungyeon Lee)
"""

"""
Please define the parameters for data preprocessing pipeline
"""
import bodhi_data_preprocessing as dp

project_name = "24-IP-BUR-1"

file_type = 'xlsx' 
# Original data format: xlsx, xls, csv

file_path = "Data/24-IP-BUR-1 - Raw Data"
# Original data location and name (excluding file extension): "Data/(name)"

file_path_others = "Data/24-IP-BUR-1 - Open-End.xlsx"
# Specify the path and name of the Excel sheet where the values from the open-ended columns will be saved (New file)
# For example: "Data/(project name) others.xlsx"

respondent_name = '1'
# Original column name for respondents' names (for anonymisation and duplicate removal)

identifiers = [respondent_name, 'today', '_id', '_uuid']
# Identifiers for detecting duplicates (list, do not remove respondent_name)
# Recommendation: At least three identifiers

dates = ['2025-01-19'] 
# Remove the dates on which the pilot test was conducted from the data
# for example ['2024-07-18', '2024-07-22', '2024-07-23']

cols_new = ['start','end', 'start-geo', 'geo_latitude', 'geo_longitude', 'geo_altitude', 'geo_precision', 'today', 'deviceid',
 '0', 'consent1', 'consent2', '1', '2', '3', '4-1', '4-2', '4-3', '4-4', '4-5', '4-6', '4-7',
 '5', '6', '7', '8', '9', '10', '11a', '11-1', '11-2', '11-3', '11-4', '11-5', '11-6', '11-7', '11-8', '11-9', '12-o',
 "13", '14', '15a', '15-1', '15-2', '15-3', '15-4', '15-5', '16-o', '17', '18', '19', '20', '21',
 '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33','34', '35', '36', '37', '38','39','40',
 '41', '42', '43', '44', '45', '46', '47','48', '49a', '49-1', '49-2', "49-3", '49-4', '49-5', '49-6', '49-7',
 '49-8', '50', '51', '52', '53', '54', '55', '56','57', '58', '59', '60', '61', '62', '63', '64', "65", '66',
 '67', '68', '0-old1', '0-old2', '0-old3', '_id', '_uuid', '_submission_time', '_validation_status', '_notes', '_status',
 '_submitted_by', '__version__', '_tags', '_index']
# Specify new column names for data analysis (ensure they match the exact order of the existing columns)

list_del_cols = ['11a', '15a','49a', '0-old1', '0-old2', '0-old3', '_id', '_uuid', '_submission_time', 
          '_validation_status', '_notes', '_status','_submitted_by','__version__','_tags','_index', 
          'start','end', 'start-geo', 'geo_latitude', 'geo_longitude', 'geo_altitude', 'geo_precision', 
          'today', 'deviceid', '0', 'consent1', 'consent2']
# Specify the columns to be excluded from the data analysis

miss_col = ['1', '2', '3', '5', '8', '9', '10']
# Specify all columns that apply to all respondents for missing value detection

open_cols = ['6', '12-o','16-o','40', '50','67', '68']
# Specify the open-ended columns (which will be saved in a separate Excel sheet and removed from the data frame)

age_col = None
# If we don't have age group in this dataset, please specify the age columns (as str)

diss_cols = None
# If we have WG-SS questions in the dataset, please specify the columns (as list [])


"""
Run the pipeline for data preprocessing
del_type = 0 or 1
-> 0: Remove all missing values from the columns where missing values are detected
-> 1: First, remove columns where missing values make up 10% or more of the total data points
      Then, remove all remaining missing values from the columns where they are detected
"""

grevillea = dp.Preprocessing(project_name, file_path, file_path_others, list_del_cols, dates, miss_col, respondent_name, identifiers, open_cols, cols_new, del_type = 0, file_type=file_type)
grevillea.processing()