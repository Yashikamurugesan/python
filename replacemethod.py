Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import numpy as np
>>> df=pd.read_csv("f://DATA SCIENCE NOTES/nba.csv")
>>> df
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
>>> d=df[:15]
>>> d
                            Name                    Team  Number Position  Age  Height  Weight                College      Salary
0   0               Avery Bradley          Boston ...                                                                            
1   1                 Jae Crowder          Boston ...                                                                            
2   2                John Holland          Boston ...                                                                            
3   3                 R.J. Hunter          Boston ...                                                                            
4   4               Jonas Jerebko          Boston ...                                                                            
5   5                Amir Johnson          Boston ...                                                                            
6   6               Jordan Mickey          Boston ...                                                                            
7   7                Kelly Olynyk          Boston ...                                                                            
8   8                Terry Rozier          Boston ...                                                                            
9   9                Marcus Smart          Boston ...                                                                            
10  10            Jared Sullinger          Boston ...                                                                            
11  11              Isaiah Thomas          Boston ...                                                                            
12  12                Evan Turner          Boston ...                                                                            
13  13                James Young          Boston ...                                                                            
14  14               Tyler Zeller          Boston ...                                                                            
>>> d.to_string()
'                             Name                    Team  Number Position  Age  Height  Weight                College      Salary\n0   0               Avery Bradley          Boston Celtics       0       PG   25  06-Feb     180                  Texas   7730337.0\n1   1                 Jae Crowder          Boston Celtics      99       SF   25  06-Jun     235              Marquette   6796117.0\n2   2                John Holland          Boston Celtics      30       SG   27  06-May     205      Boston University         NaN\n3   3                 R.J. Hunter          Boston Celtics      28       SG   22  06-May     185          Georgia State   1148640.0\n4   4               Jonas Jerebko          Boston Celtics       8       PF   29  06-Oct     231                    NaN   5000000.0\n5   5                Amir Johnson          Boston Celtics      90       PF   29  06-Sep     240                    NaN  12000000.0\n6   6               Jordan Mickey          Boston Celtics      55       PF   21  06-Aug     235                    LSU   1170960.0\n7   7                Kelly Olynyk          Boston Celtics      41        C   25  Jul-00     238                Gonzaga   2165160.0\n8   8                Terry Rozier          Boston Celtics      12       PG   22  06-Feb     190             Louisville   1824360.0\n9   9                Marcus Smart          Boston Celtics      36       PG   22  06-Apr     220         Oklahoma State   3431040.0\n10  10            Jared Sullinger          Boston Celtics       7        C   24  06-Sep     260             Ohio State   2569260.0\n11  11              Isaiah Thomas          Boston Celtics       4       PG   27  05-Sep     185             Washington   6912869.0\n12  12                Evan Turner          Boston Celtics      11       SG   27  06-Jul     220             Ohio State   3425510.0\n13  13                James Young          Boston Celtics      13       SG   20  06-Jun     215               Kentucky   1749840.0\n14  14               Tyler Zeller          Boston Celtics      44        C   26  Jul-00     253         North Carolina   2616975.0'
>>> t=d.to_string()
>>> t
'                             Name                    Team  Number Position  Age  Height  Weight                College      Salary\n0   0               Avery Bradley          Boston Celtics       0       PG   25  06-Feb     180                  Texas   7730337.0\n1   1                 Jae Crowder          Boston Celtics      99       SF   25  06-Jun     235              Marquette   6796117.0\n2   2                John Holland          Boston Celtics      30       SG   27  06-May     205      Boston University         NaN\n3   3                 R.J. Hunter          Boston Celtics      28       SG   22  06-May     185          Georgia State   1148640.0\n4   4               Jonas Jerebko          Boston Celtics       8       PF   29  06-Oct     231                    NaN   5000000.0\n5   5                Amir Johnson          Boston Celtics      90       PF   29  06-Sep     240                    NaN  12000000.0\n6   6               Jordan Mickey          Boston Celtics      55       PF   21  06-Aug     235                    LSU   1170960.0\n7   7                Kelly Olynyk          Boston Celtics      41        C   25  Jul-00     238                Gonzaga   2165160.0\n8   8                Terry Rozier          Boston Celtics      12       PG   22  06-Feb     190             Louisville   1824360.0\n9   9                Marcus Smart          Boston Celtics      36       PG   22  06-Apr     220         Oklahoma State   3431040.0\n10  10            Jared Sullinger          Boston Celtics       7        C   24  06-Sep     260             Ohio State   2569260.0\n11  11              Isaiah Thomas          Boston Celtics       4       PG   27  05-Sep     185             Washington   6912869.0\n12  12                Evan Turner          Boston Celtics      11       SG   27  06-Jul     220             Ohio State   3425510.0\n13  13                James Young          Boston Celtics      13       SG   20  06-Jun     215               Kentucky   1749840.0\n14  14               Tyler Zeller          Boston Celtics      44        C   26  Jul-00     253         North Carolina   2616975.0'
>>> print(t.replace(0,100))
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(t.replace(0,100))
TypeError: replace() argument 1 must be str, not int
>>> t.replace(0,100)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    t.replace(0,100)
TypeError: replace() argument 1 must be str, not int
>>> t
'                             Name                    Team  Number Position  Age  Height  Weight                College      Salary\n0   0               Avery Bradley          Boston Celtics       0       PG   25  06-Feb     180                  Texas   7730337.0\n1   1                 Jae Crowder          Boston Celtics      99       SF   25  06-Jun     235              Marquette   6796117.0\n2   2                John Holland          Boston Celtics      30       SG   27  06-May     205      Boston University         NaN\n3   3                 R.J. Hunter          Boston Celtics      28       SG   22  06-May     185          Georgia State   1148640.0\n4   4               Jonas Jerebko          Boston Celtics       8       PF   29  06-Oct     231                    NaN   5000000.0\n5   5                Amir Johnson          Boston Celtics      90       PF   29  06-Sep     240                    NaN  12000000.0\n6   6               Jordan Mickey          Boston Celtics      55       PF   21  06-Aug     235                    LSU   1170960.0\n7   7                Kelly Olynyk          Boston Celtics      41        C   25  Jul-00     238                Gonzaga   2165160.0\n8   8                Terry Rozier          Boston Celtics      12       PG   22  06-Feb     190             Louisville   1824360.0\n9   9                Marcus Smart          Boston Celtics      36       PG   22  06-Apr     220         Oklahoma State   3431040.0\n10  10            Jared Sullinger          Boston Celtics       7        C   24  06-Sep     260             Ohio State   2569260.0\n11  11              Isaiah Thomas          Boston Celtics       4       PG   27  05-Sep     185             Washington   6912869.0\n12  12                Evan Turner          Boston Celtics      11       SG   27  06-Jul     220             Ohio State   3425510.0\n13  13                James Young          Boston Celtics      13       SG   20  06-Jun     215               Kentucky   1749840.0\n14  14               Tyler Zeller          Boston Celtics      44        C   26  Jul-00     253         North Carolina   2616975.0'
>>> print(t)
                             Name                    Team  Number Position  Age  Height  Weight                College      Salary
