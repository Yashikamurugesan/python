Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> df=pd.DataFrame([[1,2,3],[5,6,7],[8,9,10]])
>>> df
   0  1   2
0  1  2   3
1  5  6   7
2  8  9  10
>>> df.at[1,0]
5
>>> df.at[2,1]
9
>>> df.loc[2].at[2]
10
>>> df.loc[1,2]
7
>>> df.iat[0,1]
2
>>> df.loc[0],iat[1]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    df.loc[0],iat[1]
NameError: name 'iat' is not defined
>>> df.iat[0,1]=10
>>> df
   0   1   2
0  1  10   3
1  5   6   7
2  8   9  10
>>> df.loc[0].iat[1]
10
>>> #datafram.insert
>>> df.insert(0,3,[36,92,56])
>>> df
    3  0   1   2
0  36  1  10   3
1  92  5   6   7
2  56  8   9  10
>>> df.insert(4,4,[86,56,24])
>>> df
    3  0   1   2   4
0  36  1  10   3  86
1  92  5   6   7  56
2  56  8   9  10  24
>>> df.insert(5,5,pd.Series([5,6,8]))
>>> df
    3  0   1   2   4  5
0  36  1  10   3  86  5
1  92  5   6   7  56  6
2  56  8   9  10  24  8
>>> df.empty
False
>>> df.isna()
       3      0      1      2      4      5
0  False  False  False  False  False  False
1  False  False  False  False  False  False
2  False  False  False  False  False  False
>>> df.dropna()
    3  0   1   2   4  5
0  36  1  10   3  86  5
1  92  5   6   7  56  6
2  56  8   9  10  24  8
>>> import pandas as pd
>>> df = pd.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]],index=[4, 5, 6], columns=['A', 'B', 'C'])
>>> df
    A   B   C
4   0   2   3
5   0   4   1
6  10  20  30
>>> import pandas as pd
>>> df = pd.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]],index=[1, 2, 3], columns=['X', 'Y', 'Z'])
