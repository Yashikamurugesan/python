import holidays
country=input(''' Hi i'm yasi this is 2021 year festival days datebase for
Austria
Canada
Denmark ''')
for i in holidays.Austria(years=2000).items():
    print(i,end="        ")
    
    
