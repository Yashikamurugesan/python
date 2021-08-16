from datetime import datetime
import pytz
country_zones = pytz.all_timezones
country_time_zones = []
for country_time_zone in country_zones:
    country_names=country_time_zones.append(pytz.timezone(country_time_zone))
for i in range(len(country_time_zones)):
    country_time = datetime.now(country_time_zones[i])
    dict={'country_time':country_time}
    print(dict)
    