0   0               Avery Bradley          Boston Celtics       0       PG   25  06-Feb     180                  Texas   7730337.0
1   1                 Jae Crowder          Boston Celtics      99       SF   25  06-Jun     235              Marquette   6796117.0
2   2                John Holland          Boston Celtics      30       SG   27  06-May     205      Boston University         NaN
3   3                 R.J. Hunter          Boston Celtics      28       SG   22  06-May     185          Georgia State   1148640.0
4   4               Jonas Jerebko          Boston Celtics       8       PF   29  06-Oct     231                    NaN   5000000.0
5   5                Amir Johnson          Boston Celtics      90       PF   29  06-Sep     240                    NaN  12000000.0
6   6               Jordan Mickey          Boston Celtics      55       PF   21  06-Aug     235                    LSU   1170960.0
7   7                Kelly Olynyk          Boston Celtics      41        C   25  Jul-00     238                Gonzaga   2165160.0
8   8                Terry Rozier          Boston Celtics      12       PG   22  06-Feb     190             Louisville   1824360.0
9   9                Marcus Smart          Boston Celtics      36       PG   22  06-Apr     220         Oklahoma State   3431040.0
10  10            Jared Sullinger          Boston Celtics       7        C   24  06-Sep     260             Ohio State   2569260.0
11  11              Isaiah Thomas          Boston Celtics       4       PG   27  05-Sep     185             Washington   6912869.0
12  12                Evan Turner          Boston Celtics      11       SG   27  06-Jul     220             Ohio State   3425510.0
13  13                James Young          Boston Celtics      13       SG   20  06-Jun     215               Kentucky   1749840.0
14  14               Tyler Zeller          Boston Celtics      44        C   26  Jul-00     253         North Carolina   2616975.0
>>> t.replace(180,200)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    t.replace(180,200)
TypeError: replace() argument 1 must be str, not int
>>> print(t.replace({'Weight':{180:200,235:300}}))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(t.replace({'Weight':{180:200,235:300}}))
TypeError: replace expected at least 2 arguments, got 1
>>> print(t.replace({'Weight':180},200))
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(t.replace({'Weight':180},200))
TypeError: replace() argument 1 must be str, not dict
>>> t.replace({180:200})
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    t.replace({180:200})
TypeError: replace expected at least 2 arguments, got 1
>>> t.replace(25,30)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    t.replace(25,30)
TypeError: replace() argument 1 must be str, not int
>>> t.replace("LSU",30)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    t.replace("LSU",30)
TypeError: replace() argument 2 must be str, not int
>>> t.replace({"Age":{25:30}})
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    t.replace({"Age":{25:30}})
TypeError: replace expected at least 2 arguments, got 1
>>> df.replace(to_replace=25,value=30)
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
>>> d
                            Name                    Team  Number Position  Age  Height  Weight                College      Salary
