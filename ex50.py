Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> import pandas as pd
>>> data=pd.read_csv("f://DATA SCIENCE NOTES/nba.csv")
>>> data
              Name            Team  ...            College     Salary
0    Avery Bradley  Boston Celtics  ...              Texas  7730337.0
1      Jae Crowder  Boston Celtics  ...          Marquette  6796117.0
2     John Holland  Boston Celtics  ...  Boston University        NaN
3      R.J. Hunter  Boston Celtics  ...      Georgia State  1148640.0
4    Jonas Jerebko  Boston Celtics  ...                NaN  5000000.0
..             ...             ...  ...                ...        ...
452     Trey Lyles       Utah Jazz  ...           Kentucky  2239800.0
453   Shelvin Mack       Utah Jazz  ...             Butler  2433333.0
454      Raul Neto       Utah Jazz  ...                NaN   900000.0
455   Tibor Pleiss       Utah Jazz  ...                NaN  2900000.0
456    Jeff Withey       Utah Jazz  ...             Kansas   947276.0

[457 rows x 9 columns]
>>> data.select_dtypes(include=int)
     Number  Age  Weight
0         0   25     180
1        99   25     235
2        30   27     205
3        28   22     185
4         8   29     231
..      ...  ...     ...
452      41   20     234
453       8   26     203
454      25   24     179
455      21   26     256
456      24   26     231

[457 rows x 3 columns]
>>> data.select_dtypes(include=float)
        Salary
0    7730337.0
1    6796117.0
2          NaN
3    1148640.0
4    5000000.0
..         ...
452  2239800.0
453  2433333.0
454   900000.0
455  2900000.0
456   947276.0

[457 rows x 1 columns]
>>> data.select_dtypes(include=bool)
Empty DataFrame
Columns: []
Index: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, ...]

[457 rows x 0 columns]
>>> data.select_dtypes(exclude=int)
              Name            Team  ...            College     Salary
0    Avery Bradley  Boston Celtics  ...              Texas  7730337.0
1      Jae Crowder  Boston Celtics  ...          Marquette  6796117.0
2     John Holland  Boston Celtics  ...  Boston University        NaN
3      R.J. Hunter  Boston Celtics  ...      Georgia State  1148640.0
4    Jonas Jerebko  Boston Celtics  ...                NaN  5000000.0
..             ...             ...  ...                ...        ...
452     Trey Lyles       Utah Jazz  ...           Kentucky  2239800.0
453   Shelvin Mack       Utah Jazz  ...             Butler  2433333.0
454      Raul Neto       Utah Jazz  ...                NaN   900000.0
455   Tibor Pleiss       Utah Jazz  ...                NaN  2900000.0
456    Jeff Withey       Utah Jazz  ...             Kansas   947276.0

[457 rows x 6 columns]
>>> data.select_dtypes(include=object)
              Name            Team Position  Height            College
0    Avery Bradley  Boston Celtics       PG  06-Feb              Texas
1      Jae Crowder  Boston Celtics       SF  06-Jun          Marquette
2     John Holland  Boston Celtics       SG  06-May  Boston University
3      R.J. Hunter  Boston Celtics       SG  06-May      Georgia State
4    Jonas Jerebko  Boston Celtics       PF  06-Oct                NaN
..             ...             ...      ...     ...                ...
452     Trey Lyles       Utah Jazz       PF  06-Oct           Kentucky
453   Shelvin Mack       Utah Jazz       PG  06-Mar             Butler
454      Raul Neto       Utah Jazz       PG  06-Jan                NaN
455   Tibor Pleiss       Utah Jazz        C  07-Mar                NaN
456    Jeff Withey       Utah Jazz        C  Jul-00             Kansas

[457 rows x 5 columns]
>>> data.select_dtypes(exclude=object)
     Number  Age  Weight     Salary
