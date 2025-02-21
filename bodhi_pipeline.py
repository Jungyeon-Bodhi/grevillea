#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 23:17:52 2025

@author: Bodhi Global Analysis (Jungyeon Lee)
"""

import bodhi_indicator as bd
import bodhi_PMF as pmf
import pandas as pd

"""
Evaluation
"""
# Specify the file path for the clean dataset
df = pd.read_excel('data/24-IP-BUR-1 - Cleaned Data.xlsx')
indicators = []

# Create indicators and provide additional details as needed (Evaluation)
def statistics(df, indicators):
    gender = bd.Indicator(df, "Gender", 0, ['2'], i_cal=None, i_type='count', description='Gender Distribution', period='endline', target = None)
    gender.add_breakdown({'3':'Province'})
    gender.add_var_order(['Man', 'Woman'])
    indicators.append(gender)
    
    province = bd.Indicator(df, "Province", 0, ['3'], i_cal=None, i_type='count', description="Respondents' Province", period='endline', target = None, visual = False)
    province.add_breakdown({'2':'Gender'})
    province.add_var_order(['Bujumbura Mairie', 'Bujumbura Rural',
                            'Cibitoke','Gitega','Muyinga','Ngozi','Rumonge'])
    indicators.append(province)
    
    community = bd.Indicator(df, "Community", 0, ['4'], i_cal=None, i_type='count', description="Respondents' Community", period='endline', target = None, visual = False)
    community.add_breakdown({'2':'Gender', '3':'Province'})
    indicators.append(community)
    
    age = bd.Indicator(df, "Age group", 0, ['8'], i_cal=None, i_type='count', description="Respondents Age group", period='endline', target = None, visual = False)
    age.add_breakdown({'2':'Gender', '3':'Province'})
    age.add_var_order(['18-34', '35-54', "55+"])
    indicators.append(age)
    
    platform = bd.Indicator(df, "Platform type", 0, ['5'], i_cal=None, i_type='count', description="Platform Type", period='endline', target = None)
    platform.add_breakdown({'2':'Gender', '3':'Province', '8':'Age Group'})
    platform.add_var_order(['Community platform', 'Youth Platform',
                            "Women's Leadership Platform", "Other"])
    indicators.append(platform)
    
    civil = bd.Indicator(df, "Civil Status", 0, ['9'], i_cal=None, i_type='count', description="Civil Status", period='endline', target = None, visual = False)
    civil.add_breakdown({'2':'Gender', '3':'Province', '8':'Age Group'})
    civil.add_var_order(['Married', 'Single',"Separated/Divorced",
                            "Widower", "Prefer not to answer"])
    indicators.append(civil)
    
    i_212a = bd.Indicator(df, "Indicator 212a", 0, ['212a'], i_cal=None, i_type='Percentage', description="Percentage of beneficiaries who feel that community concerns of targeted groups", period='endline', target = 70)
    i_212a.add_baseline(44)
    i_212a.add_breakdown({'2':'Gender', '3':'Province', '8':'Age Group'})
    i_212a.add_var_order(['Adequate', "Inadequate"])
    indicators.append(i_212a)
    
    i_212a_1 = bd.Indicator(df, "I212a_26", 0, ['26'], i_cal=None, i_type='count', description="Do you find that local leaders take into account issues specific to women?", period='endline', target = None, visual = False)
    i_212a_1.add_breakdown({'2':'Gender', '3':'Province', '8':'Age Group'})
    i_212a_1.add_var_order(['Completely agree', "Agree","Disagree",
                            "Completely disagree","Prefer not to answer"])
    indicators.append(i_212a_1)
    
    i_212a_2 = bd.Indicator(df, "I212a_27", 0, ['27'], i_cal=None, i_type='count', description="Do you find that local leaders take into account the specific problems of young women?", period='endline', target = None, visual = False)
    i_212a_2.add_breakdown({'2':'Gender', '3':'Province', '8':'Age Group'})
    i_212a_2.add_var_order(['Completely agree', "Agree","Disagree",
                            "Completely disagree","Prefer not to answer"])
    indicators.append(i_212a_2)
    
    i_212a_3 = bd.Indicator(df, "I212a_28", 0, ['28'], i_cal=None, i_type='count', description="Do you find that local leaders take into account the specific problems of young men?", period='endline', target = None, visual = False)
    i_212a_3.add_breakdown({'2':'Gender', '3':'Province', '8':'Age Group'})
    i_212a_3.add_var_order(['Completely agree', "Agree","Disagree",
                            "Completely disagree","Prefer not to answer"])
    indicators.append(i_212a_3)
    
    will_act_1 = bd.Indicator(df, "Will_act_1", 0, ['36'], i_cal=None, i_type='count', description="Are you comfortable speaking at community meetings?", period='endline', target = None, visual = False)
    will_act_1.add_breakdown({'2':'Gender', '3':'Province', '8':'Age Group'})
    will_act_1.add_var_order(['Completely agree', "Agree","Disagree",
                            "Completely disagree","Prefer not to answer"])
    indicators.append(will_act_1)
    
    df_women = df[df['2'] == 'Woman'].copy()
    will_act_2 = bd.Indicator(df_women, "Will_act_2", 0, ['37'], i_cal=None, i_type='count', description="(For Women) You share your priorities or those of other women during these meetings", period='endline', target = None, visual = False)
    will_act_2.add_breakdown({'2':'Gender', '3':'Province', '8':'Age Group'})
    will_act_2.add_var_order(['Completely agree', "Agree","Disagree",
                            "Completely disagree","Prefer not to answer"])
    indicators.append(will_act_2)
    
    df_youth = df[df['8'] == '18-34'].copy()
    will_act_3 = bd.Indicator(df_youth, "Will_act_3", 0, ['38'], i_cal=None, i_type='count', description="(For Youth) You share your priorities or those of young people during these meetings", period='endline', target = None, visual = False)
    will_act_3.add_breakdown({'2':'Gender', '3':'Province', '8':'Age Group'})
    will_act_3.add_var_order(['Completely agree', "Agree","Disagree",
                            "Completely disagree","Prefer not to answer"])
    indicators.append(will_act_3)
    
    remaining_needs = bd.Indicator(df, "Remaining", 0, ['49-1', '49-2', "49-3", '49-4', '49-5', '49-6', '49-7','49-8'], i_cal=None, i_type='count', description="What factors prevent you from contributing more to the peace and development of your community?", period='endline', target = None)
    remaining_needs.add_breakdown({'2':'Gender', '3':'Province', '8':'Age Group'})
    remaining_needs.add_var_change({1: "Yes", 0: "No"})
    remaining_needs.add_var_order([1, 0])
    remaining_needs.add_label(["No time",
                               "No money",
                               "Don't want to/ doesn't concern me",
                               "No talents or skills needed",
                               "No credibility in the eyes of the community",
                               "Fear of backlash",
                               "No trust in the community",
                               "Other"])
    indicators.append(remaining_needs)
    
    i_212b = bd.Indicator(df_youth, "Indicator 212b", 0, ['212b_label'], i_cal=None, i_type='Percentage', description="Percentage of young people involved in the project who report having the capacity and means to positively influence their communities", period='endline', target = 70)
    i_212b.add_baseline(41)
    i_212b.add_breakdown({'2':'Gender', '3':'Province', '8':'Age Group'})
    i_212b.add_var_order(['Adequate', "Inadequate"])
    indicators.append(i_212b)
    
    i_212b_1 = bd.Indicator(df, "I212b_1", 0, ['54'], i_cal=None, i_type='count', description="Community members respect your ideas", period='endline', target = None)
    i_212b_1.add_breakdown({'2':'Gender', '3':'Province', '8':'Age Group'})
    i_212b_1.add_var_order(['Completely agree', "Agree","Disagree",
                            "Completely disagree","Prefer not to answer"])
    indicators.append(i_212b_1)
    
    i_212b_2 = bd.Indicator(df, "I212b_2", 0, ['55'], i_cal=None, i_type='count', description="The community takes your priorities into account in its plans/priorities", period='endline', target = None)
    i_212b_2.add_breakdown({'2':'Gender', '3':'Province', '8':'Age Group'})
    i_212b_2.add_var_order(['Completely agree', "Agree","Disagree",
                            "Completely disagree","Prefer not to answer"])
    indicators.append(i_212b_2)
    
    i_212b_3 = bd.Indicator(df, "I212b_3", 0, ['56'], i_cal=None, i_type='count', description="Local leaders respect your ideas", period='endline', target = None)
    i_212b_3.add_breakdown({'2':'Gender', '3':'Province', '8':'Age Group'})
    i_212b_3.add_var_order(['Completely agree', "Agree","Disagree",
                            "Completely disagree","Prefer not to answer"])
    indicators.append(i_212b_3)
    
    mental_health = bd.Indicator(df, "Mental health", 0, ['mental_health'], i_cal=None, i_type='count', description="Percentage of people who demonstrated an adequate level of psychosocial resilience", period='endline', target = None)
    mental_health.add_breakdown({'2':'Gender', '3':'Province', '8':'Age Group'})
    mental_health.add_var_order(['Adequate', "Inadequate"])
    indicators.append(mental_health)
    
    df_female_p = df[df['5'] == "Women's Leadership Platform"].copy()
    i_212c = bd.Indicator(df_female_p, "Indicator 212c", 0, ['7_label'], i_cal=None, i_type='Percentage', description="Percentage of members of women's platforms who undertake initiatives to promote women's needs and priorities without project support", period='endline', target = 50)
    i_212c.add_baseline(65)
    i_212c.add_breakdown({'2':'Gender', '3':'Province', '8':'Age Group'})
    i_212c.add_var_order(['Adequate', "Inadequate"])
    indicators.append(i_212c)
    
    i_212c_1 = bd.Indicator(df_female_p, "I212c_1", 0, ['7'], i_cal=None, i_type='count', description="How many initiatives to promote the needs and priorities of women are you currently undertaking?", period='endline', target = None)
    i_212c_1.add_breakdown({'2':'Gender', '3':'Province', '8':'Age Group'})
    i_212c_1.add_var_order(['None', "One","Two","Three",
                            "Four and above"])
    indicators.append(i_212c_1)
    return indicators
    
# Create indicators for several statistical tests such as OLS, ANOVA, T-test and Chi2
def statistical_indicators(df, indicators):
    df_indicator = df[df['8'] != "I don't know"]
    stats_212a = bd.Indicator(df_indicator, "Indicator 212a", 0, ['212a'], i_cal=None, i_type='count', description='Indicator - 212a (Chi-square)', s_test = 'chi', s_group = {'2':'Gender', '3':'Province', '8':'Age Group'})
    indicators.append(stats_212a)
    
    stats_212b = bd.Indicator(df_indicator, "Indicator 212b", 0, ['212b_label'], i_cal=None, i_type='count', description='Indicator - 212b (Chi-square)', s_test = 'chi', s_group = {'2':'Gender', '3':'Province', '8':'Age Group'})
    indicators.append(stats_212b)
    
    stats_212c = bd.Indicator(df_indicator, "Indicator 212c", 0, ['7_label'], i_cal=None, i_type='count', description='Indicator - 212c (Chi-square)', s_test = 'chi', s_group = {'3':'Province', '8':'Age Group'})
    indicators.append(stats_212c)
    
    stats_mental = bd.Indicator(df_indicator, "Mental health", 0, ['mental_health'], i_cal=None, i_type='count', description='Psychosocial Resilience (Chi-square)', s_test = 'chi', s_group = {'2':'Gender', '3':'Province', '8':'Age Group'})
    indicators.append(stats_mental)
    return indicators

# Create the PMF class ('Project Title', 'Evaluation')
grevillea = pmf.PerformanceManagementFramework('Grevillea', 'Evaluation')

indicators = statistics(df, indicators)
indicators = statistical_indicators(df, indicators)
grevillea.add_indicators(indicators)

file_path1 = 'data/24-IP-BUR-1 - Statistics.xlsx' # File path to save the statistics (including breakdown data)
file_path2 = 'data/24-IP-BUR-1 - Test Results.xlsx'  # File path to save the chi2 test results
folder = 'visuals/' # File path for saving visuals
grevillea.PMF_generation(file_path1, file_path2, folder) # Run the PMF



