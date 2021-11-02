Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import holidays
>>> holidays.
SyntaxError: invalid syntax
>>> holidays.Australia(years=2021)
{datetime.date(2021, 1, 1): "New Year's Day", datetime.date(2021, 1, 26): 'Australia Day', datetime.date(2021, 3, 1): 'Canberra Day', datetime.date(2021, 4, 2): 'Good Friday', datetime.date(2021, 4, 3): 'Easter Saturday', datetime.date(2021, 4, 5): 'Easter Monday', datetime.date(2021, 4, 25): 'Anzac Day', datetime.date(2021, 4, 26): 'Anzac Day (Observed)', datetime.date(2021, 6, 14): "Queen's Birthday", datetime.date(2021, 10, 4): 'Labour Day', datetime.date(2021, 12, 25): 'Christmas Day', datetime.date(2021, 12, 27): 'Christmas Day (Observed)', datetime.date(2021, 12, 26): 'Boxing Day', datetime.date(2021, 12, 28): 'Boxing Day (Observed)'}
>>> print(holidays.Australia(years=2021))
{datetime.date(2021, 1, 1): "New Year's Day", datetime.date(2021, 1, 26): 'Australia Day', datetime.date(2021, 3, 1): 'Canberra Day', datetime.date(2021, 4, 2): 'Good Friday', datetime.date(2021, 4, 3): 'Easter Saturday', datetime.date(2021, 4, 5): 'Easter Monday', datetime.date(2021, 4, 25): 'Anzac Day', datetime.date(2021, 4, 26): 'Anzac Day (Observed)', datetime.date(2021, 6, 14): "Queen's Birthday", datetime.date(2021, 10, 4): 'Labour Day', datetime.date(2021, 12, 25): 'Christmas Day', datetime.date(2021, 12, 27): 'Christmas Day (Observed)', datetime.date(2021, 12, 26): 'Boxing Day', datetime.date(2021, 12, 28): 'Boxing Day (Observed)'}
>>> print(holidays.Belgium(years=2021))
{datetime.date(2021, 1, 1): 'Nieuwjaarsdag', datetime.date(2021, 4, 4): 'Pasen', datetime.date(2021, 4, 5): 'Paasmaandag', datetime.date(2021, 5, 13): 'O.L.H. Hemelvaart', datetime.date(2021, 5, 23): 'Pinksteren', datetime.date(2021, 5, 24): 'Pinkstermaandag', datetime.date(2021, 5, 1): 'Dag van de Arbeid', datetime.date(2021, 7, 21): 'Nationale feestdag', datetime.date(2021, 8, 15): 'O.L.V. Hemelvaart', datetime.date(2021, 11, 1): 'Allerheiligen', datetime.date(2021, 11, 11): 'Wapenstilstand', datetime.date(2021, 12, 25): 'Kerstmis'}
>>> print(holidays.Belgium(years=2021),end="")
{datetime.date(2021, 1, 1): 'Nieuwjaarsdag', datetime.date(2021, 4, 4): 'Pasen', datetime.date(2021, 4, 5): 'Paasmaandag', datetime.date(2021, 5, 13): 'O.L.H. Hemelvaart', datetime.date(2021, 5, 23): 'Pinksteren', datetime.date(2021, 5, 24): 'Pinkstermaandag', datetime.date(2021, 5, 1): 'Dag van de Arbeid', datetime.date(2021, 7, 21): 'Nationale feestdag', datetime.date(2021, 8, 15): 'O.L.V. Hemelvaart', datetime.date(2021, 11, 1): 'Allerheiligen', datetime.date(2021, 11, 11): 'Wapenstilstand', datetime.date(2021, 12, 25): 'Kerstmis'}
>>> print(holidays.Belgium(years=2021),end="/n")
{datetime.date(2021, 1, 1): 'Nieuwjaarsdag', datetime.date(2021, 4, 4): 'Pasen', datetime.date(2021, 4, 5): 'Paasmaandag', datetime.date(2021, 5, 13): 'O.L.H. Hemelvaart', datetime.date(2021, 5, 23): 'Pinksteren', datetime.date(2021, 5, 24): 'Pinkstermaandag', datetime.date(2021, 5, 1): 'Dag van de Arbeid', datetime.date(2021, 7, 21): 'Nationale feestdag', datetime.date(2021, 8, 15): 'O.L.V. Hemelvaart', datetime.date(2021, 11, 1): 'Allerheiligen', datetime.date(2021, 11, 11): 'Wapenstilstand', datetime.date(2021, 12, 25): 'Kerstmis'}/n
>>> print(holidays.Belgium(years=2021),end=" /n ")
{datetime.date(2021, 1, 1): 'Nieuwjaarsdag', datetime.date(2021, 4, 4): 'Pasen', datetime.date(2021, 4, 5): 'Paasmaandag', datetime.date(2021, 5, 13): 'O.L.H. Hemelvaart', datetime.date(2021, 5, 23): 'Pinksteren', datetime.date(2021, 5, 24): 'Pinkstermaandag', datetime.date(2021, 5, 1): 'Dag van de Arbeid', datetime.date(2021, 7, 21): 'Nationale feestdag', datetime.date(2021, 8, 15): 'O.L.V. Hemelvaart', datetime.date(2021, 11, 1): 'Allerheiligen', datetime.date(2021, 11, 11): 'Wapenstilstand', datetime.date(2021, 12, 25): 'Kerstmis'} /n 
>>> print(holidays.Belgium(years=2021),end=" \n ")
{datetime.date(2021, 1, 1): 'Nieuwjaarsdag', datetime.date(2021, 4, 4): 'Pasen', datetime.date(2021, 4, 5): 'Paasmaandag', datetime.date(2021, 5, 13): 'O.L.H. Hemelvaart', datetime.date(2021, 5, 23): 'Pinksteren', datetime.date(2021, 5, 24): 'Pinkstermaandag', datetime.date(2021, 5, 1): 'Dag van de Arbeid', datetime.date(2021, 7, 21): 'Nationale feestdag', datetime.date(2021, 8, 15): 'O.L.V. Hemelvaart', datetime.date(2021, 11, 1): 'Allerheiligen', datetime.date(2021, 11, 11): 'Wapenstilstand', datetime.date(2021, 12, 25): 'Kerstmis'} 
 