0         0   25     180  7730337.0
1        99   25     235  6796117.0
2        30   27     205        NaN
3        28   22     185  1148640.0
4         8   29     231  5000000.0
..      ...  ...     ...        ...
452      41   20     234  2239800.0
453       8   26     203  2433333.0
454      25   24     179   900000.0
455      21   26     256  2900000.0
456      24   26     231   947276.0

[457 rows x 4 columns]
>>> data.select_dtypes(exclude=bool)
              Name            Team  ...            College     Salary
0    Avery Bradley  Boston Celtics  ...              Texas  7730337.0
1      Jae Crowder  Boston Celtics  ...          Marquette  6796117.0
2     John Holland  Boston Celtics  ...  Boston University        NaN
3      R.J. Hunter  Boston Celtics  ...      Georgia State  1148640.0
4    Jonas Jerebko  Boston Celtics  ...                NaN  5000000.0
..             ...             ...  ...                ...        ...
452     Trey Lyles       Utah Jazz  ...           Kentucky  2239800.0
453   Shelvin Mack       Utah Jazz  ...             Butler  2433333.0
454      Raul Neto       Utah Jazz  ...                NaN   900000.0
455   Tibor Pleiss       Utah Jazz  ...                NaN  2900000.0
456    Jeff Withey       Utah Jazz  ...             Kansas   947276.0

[457 rows x 9 columns]
>>> data
              Name            Team  ...            College     Salary
0    Avery Bradley  Boston Celtics  ...              Texas  7730337.0
1      Jae Crowder  Boston Celtics  ...          Marquette  6796117.0
2     John Holland  Boston Celtics  ...  Boston University        NaN
3      R.J. Hunter  Boston Celtics  ...      Georgia State  1148640.0
4    Jonas Jerebko  Boston Celtics  ...                NaN  5000000.0
..             ...             ...  ...                ...        ...
452     Trey Lyles       Utah Jazz  ...           Kentucky  2239800.0
453   Shelvin Mack       Utah Jazz  ...             Butler  2433333.0
454      Raul Neto       Utah Jazz  ...                NaN   900000.0
455   Tibor Pleiss       Utah Jazz  ...                NaN  2900000.0
456    Jeff Withey       Utah Jazz  ...             Kansas   947276.0

[457 rows x 9 columns]
>>> data.loc[0:20]
                       Name            Team  ...            College      Salary
0             Avery Bradley  Boston Celtics  ...              Texas   7730337.0
1               Jae Crowder  Boston Celtics  ...          Marquette   6796117.0
2              John Holland  Boston Celtics  ...  Boston University         NaN
3               R.J. Hunter  Boston Celtics  ...      Georgia State   1148640.0
4             Jonas Jerebko  Boston Celtics  ...                NaN   5000000.0
5              Amir Johnson  Boston Celtics  ...                NaN  12000000.0
6             Jordan Mickey  Boston Celtics  ...                LSU   1170960.0
7              Kelly Olynyk  Boston Celtics  ...            Gonzaga   2165160.0
8              Terry Rozier  Boston Celtics  ...         Louisville   1824360.0
9              Marcus Smart  Boston Celtics  ...     Oklahoma State   3431040.0
10          Jared Sullinger  Boston Celtics  ...         Ohio State   2569260.0
11            Isaiah Thomas  Boston Celtics  ...         Washington   6912869.0
12              Evan Turner  Boston Celtics  ...         Ohio State   3425510.0
13              James Young  Boston Celtics  ...           Kentucky   1749840.0
14             Tyler Zeller  Boston Celtics  ...     North Carolina   2616975.0
15         Bojan Bogdanovic   Brooklyn Nets  ...                NaN   3425510.0
16             Markel Brown   Brooklyn Nets  ...     Oklahoma State    845059.0
17          Wayne Ellington   Brooklyn Nets  ...     North Carolina   1500000.0
18  Rondae Hollis-Jefferson   Brooklyn Nets  ...            Arizona   1335480.0
19             Jarrett Jack   Brooklyn Nets  ...       Georgia Tech   6300000.0
20           Sergey Karasev   Brooklyn Nets  ...                NaN   1599840.0

