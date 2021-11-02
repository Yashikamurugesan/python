from datetime import datetime
import pytz
UTC = pytz.utc
datetime_utc = datetime.now(UTC)
print("Date & Time in UTC : ",datetime_utc.strftime('%Y:%m:%d %I:%M:%S '))


      



  
