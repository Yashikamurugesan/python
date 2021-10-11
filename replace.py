Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import numpy as np
>>> df=pd.DataFrame({"A":[0,1,2,3,4],"B":[5,6,7,8,9],"C":['a','b','c','d','e']})
>>> df
   A  B  C
0  0  5  a
1  1  6  b
2  2  7  c
3  3  8  d
4  4  9  e
>>> df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   A       5 non-null      int64 
 1   B       5 non-null      int64 
 2   C       5 non-null      object
dtypes: int64(2), object(1)
memory usage: 248.0+ bytes
>>> df.dtypes
A     int64
B     int64
C    object
dtype: object
>>> df.replace(0,10)
    A  B  C
0  10  5  a
1   1  6  b
2   2  7  c
3   3  8  d
4   4  9  e
>>> df.B.replace(0,10)
0    5
1    6
2    7
3    8
4    9
Name: B, dtype: int64
>>> df.B.replace(5,10)
0    10
1     6
2     7
3     8
4     9
Name: B, dtype: int64
>>> df.replace([1,5,2],0)
   A  B  C
0  0  0  a
1  0  6  b
2  0  7  c
3  3  8  d
4  4  9  e
>>> df.replace([9,4,'d'],[90,40,'g'])
    A   B  C
0   0   5  a
1   1   6  b
2   2   7  c
3   3   8  g
4  40  90  e
>>> df.replace([2,3],method='bfill')
   A  B  C
0  0  5  a
1  1  6  b
2  4  7  c
3  4  8  d
4  4  9  e
>>> df.replace([2,3],method='pad')
   A  B  C
0  0  5  a
1  1  6  b
2  1  7  c
3  1  8  d
4  4  9  e
>>> df
   A  B  C
0  0  5  a
1  1  6  b
2  2  7  c
3  3  8  d
4  4  9  e
>>> df.replace({0:100,6:600})
     A    B  C
0  100    5  a
1    1  600  b
2    2    7  c
3    3    8  d
4    4    9  e
>>> df.A({'A':3,'C':'a'},100)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    df.A({'A':3,'C':'a'},100)
TypeError: 'Series' object is not callable
>>> df.A({'A':3,'B':'9'},100)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    df.A({'A':3,'B':'9'},100)
TypeError: 'Series' object is not callable
>>> df.A({'A':3,'B':9},100)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    df.A({'A':3,'B':9},100)
TypeError: 'Series' object is not callable
>>> df.replace({'A':3,'B':9},100)
     A    B  C
0    0    5  a
1    1    6  b
2    2    7  c
3  100    8  d
4    4  100  e
>>> df.replace({'A':3,'C':'e'},100)
     A  B    C
0    0  5    a
1    1  6    b
2    2  7    c
3  100  8    d
4    4  9  100
>>> df.replace({'A':0,'B':7,'C':'b'},1000)
      A     B     C
0  1000     5     a
1     1     6  1000
2     2  1000     c
3     3     8     d
4     4     9     e
>>> df.replace({'A':{0:100,4:400}})
     A  B  C
0  100  5  a
1    1  6  b
2    2  7  c
3    3  8  d
4  400  9  e
>>> df.replace({'B':{9:900,5:500}})
   A    B  C
0  0  500  a
1  1    6  b
2  2    7  c
3  3    8  d
4  4  900  e
>>> df.replace({'B':{9:900,5:500}})
   A    B  C
0  0  500  a
1  1    6  b
2  2    7  c
3  3    8  d
4  4  900  e
>>> df=pd.read_csv("f://DATA SCIENCE NOTES/nba.csv")
>>> print(df.head().to_string)
<bound method DataFrame.to_string of                            Name                    Team  Number Position  Age  Height  Weight                College      Salary
0  0               Avery Bradley          Boston ...                                                                            
1  1                 Jae Crowder          Boston ...                                                                            
2  2                John Holland          Boston ...                                                                            
3  3                 R.J. Hunter          Boston ...                                                                            
4  4               Jonas Jerebko          Boston ...                                                                            >
>>> print(df.head().to_string())
                            Name                    Team  Number Position  Age  Height  Weight                College      Salary
