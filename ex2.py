from datetime import datetime
import pytz
country_zones =  ['America/New_York', 'Asia/Kolkata', 'Australia/Sydney',
                'Canada/Atlantic', 'Brazil/East','Chile/EasterIsland', 'Cuba', 'Egypt',
                'Europe/Amsterdam', 'Europe/Athens', 'Europe/Berlin', 'Europe/Istanbul',
                'Europe/Jersey', 'Europe/London', 'Europe/Moscow', 'Europe/Paris', 
                'Europe/Rome', 'Hongkong', 'Iceland', 'Indian/Maldives', 'Iran',
                'Israel', 'Japan', 'NZ', 'US/Alaska', 'US/Arizona', 'US/Central', 
                'US/East-Indiana']
print(country_zones)
countrytime_zones=[]
for countrytime_zones in country_zones:
    countrytime_zones.append(pytz.timezone(countrytime_zones))
    for j in range(len(countrytime_zones)):
        country_time = datetime.now(countrytime_zones[j])
        print(f"The date of {country_zones[j]} is {country_time.strftime('%d/%m/%y')} and The time of {country_zones[j]} is {country_time.strftime('%H:%M:%S')}")



