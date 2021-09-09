import pandas as pd

url = 'f://DATA SCIENCE NOTES/nba.csv'

# read csv file
df = pd.read_csv(url)		
print(df.head())
df['Time'] = pd.to_datetime(df.Time)
  
print(df.head())