>>> holidays.Canada(year=2021)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    holidays.Canada(year=2021)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\holidays.py", line 337, in __init__
    HolidayBase.__init__(self, **kwargs)
TypeError: __init__() got an unexpected keyword argument 'year'
>>> holidays.Canada(years=2021)
{datetime.date(2021, 1, 1): "New Year's Day", datetime.date(2021, 12, 31): "New Year's Day (Observed)", datetime.date(2021, 2, 15): 'Family Day', datetime.date(2021, 4, 2): 'Good Friday', datetime.date(2021, 5, 24): 'Victoria Day', datetime.date(2021, 7, 1): 'Canada Day', datetime.date(2021, 8, 2): 'Civic Holiday', datetime.date(2021, 9, 6): 'Labour Day', datetime.date(2021, 10, 11): 'Thanksgiving', datetime.date(2021, 12, 25): 'Christmas Day', datetime.date(2021, 12, 24): 'Christmas Day (Observed)', datetime.date(2021, 12, 27): 'Boxing Day (Observed)'}
>>> holidays.Canada(years=2021)
{datetime.date(2021, 1, 1): "New Year's Day", datetime.date(2021, 12, 31): "New Year's Day (Observed)", datetime.date(2021, 2, 15): 'Family Day', datetime.date(2021, 4, 2): 'Good Friday', datetime.date(2021, 5, 24): 'Victoria Day', datetime.date(2021, 7, 1): 'Canada Day', datetime.date(2021, 8, 2): 'Civic Holiday', datetime.date(2021, 9, 6): 'Labour Day', datetime.date(2021, 10, 11): 'Thanksgiving', datetime.date(2021, 12, 25): 'Christmas Day', datetime.date(2021, 12, 24): 'Christmas Day (Observed)', datetime.date(2021, 12, 27): 'Boxing Day (Observed)'}
>>> print(holidays.Canada(years=2021))
{datetime.date(2021, 1, 1): "New Year's Day", datetime.date(2021, 12, 31): "New Year's Day (Observed)", datetime.date(2021, 2, 15): 'Family Day', datetime.date(2021, 4, 2): 'Good Friday', datetime.date(2021, 5, 24): 'Victoria Day', datetime.date(2021, 7, 1): 'Canada Day', datetime.date(2021, 8, 2): 'Civic Holiday', datetime.date(2021, 9, 6): 'Labour Day', datetime.date(2021, 10, 11): 'Thanksgiving', datetime.date(2021, 12, 25): 'Christmas Day', datetime.date(2021, 12, 24): 'Christmas Day (Observed)', datetime.date(2021, 12, 27): 'Boxing Day (Observed)'}
>>> holidays.Canada(years=2021).append(years=200)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    holidays.Canada(years=2021).append(years=200)
TypeError: append() got an unexpected keyword argument 'years'
>>> holidays.Canada(years=2021).items():
	
