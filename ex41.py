Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> a=[1,2,3,4,5]
>>> a
[1, 2, 3, 4, 5]
>>> data=pd.Series(a,index=['a','s','d','f','g'])
>>> data
a    1
s    2
d    3
f    4
g    5
dtype: int64
>>> type(data)
<class 'pandas.core.series.Series'>
>>> data=pd.Series(a,index=['a','s','d','f','g'],dtype:float)
SyntaxError: positional argument follows keyword argument
>>> data=pd.Series(a,index=['a','s','d','f','g'],dtype=float)
>>> print(data)
a    1.0
s    2.0
d    3.0
f    4.0
g    5.0
dtype: float64
>>> print(data)
a    1.0
s    2.0
d    3.0
f    4.0
g    5.0
dtype: float64
>>> pd.__version__
'1.3.0'
>>> import numpy as np
>>> x=np.arange(10)
>>> x
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> x[0]
0
>>> x
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> x(0)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    x(0)
TypeError: 'numpy.ndarray' object is not callable
>>> data=pd.Series(np.linspace(0,5,10),dtype=int)
>>> data
0    0.000000
1    0.555556
2    1.111111
3    1.666667
4    2.222222
5    2.777778
6    3.333333
7    3.888889
8    4.444444
9    5.000000
dtype: float64
>>> data.values
array([0.        , 0.55555556, 1.11111111, 1.66666667, 2.22222222,
       2.77777778, 3.33333333, 3.88888889, 4.44444444, 5.        ])
>>> data.items
<bound method Series.items of 0    0.000000
1    0.555556
2    1.111111
3    1.666667
4    2.222222
5    2.777778
6    3.333333
7    3.888889
8    4.444444
9    5.000000
dtype: float64>
>>> data.index
RangeIndex(start=0, stop=10, step=1)
>>> data[5]
2.7777777777777777
>>> 
>>> dict={'q','w','e','r'}
>>> data=pd.Series(dict)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    data=pd.Series(dict)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\series.py", line 439, in __init__
    data = sanitize_array(data, index, dtype, copy)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\construction.py", line 560, in sanitize_array
    raise TypeError(f"'{type(data).__name__}' type is unordered")
TypeError: 'set' type is unordered
>>> y=pd.Series(dict)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    y=pd.Series(dict)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\series.py", line 439, in __init__
    data = sanitize_array(data, index, dtype, copy)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\construction.py", line 560, in sanitize_array
    raise TypeError(f"'{type(data).__name__}' type is unordered")
TypeError: 'set' type is unordered
>>> dict{'q':1,'w':2}
SyntaxError: invalid syntax
>>> 
>>> dict={'q':1,'w':2}
>>> y=pd.Series(dict)
>>> y
q    1
w    2
dtype: int64
>>> y=pd.Series(dict,index=['e','q','r','w','u','p'])
>>> print(y)
e    NaN
q    1.0
r    NaN
w    2.0
u    NaN
p    NaN
dtype: float64
>>> x=pd.Series(np.arange(5))
>>> x
0    0
1    1
2    2
3    3
4    4
dtype: int32
>>> x[5]=10
>>> x
0     0
1     1
2     2
3     3
4     4
5    10
dtype: int64
>>> x1=pd.DataFrame(x)
>>> x1
    0
0   0
1   1
2   2
3   3
4   4
5  10
>>> x1.ndim
2
>>> x1.columns
RangeIndex(start=0, stop=1, step=1)
>>> x1.size
6
>>> x1.all(0)
0    False
dtype: bool
>>> x1.all()
0    False
dtype: bool
>>> x1.all(1)
0    False
1     True
2     True
3     True
4     True
5     True
dtype: bool
>>> 