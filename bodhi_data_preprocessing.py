#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 20:00:20 2025

@author: Bodhi Global Analysis (Jungyeon Lee)
"""

"""
Please download following Python Libraries:
1. Pandas
2. Numpy
3. uuid
4. openpyxl
"""

import pandas as pd
import numpy as np
import uuid
from openpyxl import load_workbook

class Preprocessing:
    
    def __init__(self, name, file_path, file_path_others, list_del_cols, dates, miss_col, anon_col, identifiers, opened_cols, cols_new, 
                 del_type = 0, file_type='xlsx'):
        """
        - Initialise the Performance Management Framework class

        name: str, Name of the project
        file_path: str, Directory of the raw dataset
        file_path_others: str, Directory of the opened-end questions' answers
        list_del_cols: list, Columns list for deleting
        dates: list, Dates on which the pilot test was conducted from the data
        miss_col: list, 
        anon_col: str, Column for anonymisation (Respondent Name)
        identifiers: list, Columns for checking duplicates 
        opened_cols: list, Opened-end question columns
        cols_new: list, New names for the columns (for data analysis purpose)
        del_type: int, [0 or 1]
        -> 0: Remove all missing values from the columns where missing values are detected
        -> 1: First, remove columns where missing values make up 10% or more of the total data points
              Then, remove all remaining missing values from the columns where they are detected
        file_type: str, filetype of the raw dataset
        """
        self.name = name
        self.file_path = file_path
        self.file_path_others = file_path_others
        self.file_type = file_type
        self.list_del_cols = list_del_cols
        self.dates = dates
        self.miss_col = miss_col
        self.anon_col = anon_col
        self.identifiers = identifiers
        self.opened_cols = opened_cols
        self.cols_new = cols_new
        self.del_type = del_type
        self.df = None
    
    def data_load(self):
        """
        - To load a dataset
        """
        file_path = self.file_path
        file_type = self.file_type
        if file_type == 'xlsx' or file_type == 'xls':
            df = pd.read_excel(f"{file_path}.{file_type}")
            self.df = df
            return True
        elif file_type == 'csv':
            df = pd.read_csv(f"{file_path}.{file_type}")
            self.df = df
            return True
        else:
            print("Please use 'xlsx', 'xls' or 'csv' file")
            return False
        
    def delete_columns(self):
        """
        - To drop unnecessary columns
        """
        df = self.df
        list_cols = self.list_del_cols
        df = df.drop(columns = list_cols)
        print(f'Number of columns: {len(df.columns)} | After removing the columns that are not needed for the analysis')
        self.df = df
        return True

    def date_filter(self):
        """
        - To remove dates on which the pilot test was conducted from the dataset
        """
        df = self.df 
        dates = self.dates
        for date in dates:
            df = df[df['today'] != date]
        self.df = df
        return True
        
    def missing_value_clean(self):
        """
        - To detect and remove missing values
        """
        miss_col = self.miss_col
        df = self.df
        del_type = self.del_type
        initial_data_points = len(df)
        num_missing_cols = {}
        print("")
        for col in miss_col:
            missing_count = df[col].isnull().sum()
            num_missing_cols[col] = missing_count
            print(f'Column {col} has {missing_count} missing values')
    
        if del_type == 0: # Remove all missing values from the columns where missing values are detected
            df_cleaned = df.dropna(subset=miss_col)

        # First, remove columns where missing values make up 10% or more of the total data points
        # Then, remove all remaining missing values from the columns where they are detected
        elif del_type == 1:
            threshold = 0.1 * initial_data_points
            cols_to_drop = [col for col, missing_count in num_missing_cols.items() if missing_count > threshold]
            df_cleaned = df.drop(columns=cols_to_drop)
            print("")
            print(f'Number of columns: {len(df.columns)} | After removing the columns that contained missing values more than 10% of data points')
            print(f'Dropped columns = {cols_to_drop}')
            df_cleaned = df_cleaned.dropna(subset=miss_col)
        
        remaind_data_points = len(df_cleaned)
        print("")
        print(f'Number of deleted missing values: {initial_data_points - remaind_data_points}')
        print(f"Number of data points after missing value handling: {remaind_data_points}")
        print("")
        self.df = df_cleaned
        return True
    
    def save_data(self):
        """
        - To save the new dataframe
        """
        df = self.df
        file_path = self.file_path
        file_type = self.file_type
        if file_type == 'xlsx' or file_type == 'xls':
            df.reset_index(drop=True, inplace = True)
            df.to_excel(f"{file_path}.{file_type}", index=False)
            self.df = df
            print("The revised dataset has been saved")
            return True
        elif file_type == 'csv':
            df.reset_index(drop=True, inplace = True)
            df.to_csv(f"{file_path}.{file_type}", index=False)
            self.df = df
            print("The revised dataset has been saved")
            return True
        else: 
            print("Please use 'xlsx', 'xls' or 'csv' file")
            return False
        if file_type == 'xlsx':
            df.reset_index(drop=True, inplace = True)
            df.to_excel(f"{file_path}.{file_type}", index=False)
            self.df = df
            print("The revised dataset has been saved")
            return True
        elif file_type == 'csv':
            df.reset_index(drop=True, inplace = True)
            df.to_csv(f"{file_path}.{file_type}", index=False)
            self.df = df
            print("The revised dataset has been saved")
            return True
        else: 
            print("Please use 'xlsx' or 'csv' file")
            return False
        
    def data_anonymisation(self):
        """
        - To implement a dataframe anonymisation
        """
        df = self.df
        col1 = self.anon_col
        file_path = self.file_path
    
        def generate_unique_strings(prefix, series):
            unique_values = series.unique()
            key_mapping = {value: f"{prefix}{uuid.uuid4()}" for value in unique_values}
            return series.map(key_mapping), key_mapping
    
        df[col1], respondent_mapping = generate_unique_strings('respondent_', df[col1])
        original = self.file_path
        self.file_path = f'{file_path}_anonymised'
        self.save_data()
        self.file_path = original
        self.df = df
        print("The respondent name has been anonymised")
        return True
    
    def duplicates(self):
        """
        - To detect and remove duplicates
        """
        df = self.df
        col = self.identifiers
        duplicates = df[df.duplicated(subset=col, keep=False)]
        print("")
        print(f"Number of duplicate based on '{col}': {len(duplicates)}")

        if not duplicates.empty:
            print("Duplicate rows:")
            print(duplicates)
    
        df_cleaned = df.drop_duplicates(subset=col, keep='first')
    
        print(f"Number of data points: {len(df_cleaned)} | After removing duplicates")
        print("")
        self.df = df_cleaned
        return True

    def open_ended_cols(self):
        """
        - To save opened-ended columns and remove these from the dataset
        """
        df = self.df
        cols = self.opened_cols
        file_path = self.file_path_others
        empty_df = pd.DataFrame()
        with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
            empty_df.to_excel(writer, sheet_name='basic', index=False)
        
            max_length = 0
            unique_data = {}

            for col in cols:
                unique_values = df[col].dropna().unique()
                unique_data[col] = unique_values
                max_length = max(max_length, len(unique_values))
        
            combined_df = pd.DataFrame({col: pd.Series(unique_data[col]) for col in cols})
            combined_df.to_excel(writer, sheet_name='open_ended', index=False)
        
        print(f"Open-ended columns have been saved to '{file_path}': {cols} ")
        df = df.drop(columns=cols)
        print(f'Number of columns: {len(df.columns)} | After removing the open-ended columns')
        self.df = df
        return True

    def columns_redefine(self):
        """
        - To change column names for smoother data analysis
        """
        df = self.df
        new_cols = self.cols_new
        file_path = f'{self.file_path}_columns_book.xlsx'
        original_cols = list(df.columns)
        df.columns = new_cols
    
        with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
            empty_df = pd.DataFrame()
            empty_df.to_excel(writer, sheet_name='basic', index=False)

            columns_df = pd.DataFrame({'Column Names': new_cols,'Original Names': original_cols})
        
            columns_df.to_excel(writer, sheet_name='Column_Info', index=False)

            workbook = writer.book
            worksheet = workbook['Column_Info']
        
            for col in worksheet.columns:
                max_length = max(len(str(cell.value)) for cell in col)
                adjusted_width = max(max_length, 12)
                worksheet.column_dimensions[col[0].column_letter].width = adjusted_width

        print(f"Column information has been saved: {file_path}")
        self.df = df
        return True

    def grouping(self):
        df = self.df
        df['4'] = df[['4-1', '4-2', '4-3', '4-4', '4-5', '4-6', '4-7']].bfill(axis=1).iloc[:, 0]
        df = df[df['8'] != "I don't know"].reset_index(drop=True)
        self.df = df

    def indicator1(self):
        df = self.df
        df['26_score'] = np.where(df['26'].isin(['Completely agree', 'Agree']), 1, 0)
        df['27_score'] = np.where(df['27'].isin(['Completely agree', 'Agree']), 1, 0)
        df['28_score'] = np.where(df['28'].isin(['Completely agree', 'Agree']), 1, 0)
        df['total_score'] = df['26_score'] + df['27_score'] + df['28_score']
        df['212a'] = np.where(pd.isna(df['total_score']),np.nan,np.where(df['total_score'] == 3, 'Adequate', 'Inadequate'))
        df.drop(columns=['26_score', '27_score', '28_score', 'total_score'], inplace=True)
        self.df = df
        
    def indicator2(self):
        df = self.df
        conditions = [(df['48'] == "Completely agree") & (df['52'] == "Completely agree") & (df['53'] == "Completely agree"),
            (df['48'] == "Agree") & (df['52'] == "Completely agree") & (df['53'] == "Completely agree"),
            (df['52'] == "Agree") & (df['48'] == "Completely agree") & (df['53'] == "Completely agree"),
            (df['53'] == "Agree") & (df['48'] == "Completely agree") & (df['52'] == "Completely agree"),
            (df['52'] == "Agree") & (df['53'] == "Agree") & (df['48'] == "Completely agree"),
            (df['48'] == "Agree") & (df['52'] == "Agree") & (df['53'] == "Completely agree")]
        labels = [1, 2, 3, 4, 5, 6]
        df['212b'] = np.select(conditions, labels, default=7)
        df['212b_label'] = np.where(pd.isna(df['212b']),np.nan,np.where(df['212b'] == 1, 'Adequate', 'Inadequate'))
        self.df = df
        
    def mental_health(self):
        df = self.df
        mental_health = ['57', '58', '59', '60', '61', '62', '63', '64', "65", '66']
        df['mental_health'] = np.where(
            df[mental_health].isna().any(axis=1),np.nan,
            np.where(df[mental_health].isin(['Almost always', 'Often']).all(axis=1),  'Adequate', 'Inadequate'))
        self.df = df       
        
    def indicator3(self):
        df = self.df
        df['7_label'] = np.where((df['5'] == "Women's Leadership Platform") & (df['7'] == "None"),'Inadequate',
        np.where(df['5'] == "Women's Leadership Platform",'Adequate',np.nan))
        self.df = df 

    def processing(self):
        """
        - To conduct data pre-processing
        1. Load the raw dataset
        2. Re-define variable names
        3. Handle duplicates
        4. Anonymise data (Respondents' names)
        5. Remove pilot test data points
        6. Drop unnecessary columns
        7. Handle missing values
        8. Extract answers from open-ended questions
        9. Create age and disability groups
        10. Save the cleaned dataset
        """
        self.data_load()
        self.columns_redefine()
        print(f'Initial data points: {len(self.df)}')
        self.duplicates()
        self.data_anonymisation()
        if len(self.dates) != 0:
            self.date_filter()
        print(f'Initial number of columns: {len(self.df.columns)}')
        self.delete_columns()
        self.missing_value_clean()
        self.open_ended_cols()
        self.grouping()
        self.indicator1()
        self.indicator2()
        self.indicator3()
        self.mental_health()
        original = self.file_path
        self.file_path = f'data/{self.name} - Cleaned Data'
        self.save_data()
        self.file_path = original
        print("")
        print(f'Final number of data points: {len(self.df)}')
        print(f"Cleaned dataframe has been saved: {self.file_path}_cleaned.{self.file_type}")
        return True