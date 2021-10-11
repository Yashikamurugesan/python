Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import numpy as np
>>> data=pd.read_csv("f://DATA SCIENCE NOTES/tomany.csv")
>>> data
   Unnamed: 0  Unnamed: 1  Unnamed: 2  ...   JOY  Unnamed: 5              Skill
0         NaN         NaN         NaN  ...  2017         NaN                 CV
1         NaN         NaN         NaN  ...  2016         NaN        programming
2         NaN         NaN         NaN  ...  2018         NaN           Embedded
3         NaN         NaN         NaN  ...  2017         NaN  ThermoEngineering
4         NaN         NaN         NaN  ...  2016         NaN               Data

[5 rows x 7 columns]
>>> data=pd.read_csv("f://DATA SCIENCE NOTES/wther.csv")
>>> data
          day  temperature  windspeed   event
0  01-01-2017         32.0        6.0    Rain
1  01-04-2017          NaN        9.0   Sunny
2  01-05-2017         28.0        NaN    Snow
3  01-06-2017          NaN        7.0     NaN
4  01-07-2017         32.0        NaN    Rain
5  01-08-2017          NaN        NaN   Sunny
6  01-09-2017          NaN        NaN     NaN
7  01-10-2017         34.0        8.0  Cloudy
8  01-11-2017         40.0       12.0   Sunny
>>> data.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 9 entries, 0 to 8
Data columns (total 4 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   day          9 non-null      object 
 1   temperature  5 non-null      float64
 2   windspeed    5 non-null      float64
 3   event        7 non-null      object 
dtypes: float64(2), object(2)
memory usage: 416.0+ bytes
>>> data.dtypes
day             object
temperature    float64
windspeed      float64
event           object
dtype: object
>>> data.at[0,'temperature']
32.0
>>> data.at[0,'day']
'01-01-2017'
>>> data.at[6,'event']
nan
>>> data.iloc[4,2]
nan
>>> data.iloc[4,3]
'Rain'
>>> data.iloc[6,1]
nan
>>> data.iloc[2,6,3,1],['day','windspeed','event']
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    data.iloc[2,6,3,1],['day','windspeed','event']
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 925, in __getitem__
    return self._getitem_tuple(key)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 1506, in _getitem_tuple
    self._has_valid_tuple(tup)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 751, in _has_valid_tuple
    self._validate_key_length(key)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 792, in _validate_key_length
    raise IndexingError("Too many indexers")
pandas.core.indexing.IndexingError: Too many indexers
>>> data.iloc[2],['day','windspeed','event']
(day            01-05-2017
temperature          28.0
windspeed             NaN
event                Snow
Name: 2, dtype: object, ['day', 'windspeed', 'event'])
>>> data.iloc[2:7],['day','windspeed','event']
(          day  temperature  windspeed  event
2  01-05-2017         28.0        NaN   Snow
3  01-06-2017          NaN        7.0    NaN
4  01-07-2017         32.0        NaN   Rain
5  01-08-2017          NaN        NaN  Sunny
6  01-09-2017          NaN        NaN    NaN, ['day', 'windspeed', 'event'])
>>> data.iloc[2:7]
          day  temperature  windspeed  event
2  01-05-2017         28.0        NaN   Snow
3  01-06-2017          NaN        7.0    NaN
4  01-07-2017         32.0        NaN   Rain
5  01-08-2017          NaN        NaN  Sunny
6  01-09-2017          NaN        NaN    NaN
>>> data.iat[2,0]
'01-05-2017'
>>> data.iat[2,3]
'Snow'
>>> data.loc[0].at['windspeed']
6.0
>>> data.loc[7].at['event']
'Cloudy'
>>> data.loc[3,'windspeed']=7.1
>>> data
          day  temperature  windspeed   event
0  01-01-2017         32.0        6.0    Rain
1  01-04-2017          NaN        9.0   Sunny
2  01-05-2017         28.0        NaN    Snow
3  01-06-2017          NaN        7.1     NaN
4  01-07-2017         32.0        NaN    Rain
5  01-08-2017          NaN        NaN   Sunny
6  01-09-2017          NaN        NaN     NaN
7  01-10-2017         34.0        8.0  Cloudy
8  01-11-2017         40.0       12.0   Sunny
>>> data.insert(4,'count',[4,3,3,2,3,2,1,4,4])
>>> data
          day  temperature  windspeed   event  count
0  01-01-2017         32.0        6.0    Rain      4
1  01-04-2017          NaN        9.0   Sunny      3
2  01-05-2017         28.0        NaN    Snow      3
3  01-06-2017          NaN        7.1     NaN      2
4  01-07-2017         32.0        NaN    Rain      3
5  01-08-2017          NaN        NaN   Sunny      2
6  01-09-2017          NaN        NaN     NaN      1
7  01-10-2017         34.0        8.0  Cloudy      4
8  01-11-2017         40.0       12.0   Sunny      4
>>> data.fillna(3)
          day  temperature  windspeed   event  count
0  01-01-2017         32.0        6.0    Rain      4
1  01-04-2017          3.0        9.0   Sunny      3
2  01-05-2017         28.0        3.0    Snow      3
3  01-06-2017          3.0        7.1       3      2
4  01-07-2017         32.0        3.0    Rain      3
5  01-08-2017          3.0        3.0   Sunny      2
6  01-09-2017          3.0        3.0       3      1
7  01-10-2017         34.0        8.0  Cloudy      4
8  01-11-2017         40.0       12.0   Sunny      4
>>> data.backfill()
          day  temperature  windspeed   event  count
0  01-01-2017         32.0        6.0    Rain      4
1  01-04-2017         28.0        9.0   Sunny      3
2  01-05-2017         28.0        7.1    Snow      3
3  01-06-2017         32.0        7.1    Rain      2
4  01-07-2017         32.0        8.0    Rain      3
5  01-08-2017         34.0        8.0   Sunny      2
6  01-09-2017         34.0        8.0  Cloudy      1
7  01-10-2017         34.0        8.0  Cloudy      4
8  01-11-2017         40.0       12.0   Sunny      4
>>> data.backfill()
          day  temperature  windspeed   event  count
0  01-01-2017         32.0        6.0    Rain      4
1  01-04-2017         28.0        9.0   Sunny      3
2  01-05-2017         28.0        7.1    Snow      3
3  01-06-2017         32.0        7.1    Rain      2
4  01-07-2017         32.0        8.0    Rain      3
5  01-08-2017         34.0        8.0   Sunny      2
6  01-09-2017         34.0        8.0  Cloudy      1
7  01-10-2017         34.0        8.0  Cloudy      4
8  01-11-2017         40.0       12.0   Sunny      4
>>> data.bfill()
          day  temperature  windspeed   event  count
0  01-01-2017         32.0        6.0    Rain      4
1  01-04-2017         28.0        9.0   Sunny      3
2  01-05-2017         28.0        7.1    Snow      3
3  01-06-2017         32.0        7.1    Rain      2
4  01-07-2017         32.0        8.0    Rain      3
5  01-08-2017         34.0        8.0   Sunny      2
6  01-09-2017         34.0        8.0  Cloudy      1
7  01-10-2017         34.0        8.0  Cloudy      4
8  01-11-2017         40.0       12.0   Sunny      4
>>>  data.backfill(axis=1)
 
SyntaxError: unexpected indent
>>> data.backfill(axis=1)
          day temperature windspeed   event count
0  01-01-2017        32.0       6.0    Rain     4
1  01-04-2017         9.0       9.0   Sunny     3
2  01-05-2017        28.0      Snow    Snow     3
3  01-06-2017         7.1       7.1       2     2
4  01-07-2017        32.0      Rain    Rain     3
5  01-08-2017       Sunny     Sunny   Sunny     2
6  01-09-2017           1         1       1     1
7  01-10-2017        34.0       8.0  Cloudy     4
8  01-11-2017        40.0      12.0   Sunny     4
>>> data.backfill(axis=1,limit=1)
          day temperature windspeed   event count
0  01-01-2017        32.0       6.0    Rain     4
1  01-04-2017         9.0       9.0   Sunny     3
2  01-05-2017        28.0      Snow    Snow     3
3  01-06-2017         7.1       7.1       2     2
4  01-07-2017        32.0      Rain    Rain     3
5  01-08-2017         NaN     Sunny   Sunny     2
6  01-09-2017         NaN       NaN       1     1
7  01-10-2017        34.0       8.0  Cloudy     4
8  01-11-2017        40.0      12.0   Sunny     4
>>> data.mean()

Warning (from warnings module):
  File "<pyshell#33>", line 1
FutureWarning: Dropping of nuisance columns in DataFrame reductions (with 'numeric_only=None') is deprecated; in a future version this will raise TypeError.  Select only valid columns before calling the reduction.
temperature    33.200000
windspeed       8.420000
count           2.888889
dtype: float64
>>> #data.mean('temperature','windspeed','count')
>>> data.ffill()
          day  temperature  windspeed   event  count
0  01-01-2017         32.0        6.0    Rain      4
1  01-04-2017         32.0        9.0   Sunny      3
2  01-05-2017         28.0        9.0    Snow      3
3  01-06-2017         28.0        7.1    Snow      2
4  01-07-2017         32.0        7.1    Rain      3
5  01-08-2017         32.0        7.1   Sunny      2
6  01-09-2017         32.0        7.1   Sunny      1
7  01-10-2017         34.0        8.0  Cloudy      4
8  01-11-2017         40.0       12.0   Sunny      4
>>> data.pad()
          day  temperature  windspeed   event  count
0  01-01-2017         32.0        6.0    Rain      4
1  01-04-2017         32.0        9.0   Sunny      3
2  01-05-2017         28.0        9.0    Snow      3
3  01-06-2017         28.0        7.1    Snow      2
4  01-07-2017         32.0        7.1    Rain      3
5  01-08-2017         32.0        7.1   Sunny      2
6  01-09-2017         32.0        7.1   Sunny      1
7  01-10-2017         34.0        8.0  Cloudy      4
8  01-11-2017         40.0       12.0   Sunny      4
>>> data.day.dtype
dtype('O')
>>> data.dtypes
day             object
temperature    float64
windspeed      float64
event           object
count            int64
dtype: object
>>> data["event"].fillna("No event")
0        Rain
1       Sunny
2        Snow
3    No event
4        Rain
5       Sunny
6    No event
7      Cloudy
8       Sunny
Name: event, dtype: object
>>> data.replace(to_replace = np.nan, value = -99)
          day  temperature  windspeed   event  count
0  01-01-2017         32.0        6.0    Rain      4
1  01-04-2017        -99.0        9.0   Sunny      3
2  01-05-2017         28.0      -99.0    Snow      3
3  01-06-2017        -99.0        7.1     -99      2
4  01-07-2017         32.0      -99.0    Rain      3
5  01-08-2017        -99.0      -99.0   Sunny      2
6  01-09-2017        -99.0      -99.0     -99      1
7  01-10-2017         34.0        8.0  Cloudy      4
8  01-11-2017         40.0       12.0   Sunny      4
>>> 
KeyboardInterrupt
>>> df.interpolate(method ='linear', limit_direction ='forward")
	       
SyntaxError: EOL while scanning string literal
>>> df.interpolate(method ='linear', limit_direction ='forward')
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    df.interpolate(method ='linear', limit_direction ='forward')
NameError: name 'df' is not defined
>>> data.interpolate(method ='linear', limit_direction ='forward')
          day  temperature  windspeed   event  count
0  01-01-2017    32.000000      6.000    Rain      4
1  01-04-2017    30.000000      9.000   Sunny      3
2  01-05-2017    28.000000      8.050    Snow      3
3  01-06-2017    30.000000      7.100     NaN      2
4  01-07-2017    32.000000      7.325    Rain      3
5  01-08-2017    32.666667      7.550   Sunny      2
6  01-09-2017    33.333333      7.775     NaN      1
7  01-10-2017    34.000000      8.000  Cloudy      4
8  01-11-2017    40.000000     12.000   Sunny      4
>>> df.dropna(how = 'all')
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    df.dropna(how = 'all')
NameError: name 'df' is not defined
>>> data.dropna(how = 'all')
          day  temperature  windspeed   event  count
0  01-01-2017         32.0        6.0    Rain      4
1  01-04-2017          NaN        9.0   Sunny      3
2  01-05-2017         28.0        NaN    Snow      3
3  01-06-2017          NaN        7.1     NaN      2
4  01-07-2017         32.0        NaN    Rain      3
5  01-08-2017          NaN        NaN   Sunny      2
6  01-09-2017          NaN        NaN     NaN      1
7  01-10-2017         34.0        8.0  Cloudy      4
8  01-11-2017         40.0       12.0   Sunny      4
>>> df.dropna(axis = 1)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    df.dropna(axis = 1)
NameError: name 'df' is not defined
>>> data.dropna(axis = 1)
          day  count
0  01-01-2017      4
1  01-04-2017      3
2  01-05-2017      3
3  01-06-2017      2
4  01-07-2017      3
5  01-08-2017      2
6  01-09-2017      1
7  01-10-2017      4
8  01-11-2017      4
>>> data.dropna(axis = 0, how ='any')
          day  temperature  windspeed   event  count
0  01-01-2017         32.0        6.0    Rain      4
7  01-10-2017         34.0        8.0  Cloudy      4
8  01-11-2017         40.0       12.0   Sunny      4
>>> data['Day']= pd.to_datetime(data['Day'])
Traceback (most recent call last):
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 3361, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas\_libs\index.pyx", line 76, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 5198, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 5206, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Day'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    data['Day']= pd.to_datetime(data['Day'])
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 3455, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 3363, in get_loc
    raise KeyError(key) from err
KeyError: 'Day
>>>

>>> data.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 9 entries, 0 to 8
Data columns (total 4 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   day          9 non-null      object 
 1   temperature  5 non-null      float64
 2   windspeed    5 non-null      float64
 3   event        7 non-null      object 
dtypes: float64(2), object(2)
memory usage: 416.0+ bytes
>>> data.day
0    01-01-2017
1    01-04-2017
2    01-05-2017
3    01-06-2017
4    01-07-2017
5    01-08-2017
6    01-09-2017
7    01-10-2017
8    01-11-2017
Name: day, dtype: object

>>> data['day']= pd.to_datetime(data['day'])
>>> data.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 9 entries, 0 to 8
Data columns (total 4 columns):
 #   Column       Non-Null Count  Dtype         
---  ------       --------------  -----         
 0   day          9 non-null      datetime64[ns]
 1   temperature  5 non-null      float64       
 2   windspeed    5 non-null      float64       
 3   event        7 non-null      object        
dtypes: datetime64[ns](1), float64(2), object(1)
memory usage: 416.0+ bytes
>>> 

>>> data['day'] = data['day'].astype('datetime64[ns]')
>>> data
         day  temperature  windspeed   event
0 2017-01-01         32.0        6.0    Rain
1 2017-01-04          NaN        9.0   Sunny
2 2017-01-05         28.0        NaN    Snow
3 2017-01-06          NaN        7.0     NaN
4 2017-01-07         32.0        NaN    Rain
5 2017-01-08          NaN        NaN   Sunny
6 2017-01-09          NaN        NaN     NaN
7 2017-01-10         34.0        8.0  Cloudy
8 2017-01-11         40.0       12.0   Sunny
>>> data.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 9 entries, 0 to 8
Data columns (total 4 columns):
 #   Column       Non-Null Count  Dtype         
---  ------       --------------  -----         
 0   day          9 non-null      datetime64[ns]
 1   temperature  5 non-null      float64       
 2   windspeed    5 non-null      float64       
 3   event        7 non-null      object        
dtypes: datetime64[ns](1), float64(2), object(1)
memory usage: 416.0+ bytes
>>>


>>> data=pd.read_csv("F://DATA SCIENCE NOTES/wther.csv",parse_dates=['day'])
>>> data
         day  temperature  windspeed   event
0 2017-01-01         32.0        6.0    Rain
1 2017-01-04          NaN        9.0   Sunny
2 2017-01-05         28.0        NaN    Snow
3 2017-01-06          NaN        7.0     NaN
4 2017-01-07         32.0        NaN    Rain
5 2017-01-08          NaN        NaN   Sunny
6 2017-01-09          NaN        NaN     NaN
7 2017-01-10         34.0        8.0  Cloudy
8 2017-01-11         40.0       12.0   Sunny
>>> data.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 9 entries, 0 to 8
Data columns (total 4 columns):
 #   Column       Non-Null Count  Dtype         
---  ------       --------------  -----         
 0   day          9 non-null      datetime64[ns]
 1   temperature  5 non-null      float64       
 2   windspeed    5 non-null      float64       
 3   event        7 non-null      object        
dtypes: datetime64[ns](1), float64(2), object(1)
memory usage: 416.0+ bytes
>>>


