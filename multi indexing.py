Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import io
>>> csv=io.StringIO("""Name,Place,Classes,Tricketprice
                       Rupa,Newdelhi,First class,1000
                       Santhosh,Chennai,Sleeper,950
                       Divya,Lucknow,Second Setting,1200
                       Ram,Mumbai,AC chair car,978""")
>>> data=pd.read_csv(csv)
>>> data
                              Name     Place         Classes  Tricketprice
0                             Rupa  Newdelhi     First class          1000
1                         Santhosh   Chennai         Sleeper           950
2                            Divya   Lucknow  Second Setting          1200
3                              Ram    Mumbai    AC chair car           978
>>> csv
<_io.StringIO object at 0x000001BBC2A53EE0>
>>> type(csv)
<class '_io.StringIO'>
>>> m_i=("Name","Place")
>>> m_i
('Name', 'Place')
>>> m_i=data.set_index("Name","Place")

Warning (from warnings module):
  File "<pyshell#13>", line 1
FutureWarning: In a future version of pandas all arguments of DataFrame.set_index except for the argument 'keys' will be keyword-only
>>> m=data.set_index("Name")
>>> m
                                    Place         Classes  Tricketprice
Name                                                                   
                       Rupa      Newdelhi     First class          1000
                       Santhosh   Chennai         Sleeper           950
                       Divya      Lucknow  Second Setting          1200
                       Ram         Mumbai    AC chair car           978
>>> csv=io.StringIO("""Name,Place,Classes,Tricketprice
Rupa,Newdelhi,First class,1000
Santhosh,Chennai,Sleeper,950
Divya,Lucknow,Second Setting,1200
Ram,Mumbai,AC chair car,978""")
>>> data=pd.read_csv(csv)
>>> data
       Name     Place         Classes  Tricketprice
0      Rupa  Newdelhi     First class          1000
1  Santhosh   Chennai         Sleeper           950
2     Divya   Lucknow  Second Setting          1200
3       Ram    Mumbai    AC chair car           978
>>> csv
<_io.StringIO object at 0x000001BBC2A5C5E0>
>>> type(csv)
<class '_io.StringIO'>
>>> m=data.set_index("Name")
>>> m
             Place         Classes  Tricketprice
Name                                            
Rupa      Newdelhi     First class          1000
Santhosh   Chennai         Sleeper           950
Divya      Lucknow  Second Setting          1200
Ram         Mumbai    AC chair car           978
>>> m.xs("Rupa")
Place              Newdelhi
Classes         First class
Tricketprice           1000
Name: Rupa, dtype: object
>>> m_i=data.set_index(["Name","Place"])
>>> m_i
                          Classes  Tricketprice
Name     Place                                 
Rupa     Newdelhi     First class          1000
Santhosh Chennai          Sleeper           950
Divya    Lucknow   Second Setting          1200
Ram      Mumbai      AC chair car           978
>>> data
       Name     Place         Classes  Tricketprice
0      Rupa  Newdelhi     First class          1000
1  Santhosh   Chennai         Sleeper           950
2     Divya   Lucknow  Second Setting          1200
3       Ram    Mumbai    AC chair car           978
>>> data.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries, 0 to 3
Data columns (total 4 columns):
 #   Column        Non-Null Count  Dtype 
---  ------        --------------  ----- 
 0   Name          4 non-null      object
 1   Place         4 non-null      object
 2   Classes       4 non-null      object
 3   Tricketprice  4 non-null      int64 
dtypes: int64(1), object(3)
memory usage: 256.0+ bytes
>>> m_i.info()
<class 'pandas.core.frame.DataFrame'>
MultiIndex: 4 entries, ('Rupa', 'Newdelhi') to ('Ram', 'Mumbai')
Data columns (total 2 columns):
 #   Column        Non-Null Count  Dtype 
---  ------        --------------  ----- 
 0   Classes       4 non-null      object
 1   Tricketprice  4 non-null      int64 
dtypes: int64(1), object(1)
memory usage: 587.0+ bytes
>>> data
       Name     Place         Classes  Tricketprice
0      Rupa  Newdelhi     First class          1000
1  Santhosh   Chennai         Sleeper           950
2     Divya   Lucknow  Second Setting          1200
3       Ram    Mumbai    AC chair car           978
>>> m_i
                          Classes  Tricketprice