0   0               Avery Bradley          Boston ...                                                                            
1   1                 Jae Crowder          Boston ...                                                                            
2   2                John Holland          Boston ...                                                                            
3   3                 R.J. Hunter          Boston ...                                                                            
4   4               Jonas Jerebko          Boston ...                                                                            
5   5                Amir Johnson          Boston ...                                                                            
6   6               Jordan Mickey          Boston ...                                                                            
7   7                Kelly Olynyk          Boston ...                                                                            
8   8                Terry Rozier          Boston ...                                                                            
9   9                Marcus Smart          Boston ...                                                                            
10  10            Jared Sullinger          Boston ...                                                                            
11  11              Isaiah Thomas          Boston ...                                                                            
12  12                Evan Turner          Boston ...                                                                            
13  13                James Young          Boston ...                                                                            
14  14               Tyler Zeller          Boston ...                                                                            
>>> t=d.to_string()
>>> t
'                             Name                    Team  Number Position  Age  Height  Weight                College      Salary\n0   0               Avery Bradley          Boston Celtics       0       PG   25  06-Feb     180                  Texas   7730337.0\n1   1                 Jae Crowder          Boston Celtics      99       SF   25  06-Jun     235              Marquette   6796117.0\n2   2                John Holland          Boston Celtics      30       SG   27  06-May     205      Boston University         NaN\n3   3                 R.J. Hunter          Boston Celtics      28       SG   22  06-May     185          Georgia State   1148640.0\n4   4               Jonas Jerebko          Boston Celtics       8       PF   29  06-Oct     231                    NaN   5000000.0\n5   5                Amir Johnson          Boston Celtics      90       PF   29  06-Sep     240                    NaN  12000000.0\n6   6               Jordan Mickey          Boston Celtics      55       PF   21  06-Aug     235                    LSU   1170960.0\n7   7                Kelly Olynyk          Boston Celtics      41        C   25  Jul-00     238                Gonzaga   2165160.0\n8   8                Terry Rozier          Boston Celtics      12       PG   22  06-Feb     190             Louisville   1824360.0\n9   9                Marcus Smart          Boston Celtics      36       PG   22  06-Apr     220         Oklahoma State   3431040.0\n10  10            Jared Sullinger          Boston Celtics       7        C   24  06-Sep     260             Ohio State   2569260.0\n11  11              Isaiah Thomas          Boston Celtics       4       PG   27  05-Sep     185             Washington   6912869.0\n12  12                Evan Turner          Boston Celtics      11       SG   27  06-Jul     220             Ohio State   3425510.0\n13  13                James Young          Boston Celtics      13       SG   20  06-Jun     215               Kentucky   1749840.0\n14  14               Tyler Zeller          Boston Celtics      44        C   26  Jul-00     253         North Carolina   2616975.0'
>>> print(t.replace(to_replace=25,value=30))
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(t.replace(to_replace=25,value=30))
TypeError: str.replace() takes no keyword arguments
>>> t.replace(to_replace=25,value=30)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    t.replace(to_replace=25,value=30)
TypeError: str.replace() takes no keyword arguments
>>> s= pd.DataFrame({"name":["William","Emma","Sofia","Markus","Edward","Thomas","Ethan","Olivia","Arun","Anika","Paulo"],"region":["East",'N',"East","South","West","West","S","West","West","East","South"],"sales":[50000,52000,90000,-1,42000,72000,49000,-1,67000,65000,67000],"expenses":[42000,43000,-999,44000,38000,39000,42000,-1,39000,44000,45000]})
>>> s
       name region  sales  expenses
