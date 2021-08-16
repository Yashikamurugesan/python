from datetime import datetime
import pytz
country_time_zone = pytz.timezone('America/New_York')
country_time = datetime.now(country_time_zone)
print(country_time.strftime("Date is %d/%m/%y and time is %H:%M:%S"))
