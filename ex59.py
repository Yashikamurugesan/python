Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> pd.Series(['a', 'b', 'a', 'c'], dtype=t)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    pd.Series(['a', 'b', 'a', 'c'], dtype=t)
NameError: name 't' is not defined
>>> pd.Series(['a', 'b', 'a', 'c'], dtype=True)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    pd.Series(['a', 'b', 'a', 'c'], dtype=True)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\series.py", line 373, in __init__
    dtype = self._validate_dtype(dtype)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\generic.py", line 439, in _validate_dtype
    dtype = pandas_dtype(dtype)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\dtypes\common.py", line 1776, in pandas_dtype
    npdtype = np.dtype(dtype)
TypeError: Cannot interpret 'True' as a data type
>>> pd.Series(['a', 'b', 'a', 'c'])
0    a
1    b
2    a
3    c
dtype: object
>>> t=pd.CategoricalDtype(categories=['b','a',ordered=True)
		      
SyntaxError: invalid syntax
>>> 
KeyboardInterrupt
>>> t = pd.CategoricalDtype(categories=['b', 'a'], ordered=True)
>>> pd.Series(['a', 'b', 'a', 'c'])
0    a
1    b
2    a
3    c
dtype: object
>>> t = pd.CategoricalDtype(categories=['b', 'a'], ordered=True)
>>> pd.Series(['a', 'b', 'a', 'c'],dtype=t)
0      a
1      b
2      a
3    NaN
dtype: category
Categories (2, object): ['b' < 'a']
>>> t=pd.DataFrame({"Name":['keerthi','yasi','riya','meenu','ajay'],"Age":[30,20,23,26,19],"Gender":['male','female','female','female','male'],"Phone no":[23456,45678,23466,78905,45202]})
>>> t
      Name  Age  Gender  Phone no
0  keerthi   30    male     23456
1     yasi   20  female     45678
2     riya   23  female     23466
3    meenu   26  female     78905
4     ajay   19    male     45202
>>> t.Gender
0      male
1    female
2    female
3    female
4      male
Name: Gender, dtype: object
>>> t.index
RangeIndex(start=0, stop=5, step=1)
>>> t.dtypes
Name        object
Age          int64
Gender      object
Phone no     int64
dtype: object
>>> t.info
<bound method DataFrame.info of       Name  Age  Gender  Phone no
0  keerthi   30    male     23456
1     yasi   20  female     45678
2     riya   23  female     23466
3    meenu   26  female     78905
4     ajay   19    male     45202>
>>> t.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 4 columns):
 #   Column    Non-Null Count  Dtype 
---  ------    --------------  ----- 
 0   Name      5 non-null      object
 1   Age       5 non-null      int64 
 2   Gender    5 non-null      object
 3   Phone no  5 non-null      int64 
dtypes: int64(2), object(2)
memory usage: 288.0+ bytes
>>> data=t.astype({"Age":"int32"})
>>> data
      Name  Age  Gender  Phone no
0  keerthi   30    male     23456
1     yasi   20  female     45678
2     riya   23  female     23466
3    meenu   26  female     78905
4     ajay   19    male     45202
>>> data.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 4 columns):
 #   Column    Non-Null Count  Dtype 
---  ------    --------------  ----- 
 0   Name      5 non-null      object
 1   Age       5 non-null      int32 
 2   Gender    5 non-null      object
 3   Phone no  5 non-null      int64 
dtypes: int32(1), int64(1), object(2)
memory usage: 268.0+ bytes
>>> Age=int32
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Age=int32
NameError: name 'int32' is not defined
>>> "Age"="int32"
SyntaxError: cannot assign to literal
>>> Age="int32"
>>> t.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 4 columns):
 #   Column    Non-Null Count  Dtype 
---  ------    --------------  ----- 
 0   Name      5 non-null      object
 1   Age       5 non-null      int64 
 2   Gender    5 non-null      object
 3   Phone no  5 non-null      int64 
dtypes: int64(2), object(2)
memory usage: 288.0+ bytes
>>> t[Age]="int32"
>>> t.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 5 columns):
 #   Column    Non-Null Count  Dtype 
---  ------    --------------  ----- 
 0   Name      5 non-null      object
 1   Age       5 non-null      int64 
 2   Gender    5 non-null      object
 3   Phone no  5 non-null      int64 
 4   int32     5 non-null      object
dtypes: int64(2), object(3)
memory usage: 328.0+ bytes
>>> t.Age="int32"
>>> t
      Name    Age  Gender  Phone no  int32
0  keerthi  int32    male     23456  int32
1     yasi  int32  female     45678  int32
2     riya  int32  female     23466  int32
3    meenu  int32  female     78905  int32
4     ajay  int32    male     45202  int32
>>> t=pd.DataFrame({"Name":['keerthi','yasi','riya','meenu','ajay'],"Age":[30,20,23,26,19],"Gender":['male','female','female','female','male'],"Phone no":[23456,45678,23466,78905,45202]},dtype="category")
>>> t
      Name Age  Gender Phone no
0  keerthi  30    male    23456
1     yasi  20  female    45678
2     riya  23  female    23466
3    meenu  26  female    78905
4     ajay  19    male    45202
>>> t.dtypes
Name        category
Age         category
Gender      category
Phone no    category
dtype: object
>>> t=pd.DataFrame({"Name":['keerthi','yasi','riya','meenu','ajay'],"Age":[30,20,23,26,19],"Gender":['male','female','female','female','male'],"Phone no":[23456,45678,23466,78905,45202]},dtype="category")
>>> t['Age'] = t['Age'].astype('category')
>>> t=pd.DataFrame({"Name":['keerthi','yasi','riya','meenu','ajay'],"Age":[30,20,23,26,19],"Gender":['male','female','female','female','male'],"Phone no":[23456,45678,23466,78905,45202]},dtype="category")
>>> t['Gender'] = t['Gender'].astype('category')
>>> t
      Name Age  Gender Phone no
0  keerthi  30    male    23456
1     yasi  20  female    45678
2     riya  23  female    23466
3    meenu  26  female    78905
4     ajay  19    male    45202
>>> import numpy as np
>>> t=pd.DataFrame({"Name":['keerthi','yasi','riya','meenu','ajay'],"Age":[30,20,23,26,19],"Gender":['male','female','female','female','male'],"Phone no":[23456,45678,23466,78905,45202]},dtype="category")
>>> t
      Name Age  Gender Phone no
0  keerthi  30    male    23456
1     yasi  20  female    45678
2     riya  23  female    23466
3    meenu  26  female    78905
4     ajay  19    male    45202
>>> t.set_index('Gender')
           Name Age Phone no
Gender                      
male    keerthi  30    23456
female     yasi  20    45678
female     riya  23    23466
female    meenu  26    78905
male       ajay  19    45202
>>> t
      Name Age  Gender Phone no
0  keerthi  30    male    23456
1     yasi  20  female    45678
2     riya  23  female    23466
3    meenu  26  female    78905
4     ajay  19    male    45202
>>> d=t.set_index('Gender')
>>> d
           Name Age Phone no
Gender                      
male    keerthi  30    23456
female     yasi  20    45678
female     riya  23    23466
female    meenu  26    78905
male       ajay  19    45202
>>> d[Gender]="male"
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    d[Gender]="male"
NameError: name 'Gender' is not defined
>>> Categories('female'