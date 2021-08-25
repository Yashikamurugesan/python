Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> 
KeyboardInterrupt
>>> import pandas as pd
>>> data= pd.DataFrame({'a': [1, 2] * 3,'b': [True, False] * 3,'c': [1.0, 2.0] * 3})
>>> data
   a      b    c
0  1   True  1.0
1  2  False  2.0
2  1   True  1.0
3  2  False  2.0
4  1   True  1.0
5  2  False  2.0
>>> data.select_dtypes(include='bool')
       b
0   True
1  False
2   True
3  False
4   True
5  False
>>> data.select_dtypes(include='int')
   a
0  1
1  2
2  1
3  2
4  1
5  2
>>> data.select_dtypes(include=['float64'])
     c
0  1.0
1  2.0
2  1.0
3  2.0
4  1.0
5  2.0
>>> data.select_dtypes(include='float')
     c
0  1.0
1  2.0
2  1.0
3  2.0
4  1.0
5  2.0
>>> data.select_dtypes(include='int')
   a
0  1
1  2
2  1
3  2
4  1
5  2
>>> data.select_dtypes(include='int64')
   a
0  1
1  2
2  1
3  2
4  1
5  2
>>> 