0   William   East  50000     42000
1      Emma      N  52000     43000
2     Sofia   East  90000      -999
3    Markus  South     -1     44000
4    Edward   West  42000     38000
5    Thomas   West  72000     39000
6     Ethan      S  49000     42000
7    Olivia   West     -1        -1
8      Arun   West  67000     39000
9     Anika   East  65000     44000
10    Paulo  South  67000     45000
>>> s.replace(50000,10000)
       name region  sales  expenses
0   William   East  10000     42000
1      Emma      N  52000     43000
2     Sofia   East  90000      -999
3    Markus  South     -1     44000
4    Edward   West  42000     38000
5    Thomas   West  72000     39000
6     Ethan      S  49000     42000
7    Olivia   West     -1        -1
8      Arun   West  67000     39000
9     Anika   East  65000     44000
10    Paulo  South  67000     45000
>>> s.replace({'sales':{50000:10000}})
       name region  sales  expenses
0   William   East  10000     42000
1      Emma      N  52000     43000
2     Sofia   East  90000      -999
3    Markus  South     -1     44000
4    Edward   West  42000     38000
5    Thomas   West  72000     39000
6     Ethan      S  49000     42000
7    Olivia   West     -1        -1
8      Arun   West  67000     39000
9     Anika   East  65000     44000
10    Paulo  South  67000     45000
>>> s.replace({"sales":-1,"expenses":-1},0)
       name region  sales  expenses
0   William   East  50000     42000
1      Emma      N  52000     43000
2     Sofia   East  90000      -999
3    Markus  South      0     44000
4    Edward   West  42000     38000
5    Thomas   West  72000     39000
6     Ethan      S  49000     42000
7    Olivia   West      0         0
8      Arun   West  67000     39000
9     Anika   East  65000     44000
10    Paulo  South  67000     45000
>>> s.replace({'N':'North'})
       name region  sales  expenses
0   William   East  50000     42000
1      Emma  North  52000     43000
2     Sofia   East  90000      -999
3    Markus  South     -1     44000
4    Edward   West  42000     38000
5    Thomas   West  72000     39000
6     Ethan      S  49000     42000
7    Olivia   West     -1        -1
8      Arun   West  67000     39000
9     Anika   East  65000     44000
10    Paulo  South  67000     45000
>>> s.replace(to_replace = -1, value = np.NaN)
       name region    sales  expenses
0   William   East  50000.0   42000.0
1      Emma      N  52000.0   43000.0
2     Sofia   East  90000.0    -999.0
3    Markus  South      NaN   44000.0
4    Edward   West  42000.0   38000.0
5    Thomas   West  72000.0   39000.0
6     Ethan      S  49000.0   42000.0
7    Olivia   West      NaN       NaN
8      Arun   West  67000.0   39000.0
9     Anika   East  65000.0   44000.0
10    Paulo  South  67000.0   45000.0
>>> s.replace(-1,np.NaN)
       name region    sales  expenses
0   William   East  50000.0   42000.0
1      Emma      N  52000.0   43000.0
2     Sofia   East  90000.0    -999.0
3    Markus  South      NaN   44000.0
4    Edward   West  42000.0   38000.0
5    Thomas   West  72000.0   39000.0
6     Ethan      S  49000.0   42000.0
7    Olivia   West      NaN       NaN
8      Arun   West  67000.0   39000.0
9     Anika   East  65000.0   44000.0
10    Paulo  South  67000.0   45000.0
>>> s.replace('s',np.NaN)
       name region  sales  expenses