SyntaxError: invalid syntax
>>> holidays.Canada(years=2021).items()
dict_items([(datetime.date(2021, 1, 1), "New Year's Day"), (datetime.date(2021, 12, 31), "New Year's Day (Observed)"), (datetime.date(2021, 2, 15), 'Family Day'), (datetime.date(2021, 4, 2), 'Good Friday'), (datetime.date(2021, 5, 24), 'Victoria Day'), (datetime.date(2021, 7, 1), 'Canada Day'), (datetime.date(2021, 8, 2), 'Civic Holiday'), (datetime.date(2021, 9, 6), 'Labour Day'), (datetime.date(2021, 10, 11), 'Thanksgiving'), (datetime.date(2021, 12, 25), 'Christmas Day'), (datetime.date(2021, 12, 24), 'Christmas Day (Observed)'), (datetime.date(2021, 12, 27), 'Boxing Day (Observed)')])
>>> holidays.Canada(years=2021).values()
dict_values(["New Year's Day", "New Year's Day (Observed)", 'Family Day', 'Good Friday', 'Victoria Day', 'Canada Day', 'Civic Holiday', 'Labour Day', 'Thanksgiving', 'Christmas Day', 'Christmas Day (Observed)', 'Boxing Day (Observed)'])
>>> holidays.Canada(years=2021).keys()
dict_keys([datetime.date(2021, 1, 1), datetime.date(2021, 12, 31), datetime.date(2021, 2, 15), datetime.date(2021, 4, 2), datetime.date(2021, 5, 24), datetime.date(2021, 7, 1), datetime.date(2021, 8, 2), datetime.date(2021, 9, 6), datetime.date(2021, 10, 11), datetime.date(2021, 12, 25), datetime.date(2021, 12, 24), datetime.date(2021, 12, 27)])
>>> holidays.Canada(years=2021).pop()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    holidays.Canada(years=2021).pop()
TypeError: pop() missing 1 required positional argument: 'key'
>>> holidays.Canada(years=2021).items()
dict_items([(datetime.date(2021, 1, 1), "New Year's Day"), (datetime.date(2021, 12, 31), "New Year's Day (Observed)"), (datetime.date(2021, 2, 15), 'Family Day'), (datetime.date(2021, 4, 2), 'Good Friday'), (datetime.date(2021, 5, 24), 'Victoria Day'), (datetime.date(2021, 7, 1), 'Canada Day'), (datetime.date(2021, 8, 2), 'Civic Holiday'), (datetime.date(2021, 9, 6), 'Labour Day'), (datetime.date(2021, 10, 11), 'Thanksgiving'), (datetime.date(2021, 12, 25), 'Christmas Day'), (datetime.date(2021, 12, 24), 'Christmas Day (Observed)'), (datetime.date(2021, 12, 27), 'Boxing Day (Observed)')])
>>> holidays.Canada(years=2021).values()
dict_values(["New Year's Day", "New Year's Day (Observed)", 'Family Day', 'Good Friday', 'Victoria Day', 'Canada Day', 'Civic Holiday', 'Labour Day', 'Thanksgiving', 'Christmas Day', 'Christmas Day (Observed)', 'Boxing Day (Observed)'])
>>> holidays.Canada(years=2021).keys()
dict_keys([datetime.date(2021, 1, 1), datetime.date(2021, 12, 31), datetime.date(2021, 2, 15), datetime.date(2021, 4, 2), datetime.date(2021, 5, 24), datetime.date(2021, 7, 1), datetime.date(2021, 8, 2), datetime.date(2021, 9, 6), datetime.date(2021, 10, 11), datetime.date(2021, 12, 25), datetime.date(2021, 12, 24), datetime.date(2021, 12, 27)])
>>> for i in holidays.Canada(years=2021).keys():
	print(i)

	
2021-01-01
2021-12-31
2021-02-15
2021-04-02
2021-05-24
2021-07-01
2021-08-02
2021-09-06
2021-10-11
2021-12-25
2021-12-24
2021-12-27
>>> for i in holidays.Canada(years=2021).items():
	print(i)

	
(datetime.date(2021, 1, 1), "New Year's Day")
(datetime.date(2021, 12, 31), "New Year's Day (Observed)")
(datetime.date(2021, 2, 15), 'Family Day')
(datetime.date(2021, 4, 2), 'Good Friday')
(datetime.date(2021, 5, 24), 'Victoria Day')
(datetime.date(2021, 7, 1), 'Canada Day')
(datetime.date(2021, 8, 2), 'Civic Holiday')
(datetime.date(2021, 9, 6), 'Labour Day')
(datetime.date(2021, 10, 11), 'Thanksgiving')
(datetime.date(2021, 12, 25), 'Christmas Day')
(datetime.date(2021, 12, 24), 'Christmas Day (Observed)')
(datetime.date(2021, 12, 27), 'Boxing Day (Observed)')
>>> for i in holidays.Canada(years=2021).values():
	print(i)

	
New Year's Day
New Year's Day (Observed)
Family Day
Good Friday
Victoria Day
Canada Day
Civic Holiday
Labour Day
Thanksgiving
Christmas Day
Christmas Day (Observed)
Boxing Day (Observed)
>>> can=holidays.Canada(years=2021)
>>> 
>>> can
{datetime.date(2021, 1, 1): "New Year's Day", datetime.date(2021, 12, 31): "New Year's Day (Observed)", datetime.date(2021, 2, 15): 'Family Day', datetime.date(2021, 4, 2): 'Good Friday', datetime.date(2021, 5, 24): 'Victoria Day', datetime.date(2021, 7, 1): 'Canada Day', datetime.date(2021, 8, 2): 'Civic Holiday', datetime.date(2021, 9, 6): 'Labour Day', datetime.date(2021, 10, 11): 'Thanksgiving', datetime.date(2021, 12, 25): 'Christmas Day', datetime.date(2021, 12, 24): 'Christmas Day (Observed)', datetime.date(2021, 12, 27): 'Boxing Day (Observed)'}
>>> can.update({"2021,1,1":"tomato day"})
Traceback (most recent call last):
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\holidays.py", line 71, in __keytransform__
    key = parse(key).date()
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\dateutil\parser\_parser.py", line 1368, in parse
    return DEFAULTPARSER.parse(timestr, **kwargs)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\dateutil\parser\_parser.py", line 643, in parse
    raise ParserError("Unknown string format: %s", timestr)
