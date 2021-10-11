Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import numpy as np
>>> d1=pd.DataFrame({"Name":["Sathish","Sivam","Mani","Yashika"],"Food":["Rice","Rice","Wheet","Grain"]})
>>> d1
      Name   Food
0  Sathish   Rice
1    Sivam   Rice
2     Mani  Wheet
3  Yashika  Grain
>>> d2=pd.DataFrame({"Name":["Sindhu","Arjun","Susil","Arun"],"Drinks":["Mango","Grapes","Apple","Melon"]})
>>> d2
     Name  Drinks
0  Sindhu   Mango
1   Arjun  Grapes
2   Susil   Apple
3    Arun   Melon
>>> D1,D2=np.meshgrid(d1,d2)
>>> d1
      Name   Food
0  Sathish   Rice
1    Sivam   Rice
2     Mani  Wheet
3  Yashika  Grain
>>> d2
     Name  Drinks
0  Sindhu   Mango
1   Arjun  Grapes
2   Susil   Apple
3    Arun   Melon
>>> D1
array([['Sathish', 'Rice', 'Sivam', 'Rice', 'Mani', 'Wheet', 'Yashika',
        'Grain'],
       ['Sathish', 'Rice', 'Sivam', 'Rice', 'Mani', 'Wheet', 'Yashika',
        'Grain'],
       ['Sathish', 'Rice', 'Sivam', 'Rice', 'Mani', 'Wheet', 'Yashika',
        'Grain'],
       ['Sathish', 'Rice', 'Sivam', 'Rice', 'Mani', 'Wheet', 'Yashika',
        'Grain'],
       ['Sathish', 'Rice', 'Sivam', 'Rice', 'Mani', 'Wheet', 'Yashika',
        'Grain'],
       ['Sathish', 'Rice', 'Sivam', 'Rice', 'Mani', 'Wheet', 'Yashika',
        'Grain'],
       ['Sathish', 'Rice', 'Sivam', 'Rice', 'Mani', 'Wheet', 'Yashika',
        'Grain'],
       ['Sathish', 'Rice', 'Sivam', 'Rice', 'Mani', 'Wheet', 'Yashika',
        'Grain']], dtype=object)
>>> D2
array([['Sindhu', 'Sindhu', 'Sindhu', 'Sindhu', 'Sindhu', 'Sindhu',
        'Sindhu', 'Sindhu'],
       ['Mango', 'Mango', 'Mango', 'Mango', 'Mango', 'Mango', 'Mango',
        'Mango'],
       ['Arjun', 'Arjun', 'Arjun', 'Arjun', 'Arjun', 'Arjun', 'Arjun',
        'Arjun'],
       ['Grapes', 'Grapes', 'Grapes', 'Grapes', 'Grapes', 'Grapes',
        'Grapes', 'Grapes'],
       ['Susil', 'Susil', 'Susil', 'Susil', 'Susil', 'Susil', 'Susil',
        'Susil'],
       ['Apple', 'Apple', 'Apple', 'Apple', 'Apple', 'Apple', 'Apple',
        'Apple'],
       ['Arun', 'Arun', 'Arun', 'Arun', 'Arun', 'Arun', 'Arun', 'Arun'],
       ['Melon', 'Melon', 'Melon', 'Melon', 'Melon', 'Melon', 'Melon',
        'Melon']], dtype=object)
>>> d1.loc[0:2]
      Name   Food
0  Sathish   Rice
1    Sivam   Rice
2     Mani  Wheet
>>> d1.loc[0:2,["Name"]]
      Name
0  Sathish
1    Sivam
2     Mani
>>> d1.loc[0:2,["Food"]]
    Food
0   Rice
1   Rice
2  Wheet
>>> d1.loc[0:,["Food"]]
    Food
0   Rice
1   Rice
2  Wheet
3  Grain
>>> d1.loc[0:,["Food","Name"]]
    Food     Name
0   Rice  Sathish
1   Rice    Sivam
2  Wheet     Mani
3  Grain  Yashika
>>> d1.loc[[1,2],["Name"]]
    Name
1  Sivam
2   Mani
>>> d1.loc[[1,2],["Name","Food"]]
    Name   Food
