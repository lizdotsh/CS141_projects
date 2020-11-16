#Do not change any of the import lines
#Made by Elizabeth Goodwin 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Project_4 import *

#Part 1: Data QC
#Do not change the order of lines
#Maintain the original structures (if there is a lambda, use a lambda etc)
#You can copy and paste in the line
#vaccine.head()
#or from the command line
#print(vaccine.head())
#to view the data frame
#comment these lines out before you turn in your project

#Read in the data
vaccine = pd.read_csv('vaccine_data.csv')
#Assign column names
vaccine.columns = ['Region', 'Vaccine', 'Year', 'Percentage']
#Update region names to replace & with and and remove spaces
vaccine['Region'] = vaccine['Region'].str.replace('&','and').str.replace(' ', '_')
#Change type of Year column to a string
vaccine['Year'] = vaccine['Year'].astype(str)
#print(vaccine.head())
#print(vaccine['Region'])
#Create description column
#The dictionary line is correct, you must use the dictionary
mappings = {'BCG':'tuberculosis', 'DTP1':'diphteria_pertussis_tetanus','DTP3': 'diptheria_pertussis_tetanus',\
'MCV1':'meningococcal_disease','MCV2':'meningococcal_disease','HEPBB':'hepatitis B', 'HEPB3':'hepatitis B',\
'HIB1':'Haeomphilus influenza', 'HIB3':'Haemophilus influenza','IPV1': 'polio','IPV3': 'polio', 'POL3': 'polio','PCV3':'pneumococcal disease', 'RCV1':'rubella',\
'ROTAC':'rotavirus','YFV':'Yellow Fever Virus'}
vaccine['Description'] = vaccine['Vaccine'].apply(lambda x: mappings[x])
#print(vaccine.head())
#Check the data frame before continuing



#Create a data frame called BCG_2019 that contains the rows for BCG vaccine for 2019
BCG_2019 = make_subset(vaccine, year = ['2019'], vaccine = ['BCG'])
#print(BCG_2019)
#BCG_temp = BCG_2019['Region'].map()
#From the data frame you made, create a Series called BCG2019_Series with Region  as the index and Percentage as the values
BCG2019_Series = pd.Series(BCG_2019['Percentage'].values, index = BCG_2019['Region'])
#print(BCG2019_Series)
#Create a barplot for the percentage outreach (Percentage) of BCG vaccine by region in 2019.
sns.barplot(x=BCG2019_Series.values, y=BCG2019_Series.index)

#Create a data frame called DPT1_Years that contains the rows for DPT1 vaccinations in the East Asia and Pacific region

DTP1_Years = make_subset(vaccine, region = ['East_Asia_and_Pacific'], vaccine = ['DTP1'])
#print(DTP1_Years)
#From the data frame you made, create a Series called DPT1_series that has Year as the index and Percentage as the values
DTP1_Series = pd.Series(DTP1_Years['Percentage'].values, index=DTP1_Years['Year'])
#Create a line plot of the data stored in DPT1_series with the title: DPT1 Vaccinations by Year in East Asia and Pacific Region
plt.title('DTP1 Vaccinations by Year in East Asia and Pacific Region')
plt.xticks(rotation=90)
sns.lineplot(y = DTP1_Series.values, x = DTP1_Series.index)