0  0               Avery Bradley          Boston Celtics       0       PG   25  06-Feb     180                  Texas   7730337.0
1  1                 Jae Crowder          Boston Celtics      99       SF   25  06-Jun     235              Marquette   6796117.0
2  2                John Holland          Boston Celtics      30       SG   27  06-May     205      Boston University         NaN
3  3                 R.J. Hunter          Boston Celtics      28       SG   22  06-May     185          Georgia State   1148640.0
4  4               Jonas Jerebko          Boston Celtics       8       PF   29  06-Oct     231                    NaN   5000000.0
>>> data=df.head(10).to_string()
>>> data
'                            Name                    Team  Number Position  Age  Height  Weight                College      Salary\n0  0               Avery Bradley          Boston Celtics       0       PG   25  06-Feb     180                  Texas   7730337.0\n1  1                 Jae Crowder          Boston Celtics      99       SF   25  06-Jun     235              Marquette   6796117.0\n2  2                John Holland          Boston Celtics      30       SG   27  06-May     205      Boston University         NaN\n3  3                 R.J. Hunter          Boston Celtics      28       SG   22  06-May     185          Georgia State   1148640.0\n4  4               Jonas Jerebko          Boston Celtics       8       PF   29  06-Oct     231                    NaN   5000000.0\n5  5                Amir Johnson          Boston Celtics      90       PF   29  06-Sep     240                    NaN  12000000.0\n6  6               Jordan Mickey          Boston Celtics      55       PF   21  06-Aug     235                    LSU   1170960.0\n7  7                Kelly Olynyk          Boston Celtics      41        C   25  Jul-00     238                Gonzaga   2165160.0\n8  8                Terry Rozier          Boston Celtics      12       PG   22  06-Feb     190             Louisville   1824360.0\n9  9                Marcus Smart          Boston Celtics      36       PG   22  06-Apr     220         Oklahoma State   3431040.0'
>>> data.replace({"Position":{'PG':'PS'}})
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    data.replace({"Position":{'PG':'PS'}})
TypeError: replace expected at least 2 arguments, got 1
>>> data.replace({"Position":{'PG':'PS','SG':'SP'}})
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    data.replace({"Position":{'PG':'PS','SG':'SP'}})
TypeError: replace expected at least 2 arguments, got 1
>>> data.replace({"Position":'PG','College':'NaN'},0)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    data.replace({"Position":'PG','College':'NaN'},0)
TypeError: replace() argument 1 must be str, not dict
>>> #data.replace({"Position":'PG','College':'NaN'},0)
>>> df[:10]
                           Name                    Team  Number Position  Age  Height  Weight                College      Salary
