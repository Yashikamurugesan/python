Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> data=pd.read_csv("f://DATA SCIENCE NOTES/nchs.csv")
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
>>> data.shape
(10296, 6)
>>> data.size
61776
>>> data.Deaths
0         2755
1          439
2         4010
3         1604
4        13213
         ...  
10291      273
10292      289
10293      272
10294      245
10295      258
Name: Deaths, Length: 10296, dtype: int64
>>> data.State.to_string()

>>> data.dtypes
Year                         int64
113 Cause Name              object
Cause Name                  object
State                       object
Deaths                       int64
Age-adjusted Death Rate    float64
dtype: object
>>> type(data)
<class 'pandas.core.frame.DataFrame'>
>>> data.ndim
2
>>> data['Year'].unique()
array([2016, 2006, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007,
       2005, 2004, 2003, 2002, 2001, 2000, 1999], dtype=int64)
>>> len(data['Year'].unique())
18
>>> data.State
0           Alabama
1            Alaska
2           Arizona
3          Arkansas
4        California
            ...    
10291       Wyoming
10292       Wyoming
10293       Wyoming
10294       Wyoming
10295       Wyoming
Name: State, Length: 10296, dtype: object
>>> data['State'].unique()
array(['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California',
       'Colorado', 'Connecticut', 'Delaware', 'District of Columbia',
       'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana',
       'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland',
       'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
       'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
       'New Jersey', 'New Mexico', 'New York', 'North Carolina',
       'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
       'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee',
       'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
       'West Virginia', 'Wisconsin', 'Wyoming', 'United States'],
      dtype=object)