Name     Place                                 
Rupa     Newdelhi     First class          1000
Santhosh Chennai          Sleeper           950
Divya    Lucknow   Second Setting          1200
Ram      Mumbai      AC chair car           978
>>> m_i.Tricketprice
Name      Place   
Rupa      Newdelhi    1000
Santhosh  Chennai      950
Divya     Lucknow     1200
Ram       Mumbai       978
Name: Tricketprice, dtype: int64
>>> m_i.columns
Index(['Classes', 'Tricketprice'], dtype='object')
>>> m_i.dtypes
Classes         object
Tricketprice     int64
dtype: object
>>> m_i.items()
<generator object DataFrame.items at 0x000001BBC2A46D60>
>>> for i in m_i.dtypes():
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    for i in m_i.dtypes():
TypeError: 'Series' object is not callable
>>> for i in m_i.dtypes:
	print(i)

	
object
int64
>>> m_i.xs("Santhosh")
         Classes  Tricketprice
Place                         
Chennai  Sleeper           950
>>> m_i.xs("Divya")
                Classes  Tricketprice
Place                                
Lucknow  Second Setting          1200
>>> m_i.loc[Rupa,:]
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    m_i.loc[Rupa,:]
NameError: name 'Rupa' is not defined
>>> m_i.loc['Rupa',:]
              Classes  Tricketprice