dateutil.parser._parser.ParserError: Unknown string format: 2021,1,1

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    can.update({"2021,1,1":"tomato day"})
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\holidays.py", line 101, in update
    self[key] = value
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\holidays.py", line 88, in __setitem__
    if key in self:
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\holidays.py", line 82, in __contains__
    return dict.__contains__(self, self.__keytransform__(key))
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\holidays.py", line 73, in __keytransform__
    raise ValueError("Cannot parse date from string '%s'" % key)
ValueError: Cannot parse date from string '2021,1,1'
>>> can.update({"01-01-2021":"tomato day"})
>>> can
{datetime.date(2021, 1, 1): "tomato day, New Year's Day", datetime.date(2021, 12, 31): "New Year's Day (Observed)", datetime.date(2021, 2, 15): 'Family Day', datetime.date(2021, 4, 2): 'Good Friday', datetime.date(2021, 5, 24): 'Victoria Day', datetime.date(2021, 7, 1): 'Canada Day', datetime.date(2021, 8, 2): 'Civic Holiday', datetime.date(2021, 9, 6): 'Labour Day', datetime.date(2021, 10, 11): 'Thanksgiving', datetime.date(2021, 12, 25): 'Christmas Day', datetime.date(2021, 12, 24): 'Christmas Day (Observed)', datetime.date(2021, 12, 27): 'Boxing Day (Observed)'}
>>> for i in can():
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    for i in can():
TypeError: 'Canada' object is not callable
>>> for i in can:
	print(i)

	
2021-01-01
2021-12-31
2021-02-15
2021-04-02
2021-05-24
2021-07-01
2021-08-02
2021-09-06
2021-10-11
2021-12-25
2021-12-24
2021-12-27
>>> for i in holidays.Canada(years=2021).values():
	print(i)

	
New Year's Day
New Year's Day (Observed)
Family Day
Good Friday
Victoria Day
Canada Day
Civic Holiday
Labour Day
Thanksgiving
Christmas Day
Christmas Day (Observed)
Boxing Day (Observed)
>>> for i in holidays.Canada(years=2021).items():
	print(i)

	
(datetime.date(2021, 1, 1), "New Year's Day")
(datetime.date(2021, 12, 31), "New Year's Day (Observed)")
(datetime.date(2021, 2, 15), 'Family Day')
(datetime.date(2021, 4, 2), 'Good Friday')
(datetime.date(2021, 5, 24), 'Victoria Day')
(datetime.date(2021, 7, 1), 'Canada Day')
(datetime.date(2021, 8, 2), 'Civic Holiday')
(datetime.date(2021, 9, 6), 'Labour Day')
(datetime.date(2021, 10, 11), 'Thanksgiving')
(datetime.date(2021, 12, 25), 'Christmas Day')
(datetime.date(2021, 12, 24), 'Christmas Day (Observed)')
(datetime.date(2021, 12, 27), 'Boxing Day (Observed)')
>>> can=holidays.Canada(years=2021)
>>> can
{datetime.date(2021, 1, 1): "New Year's Day", datetime.date(2021, 12, 31): "New Year's Day (Observed)", datetime.date(2021, 2, 15): 'Family Day', datetime.date(2021, 4, 2): 'Good Friday', datetime.date(2021, 5, 24): 'Victoria Day', datetime.date(2021, 7, 1): 'Canada Day', datetime.date(2021, 8, 2): 'Civic Holiday', datetime.date(2021, 9, 6): 'Labour Day', datetime.date(2021, 10, 11): 'Thanksgiving', datetime.date(2021, 12, 25): 'Christmas Day', datetime.date(2021, 12, 24): 'Christmas Day (Observed)', datetime.date(2021, 12, 27): 'Boxing Day (Observed)'}
>>> can.update({"01-01-2021":"remembrance day"})
>>> can
{datetime.date(2021, 1, 1): "remembrance day, New Year's Day", datetime.date(2021, 12, 31): "New Year's Day (Observed)", datetime.date(2021, 2, 15): 'Family Day', datetime.date(2021, 4, 2): 'Good Friday', datetime.date(2021, 5, 24): 'Victoria Day', datetime.date(2021, 7, 1): 'Canada Day', datetime.date(2021, 8, 2): 'Civic Holiday', datetime.date(2021, 9, 6): 'Labour Day', datetime.date(2021, 10, 11): 'Thanksgiving', datetime.date(2021, 12, 25): 'Christmas Day', datetime.date(2021, 12, 24): 'Christmas Day (Observed)', datetime.date(2021, 12, 27): 'Boxing Day (Observed)'}
>>> type(can)
<class 'holidays.Canada'>
>>> print(type(can))
<class 'holidays.Canada'>
>>> for i in can.items():
	print(i)

	
