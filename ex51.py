Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
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
>>> data.iloc[1:6],["Name":"College"]
SyntaxError: invalid syntax
>>> data.iloc[1:6],["Name","College"]
(            Name            Team  Number  ... Weight            College      Salary
1    Jae Crowder  Boston Celtics      99  ...    235          Marquette   6796117.0
2   John Holland  Boston Celtics      30  ...    205  Boston University         NaN
3    R.J. Hunter  Boston Celtics      28  ...    185      Georgia State   1148640.0
4  Jonas Jerebko  Boston Celtics       8  ...    231                NaN   5000000.0
5   Amir Johnson  Boston Celtics      90  ...    240                NaN  12000000.0

[5 rows x 9 columns], ['Name', 'College'])
>>> data.iloc[1:6],["Name","College",'Team']
(            Name            Team  Number  ... Weight            College      Salary
1    Jae Crowder  Boston Celtics      99  ...    235          Marquette   6796117.0
2   John Holland  Boston Celtics      30  ...    205  Boston University         NaN
3    R.J. Hunter  Boston Celtics      28  ...    185      Georgia State   1148640.0
4  Jonas Jerebko  Boston Celtics       8  ...    231                NaN   5000000.0
5   Amir Johnson  Boston Celtics      90  ...    240                NaN  12000000.0

[5 rows x 9 columns], ['Name', 'College', 'Team'])
>>> data.iloc[1:6],["Name","College",'Team','Number','Weight','College','Salary']
(            Name            Team  Number  ... Weight            College      Salary
1    Jae Crowder  Boston Celtics      99  ...    235          Marquette   6796117.0
2   John Holland  Boston Celtics      30  ...    205  Boston University         NaN
3    R.J. Hunter  Boston Celtics      28  ...    185      Georgia State   1148640.0
4  Jonas Jerebko  Boston Celtics       8  ...    231                NaN   5000000.0
5   Amir Johnson  Boston Celtics      90  ...    240                NaN  12000000.0

[5 rows x 9 columns], ['Name', 'College', 'Team', 'Number', 'Weight', 'College', 'Salary'])
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
>>> data.iloc[1:6],["Name"]
(            Name            Team  Number  ... Weight            College      Salary
1    Jae Crowder  Boston Celtics      99  ...    235          Marquette   6796117.0
2   John Holland  Boston Celtics      30  ...    205  Boston University         NaN
3    R.J. Hunter  Boston Celtics      28  ...    185      Georgia State   1148640.0
4  Jonas Jerebko  Boston Celtics       8  ...    231                NaN   5000000.0
5   Amir Johnson  Boston Celtics      90  ...    240                NaN  12000000.0

[5 rows x 9 columns], ['Name'])
>>> data.iloc[1:6],["Name","College",'Team','Number','Weight','College','Salary','position','Age','Height']
(            Name            Team  Number  ... Weight            College      Salary
1    Jae Crowder  Boston Celtics      99  ...    235          Marquette   6796117.0
2   John Holland  Boston Celtics      30  ...    205  Boston University         NaN
3    R.J. Hunter  Boston Celtics      28  ...    185      Georgia State   1148640.0
4  Jonas Jerebko  Boston Celtics       8  ...    231                NaN   5000000.0
5   Amir Johnson  Boston Celtics      90  ...    240                NaN  12000000.0

[5 rows x 9 columns], ['Name', 'College', 'Team', 'Number', 'Weight', 'College', 'Salary', 'position', 'Age', 'Height'])
>>> data.iloc[1:],["Name","College",'Team','Number','Weight','College','Salary','position','Age','Height']
(              Name            Team  ...            College      Salary
1      Jae Crowder  Boston Celtics  ...          Marquette   6796117.0
2     John Holland  Boston Celtics  ...  Boston University         NaN
3      R.J. Hunter  Boston Celtics  ...      Georgia State   1148640.0
4    Jonas Jerebko  Boston Celtics  ...                NaN   5000000.0
5     Amir Johnson  Boston Celtics  ...                NaN  12000000.0
..             ...             ...  ...                ...         ...
452     Trey Lyles       Utah Jazz  ...           Kentucky   2239800.0
453   Shelvin Mack       Utah Jazz  ...             Butler   2433333.0
454      Raul Neto       Utah Jazz  ...                NaN    900000.0
455   Tibor Pleiss       Utah Jazz  ...                NaN   2900000.0
456    Jeff Withey       Utah Jazz  ...             Kansas    947276.0

[456 rows x 9 columns], ['Name', 'College', 'Team', 'Number', 'Weight', 'College', 'Salary', 'position', 'Age', 'Height'])
>>> data.iloc[:],["Name","College",'Team','Number','Weight','College','Salary','position','Age','Height']
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