1  Sivam   Rice
2   Mani  Wheet
>>> d1.loc[3,:]
Name    Yashika
Food      Grain
Name: 3, dtype: object
>>> d1.loc[2,:]
Name     Mani
Food    Wheet
Name: 2, dtype: object
>>> d1.iloc[0:3],[2]
(      Name   Food
0  Sathish   Rice
1    Sivam   Rice
2     Mani  Wheet, [2])
>>> d2.at[1,'Sivam']
Traceback (most recent call last):
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 3361, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas\_libs\index.pyx", line 76, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 5198, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 5206, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Sivam'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    d2.at[1,'Sivam']
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 2275, in __getitem__
    return super().__getitem__(key)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 2222, in __getitem__
    return self.obj._get_value(*key, takeable=self._takeable)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 3565, in _get_value
    series = self._get_item_cache(col)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 3879, in _get_item_cache
    loc = self.columns.get_loc(item)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 3363, in get_loc
    raise KeyError(key) from err
KeyError: 'Sivam'
>>> d2
     Name  Drinks
0  Sindhu   Mango
1   Arjun  Grapes
2   Susil   Apple
3    Arun   Melon
>>> d2.iloc[1,'Grapes']
Traceback (most recent call last):
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 754, in _has_valid_tuple
    self._validate_key(k, i)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 1426, in _validate_key
    raise ValueError(f"Can only index by location with a [{self._valid_types}]")
