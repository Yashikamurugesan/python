Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> data=pd.read_csv("f://DATA SCIENCE NOTES/nchs.csv")
>>> data.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10296 entries, 0 to 10295
Data columns (total 6 columns):
 #   Column                   Non-Null Count  Dtype  
---  ------                   --------------  -----  
 0   Year                     10296 non-null  int64  
 1   113 Cause Name           10296 non-null  object 
 2   Cause Name               10296 non-null  object 
 3   State                    10296 non-null  object 
 4   Deaths                   10296 non-null  int64  
 5   Age-adjusted Death Rate  10296 non-null  float64
dtypes: float64(1), int64(2), object(3)
memory usage: 482.8+ KB
>>> data.Year.loc[2011:2015]
2011    2000
2012    1999
2013    2016
2014    2015
2015    2014
Name: Year, dtype: int64
>>> data.Year.loc[1999:2016]
1999    2012
2000    2011
2001    2010
2002    2009
2003    2008
2004    2007
2005    2006
2006    2005
2007    2004
2008    2003
2009    2002
2010    2001
2011    2000
2012    1999
2013    2016
2014    2015
2015    2014
2016    2013
Name: Year, dtype: int64
>>> len(data.Year)
10296
>>> data.Year.iloc[2014:2016]
2014    2015
2015    2014
Name: Year, dtype: int64
>>> data.Year.loc[2014:2016]
2014    2015
2015    2014
2016    2013
Name: Year, dtype: int64
>>> data.Year.iloc[2000:2016][2013,2014]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    data.Year.iloc[2000:2016][2013,2014]
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\series.py", line 966, in __getitem__
    return self._get_with(key)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\series.py", line 981, in _get_with
    return self._get_values_tuple(key)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\series.py", line 1016, in _get_values_tuple
    raise KeyError("key of type tuple not found and not a MultiIndex")
KeyError: 'key of type tuple not found and not a MultiIndex'
>>> data.Year.iloc[2000:2016],[2013,2014]
(2000    2011
2001    2010
2002    2009
2003    2008
2004    2007
2005    2006
2006    2005
2007    2004
2008    2003
2009    2002
2010    2001
2011    2000
2012    1999
2013    2016
2014    2015
2015    2014
Name: Year, dtype: int64, [2013, 2014])
>>> data.Year.size
10296
>>> data.Year.sort_index()
0        2016
1        2016
2        2016
3        2016
4        2016
         ... 
10291    2003
10292    2002
10293    2001
10294    2000
10295    1999
Name: Year, Length: 10296, dtype: int64
>>> data.Year.sort_index(12)

Warning (from warnings module):
  File "<pyshell#12>", line 1
FutureWarning: In a future version of pandas all arguments of Series.sort_index will be keyword-only
Traceback (most recent call last):
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\generic.py", line 543, in _get_axis_number
    return cls._AXIS_TO_AXIS_NUMBER[axis]
