Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import numpy as np
>>> t=pd.DataFrame({"Name":['keerthi','yasi','riya','meenu','ajay'],"Age":[30,20,23,26,19],"Gender":['male','female','female','female','male'],"Phone no":[23456,45678,23466,78905,45202]})
>>> d=t.set_index('Gender')
>>> d
           Name  Age  Phone no
Gender                        
male    keerthi   30     23456
female     yasi   20     45678
female     riya   23     23466
female    meenu   26     78905
male       ajay   19     45202
>>> t['Gender'].unique
<bound method Series.unique of 0      male
1    female
2    female
3    female
4      male
Name: Gender, dtype: object>
>>> t['Gender'].unique()
array(['male', 'female'], dtype=object)
>>> t.Age=t.Age.astype(float)
>>> t
      Name   Age  Gender  Phone no
0  keerthi  30.0    male     23456
1     yasi  20.0  female     45678
2     riya  23.0  female     23466
3    meenu  26.0  female     78905
4     ajay  19.0    male     45202
>>> data=pd.read_csv("f://DATA SCIENCE NOTES/nba.csv")
>>> data
                             Name                    Team  Number Position  Age  Height  Weight                College      Salary
0    0               Avery Bradley          Boston ...                                                                            
1    1                 Jae Crowder          Boston ...                                                                            
2    2                John Holland          Boston ...                                                                            
3    3                 R.J. Hunter          Boston ...                                                                            
4    4               Jonas Jerebko          Boston ...                                                                            
..                                                 ...                                                                            
452  452                Trey Lyles               Ut...                                                                            
453  453              Shelvin Mack               Ut...                                                                            
454  454                 Raul Neto               Ut...                                                                            
455  455              Tibor Pleiss               Ut...                                                                            
456  456               Jeff Withey               Ut...                                                                            

[457 rows x 1 columns]
>>> data.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 457 entries, 0 to 456
Data columns (total 1 columns):
 #   Column                                                                                                                          Non-Null Count  Dtype 
---  ------                                                                                                                          --------------  ----- 
 0                            Name                    Team  Number Position  Age  Height  Weight                College      Salary  457 non-null    object
dtypes: object(1)
memory usage: 3.7+ KB
>>> data.info
<bound method DataFrame.info of                              Name                    Team  Number Position  Age  Height  Weight                College      Salary
0    0               Avery Bradley          Boston ...                                                                            
1    1                 Jae Crowder          Boston ...                                                                            
2    2                John Holland          Boston ...                                                                            
3    3                 R.J. Hunter          Boston ...                                                                            
4    4               Jonas Jerebko          Boston ...                                                                            
..                                                 ...                                                                            
452  452                Trey Lyles               Ut...                                                                            
453  453              Shelvin Mack               Ut...                                                                            
454  454                 Raul Neto               Ut...                                                                            
455  455              Tibor Pleiss               Ut...                                                                            
456  456               Jeff Withey               Ut...                                                                            

[457 rows x 1 columns]>
>>> data.dropna(inplace=True)
>>> print(data.dtypes)
                         Name                    Team  Number Position  Age  Height  Weight                College      Salary    object
dtype: object
>>> data["Salary"]= data["Salary"].astype(int)
Traceback (most recent call last):
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 3361, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas\_libs\index.pyx", line 76, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 5198, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 5206, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Salary'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    data["Salary"]= data["Salary"].astype(int)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 3455, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 3363, in get_loc
    raise KeyError(key) from err
KeyError: 'Salary'
>>> data["Age"]= data["Age"].astype(int)
Traceback (most recent call last):
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 3361, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas\_libs\index.pyx", line 76, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 5198, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 5206, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Age'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    data["Age"]= data["Age"].astype(int)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 3455, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 3363, in get_loc
    raise KeyError(key) from err
KeyError: 'Age'
>>> 
KeyboardInterrupt
>>> 
==== RESTART: C:/Users/Asus/OneDrive/programs/ex60.py ====
                             Name                    Team  Number Position  Age  Height  Weight                College      Salary
0    0               Avery Bradley          Boston ...                                                                            
1    1                 Jae Crowder          Boston ...                                                                            
2    2                John Holland          Boston ...                                                                            
3    3                 R.J. Hunter          Boston ...                                                                            
4    4               Jonas Jerebko          Boston ...                                                                            
..                                                 ...                                                                            
452  452                Trey Lyles               Ut...                                                                            
453  453              Shelvin Mack               Ut...                                                                            
454  454                 Raul Neto               Ut...                                                                            
455  455              Tibor Pleiss               Ut...                                                                            
456  456               Jeff Withey               Ut...                                                                            

[457 rows x 1 columns]
Traceback (most recent call last):
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 3361, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas\_libs\index.pyx", line 76, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 5198, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 5206, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Salary'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex60.py", line 6, in <module>
    data["Salary"]= data["Salary"].astype(int)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 3455, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 3363, in get_loc
    raise KeyError(key) from err
KeyError: 'Salary'
>>> data = pd.read_csv("f://DATA SCIENCE NOTES/nba.csv")

>>> data.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 457 entries, 0 to 456
Data columns (total 1 columns):
 #   Column                                                                                                                          Non-Null Count  Dtype 
---  ------                                                                                                                          --------------  ----- 
 0                            Name                    Team  Number Position  Age  Height  Weight                College      Salary  457 non-null    object
dtypes: object(1)
memory usage: 3.7+ KB
>>> print(data.info())
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 457 entries, 0 to 456
Data columns (total 1 columns):
 #   Column                                                                                                                          Non-Null Count  Dtype 
---  ------                                                                                                                          --------------  ----- 
 0                            Name                    Team  Number Position  Age  Height  Weight                College      Salary  457 non-null    object
dtypes: object(1)
memory usage: 3.7+ KB
None
>>> 