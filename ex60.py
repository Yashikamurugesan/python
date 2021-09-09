import pandas as pd
data = pd.read_csv("f://DATA SCIENCE NOTES/nba.csv")
print(data)
data.dropna(inplace = True)
before = data.dtypes
data["Salary"]= data["Salary"].astype(int)
data["Age"]= data["Age"].astype(str)
after = data.dtypes
print("BEFORE CONVERSION\n", before, "\n")
print("AFTER CONVERSION\n", after, "\n")
