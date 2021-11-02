from datetime import date
import holidays
fr_holidays=holidays.France()
for i in holidays.France(years = 2018).items():
	print(i)