[21 rows x 9 columns]
>>> data.select_dtypes(include=float)
        Salary
0    7730337.0
1    6796117.0
2          NaN
3    1148640.0
4    5000000.0
..         ...
452  2239800.0
453  2433333.0
454   900000.0
455  2900000.0
456   947276.0

[457 rows x 1 columns]
>>> data.select_dtypes(include=float64)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    data.select_dtypes(include=float64)
NameError: name 'float64' is not defined
>>> data.select_dtypes(include='float64')
        Salary
0    7730337.0
1    6796117.0
2          NaN
3    1148640.0
4    5000000.0
..         ...
452  2239800.0
453  2433333.0
454   900000.0
455  2900000.0
456   947276.0

[457 rows x 1 columns]
>>> data.loc[0:10]
               Name            Team  ...            College      Salary
0     Avery Bradley  Boston Celtics  ...              Texas   7730337.0
1       Jae Crowder  Boston Celtics  ...          Marquette   6796117.0
2      John Holland  Boston Celtics  ...  Boston University         NaN
3       R.J. Hunter  Boston Celtics  ...      Georgia State   1148640.0
4     Jonas Jerebko  Boston Celtics  ...                NaN   5000000.0
5      Amir Johnson  Boston Celtics  ...                NaN  12000000.0
6     Jordan Mickey  Boston Celtics  ...                LSU   1170960.0
7      Kelly Olynyk  Boston Celtics  ...            Gonzaga   2165160.0
8      Terry Rozier  Boston Celtics  ...         Louisville   1824360.0
9      Marcus Smart  Boston Celtics  ...     Oklahoma State   3431040.0
10  Jared Sullinger  Boston Celtics  ...         Ohio State   2569260.0

[11 rows x 9 columns]
>>> data.loc[:]
              Name            Team  ...            College     Salary
0    Avery Bradley  Boston Celtics  ...              Texas  7730337.0
1      Jae Crowder  Boston Celtics  ...          Marquette  6796117.0
2     John Holland  Boston Celtics  ...  Boston University        NaN
3      R.J. Hunter  Boston Celtics  ...      Georgia State  1148640.0
4    Jonas Jerebko  Boston Celtics  ...                NaN  5000000.0
..             ...             ...  ...                ...        ...
452     Trey Lyles       Utah Jazz  ...           Kentucky  2239800.0
453   Shelvin Mack       Utah Jazz  ...             Butler  2433333.0
454      Raul Neto       Utah Jazz  ...                NaN   900000.0
455   Tibor Pleiss       Utah Jazz  ...                NaN  2900000.0
456    Jeff Withey       Utah Jazz  ...             Kansas   947276.0

[457 rows x 9 columns]
>>> data.loc[1:10,['Name','Team','Salary']]
               Name            Team      Salary
1       Jae Crowder  Boston Celtics   6796117.0
2      John Holland  Boston Celtics         NaN
3       R.J. Hunter  Boston Celtics   1148640.0
4     Jonas Jerebko  Boston Celtics   5000000.0
5      Amir Johnson  Boston Celtics  12000000.0
6     Jordan Mickey  Boston Celtics   1170960.0
7      Kelly Olynyk  Boston Celtics   2165160.0
8      Terry Rozier  Boston Celtics   1824360.0
9      Marcus Smart  Boston Celtics   3431040.0
10  Jared Sullinger  Boston Celtics   2569260.0
>>> data.loc[1:10,:]
               Name            Team  ...            College      Salary
1       Jae Crowder  Boston Celtics  ...          Marquette   6796117.0
2      John Holland  Boston Celtics  ...  Boston University         NaN
3       R.J. Hunter  Boston Celtics  ...      Georgia State   1148640.0
4     Jonas Jerebko  Boston Celtics  ...                NaN   5000000.0
5      Amir Johnson  Boston Celtics  ...                NaN  12000000.0
6     Jordan Mickey  Boston Celtics  ...                LSU   1170960.0
7      Kelly Olynyk  Boston Celtics  ...            Gonzaga   2165160.0
8      Terry Rozier  Boston Celtics  ...         Louisville   1824360.0
9      Marcus Smart  Boston Celtics  ...     Oklahoma State   3431040.0
10  Jared Sullinger  Boston Celtics  ...         Ohio State   2569260.0

