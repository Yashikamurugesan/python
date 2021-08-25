Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> data = pd.DataFrame([[1, 2], [4, 5], [7, 8]],index=['x', 'y', 'z1'],columns=['max_speed', 'shield'])
>>> data.loc['y']
max_speed    4
shield       5
Name: y, dtype: int64
>>> data.loc[['y','x']]
   max_speed  shield
y          4       5
x          1       2
>>> data1 = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
          {'a': 100, 'b': 200, 'c': 300, 'd': 400},
          {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000 }]
>>> data1
[{'a': 1, 'b': 2, 'c': 3, 'd': 4}, {'a': 100, 'b': 200, 'c': 300, 'd': 400}, {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000}]
>>> data=pd.DataFrame(data1)
>>> data
      a     b     c     d
0     1     2     3     4
1   100   200   300   400
2  1000  2000  3000  4000
>>> type(data.iloc[0])
<class 'pandas.core.series.Series'>
>>> data.iloc[0]
a    1
b    2
c    3
d    4
Name: 0, dtype: int64
>>> type(data.iloc[0])
<class 'pandas.core.series.Series'>
>>> type(data.iloc[[0]])
<class 'pandas.core.frame.DataFrame'>
>>> data.iloc[:]
      a     b     c     d
0     1     2     3     4
1   100   200   300   400
2  1000  2000  3000  4000
>>> data.iloc[lambda x:x.index % 2 ==0]
      a     b     c     d
0     1     2     3     4
2  1000  2000  3000  4000
>>> df.iloc[[True, False, True]]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    df.iloc[[True, False, True]]
NameError: name 'df' is not defined
>>> data.iloc[[True, False, True]]
      a     b     c     d
0     1     2     3     4
2  1000  2000  3000  4000
>>> data
      a     b     c     d
0     1     2     3     4
1   100   200   300   400
2  1000  2000  3000  4000
>>> data.iloc[:, [True, False, True, False]]
      a     c
0     1     3
1   100   300
2  1000  3000
>>> data.iloc[:, lambda data: [0, 2]]
      a     c
0     1     3
1   100   300
2  1000  3000
>>> 