Place                              
Newdelhi  First class          1000
>>> m_i.loc['Rupa':,:]
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    m_i.loc['Rupa':,:]
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 925, in __getitem__
    return self._getitem_tuple(key)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 1100, in _getitem_tuple
    return self._getitem_lowerdim(tup)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 822, in _getitem_lowerdim
    return self._getitem_nested_tuple(tup)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 906, in _getitem_nested_tuple
    obj = getattr(obj, self.name)._getitem_axis(key, axis=axis)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 1142, in _getitem_axis
    return self._get_slice_axis(key, axis=axis)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 1176, in _get_slice_axis
    indexer = labels.slice_indexer(slice_obj.start, slice_obj.stop, slice_obj.step)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 5686, in slice_indexer
    start_slice, end_slice = self.slice_locs(start, end, step=step)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\multi.py", line 2793, in slice_locs
    return super().slice_locs(start, end, step)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 5888, in slice_locs
    start_slice = self.get_slice_bound(start, "left")
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\multi.py", line 2737, in get_slice_bound
    return self._partial_tup_index(label, side=side)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\multi.py", line 2797, in _partial_tup_index
    raise UnsortedIndexError(
pandas.errors.UnsortedIndexError: 'Key length (1) was greater than MultiIndex lexsort depth (0)'
>>> 


>>> 

>>> 
>>> m_i
                          Classes  Tricketprice
Name     Place                                 
Rupa     Newdelhi     First class          1000
Santhosh Chennai          Sleeper           950
Divya    Lucknow   Second Setting          1200
Ram      Mumbai      AC chair car           978
>>> m_i.loc["Rupa":"Divya",:]
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    m_i.loc["Rupa":"Divya",:]
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 925, in __getitem__
    return self._getitem_tuple(key)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 1100, in _getitem_tuple
    return self._getitem_lowerdim(tup)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 822, in _getitem_lowerdim
    return self._getitem_nested_tuple(tup)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 906, in _getitem_nested_tuple
    obj = getattr(obj, self.name)._getitem_axis(key, axis=axis)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 1142, in _getitem_axis
    return self._get_slice_axis(key, axis=axis)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 1176, in _get_slice_axis
    indexer = labels.slice_indexer(slice_obj.start, slice_obj.stop, slice_obj.step)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 5686, in slice_indexer
    start_slice, end_slice = self.slice_locs(start, end, step=step)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\multi.py", line 2793, in slice_locs
    return super().slice_locs(start, end, step)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 5888, in slice_locs
    start_slice = self.get_slice_bound(start, "left")
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\multi.py", line 2737, in get_slice_bound
    return self._partial_tup_index(label, side=side)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\multi.py", line 2797, in _partial_tup_index
    raise UnsortedIndexError(
pandas.errors.UnsortedIndexError: 'Key length (1) was greater than MultiIndex lexsort depth (0)'
>>> m_i
                          Classes  Tricketprice
Name     Place                                 
Rupa     Newdelhi     First class          1000
Santhosh Chennai          Sleeper           950
Divya    Lucknow   Second Setting          1200
Ram      Mumbai      AC chair car           978
>>> m_i.loc["Rupa","Divya",:]
Traceback (most recent call last):
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 3361, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas\_libs\index.pyx", line 76, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 5198, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 5206, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Divya'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    m_i.loc["Rupa","Divya",:]
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 925, in __getitem__
    return self._getitem_tuple(key)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 1100, in _getitem_tuple
    return self._getitem_lowerdim(tup)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 822, in _getitem_lowerdim
    return self._getitem_nested_tuple(tup)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 892, in _getitem_nested_tuple
    return self._getitem_axis(tup, axis=axis)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 1157, in _getitem_axis
    locs = labels.get_locs(key)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\multi.py", line 3349, in get_locs
    self.get_loc_level(k, level=i, drop_level=False)[0]
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\multi.py", line 3011, in get_loc_level
    return self._get_loc_level(key, level=level, drop_level=drop_level)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\multi.py", line 3112, in _get_loc_level
    indexer = self._get_level_indexer(key, level=level)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\multi.py", line 3204, in _get_level_indexer
    idx = self._get_loc_single_level_index(level_index, key)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\multi.py", line 2855, in _get_loc_single_level_index
    return level_index.get_loc(key)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 3363, in get_loc
    raise KeyError(key) from err
KeyError: 'Divya'
>>> m_i
                          Classes  Tricketprice
Name     Place                                 
Rupa     Newdelhi     First class          1000
Santhosh Chennai          Sleeper           950
Divya    Lucknow   Second Setting          1200
Ram      Mumbai      AC chair car           978
>>> m_i.loc[("Rupa",),:]

Warning (from warnings module):
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 925
    return self._getitem_tuple(key)
PerformanceWarning: indexing past lexsort depth may impact performance.
              Classes  Tricketprice
Place                              
Newdelhi  First class          1000
>>> m.loc["Rupa",["Classes"]]
Classes    First class
Name: Rupa, dtype: object
>>> m.loc["Rupa","Classes"]
'First class'
>>> m.loc[:,"Classes"]
Name
Rupa           First class
Santhosh           Sleeper
Divya       Second Setting
Ram           AC chair car
Name: Classes, dtype: object
>>> m.loc[:,:]
             Place         Classes  Tricketprice
Name                                            
Rupa      Newdelhi     First class          1000
Santhosh   Chennai         Sleeper           950
Divya      Lucknow  Second Setting          1200
Ram         Mumbai    AC chair car           978
>>> m.loc[["Divya","Santhosh"],["Classes"]]
                 Classes
Name                    
Divya     Second Setting
Santhosh         Sleeper
>>> m.iat[1,1]
'Sleeper'
>>> m_i.iat[1,1]
950
>>> m_i.iat[3,0]
'AC chair car'
>>> m.loc["Rupa","Classes"]="FC"
>>> m_i.loc["Rupa","Classes"]="FC"
>>> m_i
                          Classes  Tricketprice
Name     Place                                 
Rupa     Newdelhi              FC          1000
Santhosh Chennai          Sleeper           950
Divya    Lucknow   Second Setting          1200
Ram      Mumbai      AC chair car           978
>>> m.loc["Ram"].iat[0,1]
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    m.loc["Ram"].iat[0,1]
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 2222, in __getitem__
    return self.obj._get_value(*key, takeable=self._takeable)
TypeError: _get_value() got multiple values for argument 'takeable'
>>> m_i.loc["Ram"].iat[0,1]
978
>>> m_i.loc["Ram"].iat[0,0]
'AC chair car'
>>> m_i.loc["Rupa"].iat[0,0]
'FC'
>>> m_i.loc[("Rupa","Newdelhi"),:]
Classes           FC
Tricketprice    1000
Name: (Rupa, Newdelhi), dtype: object
>>> m_i.loc[("Rupa"),:]
         Classes  Tricketprice
Place                         
Newdelhi      FC          1000
>>> m_i.loc[("Rupa",),:]

Warning (from warnings module):
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 925
    return self._getitem_tuple(key)
PerformanceWarning: indexing past lexsort depth may impact performance.
         Classes  Tricketprice
Place                         
Newdelhi      FC          1000
>>> m_i.xs("Nmae")
Traceback (most recent call last):
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 3361, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas\_libs\index.pyx", line 76, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 5198, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 5206, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Nmae'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    m_i.xs("Nmae")
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\generic.py", line 3767, in xs
    loc, new_index = index._get_loc_level(
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\multi.py", line 3112, in _get_loc_level
    indexer = self._get_level_indexer(key, level=level)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\multi.py", line 3204, in _get_level_indexer
    idx = self._get_loc_single_level_index(level_index, key)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\multi.py", line 2855, in _get_loc_single_level_index
    return level_index.get_loc(key)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 3363, in get_loc
    raise KeyError(key) from err
KeyError: 'Nmae'
>>> m_i.xs("Ram")
             Classes  Tricketprice
Place                             
Mumbai  AC chair car           978
>>> m_i.index.names
FrozenList(['Name', 'Place'])
>>> m_i.index.name
>>> x=m_i.index.name
>>> x
>>> m_i.index.levels
FrozenList([['Divya', 'Ram', 'Rupa', 'Santhosh'], ['Chennai', 'Lucknow', 'Mumbai', 'Newdelhi']])
>>> dm.xs("Mumbai",level="Ticketprice")
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    dm.xs("Mumbai",level="Ticketprice")
NameError: name 'dm' is not defined
>>> m_i.xs("Mumbai",level="Ticketprice")
Traceback (most recent call last):
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\multi.py", line 1523, in _get_level_number
    level = self.names.index(level)
ValueError: 'Ticketprice' is not in list

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    m_i.xs("Mumbai",level="Ticketprice")
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\generic.py", line 3745, in xs
    loc, new_ax = labels.get_loc_level(key, level=level, drop_level=drop_level)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\multi.py", line 3008, in get_loc_level
    level = self._get_level_number(level)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\multi.py", line 1526, in _get_level_number
    raise KeyError(f"Level {level} not found") from err
KeyError: 'Level Ticketprice not found'
>>> m_i
                          Classes  Tricketprice
Name     Place                                 
Rupa     Newdelhi              FC          1000
Santhosh Chennai          Sleeper           950
Divya    Lucknow   Second Setting          1200
Ram      Mumbai      AC chair car           978
>>> m_i.xs("Mumbai",level="Tricketprice")
Traceback (most recent call last):
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\multi.py", line 1523, in _get_level_number
    level = self.names.index(level)
ValueError: 'Tricketprice' is not in list

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    m_i.xs("Mumbai",level="Tricketprice")
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\generic.py", line 3745, in xs
    loc, new_ax = labels.get_loc_level(key, level=level, drop_level=drop_level)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\multi.py", line 3008, in get_loc_level
    level = self._get_level_number(level)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\multi.py", line 1526, in _get_level_number
    raise KeyError(f"Level {level} not found") from err
KeyError: 'Level Tricketprice not found'
>>> m_i.xs("Ram",level="Tricketprice")
Traceback (most recent call last):
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\multi.py", line 1523, in _get_level_number
    level = self.names.index(level)
ValueError: 'Tricketprice' is not in list

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    m_i.xs("Ram",level="Tricketprice")
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\generic.py", line 3745, in xs
    loc, new_ax = labels.get_loc_level(key, level=level, drop_level=drop_level)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\multi.py", line 3008, in get_loc_level
    level = self._get_level_number(level)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\multi.py", line 1526, in _get_level_number
    raise KeyError(f"Level {level} not found") from err
KeyError: 'Level Tricketprice not found'
>>> m_i.index.values
array([('Rupa', 'Newdelhi'), ('Santhosh', 'Chennai'),
       ('Divya', 'Lucknow'), ('Ram', 'Mumbai')], dtype=object)
>>> m=data.set_index(["Name","Place"]).sort_index()
>>> m
                          Classes  Tricketprice
Name     Place                                 
Divya    Lucknow   Second Setting          1200
Ram      Mumbai      AC chair car           978
Rupa     Newdelhi     First class          1000
Santhosh Chennai          Sleeper           950
>>> m_i.reset_index()
       Name     Place         Classes  Tricketprice
0      Rupa  Newdelhi              FC          1000
1  Santhosh   Chennai         Sleeper           950
2     Divya   Lucknow  Second Setting          1200
3       Ram    Mumbai    AC chair car           978
>>> 
=== RESTART: C:/Users/Asus/OneDrive/programs/csv file download.py ==
>>> 
=== RESTART: C:/Users/Asus/OneDrive/programs/csv file download.py ==
<IPython.core.display.HTML object>
>>> mi= pd.MultiIndex.from_arrays([['Networking', 'Cryptography', 
                                     'Anthropology', 'Science'], 
                                             [88, 84, 98, 95]])
>>> mi
MultiIndex([(  'Networking', 88),
            ('Cryptography', 84),
            ('Anthropology', 98),
            (     'Science', 95)],
           )
>>> midx.droplevel(level = 0)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    midx.droplevel(level = 0)
NameError: name 'midx' is not defined
>>> mi.droplevel(level = 0)
Int64Index([88, 84, 98, 95], dtype='int64')
>>> 