[10 rows x 9 columns]
>>> data.loc[[1,7,12,99,10],:]
                        Name                  Team  ...     College     Salary
1                Jae Crowder        Boston Celtics  ...   Marquette  6796117.0
7               Kelly Olynyk        Boston Celtics  ...     Gonzaga  2165160.0
12               Evan Turner        Boston Celtics  ...  Ohio State  3425510.0
99  Luc Richard Mbah a Moute  Los Angeles Clippers  ...        UCLA   947276.0
10           Jared Sullinger        Boston Celtics  ...  Ohio State  2569260.0

[5 rows x 9 columns]
>>> data.loc[[1,77,55,66],["Salary","Name","Team"]]
       Salary             Name                   Team
1   6796117.0      Jae Crowder         Boston Celtics
77  3873398.0  Harrison Barnes  Golden State Warriors
55  3457800.0     Nerlens Noel     Philadelphia 76ers
66  7000000.0      Cory Joseph        Toronto Raptors
>>> data.loc[:,:]
              Name            Team  ...            College     Salary
0    Avery Bradley  Boston Celtics  ...              Texas  7730337.0
1      Jae Crowder  Boston Celtics  ...          Marquette  6796117.0
2     John Holland  Boston Celtics  ...  Boston University        NaN
3      R.J. Hunter  Boston Celtics  ...      Georgia State  1148640.0
4    Jonas Jerebko  Boston Celtics  ...                NaN  5000000.0
..             ...             ...  ...                ...        ...
452     Trey Lyles       Utah Jazz  ...           Kentucky  2239800.0
453   Shelvin Mack       Utah Jazz  ...             Butler  2433333.0
454      Raul Neto       Utah Jazz  ...                NaN   900000.0
455   Tibor Pleiss       Utah Jazz  ...                NaN  2900000.0
456    Jeff Withey       Utah Jazz  ...             Kansas   947276.0

[457 rows x 9 columns]
>>> data.iloc[0:10]
            Name            Team  Number  ... Weight            College      Salary
0  Avery Bradley  Boston Celtics       0  ...    180              Texas   7730337.0
1    Jae Crowder  Boston Celtics      99  ...    235          Marquette   6796117.0
2   John Holland  Boston Celtics      30  ...    205  Boston University         NaN
3    R.J. Hunter  Boston Celtics      28  ...    185      Georgia State   1148640.0
4  Jonas Jerebko  Boston Celtics       8  ...    231                NaN   5000000.0
5   Amir Johnson  Boston Celtics      90  ...    240                NaN  12000000.0
6  Jordan Mickey  Boston Celtics      55  ...    235                LSU   1170960.0
7   Kelly Olynyk  Boston Celtics      41  ...    238            Gonzaga   2165160.0
8   Terry Rozier  Boston Celtics      12  ...    190         Louisville   1824360.0
9   Marcus Smart  Boston Celtics      36  ...    220     Oklahoma State   3431040.0