ValueError: Can only index by location with a [integer, integer slice (START point is INCLUDED, END point is EXCLUDED), listlike of integers, boolean array]

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    d2.iloc[1,'Grapes']
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 925, in __getitem__
    return self._getitem_tuple(key)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 1506, in _getitem_tuple
    self._has_valid_tuple(tup)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 756, in _has_valid_tuple
    raise ValueError(
ValueError: Location based indexing can only have [integer, integer slice (START point is INCLUDED, END point is EXCLUDED), listlike of integers, boolean array] types
>>> d2.at[1,'Grapes']
Traceback (most recent call last):
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 3361, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas\_libs\index.pyx", line 76, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 5198, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 5206, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Grapes'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    d2.at[1,'Grapes']
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 2275, in __getitem__
    return super().__getitem__(key)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 2222, in __getitem__
    return self.obj._get_value(*key, takeable=self._takeable)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 3565, in _get_value
    series = self._get_item_cache(col)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 3879, in _get_item_cache
    loc = self.columns.get_loc(item)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 3363, in get_loc
    raise KeyError(key) from err
KeyError: 'Grapes'
>>> d2
     Name  Drinks
0  Sindhu   Mango
1   Arjun  Grapes
2   Susil   Apple
3    Arun   Melon
>>> d2.at[1,0]
Traceback (most recent call last):
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 3361, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas\_libs\index.pyx", line 76, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 5198, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 5206, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 0

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    d2.at[1,0]
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 2275, in __getitem__
    return super().__getitem__(key)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 2222, in __getitem__
    return self.obj._get_value(*key, takeable=self._takeable)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 3565, in _get_value
    series = self._get_item_cache(col)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 3879, in _get_item_cache
    loc = self.columns.get_loc(item)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 3363, in get_loc
    raise KeyError(key) from err
KeyError: 0
>>> d2.at[1,"Name"]
'Arjun'
>>> d2.at[2,"Drink"]
Traceback (most recent call last):
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 3361, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas\_libs\index.pyx", line 76, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 5198, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 5206, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Drink'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    d2.at[2,"Drink"]
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 2275, in __getitem__
    return super().__getitem__(key)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 2222, in __getitem__
    return self.obj._get_value(*key, takeable=self._takeable)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 3565, in _get_value
    series = self._get_item_cache(col)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 3879, in _get_item_cache
    loc = self.columns.get_loc(item)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 3363, in get_loc
    raise KeyError(key) from err
KeyError: 'Drink'
>>> d2.at[2,"Drinks"]
'Apple'
>>> d2.at[1,"Name"]
'Arjun'
>>> d2.iat[1,0]
'Arjun'
>>> d2.iat[1,1]
'Grapes'
>>> d1.loc[3].at["Name"]
'Yashika'
>>> d1.loc[3].at["Name"]="navetha"
>>> d1
      Name   Food
0  Sathish   Rice
1    Sivam   Rice
2     Mani  Wheet
3  navetha  Grain
>>> d1.empty
False
>>> d2.empty
False
>>> d1.insert(loc=2,column="values",value=[9,2,6,7])
>>> d1
      Name   Food  values
0  Sathish   Rice       9
1    Sivam   Rice       2
2     Mani  Wheet       6
3  navetha  Grain       7
>>> d1.insert(loc=3,column="values",value=[9,2,6,7])
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    d1.insert(loc=3,column="values",value=[9,2,6,7])
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 4409, in insert
    raise ValueError(f"cannot insert {column}, already exists")
ValueError: cannot insert values, already exists
>>> d1.insert(loc=3,column="ID",value=[1,5,3])
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    d1.insert(loc=3,column="ID",value=[1,5,3])
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 4413, in insert
    value = self._sanitize_column(value)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 4504, in _sanitize_column
    com.require_length_match(value, self.index)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\common.py", line 527, in require_length_match
    raise ValueError(
ValueError: Length of values (3) does not match length of index (4)
>>> d1.insert(loc=3,column="ID",value=[1,5,3,NAN])
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    d1.insert(loc=3,column="ID",value=[1,5,3,NAN])
NameError: name 'NAN' is not defined
>>> d1.insert(loc=3,column="ID",value=[1,5,3,NaN])
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    d1.insert(loc=3,column="ID",value=[1,5,3,NaN])
NameError: name 'NaN' is not defined
>>> d1.insert(loc=3,column="ID",value=[1,5,3,'NaN'])
>>> d1
      Name   Food  values   ID
0  Sathish   Rice       9    1
1    Sivam   Rice       2    5
2     Mani  Wheet       6    3
3  navetha  Grain       7  NaN
>>> d1.dropna()
      Name   Food  values   ID
0  Sathish   Rice       9    1
1    Sivam   Rice       2    5
2     Mani  Wheet       6    3
3  navetha  Grain       7  NaN
>>> d1.isna()
    Name   Food  values     ID
0  False  False   False  False
1  False  False   False  False
2  False  False   False  False
3  False  False   False  False
>>> d1.items()
<generator object DataFrame.items at 0x0000022243C06F20>
>>> for i in d1.items()
SyntaxError: invalid syntax
>>> for i in d1.items():
	print(i)

	
('Name', 0    Sathish
1      Sivam
2       Mani
3    navetha
Name: Name, dtype: object)
('Food', 0     Rice
1     Rice
2    Wheet
3    Grain
Name: Food, dtype: object)
('values', 0    9
1    2
2    6
3    7
Name: values, dtype: int64)
('ID', 0      1
1      5
2      3
3    NaN
Name: ID, dtype: object)
>>> d1.iteritems()
<generator object DataFrame.iteritems at 0x0000022243D32BA0>
>>> for i in d1.iteritems():
	print(i)

	
('Name', 0    Sathish
1      Sivam
2       Mani
3    navetha
Name: Name, dtype: object)
('Food', 0     Rice
1     Rice
2    Wheet
3    Grain
Name: Food, dtype: object)
('values', 0    9
1    2
2    6
3    7
Name: values, dtype: int64)
('ID', 0      1
1      5
2      3
3    NaN
Name: ID, dtype: object)
>>> d1
      Name   Food  values   ID
0  Sathish   Rice       9    1
1    Sivam   Rice       2    5
2     Mani  Wheet       6    3
3  navetha  Grain       7  NaN
>>> d1.set_index("Values")
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    d1.set_index("Values")
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\util\_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 5446, in set_index
    raise KeyError(f"None of {missing} are in the columns")
KeyError: "None of ['Values'] are in the columns"
>>> d1.set_index("values")
           Name   Food   ID
values                     
9       Sathish   Rice    1
2         Sivam   Rice    5
6          Mani  Wheet    3
7       navetha  Grain  NaN
>>> d1.index()
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    d1.index()
TypeError: 'RangeIndex' object is not callable
>>> d2.index()
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    d2.index()
TypeError: 'RangeIndex' object is not callable
>>> d1.xs()
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    d1.xs()
TypeError: xs() missing 1 required positional argument: 'key'
>>> 