0  0               Avery Bradley          Boston ...                                                                            
1  1                 Jae Crowder          Boston ...                                                                            
2  2                John Holland          Boston ...                                                                            
3  3                 R.J. Hunter          Boston ...                                                                            
4  4               Jonas Jerebko          Boston ...                                                                            
5  5                Amir Johnson          Boston ...                                                                            
6  6               Jordan Mickey          Boston ...                                                                            
7  7                Kelly Olynyk          Boston ...                                                                            
8  8                Terry Rozier          Boston ...                                                                            
9  9                Marcus Smart          Boston ...                                                                            
>>> data.replace("Boston Celtiics","Omega Warrior")
'                            Name                    Team  Number Position  Age  Height  Weight                College      Salary\n0  0               Avery Bradley          Boston Celtics       0       PG   25  06-Feb     180                  Texas   7730337.0\n1  1                 Jae Crowder          Boston Celtics      99       SF   25  06-Jun     235              Marquette   6796117.0\n2  2                John Holland          Boston Celtics      30       SG   27  06-May     205      Boston University         NaN\n3  3                 R.J. Hunter          Boston Celtics      28       SG   22  06-May     185          Georgia State   1148640.0\n4  4               Jonas Jerebko          Boston Celtics       8       PF   29  06-Oct     231                    NaN   5000000.0\n5  5                Amir Johnson          Boston Celtics      90       PF   29  06-Sep     240                    NaN  12000000.0\n6  6               Jordan Mickey          Boston Celtics      55       PF   21  06-Aug     235                    LSU   1170960.0\n7  7                Kelly Olynyk          Boston Celtics      41        C   25  Jul-00     238                Gonzaga   2165160.0\n8  8                Terry Rozier          Boston Celtics      12       PG   22  06-Feb     190             Louisville   1824360.0\n9  9                Marcus Smart          Boston Celtics      36       PG   22  06-Apr     220         Oklahoma State   3431040.0'
>>> data.replace(to_replace =["Boston Celtics", "Texas"], value ="Omega Warrior")
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    data.replace(to_replace =["Boston Celtics", "Texas"], value ="Omega Warrior")
TypeError: str.replace() takes no keyword arguments
>>> df.replace(to_replace =["Boston Celtics", "Texas"], value ="Omega Warrior")
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
>>> d=df.replace(to_replace =["Boston Celtics", "Texas"], value ="Omega Warrior")
>>> d.head(20).to_string()
'                             Name                    Team  Number Position  Age  Height  Weight                College      Salary\n0   0               Avery Bradley          Boston Celtics       0       PG   25  06-Feb     180                  Texas   7730337.0\n1   1                 Jae Crowder          Boston Celtics      99       SF   25  06-Jun     235              Marquette   6796117.0\n2   2                John Holland          Boston Celtics      30       SG   27  06-May     205      Boston University         NaN\n3   3                 R.J. Hunter          Boston Celtics      28       SG   22  06-May     185          Georgia State   1148640.0\n4   4               Jonas Jerebko          Boston Celtics       8       PF   29  06-Oct     231                    NaN   5000000.0\n5   5                Amir Johnson          Boston Celtics      90       PF   29  06-Sep     240                    NaN  12000000.0\n6   6               Jordan Mickey          Boston Celtics      55       PF   21  06-Aug     235                    LSU   1170960.0\n7   7                Kelly Olynyk          Boston Celtics      41        C   25  Jul-00     238                Gonzaga   2165160.0\n8   8                Terry Rozier          Boston Celtics      12       PG   22  06-Feb     190             Louisville   1824360.0\n9   9                Marcus Smart          Boston Celtics      36       PG   22  06-Apr     220         Oklahoma State   3431040.0\n10  10            Jared Sullinger          Boston Celtics       7        C   24  06-Sep     260             Ohio State   2569260.0\n11  11              Isaiah Thomas          Boston Celtics       4       PG   27  05-Sep     185             Washington   6912869.0\n12  12                Evan Turner          Boston Celtics      11       SG   27  06-Jul     220             Ohio State   3425510.0\n13  13                James Young          Boston Celtics      13       SG   20  06-Jun     215               Kentucky   1749840.0\n14  14               Tyler Zeller          Boston Celtics      44        C   26  Jul-00     253         North Carolina   2616975.0\n15  15           Bojan Bogdanovic           Brooklyn Nets      44       SG   27  06-Aug     216                    NaN   3425510.0\n16  16               Markel Brown           Brooklyn Nets      22       SG   24  06-Mar     190         Oklahoma State    845059.0\n17  17            Wayne Ellington           Brooklyn Nets      21       SG   28  06-Apr     200         North Carolina   1500000.0\n18  18    Rondae Hollis-Jefferson           Brooklyn Nets      24       SG   21  06-Jul     220                Arizona   1335480.0\n19  19               Jarrett Jack           Brooklyn Nets       2       PG   32  06-Mar     200           Georgia Tech   6300000.0'
>>> data.replace(to_replace = np.nan, value =-99999)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    data.replace(to_replace = np.nan, value =-99999)
TypeError: str.replace() takes no keyword arguments
>>> df.replace(to_replace = np.nan, value =-99999)
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
>>> d=df.replace(to_replace = np.nan, value =-99999)
>>> d.head(10).to_string()
'                            Name                    Team  Number Position  Age  Height  Weight                College      Salary\n0  0               Avery Bradley          Boston Celtics       0       PG   25  06-Feb     180                  Texas   7730337.0\n1  1                 Jae Crowder          Boston Celtics      99       SF   25  06-Jun     235              Marquette   6796117.0\n2  2                John Holland          Boston Celtics      30       SG   27  06-May     205      Boston University         NaN\n3  3                 R.J. Hunter          Boston Celtics      28       SG   22  06-May     185          Georgia State   1148640.0\n4  4               Jonas Jerebko          Boston Celtics       8       PF   29  06-Oct     231                    NaN   5000000.0\n5  5                Amir Johnson          Boston Celtics      90       PF   29  06-Sep     240                    NaN  12000000.0\n6  6               Jordan Mickey          Boston Celtics      55       PF   21  06-Aug     235                    LSU   1170960.0\n7  7                Kelly Olynyk          Boston Celtics      41        C   25  Jul-00     238                Gonzaga   2165160.0\n8  8                Terry Rozier          Boston Celtics      12       PG   22  06-Feb     190             Louisville   1824360.0\n9  9                Marcus Smart          Boston Celtics      36       PG   22  06-Apr     220         Oklahoma State   3431040.0'
>>> ata["Age"]= data["Age"].replace(25.0, "Twenty five")
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    ata["Age"]= data["Age"].replace(25.0, "Twenty five")
TypeError: string indices must be integers
>>> data["Age"]= data["Age"].replace(25.0, "Twenty five")
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    data["Age"]= data["Age"].replace(25.0, "Twenty five")
TypeError: string indices must be integers
>>> 