[457 rows x 9 columns], ['Name', 'College', 'Team', 'Number', 'Weight', 'College', 'Salary', 'position', 'Age', 'Height'])
>>> data.iloc[:41],["Name","College",'Team','Number','Weight','College','Salary','position','Age','Height']
(                       Name             Team  ...            College      Salary
0             Avery Bradley   Boston Celtics  ...              Texas   7730337.0
1               Jae Crowder   Boston Celtics  ...          Marquette   6796117.0
2              John Holland   Boston Celtics  ...  Boston University         NaN
3               R.J. Hunter   Boston Celtics  ...      Georgia State   1148640.0
4             Jonas Jerebko   Boston Celtics  ...                NaN   5000000.0
5              Amir Johnson   Boston Celtics  ...                NaN  12000000.0
6             Jordan Mickey   Boston Celtics  ...                LSU   1170960.0
7              Kelly Olynyk   Boston Celtics  ...            Gonzaga   2165160.0
8              Terry Rozier   Boston Celtics  ...         Louisville   1824360.0
9              Marcus Smart   Boston Celtics  ...     Oklahoma State   3431040.0
10          Jared Sullinger   Boston Celtics  ...         Ohio State   2569260.0
11            Isaiah Thomas   Boston Celtics  ...         Washington   6912869.0
12              Evan Turner   Boston Celtics  ...         Ohio State   3425510.0
13              James Young   Boston Celtics  ...           Kentucky   1749840.0
14             Tyler Zeller   Boston Celtics  ...     North Carolina   2616975.0
15         Bojan Bogdanovic    Brooklyn Nets  ...                NaN   3425510.0
16             Markel Brown    Brooklyn Nets  ...     Oklahoma State    845059.0
17          Wayne Ellington    Brooklyn Nets  ...     North Carolina   1500000.0
18  Rondae Hollis-Jefferson    Brooklyn Nets  ...            Arizona   1335480.0
19             Jarrett Jack    Brooklyn Nets  ...       Georgia Tech   6300000.0
20           Sergey Karasev    Brooklyn Nets  ...                NaN   1599840.0
21          Sean Kilpatrick    Brooklyn Nets  ...         Cincinnati    134215.0
22             Shane Larkin    Brooklyn Nets  ...         Miami (FL)   1500000.0
23              Brook Lopez    Brooklyn Nets  ...           Stanford  19689000.0
24         Chris McCullough    Brooklyn Nets  ...           Syracuse   1140240.0
25              Willie Reed    Brooklyn Nets  ...        Saint Louis    947276.0
26          Thomas Robinson    Brooklyn Nets  ...             Kansas    981348.0
27               Henry Sims    Brooklyn Nets  ...         Georgetown    947276.0
28             Donald Sloan    Brooklyn Nets  ...          Texas A&M    947276.0
29           Thaddeus Young    Brooklyn Nets  ...       Georgia Tech  11235955.0
30            Arron Afflalo  New York Knicks  ...               UCLA   8000000.0
31             Lou Amundson  New York Knicks  ...               UNLV   1635476.0
32   Thanasis Antetokounmpo  New York Knicks  ...                NaN     30888.0
33          Carmelo Anthony  New York Knicks  ...           Syracuse  22875000.0
34            Jose Calderon  New York Knicks  ...                NaN   7402812.0
35         Cleanthony Early  New York Knicks  ...      Wichita State    845059.0
36        Langston Galloway  New York Knicks  ...     Saint Joseph's    845059.0
37             Jerian Grant  New York Knicks  ...         Notre Dame   1572360.0
38              Robin Lopez  New York Knicks  ...           Stanford  12650000.0
39             Kyle O'Quinn  New York Knicks  ...      Norfolk State   3750000.0
40       Kristaps Porzingis  New York Knicks  ...                NaN   4131720.0

[41 rows x 9 columns], ['Name', 'College', 'Team', 'Number', 'Weight', 'College', 'Salary', 'position', 'Age', 'Height'])
>>> 