0   William   East  50000     42000
1      Emma      N  52000     43000
2     Sofia   East  90000      -999
3    Markus  South     -1     44000
4    Edward   West  42000     38000
5    Thomas   West  72000     39000
6     Ethan      S  49000     42000
7    Olivia   West     -1        -1
8      Arun   West  67000     39000
9     Anika   East  65000     44000
10    Paulo  South  67000     45000
>>> s.replace('S',np.NaN)
       name region  sales  expenses
0   William   East  50000     42000
1      Emma      N  52000     43000
2     Sofia   East  90000      -999
3    Markus  South     -1     44000
4    Edward   West  42000     38000
5    Thomas   West  72000     39000
6     Ethan    NaN  49000     42000
7    Olivia   West     -1        -1
8      Arun   West  67000     39000
9     Anika   East  65000     44000
10    Paulo  South  67000     45000
>>> s.replace([-1,-999],np.NaN)
       name region    sales  expenses
0   William   East  50000.0   42000.0
1      Emma      N  52000.0   43000.0
2     Sofia   East  90000.0       NaN
3    Markus  South      NaN   44000.0
4    Edward   West  42000.0   38000.0
5    Thomas   West  72000.0   39000.0
6     Ethan      S  49000.0   42000.0
7    Olivia   West      NaN       NaN
8      Arun   West  67000.0   39000.0
9     Anika   East  65000.0   44000.0
10    Paulo  South  67000.0   45000.0
>>> s_c = s.copy()
>>> s_c
       name region  sales  expenses
0   William   East  50000     42000
1      Emma      N  52000     43000
2     Sofia   East  90000      -999
3    Markus  South     -1     44000
4    Edward   West  42000     38000
5    Thomas   West  72000     39000
6     Ethan      S  49000     42000
7    Olivia   West     -1        -1
8      Arun   West  67000     39000
9     Anika   East  65000     44000
10    Paulo  South  67000     45000
>>> s.replace({'region':{'N':'North'}})
       name region  sales  expenses
0   William   East  50000     42000
1      Emma  North  52000     43000
2     Sofia   East  90000      -999
3    Markus  South     -1     44000
4    Edward   West  42000     38000
5    Thomas   West  72000     39000
6     Ethan      S  49000     42000
7    Olivia   West     -1        -1
8      Arun   West  67000     39000
9     Anika   East  65000     44000
10    Paulo  South  67000     45000
>>> print(s.replace({'region':{'N':'North'}})
 .replace({'region':{'S':'South'}})
 .replace({'sales':{-1:np.nan}})
 .replace({'expenses':{-1:np.nan}})
 .replace({'expenses':{-999:np.nan}})
)
       name region    sales  expenses
0   William   East  50000.0   42000.0
1      Emma  North  52000.0   43000.0
2     Sofia   East  90000.0       NaN
3    Markus  South      NaN   44000.0
4    Edward   West  42000.0   38000.0
5    Thomas   West  72000.0   39000.0
6     Ethan  South  49000.0   42000.0
7    Olivia   West      NaN       NaN
8      Arun   West  67000.0   39000.0
9     Anika   East  65000.0   44000.0
10    Paulo  South  67000.0   45000.0
>>> (s.replace({'region':{'N':'North'}})
 .replace({'region':{'S':'South'}})
 .replace({'sales':{-1:np.nan}})
 .replace({'expenses':{-1:np.nan}})
 .replace({'expenses':{-999:np.nan}}))
       name region    sales  expenses
0   William   East  50000.0   42000.0
1      Emma  North  52000.0   43000.0
2     Sofia   East  90000.0       NaN
3    Markus  South      NaN   44000.0
4    Edward   West  42000.0   38000.0
5    Thomas   West  72000.0   39000.0
6     Ethan  South  49000.0   42000.0
7    Olivia   West      NaN       NaN
8      Arun   West  67000.0   39000.0
9     Anika   East  65000.0   44000.0
10    Paulo  South  67000.0   45000.0
>>> (s.replace(-1,0))
       name region  sales  expenses
