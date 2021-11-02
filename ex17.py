from datetime import date
import holidays
uk_holidays = holidays.UnitedKingdom()
print('01-01-2018' in uk_holidays)
print('02-01-2018' in uk_holidays)
print(uk_holidays.get('01-01-2018'))
print(uk_holidays.get('02-01-2018'))




operation=input("""hi how are u""")
