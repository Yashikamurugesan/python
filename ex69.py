Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> import pandas as pd
>>> data=pd.to_datetime("23rd september 2021")
>>> data
Timestamp('2021-09-23 00:00:00')
>>> data=pd.to_datetime("23 09 2021")
>>> data
Timestamp('2021-09-23 00:00:00')
>>> day=pd.Timestamp("23 09 2021")
>>> day
Timestamp('2021-09-23 00:00:00')
>>> day.day_name()
'Thursday'
>>> day=pd.Timestamp("22 09 2021")
>>> day.day_name()
'Wednesday'
>>> pd.Series(range(3), index=pd.date_range("2022", freq="D"))
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    pd.Series(range(3), index=pd.date_range("2022", freq="D"))
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\datetimes.py", line 1096, in date_range
    dtarr = DatetimeArray._generate_range(
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\arrays\datetimes.py", line 402, in _generate_range
    raise ValueError(
ValueError: Of the four parameters: start, end, periods, and freq, exactly three must be specified
>>> pd.Series(range(3), index=pd.date_range("2022", freq="D",, periods=3))
SyntaxError: invalid syntax
>>> pd.Series(range(3), index=pd.date_range("2022", freq="D", periods=3))
2022-01-01    0
2022-01-02    1
2022-01-03    2
Freq: D, dtype: int64
>>> data = pd.date_range('1/1/2011', periods = 10, freq ='H')
>>> data
DatetimeIndex(['2011-01-01 00:00:00', '2011-01-01 01:00:00',
               '2011-01-01 02:00:00', '2011-01-01 03:00:00',
               '2011-01-01 04:00:00', '2011-01-01 05:00:00',
               '2011-01-01 06:00:00', '2011-01-01 07:00:00',
               '2011-01-01 08:00:00', '2011-01-01 09:00:00'],
              dtype='datetime64[ns]', freq='H')
>>> data = pd.date_range('01/09/2022', periods = 10, freq ='H')
>>> data
DatetimeIndex(['2022-01-09 00:00:00', '2022-01-09 01:00:00',
               '2022-01-09 02:00:00', '2022-01-09 03:00:00',
               '2022-01-09 04:00:00', '2022-01-09 05:00:00',
               '2022-01-09 06:00:00', '2022-01-09 07:00:00',
               '2022-01-09 08:00:00', '2022-01-09 09:00:00'],
              dtype='datetime64[ns]', freq='H')
>>> data = pd.date_range('01/09/2022', periods = 10, freq ='D')
>>> data
DatetimeIndex(['2022-01-09', '2022-01-10', '2022-01-11', '2022-01-12',
               '2022-01-13', '2022-01-14', '2022-01-15', '2022-01-16',
               '2022-01-17', '2022-01-18'],
              dtype='datetime64[ns]', freq='D')
>>> x= pd.DataFrame()
>>> x
Empty DataFrame
Columns: []
Index: []
>>> x['date'] = pd.date_range('1/1/2011', periods = 72, freq ='H')
>>> x[:4]
                 date
0 2011-01-01 00:00:00
1 2011-01-01 01:00:00
2 2011-01-01 02:00:00
3 2011-01-01 03:00:00
>>> x['date'] = pd.date_range('1/9/2021', periods = 72, freq ='H')
>>> x[3:7]
                 date
3 2021-01-09 03:00:00
4 2021-01-09 04:00:00
5 2021-01-09 05:00:00
6 2021-01-09 06:00:00
>>> import datetime as dt
>>> x['year']=x['year'].dt.year
Traceback (most recent call last):
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 3361, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas\_libs\index.pyx", line 76, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 5198, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 5206, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'year'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    x['year']=x['year'].dt.year
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 3455, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 3363, in get_loc
    raise KeyError(key) from err
KeyError: 'year'
>>> x['year']=x['date'].dt.year
>>> x['month']=x['date'].dt.year
>>> x['day']=x['date'].dt.year
>>> x['hour']=x['date'].dt.year
>>> x['year']=x['date'].dt.year
>>> x['month']=x['date'].dt.month
>>> x['day']=x['date'].dt.day
>>> x['hour']=x['date'].dt.hour
>>> x.head(3)
                 date  year  month  day  hour
0 2021-01-09 00:00:00  2021      1    9     0
1 2021-01-09 01:00:00  2021      1    9     1
2 2021-01-09 02:00:00  2021      1    9     2
>>> x.head(10)
                 date  year  month  day  hour
0 2021-01-09 00:00:00  2021      1    9     0
1 2021-01-09 01:00:00  2021      1    9     1
2 2021-01-09 02:00:00  2021      1    9     2
3 2021-01-09 03:00:00  2021      1    9     3
4 2021-01-09 04:00:00  2021      1    9     4
5 2021-01-09 05:00:00  2021      1    9     5
6 2021-01-09 06:00:00  2021      1    9     6
7 2021-01-09 07:00:00  2021      1    9     7
8 2021-01-09 08:00:00  2021      1    9     8
9 2021-01-09 09:00:00  2021      1    9     9
>>> url = 'http://bit.ly/uforeports'
>>> data=pd.read_csv(url)
>>> data
                       City Colors Reported  ... State              Time
0                    Ithaca             NaN  ...    NY    6/1/1930 22:00
1               Willingboro             NaN  ...    NJ   6/30/1930 20:00
2                   Holyoke             NaN  ...    CO   2/15/1931 14:00
3                   Abilene             NaN  ...    KS    6/1/1931 13:00
4      New York Worlds Fair             NaN  ...    NY   4/18/1933 19:00
...                     ...             ...  ...   ...               ...
18236            Grant Park             NaN  ...    IL  12/31/2000 23:00
18237           Spirit Lake             NaN  ...    IA  12/31/2000 23:00
18238           Eagle River             NaN  ...    WI  12/31/2000 23:45
18239           Eagle River             RED  ...    WI  12/31/2000 23:45
18240                  Ybor             NaN  ...    FL  12/31/2000 23:59

[18241 rows x 5 columns]
>>> data.head()
                   City Colors Reported Shape Reported State             Time
0                Ithaca             NaN       TRIANGLE    NY   6/1/1930 22:00
1           Willingboro             NaN          OTHER    NJ  6/30/1930 20:00
2               Holyoke             NaN           OVAL    CO  2/15/1931 14:00
3               Abilene             NaN           DISK    KS   6/1/1931 13:00
4  New York Worlds Fair             NaN          LIGHT    NY  4/18/1933 19:00
>>> data['Time']=pd.to_datetime(data.Time)
>>> data.head(5)
                   City Colors Reported  ... State                Time
0                Ithaca             NaN  ...    NY 1930-06-01 22:00:00
1           Willingboro             NaN  ...    NJ 1930-06-30 20:00:00
2               Holyoke             NaN  ...    CO 1931-02-15 14:00:00
3               Abilene             NaN  ...    KS 1931-06-01 13:00:00
4  New York Worlds Fair             NaN  ...    NY 1933-04-18 19:00:00

[5 rows x 5 columns]
>>> data.dtypes
City                       object
Colors Reported            object
Shape Reported             object
State                      object
Time               datetime64[ns]
dtype: object
>>> 