0   William   East  50000     42000
1      Emma      N  52000     43000
2     Sofia   East  90000      -999
3    Markus  South      0     44000
4    Edward   West  42000     38000
5    Thomas   West  72000     39000
6     Ethan      S  49000     42000
7    Olivia   West      0         0
8      Arun   West  67000     39000
9     Anika   East  65000     44000
10    Paulo  South  67000     45000
>>> t
'                             Name                    Team  Number Position  Age  Height  Weight                College      Salary\n0   0               Avery Bradley          Boston Celtics       0       PG   25  06-Feb     180                  Texas   7730337.0\n1   1                 Jae Crowder          Boston Celtics      99       SF   25  06-Jun     235              Marquette   6796117.0\n2   2                John Holland          Boston Celtics      30       SG   27  06-May     205      Boston University         NaN\n3   3                 R.J. Hunter          Boston Celtics      28       SG   22  06-May     185          Georgia State   1148640.0\n4   4               Jonas Jerebko          Boston Celtics       8       PF   29  06-Oct     231                    NaN   5000000.0\n5   5                Amir Johnson          Boston Celtics      90       PF   29  06-Sep     240                    NaN  12000000.0\n6   6               Jordan Mickey          Boston Celtics      55       PF   21  06-Aug     235                    LSU   1170960.0\n7   7                Kelly Olynyk          Boston Celtics      41        C   25  Jul-00     238                Gonzaga   2165160.0\n8   8                Terry Rozier          Boston Celtics      12       PG   22  06-Feb     190             Louisville   1824360.0\n9   9                Marcus Smart          Boston Celtics      36       PG   22  06-Apr     220         Oklahoma State   3431040.0\n10  10            Jared Sullinger          Boston Celtics       7        C   24  06-Sep     260             Ohio State   2569260.0\n11  11              Isaiah Thomas          Boston Celtics       4       PG   27  05-Sep     185             Washington   6912869.0\n12  12                Evan Turner          Boston Celtics      11       SG   27  06-Jul     220             Ohio State   3425510.0\n13  13                James Young          Boston Celtics      13       SG   20  06-Jun     215               Kentucky   1749840.0\n14  14               Tyler Zeller          Boston Celtics      44        C   26  Jul-00     253         North Carolina   2616975.0'
>>> (t)
'                             Name                    Team  Number Position  Age  Height  Weight                College      Salary\n0   0               Avery Bradley          Boston Celtics       0       PG   25  06-Feb     180                  Texas   7730337.0\n1   1                 Jae Crowder          Boston Celtics      99       SF   25  06-Jun     235              Marquette   6796117.0\n2   2                John Holland          Boston Celtics      30       SG   27  06-May     205      Boston University         NaN\n3   3                 R.J. Hunter          Boston Celtics      28       SG   22  06-May     185          Georgia State   1148640.0\n4   4               Jonas Jerebko          Boston Celtics       8       PF   29  06-Oct     231                    NaN   5000000.0\n5   5                Amir Johnson          Boston Celtics      90       PF   29  06-Sep     240                    NaN  12000000.0\n6   6               Jordan Mickey          Boston Celtics      55       PF   21  06-Aug     235                    LSU   1170960.0\n7   7                Kelly Olynyk          Boston Celtics      41        C   25  Jul-00     238                Gonzaga   2165160.0\n8   8                Terry Rozier          Boston Celtics      12       PG   22  06-Feb     190             Louisville   1824360.0\n9   9                Marcus Smart          Boston Celtics      36       PG   22  06-Apr     220         Oklahoma State   3431040.0\n10  10            Jared Sullinger          Boston Celtics       7        C   24  06-Sep     260             Ohio State   2569260.0\n11  11              Isaiah Thomas          Boston Celtics       4       PG   27  05-Sep     185             Washington   6912869.0\n12  12                Evan Turner          Boston Celtics      11       SG   27  06-Jul     220             Ohio State   3425510.0\n13  13                James Young          Boston Celtics      13       SG   20  06-Jun     215               Kentucky   1749840.0\n14  14               Tyler Zeller          Boston Celtics      44        C   26  Jul-00     253         North Carolina   2616975.0'
>>> 
KeyboardInterrupt
>>> 