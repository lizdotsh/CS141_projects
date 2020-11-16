import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#Made by Elizabeth Goodwin 

#Write your def lines and functions below
#The def lines you create must match the specifications exactly
#You cannot change the names of the functions, the variables, or the default arguments
#Expect a large grade penalty if your def lines are not correct
#This file should not contain any function calls or any code that is not part of
#A function definition
#This means any code unindented besides a def line or the import lines at the top

def make_subset(df, region = None, vaccine = None, year = None):
    df_new = df.copy()
    if region != None: df_new = df_new.loc[df_new['Region'].isin(region)]
    if vaccine != None: df_new = df_new.loc[df_new['Vaccine'].isin(vaccine)]
    if year != None: df_new = df_new.loc[df_new['Year'].isin(year)]
    return df_new

def make_plot(series_object, title ='', bar=True):
    plt.title(title)
    if bar == True: return(sns.barplot(x=series_object.values, y=series_object.index))
    elif bar == False: 
        plt.xticks(rotation=90)
        return (sns.lineplot(y=series_object.values, x=series_object.index))



