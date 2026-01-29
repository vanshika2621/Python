#Which pandas function would you use to fill missing values in a DataFrame?
import pandas as pd 
df=pd.read_csv('student.csv')
df.fillna(method='ffill', inplace=True) #ffill fills missing values forward
df.fillna(method='bfill', inplace=True) #bfill fills missing values backward
df['Marks'].fillna(df['Marks'].mean(), inplace=True) #Filling missing values in 'Marks' column with mean
df['Marks'].fillna(df['Marks'].median(), inplace=True)#Filling missing values in 'Marks' column with median
df['Marks'].fillna(df['Marks'].mode()[0], inplace=True) #Filling missing values in 'Marks' column with 