(datetime.date(2021, 1, 1), "remembrance day, New Year's Day")
(datetime.date(2021, 12, 31), "New Year's Day (Observed)")
(datetime.date(2021, 2, 15), 'Family Day')
(datetime.date(2021, 4, 2), 'Good Friday')
(datetime.date(2021, 5, 24), 'Victoria Day')
(datetime.date(2021, 7, 1), 'Canada Day')
(datetime.date(2021, 8, 2), 'Civic Holiday')
(datetime.date(2021, 9, 6), 'Labour Day')
(datetime.date(2021, 10, 11), 'Thanksgiving')
(datetime.date(2021, 12, 25), 'Christmas Day')
(datetime.date(2021, 12, 24), 'Christmas Day (Observed)')
(datetime.date(2021, 12, 27), 'Boxing Day (Observed)')
>>> from datetime import date
>>> import holidays
>>> datetime.time(12,34,53)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    datetime.time(12,34,53)
NameError: name 'datetime' is not defined
>>> from datetime import datetime
>>> import holidays
>>> now=datetime.now()
>>> print(now.strftime("%H:%M:%S"))
13:29:34
>>> print(now.strftime("%I:%M:%S"))
01:29:34
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex15.py =======
13:32:26
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex15.py =======
01:32:37
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex15.py =======
01:34:30
{datetime.date(2021, 1, 1): "New Year's Day", datetime.date(2021, 1, 26): 'Australia Day', datetime.date(2021, 3, 1): 'Canberra Day', datetime.date(2021, 4, 2): 'Good Friday', datetime.date(2021, 4, 3): 'Easter Saturday', datetime.date(2021, 4, 5): 'Easter Monday', datetime.date(2021, 4, 25): 'Anzac Day', datetime.date(2021, 4, 26): 'Anzac Day (Observed)', datetime.date(2021, 6, 14): "Queen's Birthday", datetime.date(2021, 10, 4): 'Labour Day', datetime.date(2021, 12, 25): 'Christmas Day', datetime.date(2021, 12, 27): 'Christmas Day (Observed)', datetime.date(2021, 12, 26): 'Boxing Day', datetime.date(2021, 12, 28): 'Boxing Day (Observed)'}
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex15.py =======
01:35:11
{datetime.date(2021, 1, 1): "New Year's Day", datetime.date(2021, 1, 26): 'Australia Day', datetime.date(2021, 3, 1): 'Canberra Day', datetime.date(2021, 4, 2): 'Good Friday', datetime.date(2021, 4, 3): 'Easter Saturday', datetime.date(2021, 4, 5): 'Easter Monday', datetime.date(2021, 4, 25): 'Anzac Day', datetime.date(2021, 4, 26): 'Anzac Day (Observed)', datetime.date(2021, 6, 14): "Queen's Birthday", datetime.date(2021, 10, 4): 'Labour Day', datetime.date(2021, 12, 25): 'Christmas Day', datetime.date(2021, 12, 27): 'Christmas Day (Observed)', datetime.date(2021, 12, 26): 'Boxing Day', datetime.date(2021, 12, 28): 'Boxing Day (Observed)'}
{datetime.date(2021, 1, 1): "New Year's Day", datetime.date(2021, 1, 26): 'Australia Day', datetime.date(2021, 3, 1): 'Canberra Day', datetime.date(2021, 4, 2): 'Good Friday', datetime.date(2021, 4, 3): 'Easter Saturday', datetime.date(2021, 4, 5): 'Easter Monday', datetime.date(2021, 4, 25): 'Anzac Day', datetime.date(2021, 4, 26): 'Anzac Day (Observed)', datetime.date(2021, 6, 14): "Queen's Birthday", datetime.date(2021, 10, 4): 'Labour Day', datetime.date(2021, 12, 25): 'Christmas Day', datetime.date(2021, 12, 27): 'Christmas Day (Observed)', datetime.date(2021, 12, 26): 'Boxing Day', datetime.date(2021, 12, 28): 'Boxing Day (Observed)'}
{datetime.date(2021, 1, 1): "New Year's Day", datetime.date(2021, 1, 26): 'Australia Day', datetime.date(2021, 3, 1): 'Canberra Day', datetime.date(2021, 4, 2): 'Good Friday', datetime.date(2021, 4, 3): 'Easter Saturday', datetime.date(2021, 4, 5): 'Easter Monday', datetime.date(2021, 4, 25): 'Anzac Day', datetime.date(2021, 4, 26): 'Anzac Day (Observed)', datetime.date(2021, 6, 14): "Queen's Birthday", datetime.date(2021, 10, 4): 'Labour Day', datetime.date(2021, 12, 25): 'Christmas Day', datetime.date(2021, 12, 27): 'Christmas Day (Observed)', datetime.date(2021, 12, 26): 'Boxing Day', datetime.date(2021, 12, 28): 'Boxing Day (Observed)'}
{datetime.date(2021, 1, 1): "New Year's Day", datetime.date(2021, 1, 26): 'Australia Day', datetime.date(2021, 3, 1): 'Canberra Day', datetime.date(2021, 4, 2): 'Good Friday', datetime.date(2021, 4, 3): 'Easter Saturday', datetime.date(2021, 4, 5): 'Easter Monday', datetime.date(2021, 4, 25): 'Anzac Day', datetime.date(2021, 4, 26): 'Anzac Day (Observed)', datetime.date(2021, 6, 14): "Queen's Birthday", datetime.date(2021, 10, 4): 'Labour Day', datetime.date(2021, 12, 25): 'Christmas Day', datetime.date(2021, 12, 27): 'Christmas Day (Observed)', datetime.date(2021, 12, 26): 'Boxing Day', datetime.date(2021, 12, 28): 'Boxing Day (Observed)'}
{datetime.date(2021, 1, 1): "New Year's Day", datetime.date(2021, 1, 26): 'Australia Day', datetime.date(2021, 3, 1): 'Canberra Day', datetime.date(2021, 4, 2): 'Good Friday', datetime.date(2021, 4, 3): 'Easter Saturday', datetime.date(2021, 4, 5): 'Easter Monday', datetime.date(2021, 4, 25): 'Anzac Day', datetime.date(2021, 4, 26): 'Anzac Day (Observed)', datetime.date(2021, 6, 14): "Queen's Birthday", datetime.date(2021, 10, 4): 'Labour Day', datetime.date(2021, 12, 25): 'Christmas Day', datetime.date(2021, 12, 27): 'Christmas Day (Observed)', datetime.date(2021, 12, 26): 'Boxing Day', datetime.date(2021, 12, 28): 'Boxing Day (Observed)'}
{datetime.date(2021, 1, 1): "New Year's Day", datetime.date(2021, 1, 26): 'Australia Day', datetime.date(2021, 3, 1): 'Canberra Day', datetime.date(2021, 4, 2): 'Good Friday', datetime.date(2021, 4, 3): 'Easter Saturday', datetime.date(2021, 4, 5): 'Easter Monday', datetime.date(2021, 4, 25): 'Anzac Day', datetime.date(2021, 4, 26): 'Anzac Day (Observed)', datetime.date(2021, 6, 14): "Queen's Birthday", datetime.date(2021, 10, 4): 'Labour Day', datetime.date(2021, 12, 25): 'Christmas Day', datetime.date(2021, 12, 27): 'Christmas Day (Observed)', datetime.date(2021, 12, 26): 'Boxing Day', datetime.date(2021, 12, 28): 'Boxing Day (Observed)'}
{datetime.date(2021, 1, 1): "New Year's Day", datetime.date(2021, 1, 26): 'Australia Day', datetime.date(2021, 3, 1): 'Canberra Day', datetime.date(2021, 4, 2): 'Good Friday', datetime.date(2021, 4, 3): 'Easter Saturday', datetime.date(2021, 4, 5): 'Easter Monday', datetime.date(2021, 4, 25): 'Anzac Day', datetime.date(2021, 4, 26): 'Anzac Day (Observed)', datetime.date(2021, 6, 14): "Queen's Birthday", datetime.date(2021, 10, 4): 'Labour Day', datetime.date(2021, 12, 25): 'Christmas Day', datetime.date(2021, 12, 27): 'Christmas Day (Observed)', datetime.date(2021, 12, 26): 'Boxing Day', datetime.date(2021, 12, 28): 'Boxing Day (Observed)'}
{datetime.date(2021, 1, 1): "New Year's Day", datetime.date(2021, 1, 26): 'Australia Day', datetime.date(2021, 3, 1): 'Canberra Day', datetime.date(2021, 4, 2): 'Good Friday', datetime.date(2021, 4, 3): 'Easter Saturday', datetime.date(2021, 4, 5): 'Easter Monday', datetime.date(2021, 4, 25): 'Anzac Day', datetime.date(2021, 4, 26): 'Anzac Day (Observed)', datetime.date(2021, 6, 14): "Queen's Birthday", datetime.date(2021, 10, 4): 'Labour Day', datetime.date(2021, 12, 25): 'Christmas Day', datetime.date(2021, 12, 27): 'Christmas Day (Observed)', datetime.date(2021, 12, 26): 'Boxing Day', datetime.date(2021, 12, 28): 'Boxing Day (Observed)'}
{datetime.date(2021, 1, 1): "New Year's Day", datetime.date(2021, 1, 26): 'Australia Day', datetime.date(2021, 3, 1): 'Canberra Day', datetime.date(2021, 4, 2): 'Good Friday', datetime.date(2021, 4, 3): 'Easter Saturday', datetime.date(2021, 4, 5): 'Easter Monday', datetime.date(2021, 4, 25): 'Anzac Day', datetime.date(2021, 4, 26): 'Anzac Day (Observed)', datetime.date(2021, 6, 14): "Queen's Birthday", datetime.date(2021, 10, 4): 'Labour Day', datetime.date(2021, 12, 25): 'Christmas Day', datetime.date(2021, 12, 27): 'Christmas Day (Observed)', datetime.date(2021, 12, 26): 'Boxing Day', datetime.date(2021, 12, 28): 'Boxing Day (Observed)'}
{datetime.date(2021, 1, 1): "New Year's Day", datetime.date(2021, 1, 26): 'Australia Day', datetime.date(2021, 3, 1): 'Canberra Day', datetime.date(2021, 4, 2): 'Good Friday', datetime.date(2021, 4, 3): 'Easter Saturday', datetime.date(2021, 4, 5): 'Easter Monday', datetime.date(2021, 4, 25): 'Anzac Day', datetime.date(2021, 4, 26): 'Anzac Day (Observed)', datetime.date(2021, 6, 14): "Queen's Birthday", datetime.date(2021, 10, 4): 'Labour Day', datetime.date(2021, 12, 25): 'Christmas Day', datetime.date(2021, 12, 27): 'Christmas Day (Observed)', datetime.date(2021, 12, 26): 'Boxing Day', datetime.date(2021, 12, 28): 'Boxing Day (Observed)'}
{datetime.date(2021, 1, 1): "New Year's Day", datetime.date(2021, 1, 26): 'Australia Day', datetime.date(2021, 3, 1): 'Canberra Day', datetime.date(2021, 4, 2): 'Good Friday', datetime.date(2021, 4, 3): 'Easter Saturday', datetime.date(2021, 4, 5): 'Easter Monday', datetime.date(2021, 4, 25): 'Anzac Day', datetime.date(2021, 4, 26): 'Anzac Day (Observed)', datetime.date(2021, 6, 14): "Queen's Birthday", datetime.date(2021, 10, 4): 'Labour Day', datetime.date(2021, 12, 25): 'Christmas Day', datetime.date(2021, 12, 27): 'Christmas Day (Observed)', datetime.date(2021, 12, 26): 'Boxing Day', datetime.date(2021, 12, 28): 'Boxing Day (Observed)'}
{datetime.date(2021, 1, 1): "New Year's Day", datetime.date(2021, 1, 26): 'Australia Day', datetime.date(2021, 3, 1): 'Canberra Day', datetime.date(2021, 4, 2): 'Good Friday', datetime.date(2021, 4, 3): 'Easter Saturday', datetime.date(2021, 4, 5): 'Easter Monday', datetime.date(2021, 4, 25): 'Anzac Day', datetime.date(2021, 4, 26): 'Anzac Day (Observed)', datetime.date(2021, 6, 14): "Queen's Birthday", datetime.date(2021, 10, 4): 'Labour Day', datetime.date(2021, 12, 25): 'Christmas Day', datetime.date(2021, 12, 27): 'Christmas Day (Observed)', datetime.date(2021, 12, 26): 'Boxing Day', datetime.date(2021, 12, 28): 'Boxing Day (Observed)'}
{datetime.date(2021, 1, 1): "New Year's Day", datetime.date(2021, 1, 26): 'Australia Day', datetime.date(2021, 3, 1): 'Canberra Day', datetime.date(2021, 4, 2): 'Good Friday', datetime.date(2021, 4, 3): 'Easter Saturday', datetime.date(2021, 4, 5): 'Easter Monday', datetime.date(2021, 4, 25): 'Anzac Day', datetime.date(2021, 4, 26): 'Anzac Day (Observed)', datetime.date(2021, 6, 14): "Queen's Birthday", datetime.date(2021, 10, 4): 'Labour Day', datetime.date(2021, 12, 25): 'Christmas Day', datetime.date(2021, 12, 27): 'Christmas Day (Observed)', datetime.date(2021, 12, 26): 'Boxing Day', datetime.date(2021, 12, 28): 'Boxing Day (Observed)'}
{datetime.date(2021, 1, 1): "New Year's Day", datetime.date(2021, 1, 26): 'Australia Day', datetime.date(2021, 3, 1): 'Canberra Day', datetime.date(2021, 4, 2): 'Good Friday', datetime.date(2021, 4, 3): 'Easter Saturday', datetime.date(2021, 4, 5): 'Easter Monday', datetime.date(2021, 4, 25): 'Anzac Day', datetime.date(2021, 4, 26): 'Anzac Day (Observed)', datetime.date(2021, 6, 14): "Queen's Birthday", datetime.date(2021, 10, 4): 'Labour Day', datetime.date(2021, 12, 25): 'Christmas Day', datetime.date(2021, 12, 27): 'Christmas Day (Observed)', datetime.date(2021, 12, 26): 'Boxing Day', datetime.date(2021, 12, 28): 'Boxing Day (Observed)'}
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex15.py =======
01:35:23
2021-01-01
2021-01-26
2021-03-01
2021-04-02
2021-04-03
2021-04-05
2021-04-25
2021-04-26
2021-06-14
2021-10-04
2021-12-25
2021-12-27
2021-12-26
2021-12-28
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex15.py =======
01:35:38
(datetime.date(2021, 1, 1), "New Year's Day")
(datetime.date(2021, 1, 26), 'Australia Day')
(datetime.date(2021, 3, 1), 'Canberra Day')
(datetime.date(2021, 4, 2), 'Good Friday')
(datetime.date(2021, 4, 3), 'Easter Saturday')
(datetime.date(2021, 4, 5), 'Easter Monday')
(datetime.date(2021, 4, 25), 'Anzac Day')
(datetime.date(2021, 4, 26), 'Anzac Day (Observed)')
(datetime.date(2021, 6, 14), "Queen's Birthday")
(datetime.date(2021, 10, 4), 'Labour Day')
(datetime.date(2021, 12, 25), 'Christmas Day')
(datetime.date(2021, 12, 27), 'Christmas Day (Observed)')
(datetime.date(2021, 12, 26), 'Boxing Day')
(datetime.date(2021, 12, 28), 'Boxing Day (Observed)')
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex15.py =======
01:37:14
(datetime.date(2021, 1, 1), "New Year's Day")
(datetime.date(2021, 1, 26), 'Australia Day')
(datetime.date(2021, 3, 1), 'Canberra Day')
(datetime.date(2021, 4, 2), 'Good Friday')
(datetime.date(2021, 4, 3), 'Easter Saturday')
(datetime.date(2021, 4, 5), 'Easter Monday')
(datetime.date(2021, 4, 25), 'Anzac Day')
(datetime.date(2021, 4, 26), 'Anzac Day (Observed)')
(datetime.date(2021, 6, 14), "Queen's Birthday")
(datetime.date(2021, 10, 4), 'Labour Day')
(datetime.date(2021, 12, 25), 'Christmas Day')
(datetime.date(2021, 12, 27), 'Christmas Day (Observed)')
(datetime.date(2021, 12, 26), 'Boxing Day')
(datetime.date(2021, 12, 28), 'Boxing Day (Observed)')
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex15.py =======
01:37:59
(datetime.date(2021, 1, 1), "New Year's Day")
(datetime.date(2021, 1, 26), 'Australia Day')
(datetime.date(2021, 3, 1), 'Canberra Day')
(datetime.date(2021, 4, 2), 'Good Friday')
(datetime.date(2021, 4, 3), 'Easter Saturday')
(datetime.date(2021, 4, 5), 'Easter Monday')
(datetime.date(2021, 4, 25), 'Anzac Day')
(datetime.date(2021, 4, 26), 'Anzac Day (Observed)')
(datetime.date(2021, 6, 14), "Queen's Birthday")
(datetime.date(2021, 10, 4), 'Labour Day')
(datetime.date(2021, 12, 25), 'Christmas Day')
(datetime.date(2021, 12, 27), 'Christmas Day (Observed)')
(datetime.date(2021, 12, 26), 'Boxing Day')
(datetime.date(2021, 12, 28), 'Boxing Day (Observed)')
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex15.py =======
01:38:35
(datetime.date(2021, 1, 1), "New Year's Day")
(datetime.date(2021, 1, 26), 'Australia Day')
(datetime.date(2021, 3, 1), 'Canberra Day')
(datetime.date(2021, 4, 2), 'Good Friday')
(datetime.date(2021, 4, 3), 'Easter Saturday')
(datetime.date(2021, 4, 5), 'Easter Monday')
(datetime.date(2021, 4, 25), 'Anzac Day')
(datetime.date(2021, 4, 26), 'Anzac Day (Observed)')
(datetime.date(2021, 6, 14), "Queen's Birthday")
(datetime.date(2021, 10, 4), 'Labour Day')
(datetime.date(2021, 12, 25), 'Christmas Day')
(datetime.date(2021, 12, 27), 'Christmas Day (Observed)')
(datetime.date(2021, 12, 26), 'Boxing Day')
(datetime.date(2021, 12, 28), 'Boxing Day (Observed)')
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex15.py =======
Hi i'm yasi this is 2021 year festival days datebase for australia
it's
True or FalseTrue
01:39:52
(datetime.date(2021, 1, 1), "New Year's Day")
(datetime.date(2021, 1, 26), 'Australia Day')
(datetime.date(2021, 3, 1), 'Canberra Day')
(datetime.date(2021, 4, 2), 'Good Friday')
(datetime.date(2021, 4, 3), 'Easter Saturday')
(datetime.date(2021, 4, 5), 'Easter Monday')
(datetime.date(2021, 4, 25), 'Anzac Day')
(datetime.date(2021, 4, 26), 'Anzac Day (Observed)')
(datetime.date(2021, 6, 14), "Queen's Birthday")
(datetime.date(2021, 10, 4), 'Labour Day')
(datetime.date(2021, 12, 25), 'Christmas Day')
(datetime.date(2021, 12, 27), 'Christmas Day (Observed)')
(datetime.date(2021, 12, 26), 'Boxing Day')
(datetime.date(2021, 12, 28), 'Boxing Day (Observed)')
>>> 

