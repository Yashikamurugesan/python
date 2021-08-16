from datetime import date
import holidays
holidays_country=holidays.Austria(years=2020)+holidays.Denmark(years=2021)+holidays.France(years=2022)
for i in holidays_country.items():
    print(i,end="\n")
    print("")
