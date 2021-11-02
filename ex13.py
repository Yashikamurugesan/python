from datetime import date

import holidays

us_holidays = holidays.UnitedStates()
# or:
# us_holidays = holidays.US()
# or:
# us_holidays = holidays.CountryHoliday('US')
# or, for specific prov / states:
# us_holidays = holidays.CountryHoliday('US', prov=None, state='CA')

date(2015, 1, 1) in us_holidays  # True
date(2015, 1, 2) in us_holidays  # False

# The Holiday class will also recognize strings of any format
# and int/float representing a Unix timestamp
'2014-01-01' in us_holidays  # True
'1/1/2014' in us_holidays    # True
1388597445 in us_holidays    # True

us_holidays.get('2014-01-01')  # "New Year's Day"

us_holidays['2014-01-01': '2014-01-03']  # [date(2014, 1, 1)]

us_pr_holidays = holidays.UnitedStates(state='PR')  # or holidays.US(...), or holidays.CountryHoliday('US', state='PR')

# some holidays are only present in parts of a country
'2018-01-06' in us_holidays     # False
'2018-01-06' in us_pr_holidays  # True

# Easily create custom Holiday objects with your own dates instead
# of using the pre-defined countries/states/provinces available
custom_holidays = holidays.HolidayBase()
# Append custom holiday dates by passing:
# 1) a dict with date/name key/value pairs,
custom_holidays.append({"2015-01-01": "New Year's Day"})
# 2) a list of dates (in any format: date, datetime, string, integer),
custom_holidays.append(['2015-07-01', '07/04/2015'])
# 3) a single date item
custom_holidays.append(date(2015, 12, 25))

date(2015, 1, 1) in custom_holidays  # True
date(2015, 1, 2) in custom_holidays  # False
'12/25/2015' in custom_holidays      # True

# For more complex logic like 4th Monday of January, you can inherit the
# HolidayBase class and define your own _populate(year) method. See below
# documentation for examples.