======= RESTART: C:/Users/Asus/OneDrive/programs/ex15.py =======
>>> 
Hi i'm yasi this is 2021 year festival days datebase for australia
it's
True or FalseFalse
01:40:05
(datetime.date(2021, 1, 1), "New Year's Day")
(datetime.date(2021, 1, 26), 'Australia Day')
(datetime.date(2021, 3, 1), 'Canberra Day')
(datetime.date(2021, 4, 2), 'Good Friday')
(datetime.date(2021, 4, 3), 'Easter Saturday')
(datetime.date(2021, 4, 5), 'Easter Monday')
(datetime.date(2021, 4, 25), 'Anzac Day')
(datetime.date(2021, 4, 26), 'Anzac Day (Observed)')
(datetime.date(2021, 6, 14), "Queen's Birthday")
(datetime.date(2021, 10, 4), 'Labour Day')
(datetime.date(2021, 12, 25), 'Christmas Day')
(datetime.date(2021, 12, 27), 'Christmas Day (Observed)')
(datetime.date(2021, 12, 26), 'Boxing Day')
(datetime.date(2021, 12, 28), 'Boxing Day (Observed)')
>>> 
= RESTART: C:/Users/Asus/OneDrive/programs/ex15.py =
Hi i'm yasi this is 2021 year festival days datebase for 
Austria
Canada
Denmark
Denmark Austria
please enter the country name :Austria
>>> 