KeyError: 12

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    data.Year.sort_index(12)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\util\_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\series.py", line 3616, in sort_index
    return super().sort_index(
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\generic.py", line 4530, in sort_index
    axis = self._get_axis_number(axis)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\generic.py", line 545, in _get_axis_number
    raise ValueError(f"No axis named {axis} for object type {cls.__name__}")
ValueError: No axis named 12 for object type Series
>>> data.Year.sum()
20669220
>>> data.Year.to_string()

>>> data.set_index('Year')
                                         113 Cause Name  ... Age-adjusted Death Rate
Year                                                     ...                        
2016  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    55.5
2016  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    63.1
2016  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    54.2
2016  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    51.8
2016  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    32.0
...                                                 ...  ...                     ...
2003  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    55.1
2002  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    58.1
2001  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    55.5
2000  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    50.8
1999  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    52.8

[10296 rows x 5 columns]
>>> data
       Year  ... Age-adjusted Death Rate
0      2016  ...                    55.5
1      2016  ...                    63.1
2      2016  ...                    54.2
3      2016  ...                    51.8
4      2016  ...                    32.0
...     ...  ...                     ...
10291  2003  ...                    55.1
10292  2002  ...                    58.1
10293  2001  ...                    55.5
10294  2000  ...                    50.8
10295  1999  ...                    52.8

[10296 rows x 6 columns]
>>> data1=data.set_index('Year')
>>> data
       Year  ... Age-adjusted Death Rate
0      2016  ...                    55.5
1      2016  ...                    63.1
2      2016  ...                    54.2
3      2016  ...                    51.8
4      2016  ...                    32.0
...     ...  ...                     ...
10291  2003  ...                    55.1
10292  2002  ...                    58.1
10293  2001  ...                    55.5
10294  2000  ...                    50.8
10295  1999  ...                    52.8

[10296 rows x 6 columns]
>>> data.set_index('Year')
                                         113 Cause Name  ... Age-adjusted Death Rate
Year                                                     ...                        
2016  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    55.5
2016  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    63.1
2016  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    54.2
2016  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    51.8
2016  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    32.0
...                                                 ...  ...                     ...
2003  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    55.1
2002  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    58.1
2001  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    55.5
2000  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    50.8
1999  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    52.8

[10296 rows x 5 columns]
>>> data.set_index('Year',inplace:True)
SyntaxError: invalid syntax
>>> data.set_index('Year',inplace=True)
>>> data1=data.set_index('Year',inplace=True)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    data1=data.set_index('Year',inplace=True)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\util\_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 5446, in set_index
    raise KeyError(f"None of {missing} are in the columns")
KeyError: "None of ['Year'] are in the columns"
>>> print(data.set_index('Year',inplace=True))
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print(data.set_index('Year',inplace=True))
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\util\_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 5446, in set_index
    raise KeyError(f"None of {missing} are in the columns")
KeyError: "None of ['Year'] are in the columns"
>>> data1=data.set_index(('Year'),inplace=True)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    data1=data.set_index(('Year'),inplace=True)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\util\_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 5446, in set_index
    raise KeyError(f"None of {missing} are in the columns")
KeyError: "None of ['Year'] are in the columns"
>>> data1=data.set_index(['Year'],inplace=True)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    data1=data.set_index(['Year'],inplace=True)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\util\_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 5446, in set_index
    raise KeyError(f"None of {missing} are in the columns")
KeyError: "None of ['Year'] are in the columns"
>>> data1=data.set_index(['Year'])
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    data1=data.set_index(['Year'])
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\util\_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 5446, in set_index
    raise KeyError(f"None of {missing} are in the columns")
KeyError: "None of ['Year'] are in the columns"
>>> data1=data.set_index('Year')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    data1=data.set_index('Year')
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\util\_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 5446, in set_index
    raise KeyError(f"None of {missing} are in the columns")
KeyError: "None of ['Year'] are in the columns"
>>> data.set_index('Year')
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    data.set_index('Year')
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\util\_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 5446, in set_index
    raise KeyError(f"None of {missing} are in the columns")
KeyError: "None of ['Year'] are in the columns"
>>> data.set_index('Year',inplace=True)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    data.set_index('Year',inplace=True)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\util\_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 5446, in set_index
    raise KeyError(f"None of {missing} are in the columns")
KeyError: "None of ['Year'] are in the columns"
>>> data
                                         113 Cause Name  ... Age-adjusted Death Rate
Year                                                     ...                        
2016  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    55.5
2016  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    63.1
2016  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    54.2
2016  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    51.8
2016  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    32.0
...                                                 ...  ...                     ...
2003  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    55.1
2002  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    58.1
2001  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    55.5
2000  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    50.8
1999  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    52.8

[10296 rows x 5 columns]
>>> data.index
Int64Index([2016, 2016, 2016, 2016, 2016, 2016, 2016, 2016, 2016, 2016,
            ...
            2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001, 2000, 1999],
           dtype='int64', name='Year', length=10296)
>>> data.index[2010:2012]
Int64Index([2001, 2000], dtype='int64', name='Year')
>>> data.dtypes
113 Cause Name              object
Cause Name                  object
State                       object
Deaths                       int64
Age-adjusted Death Rate    float64
dtype: object
>>> data
                                         113 Cause Name  ... Age-adjusted Death Rate
Year                                                     ...                        
2016  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    55.5
2016  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    63.1
2016  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    54.2
2016  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    51.8
2016  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    32.0
...                                                 ...  ...                     ...
2003  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    55.1
2002  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    58.1
2001  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    55.5
2000  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    50.8
1999  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    52.8

[10296 rows x 5 columns]
>>> data.reindex()
                                         113 Cause Name  ... Age-adjusted Death Rate
Year                                                     ...                        
2016  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    55.5
2016  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    63.1
2016  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    54.2
2016  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    51.8
2016  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    32.0
...                                                 ...  ...                     ...
2003  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    55.1
2002  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    58.1
2001  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    55.5
2000  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    50.8
1999  Accidents (unintentional injuries) (V01-X59,Y8...  ...                    52.8

[10296 rows x 5 columns]
>>> 