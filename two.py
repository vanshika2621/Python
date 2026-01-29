import pandas as pd 
df=pd.read_csv('student.csv')
a = df.isnull().sum()
print("Missing values in each column:\n", a)
#Remove rows with missing values 
b = df.dropna()
print("Data after removing missing values:\n", b)
  
