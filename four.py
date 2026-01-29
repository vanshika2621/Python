#changing the case 
import pandas as pd
df=pd.read_csv('student.csv')
df.columns = [col.upper() for col in df.columns]
print(df.head()) 