[10 rows x 9 columns]
>>> data.iloc[[0:10],[2,3,6]]
SyntaxError: invalid syntax
>>> data.iloc[0:10],[2,3,6]
(            Name            Team  Number  ... Weight            College      Salary
0  Avery Bradley  Boston Celtics       0  ...    180              Texas   7730337.0
1    Jae Crowder  Boston Celtics      99  ...    235          Marquette   6796117.0
2   John Holland  Boston Celtics      30  ...    205  Boston University         NaN
3    R.J. Hunter  Boston Celtics      28  ...    185      Georgia State   1148640.0
4  Jonas Jerebko  Boston Celtics       8  ...    231                NaN   5000000.0
5   Amir Johnson  Boston Celtics      90  ...    240                NaN  12000000.0
6  Jordan Mickey  Boston Celtics      55  ...    235                LSU   1170960.0
7   Kelly Olynyk  Boston Celtics      41  ...    238            Gonzaga   2165160.0
8   Terry Rozier  Boston Celtics      12  ...    190         Louisville   1824360.0
9   Marcus Smart  Boston Celtics      36  ...    220     Oklahoma State   3431040.0

[10 rows x 9 columns], [2, 3, 6])
>>> data.iloc[:],[2,3,6]
(              Name            Team  ...            College     Salary
0    Avery Bradley  Boston Celtics  ...              Texas  7730337.0
1      Jae Crowder  Boston Celtics  ...          Marquette  6796117.0
2     John Holland  Boston Celtics  ...  Boston University        NaN
3      R.J. Hunter  Boston Celtics  ...      Georgia State  1148640.0
4    Jonas Jerebko  Boston Celtics  ...                NaN  5000000.0
..             ...             ...  ...                ...        ...
452     Trey Lyles       Utah Jazz  ...           Kentucky  2239800.0
453   Shelvin Mack       Utah Jazz  ...             Butler  2433333.0
454      Raul Neto       Utah Jazz  ...                NaN   900000.0
455   Tibor Pleiss       Utah Jazz  ...                NaN  2900000.0
456    Jeff Withey       Utah Jazz  ...             Kansas   947276.0

[457 rows x 9 columns], [2, 3, 6])
>>> data.iloc[4,7,3],[2,3,6]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    data.iloc[4,7,3],[2,3,6]
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 925, in __getitem__
    return self._getitem_tuple(key)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 1506, in _getitem_tuple
    self._has_valid_tuple(tup)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 751, in _has_valid_tuple
    self._validate_key_length(key)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexing.py", line 792, in _validate_key_length
    raise IndexingError("Too many indexers")
pandas.core.indexing.IndexingError: Too many indexers
>>> data.iloc[4:13],["Name"]
(               Name            Team  Number  ... Weight         College      Salary
4     Jonas Jerebko  Boston Celtics       8  ...    231             NaN   5000000.0
5      Amir Johnson  Boston Celtics      90  ...    240             NaN  12000000.0
6     Jordan Mickey  Boston Celtics      55  ...    235             LSU   1170960.0
7      Kelly Olynyk  Boston Celtics      41  ...    238         Gonzaga   2165160.0
8      Terry Rozier  Boston Celtics      12  ...    190      Louisville   1824360.0
9      Marcus Smart  Boston Celtics      36  ...    220  Oklahoma State   3431040.0
10  Jared Sullinger  Boston Celtics       7  ...    260      Ohio State   2569260.0
11    Isaiah Thomas  Boston Celtics       4  ...    185      Washington   6912869.0
12      Evan Turner  Boston Celtics      11  ...    220      Ohio State   3425510.0

[9 rows x 9 columns], ['Name'])
>>> data.iloc[4:13],["Name","Team"]
(               Name            Team  Number  ... Weight         College      Salary
4     Jonas Jerebko  Boston Celtics       8  ...    231             NaN   5000000.0
5      Amir Johnson  Boston Celtics      90  ...    240             NaN  12000000.0
6     Jordan Mickey  Boston Celtics      55  ...    235             LSU   1170960.0
7      Kelly Olynyk  Boston Celtics      41  ...    238         Gonzaga   2165160.0
8      Terry Rozier  Boston Celtics      12  ...    190      Louisville   1824360.0
9      Marcus Smart  Boston Celtics      36  ...    220  Oklahoma State   3431040.0
10  Jared Sullinger  Boston Celtics       7  ...    260      Ohio State   2569260.0
11    Isaiah Thomas  Boston Celtics       4  ...    185      Washington   6912869.0
12      Evan Turner  Boston Celtics      11  ...    220      Ohio State   3425510.0

[9 rows x 9 columns], ['Name', 'Team'])
>>> 