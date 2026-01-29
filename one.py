import pandas as pd 
import matplotlib.pyplot as plt 
df=pd.read_csv('student.csv')
print(df.head())
df.plot(x ='Student_ID', y='Marks', kind='bar', color='skyblue')
plt.show() 
  
