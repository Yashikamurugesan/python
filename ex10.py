from datetime import date
import holidays
uk_holidays = holidays.UnitedKingdom()
for i in holidays.UnitedKingdom(years = 2018).items():
	print(i)
