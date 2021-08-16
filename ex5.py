from datetime import datetime
import pytz
country_time_zone = pytz.timezone('America/New_York')
country_time = datetime.now(country_time_zone)
dict={country_time_zone:''}
print(dict)


    
