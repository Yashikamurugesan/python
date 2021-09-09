Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import numpy as np
>>> data=pd.read_csv("f://DATA SCIENCE NOTES/pmk.csv",encoding="latin")
>>> data
       #      Position            Candidate  ... Turnout PMK Votes PMK Votes %
0          1         2         Annadurai. N  ...  85.50%    56,681      25.30%
1          2         2  Guru @ Gurunathan.J  ...  80.80%    52,738      26.10%
2          3         2    Sathiyamoorthy. A  ...  85.30%    61,521      29.70%
3          4         2    Anbumani Ramadoss  ...  87.30%    58,402      29.60%
4          5         3            Sekar K N  ...  63.40%    16,635       7.40%
..       ...       ...                  ...  ...     ...       ...         ...
225      226        11          Nagarajan B  ...  76.10%       490       0.30%
226      227        11          Hariharan R  ...  66.90%       398       0.30%
227      228        12          Shanmugam K  ...  84.10%       367       0.20%
228      229        13         Muniasamy A.  ...  81.10%       260       0.20%
229      230        13             Pandi. V  ...  68.30%       522       0.30%

[230 rows x 9 columns]
>>> data.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 230 entries, 0 to 229
Data columns (total 9 columns):
 #   Column          Non-Null Count  Dtype 
---  ------          --------------  ----- 
 0     #             230 non-null    int64 
 1   Position        230 non-null    int64 
 2   Candidate       230 non-null    object
 3   AC Name         230 non-null    object
 4   Total Electors  230 non-null    object
 5   Total Votes     230 non-null    object
 6   Turnout         230 non-null    object
 7   PMK Votes       230 non-null    object
 8   PMK Votes %     230 non-null    object
dtypes: int64(2), object(7)
memory usage: 16.3+ KB
>>> data.dtypes
  #                int64
Position           int64
Candidate         object
AC Name           object
Total Electors    object
Total Votes       object
Turnout           object
PMK Votes         object
PMK Votes %       object
dtype: object
>>> data.index
RangeIndex(start=0, stop=230, step=1)
>>> data.set_index('Position')
            #                Candidate  ... PMK Votes PMK Votes %
Position                                ...                      
2               1         Annadurai. N  ...    56,681      25.30%
2               2  Guru @ Gurunathan.J  ...    52,738      26.10%
2               3    Sathiyamoorthy. A  ...    61,521      29.70%
2               4    Anbumani Ramadoss  ...    58,402      29.60%
3               5            Sekar K N  ...    16,635       7.40%
...           ...                  ...  ...       ...         ...
11            226          Nagarajan B  ...       490       0.30%
11            227          Hariharan R  ...       398       0.30%
12            228          Shanmugam K  ...       367       0.20%
13            229         Muniasamy A.  ...       260       0.20%
13            230             Pandi. V  ...       522       0.30%

[230 rows x 8 columns]
>>> data
       #      Position            Candidate  ... Turnout PMK Votes PMK Votes %
0          1         2         Annadurai. N  ...  85.50%    56,681      25.30%
1          2         2  Guru @ Gurunathan.J  ...  80.80%    52,738      26.10%
2          3         2    Sathiyamoorthy. A  ...  85.30%    61,521      29.70%
3          4         2    Anbumani Ramadoss  ...  87.30%    58,402      29.60%
4          5         3            Sekar K N  ...  63.40%    16,635       7.40%
..       ...       ...                  ...  ...     ...       ...         ...
225      226        11          Nagarajan B  ...  76.10%       490       0.30%
226      227        11          Hariharan R  ...  66.90%       398       0.30%
227      228        12          Shanmugam K  ...  84.10%       367       0.20%
228      229        13         Muniasamy A.  ...  81.10%       260       0.20%
229      230        13             Pandi. V  ...  68.30%       522       0.30%

[230 rows x 9 columns]
>>> dt=data.set_index('Position')
>>> dt
            #                Candidate  ... PMK Votes PMK Votes %
Position                                ...                      
2               1         Annadurai. N  ...    56,681      25.30%
2               2  Guru @ Gurunathan.J  ...    52,738      26.10%
2               3    Sathiyamoorthy. A  ...    61,521      29.70%
2               4    Anbumani Ramadoss  ...    58,402      29.60%
3               5            Sekar K N  ...    16,635       7.40%
...           ...                  ...  ...       ...         ...
11            226          Nagarajan B  ...       490       0.30%
11            227          Hariharan R  ...       398       0.30%
12            228          Shanmugam K  ...       367       0.20%
13            229         Muniasamy A.  ...       260       0.20%
13            230             Pandi. V  ...       522       0.30%

[230 rows x 8 columns]
>>> df=pd.Categorical(dt)
>>> df
['  #    ', 'Candidate', 'AC Name', 'Total Electors', 'Total Votes', 'Turnout', 'PMK Votes', 'PMK Votes %']
Categories (8, object): ['AC Name', 'Candidate', 'PMK Votes', 'PMK Votes %', 'Total Electors',
                         'Total Votes', 'Turnout', '  #    ']
>>> 