import pandas as pd
import numpy as np      
      
      
dict= {'2018':[85,73,80,64], '2019':[60,80,58,96], '2020':[90,64,74,87] }      
      
df=pd.DataFrame(dict,index=['English','Math','Science','French'])      
print("When we use 'Columns':")    
print(df.columns)    
print("\n")    
print("When we use 'Axes':")    
print(df.axes)

print("Size of the DataFrame is:",df.size)    
print("Shape of the DataFrame is:",df.shape)    
print("Dimension of the DataFrame is:",df.ndim)
print("\n")

print(df.dtypes)
print("\n")


print("Using 'Empty' on Dataframe:",df.empty)    
print('DataFrame is not Empty')      
print('\n')      
print('Finding NaN values... ','\n',df.isna())      
print('NOT FOUND!!')    
print('\n')    
      
df1=pd.DataFrame(index=['English','Math','Science','French'])      
print("Using 'Empty' on Dataframe1:")    
print('DataFrame is Empty',df1.empty)      
print('\n')      
print('Finding NaN values...',df1.isna())    
print('FOUND!!')
print("\n")


print(df)      
print('\n')    
print("When we use 'count()':")    
print(df.count())      
print('\n')    
print("When we use 'count(axis='index')':")    
print(df.count(axis='index'))      
print('\n')    
print("When we use 'count(1)':")    
print(df.count(1))      
print('\n')    
print("When we use 'count(axis='columns')':")    
print(df.count(axis='columns'))   

