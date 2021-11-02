from datetime import datetime
import pytz
country_zones = pytz.all_timezones
print(country_zones)
country_time_zones = []
for country_time_zone in country_zones:
    country_time_zones.append(pytz.timezone(country_time_zone))
for i in range(len(country_time_zones)):
    country_time = datetime.now(country_time_zones[i])
    print(f"The date of {country_zones[i]} is {country_time.strftime('%d/%m/%y')} and the time of {country_zones[i]} is {country_time.strftime('%H:%M:%S')}")
    