>>> data['Deaths','Cause Name'][data['State']!=United States
			    
SyntaxError: invalid syntax
>>> data['Deaths','Cause Name'][data['State']!='United States']
Traceback (most recent call last):
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 3361, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas\_libs\index.pyx", line 76, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 5198, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 5206, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: ('Deaths', 'Cause Name')

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    data['Deaths','Cause Name'][data['State']!='United States']
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 3455, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 3363, in get_loc
    raise KeyError(key) from err
KeyError: ('Deaths', 'Cause Name')
>>> data['Deaths','Cause Name','State'][data['State']!='United States']
Traceback (most recent call last):
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 3361, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas\_libs\index.pyx", line 76, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 5198, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 5206, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: ('Deaths', 'Cause Name', 'State')

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    data['Deaths','Cause Name','State'][data['State']!='United States']
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 3455, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 3363, in get_loc
    raise KeyError(key) from err
KeyError: ('Deaths', 'Cause Name', 'State')
>>> state=data['State'][data['State']!='United States']
>>> state
0           Alabama
1            Alaska
2           Arizona
3          Arkansas
4        California
            ...    
10291       Wyoming
10292       Wyoming
10293       Wyoming
10294       Wyoming
10295       Wyoming
Name: State, Length: 10098, dtype: object
>>> state=data['State'][data['State']!='United States'].unique()
>>> state
array(['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California',
       'Colorado', 'Connecticut', 'Delaware', 'District of Columbia',
       'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana',
       'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland',
       'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
       'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
       'New Jersey', 'New Mexico', 'New York', 'North Carolina',
       'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
       'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee',
       'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
       'West Virginia', 'Wisconsin', 'Wyoming'], dtype=object)
>>> state=data['State'][data['State']!='United States'].to_string()
>>> state

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
>>> data.Deaths.unique()
array([2755,  439, 4010, ..., 2490, 2345, 2159], dtype=int64)
>>> data.Deaths.to_string().unique()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    data.Deaths.to_string().unique()
AttributeError: 'str' object has no attribute 'unique'
>>> data.Deaths.sum()
157803463
>>> data.Deaths.count(2011)

Warning (from warnings module):
  File "<pyshell#29>", line 1
FutureWarning: Using the level keyword in DataFrame and Series aggregations is deprecated and will be removed in a future version. Use groupby instead. ser.count(level=1) should use ser.groupby(level=1).count().
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    data.Deaths.count(2011)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\series.py", line 1937, in count
    raise ValueError("Series.count level is only valid with a MultiIndex")
ValueError: Series.count level is only valid with a MultiIndex
>>> data.Deaths.count(level=None)
10296
>>> data.Deaths.count(None)
10296
>>> data.Deaths.count()
10296
>>> data.Deaths.dropna()
0         2755
1          439
2         4010
3         1604
4        13213
         ...  
10291      273
10292      289
10293      272
10294      245
10295      258
Name: Deaths, Length: 10296, dtype: int64
>>> data.Deaths.dtypes
dtype('int64')
>>> data.Deaths.groupby('Deaths')
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    data.Deaths.groupby('Deaths')
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\series.py", line 1883, in groupby
    return SeriesGroupBy(
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\groupby\groupby.py", line 888, in __init__
    grouper, exclusions, obj = get_grouper(
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\groupby\grouper.py", line 860, in get_grouper
    raise KeyError(gpr)
KeyError: 'Deaths'
>>> data.Deaths.groupby('Deaths')
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    data.Deaths.groupby('Deaths')
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\series.py", line 1883, in groupby
    return SeriesGroupBy(
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\groupby\groupby.py", line 888, in __init__
    grouper, exclusions, obj = get_grouper(
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\groupby\grouper.py", line 860, in get_grouper
    raise KeyError(gpr)
KeyError: 'Deaths'
>>> data.groupby('Deaths')
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001F7F7BDE580>
>>> data.groupby('Deaths').tail
<bound method GroupBy.tail of <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001F7F7BDE8B0>>
>>> d=data.groupby('Deaths').tail
>>> d
<bound method GroupBy.tail of <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001F7F7BDE580>>
>>> d=data.groupby('Deaths').sum
>>> d
<bound method GroupBy.sum of <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001F7F7BDE8B0>>
>>> d=data.groupby('Deaths').sum()
>>> d
         Year  Age-adjusted Death Rate
Deaths                                
21       4014                      9.4
23       4004                     10.9
24       4000                     19.1
28       2003                      8.4
29       2009                      4.4
...       ...                      ...
2515458  2011                    741.3
2543279  2012                    732.8
2596993  2013                    731.9
2626418  2014                    724.6
2712630  2015                    733.1

[5741 rows x 2 columns]
>>> d=data.groupby('Deaths').sum().sort_values
>>> d
<bound method DataFrame.sort_values of          Year  Age-adjusted Death Rate
Deaths                                
21       4014                      9.4
23       4004                     10.9
24       4000                     19.1
28       2003                      8.4
29       2009                      4.4
...       ...                      ...
2515458  2011                    741.3
2543279  2012                    732.8
2596993  2013                    731.9
2626418  2014                    724.6
2712630  2015                    733.1

[5741 rows x 2 columns]>
>>> d=data.groupby('Deaths').sum().sort_values("Deaths",ascending=False,inplace=	True)
>>> d
>>> d=data.groupby('Deaths').sum()
>>> d
         Year  Age-adjusted Death Rate
Deaths                                
21       4014                      9.4
23       4004                     10.9
24       4000                     19.1
28       2003                      8.4
29       2009                      4.4
...       ...                      ...
2515458  2011                    741.3
2543279  2012                    732.8
2596993  2013                    731.9
2626418  2014                    724.6
2712630  2015                    733.1

[5741 rows x 2 columns]
>>> data.sort_values("Deaths",ascending=False,inplace=True)
>>> dt=data.sort_values("Deaths",ascending=False,inplace=True)
>>> dt
>>> print(data.sort_values("Deaths",ascending=False,inplace=True))
None
>>> print(data.sort_values("Year",ascending=False,inplace=True))
None
>>> states=data['State'][data['State']!='United States'].unique()

>>> states
array(['Washington', 'South Carolina', 'Connecticut', 'Pennsylvania',
       'North Carolina', 'Florida', 'Oklahoma', 'Wisconsin', 'Louisiana',
       'Montana', 'Minnesota', 'Illinois', 'Arkansas', 'Kansas',
       'Alabama', 'Maryland', 'Utah', 'Texas', 'Georgia', 'Maine',
       'Hawaii', 'Rhode Island', 'New Mexico', 'Idaho', 'New Hampshire',
       'Colorado', 'Nevada', 'New Jersey', 'Tennessee', 'Alaska',
       'Massachusetts', 'Michigan', 'Iowa', 'Arizona', 'Nebraska',
       'Indiana', 'Kentucky', 'Mississippi', 'Oregon', 'West Virginia',
       'California', 'South Dakota', 'Virginia', 'Delaware', 'New York',
       'Missouri', 'Ohio', 'North Dakota', 'Vermont',
       'District of Columbia', 'Wyoming'], dtype=object)
>>> states=data['State'][data['State','Deaths']!='United States'].unique()
Traceback (most recent call last):
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 3361, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas\_libs\index.pyx", line 76, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 5198, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 5206, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: ('State', 'Deaths')

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    states=data['State'][data['State','Deaths']!='United States'].unique()
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 3455, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 3363, in get_loc
    raise KeyError(key) from err
KeyError: ('State', 'Deaths')
>>> states=data['State','Deaths'][data['State']!='United States'].unique()
Traceback (most recent call last):
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 3361, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas\_libs\index.pyx", line 76, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 5198, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 5206, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: ('State', 'Deaths')

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    states=data['State','Deaths'][data['State']!='United States'].unique()
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 3455, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 3363, in get_loc
    raise KeyError(key) from err
KeyError: ('State', 'Deaths')
>>> states=data[['State','Deaths']][data['State']!='United States'].unique()
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    states=data[['State','Deaths']][data['State']!='United States'].unique()
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\generic.py", line 5478, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'unique'
>>> states=data[[['State','Deaths']]][data['State']!='United States'].unique()
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    states=data[[['State','Deaths']]][data['State']!='United States'].unique()
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 3461, in __getitem__
    indexer = self.loc._get_listlike_indexer(key, axis=1)[1]
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 1314, in _get_listlike_indexer
    self._validate_read_indexer(keyarr, indexer, axis)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 1374, in _validate_read_indexer
    raise KeyError(f"None of [{key}] are in the [{axis_name}]")
KeyError: "None of [Index([('State', 'Deaths')], dtype='object')] are in the [columns]"
>>> 