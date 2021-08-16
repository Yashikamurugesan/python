from datetime import date
import holidays
north_america = holidays.CA() + holidays.US() + holidays.MX()
print(north_america.country)
print(north_america.get('07-01-2018'))
print(north_america.get('07-04-2018'))
