Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> a=[1,2,3]
>>> df=pd.Series(a,index=['x','y','z'])
>>> df
x    1
y    2
z    3
dtype: int64
>>> print(df)
x    1
y    2
z    3
dtype: int64
>>> df=pd.Series(a)
>>> print(df)
0    1
1    2
2    3
dtype: int64
>>> pf=pd.DataFrame({x=(1,2,3),y=(2,3,4)}
		
SyntaxError: invalid syntax
>>> pf=pd.DataFrame({x:(1,2,3),y:(2,3,4)})
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    pf=pd.DataFrame({x:(1,2,3),y:(2,3,4)})
NameError: name 'x' is not defined
>>> pf=pd.DataFrame({'x':(1,2,3),'y':(2,3,4)})
>>> pf
   x  y
0  1  2
1  2  3
2  3  4
>>> pd.DatetimeIndex(PF)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    pd.DatetimeIndex(PF)
NameError: name 'PF' is not defined
>>> pd.DatetimeIndex(pf)
DatetimeIndex(['<DatetimeArray>
['1970-01-01 00:00:00.000000001', '1970-01-01 00:00:00.000000002']
Length: 2, dtype: datetime64[ns]',
               '<DatetimeArray>
['1970-01-01 00:00:00.000000002', '1970-01-01 00:00:00.000000003']
Length: 2, dtype: datetime64[ns]',
               '<DatetimeArray>
['1970-01-01 00:00:00.000000003', '1970-01-01 00:00:00.000000004']
Length: 2, dtype: datetime64[ns]'],
              dtype='datetime64[ns]', freq=None)
>>> 
>>> 