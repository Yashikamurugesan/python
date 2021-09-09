Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> data=pd.read_csv("f://DATA SCIENCE NOTES/diabetes.csv")
>>> data
     Pregnancies  Glucose  ...  Age  Outcome
0              6      148  ...   50        1
1              1       85  ...   31        0
2              8      183  ...   32        1
3              1       89  ...   21        0
4              0      137  ...   33        1
..           ...      ...  ...  ...      ...
763           10      101  ...   63        0
764            2      122  ...   27        0
765            5      121  ...   30        0
766            1      126  ...   47        1
767            1       93  ...   23        0

[768 rows x 9 columns]
>>> data.to_string()

>>> data.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 768 entries, 0 to 767
Data columns (total 9 columns):
 #   Column                    Non-Null Count  Dtype  
---  ------                    --------------  -----  
 0   Pregnancies               768 non-null    int64  
 1   Glucose                   768 non-null    int64  
 2   BloodPressure             768 non-null    int64  
 3   SkinThickness             768 non-null    int64  
 4   Insulin                   768 non-null    int64  
 5   BMI                       768 non-null    float64
 6   DiabetesPedigreeFunction  768 non-null    float64
 7   Age                       768 non-null    int64  
 8   Outcome                   768 non-null    int64  
dtypes: float64(2), int64(7)
memory usage: 54.1 KB
>>> data.BloodPressure.max()
122
>>> data.BloodPressure
0      72
1      66
2      64
3      66
4      40
       ..
763    76
764    70
765    72
766    60
767    70
Name: BloodPressure, Length: 768, dtype: int64
>>> data.BloodPressure.unique()
array([ 72,  66,  64,  40,  74,  50,   0,  70,  96,  92,  80,  60,  84,
        30,  88,  90,  94,  76,  82,  75,  58,  78,  68, 110,  56,  62,
        85,  86,  48,  44,  65, 108,  55, 122,  54,  52,  98, 104,  95,
        46, 102, 100,  61,  24,  38, 106, 114], dtype=int64)
>>> value=data.at[1,'BloodPressure']
>>> value
66
>>> value=data.at[767,'BloodPressure']
>>> value
70
>>> value1=data.iat[1,2]
>>> value1
66
>>> data.head()
   Pregnancies  Glucose  BloodPressure  ...  DiabetesPedigreeFunction  Age  Outcome
0            6      148             72  ...                     0.627   50        1
1            1       85             66  ...                     0.351   31        0
2            8      183             64  ...                     0.672   32        1
3            1       89             66  ...                     0.167   21        0
4            0      137             40  ...                     2.288   33        1

[5 rows x 9 columns]
>>> data.head().to_string()
'   Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin   BMI  DiabetesPedigreeFunction  Age  Outcome\n0            6      148             72             35        0  33.6                     0.627   50        1\n1            1       85             66             29        0  26.6                     0.351   31        0\n2            8      183             64              0        0  23.3                     0.672   32        1\n3            1       89             66             23       94  28.1                     0.167   21        0\n4            0      137             40             35      168  43.1                     2.288   33        1'
>>> print(data.head().to_string())
   Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin   BMI  DiabetesPedigreeFunction  Age  Outcome
0            6      148             72             35        0  33.6                     0.627   50        1
1            1       85             66             29        0  26.6                     0.351   31        0
2            8      183             64              0        0  23.3                     0.672   32        1
3            1       89             66             23       94  28.1                     0.167   21        0
4            0      137             40             35      168  43.1                     2.288   33        1
>>> data['Outcome'].unique()
array([1, 0], dtype=int64)
>>> dt=data.loc[2,'BloodPressure']
>>> dt
64
>>> dt=data.loc[2,'BloodPressure'].iat[0]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    dt=data.loc[2,'BloodPressure'].iat[0]
AttributeError: 'numpy.int64' object has no attribute 'iat'
>>> data.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 768 entries, 0 to 767
Data columns (total 9 columns):
 #   Column                    Non-Null Count  Dtype  
---  ------                    --------------  -----  
 0   Pregnancies               768 non-null    int64  
 1   Glucose                   768 non-null    int64  
 2   BloodPressure             768 non-null    int64  
 3   SkinThickness             768 non-null    int64  
 4   Insulin                   768 non-null    int64  
 5   BMI                       768 non-null    float64
 6   DiabetesPedigreeFunction  768 non-null    float64
 7   Age                       768 non-null    int64  
 8   Outcome                   768 non-null    int64  
dtypes: float64(2), int64(7)
memory usage: 54.1 KB
>>> sort=data.sort_values(['Age','Pregnancies','Pregnancies','BloodPressure'],ascending=[True,False])
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    sort=data.sort_values(['Age','Pregnancies','Pregnancies','BloodPressure'],ascending=[True,False])
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\util\_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 6232, in sort_values
    raise ValueError(
ValueError: Length of ascending (2) != length of by (4)
>>> sort=data.sort_values(['BloodPressure'],ascending=[True,False])
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    sort=data.sort_values(['BloodPressure'],ascending=[True,False])
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\util\_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 6232, in sort_values
    raise ValueError(
ValueError: Length of ascending (2) != length of by (1)
>>> sort=data.sort_values(['BloodPressure'],ascending=True,inplace=False)
>>> sort
     Pregnancies  Glucose  ...  Age  Outcome
347            3      116  ...   23        0
494            3       80  ...   22        0
222            7      119  ...   37        0
81             2       74  ...   22        0
78             0      131  ...   26        1
..           ...      ...  ...  ...      ...
549            4      189  ...   37        0
43             9      171  ...   54        1
177            0      129  ...   26        1
691           13      158  ...   44        1
106            1       96  ...   27        0

[768 rows x 9 columns]
>>> sort.head(10)
     Pregnancies  Glucose  ...  Age  Outcome
347            3      116  ...   23        0
494            3       80  ...   22        0
222            7      119  ...   37        0
81             2       74  ...   22        0
78             0      131  ...   26        1
484            0      145  ...   31        1
468            8      120  ...   38        1
60             2       84  ...   21        0
453            2      119  ...   72        0
300            0      167  ...   30        1

[10 rows x 9 columns]
>>> sort.BloodPressure.head(10)
347    0
494    0
222    0
81     0
78     0
484    0
468    0
60     0
453    0
300    0
Name: BloodPressure, dtype: int64
>>> sort.BloodPressure
347      0
494      0
222      0
81       0
78       0
      ... 
549    110
43     110
177    110
691    114
106    122
Name: BloodPressure, Length: 768, dtype: int64
>>> sort.BloodPressure.tail()
549    110
43     110
177    110
691    114
106    122
Name: BloodPressure, dtype: int64
>>> sort=data.sort_values(['BloodPressure','Outcome','Age','Pregnancies'],ascending=True,inplace=False)
>>> sort
     Pregnancies  Glucose  ...  Age  Outcome
60             2       84  ...   21        0
697            0       99  ...   22        0
81             2       74  ...   22        0
494            3       80  ...   22        0
430            2       99  ...   23        0
..           ...      ...  ...  ...      ...
549            4      189  ...   37        0
177            0      129  ...   26        1
43             9      171  ...   54        1
691           13      158  ...   44        1
106            1       96  ...   27        0

[768 rows x 9 columns]
>>> sort.head()
     Pregnancies  Glucose  ...  Age  Outcome
60             2       84  ...   21        0
697            0       99  ...   22        0
81             2       74  ...   22        0
494            3       80  ...   22        0
430            2       99  ...   23        0

[5 rows x 9 columns]
>>> sort.Age
60     21
697    22
81     22
494    22
430    23
       ..
549    37
177    26
43     54
691    44
106    27
Name: Age, Length: 768, dtype: int64
>>> sort.Outcome.head()
60     0
697    0
81     0
494    0
430    0
Name: Outcome, dtype: int64
>>> sort.Age.head(10)
60     21
697    22
81     22
494    22
430    23
347    23
49     24
426    25
589    25
172    25
Name: Age, dtype: int64
>>> sort.Pregnancies.head(10)
60     2
697    0
81     2
494    3
430    2
347    3
49     7
426    0
589    0
172    2
Name: Pregnancies, dtype: int64
>>> data.groupby('Pregnancies').count()
             Glucose  BloodPressure  ...  Age  Outcome
Pregnancies                          ...              
0                111            111  ...  111      111
1                135            135  ...  135      135
2                103            103  ...  103      103
3                 75             75  ...   75       75
4                 68             68  ...   68       68
5                 57             57  ...   57       57
6                 50             50  ...   50       50
7                 45             45  ...   45       45
8                 38             38  ...   38       38
9                 28             28  ...   28       28
10                24             24  ...   24       24
11                11             11  ...   11       11
12                 9              9  ...    9        9
13                10             10  ...   10       10
14                 2              2  ...    2        2
15                 1              1  ...    1        1
17                 1              1  ...    1        1

[17 rows x 8 columns]
>>> data.dropna()
     Pregnancies  Glucose  ...  Age  Outcome
0              6      148  ...   50        1
1              1       85  ...   31        0
2              8      183  ...   32        1
3              1       89  ...   21        0
4              0      137  ...   33        1
..           ...      ...  ...  ...      ...
763           10      101  ...   63        0
764            2      122  ...   27        0
765            5      121  ...   30        0
766            1      126  ...   47        1
767            1       93  ...   23        0

[768 rows x 9 columns]
>>> g=data.groupby('Age')
>>> g
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000026073E91640>
>>> g.head()
     Pregnancies  Glucose  ...  Age  Outcome
0              6      148  ...   50        1
1              1       85  ...   31        0
2              8      183  ...   32        1
3              1       89  ...   21        0
4              0      137  ...   33        1
..           ...      ...  ...  ...      ...
717           10       94  ...   56        0
734            2      105  ...   53        0
740           11      120  ...   48        1
759            6      190  ...   66        1
763           10      101  ...   63        0

[222 rows x 9 columns]
>>> print(data.groupby('Age'))
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000026073E2E7C0>
>>> print(data.groupby['Age'])
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print(data.groupby['Age'])
TypeError: 'method' object is not subscriptable
>>> print(data.groupby['Age','Pregnancies'])
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print(data.groupby['Age','Pregnancies'])
TypeError: 'method' object is not subscriptable
>>> g=data.groupby(['Age','Pregnancies'])
>>> g
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000026073EA14C0>
>>> g=data.groupby(['Age','Pregnancies']).groups
>>> g
{(21, 0): [102, 136, 145, 200, 220, 268, 290, 307, 367, 371, 372, 414, 422, 465, 511, 580, 623, 626, 627, 713, 736], (21, 1): [3, 55, 90, 105, 182, 196, 208, 240, 255, 273, 382, 392, 413, 438, 486, 507, 526, 550, 566, 597, 605, 671, 721], (21, 2): [60, 94, 156, 163, 271, 324, 421, 423, 500, 508, 571, 577, 624, 738], (21, 3): [190, 354, 525], (21, 4): [119, 629], (22, 0): [59, 83, 137, 311, 376, 381, 397, 448, 466, 471, 472, 528, 595, 647, 682, 697, 727], (22, 1): [27, 50, 74, 75, 97, 101, 225, 232, 334, 340, 342, 346, 377, 412, 416, 432, 585, 606, 633, 654, 661, 742], (22, 2): [47, 81, 142, 149, 158, 279, 441, 513, 530, 565, 573, 656, 680, 707, 728, 729, 733, 760], (22, 3): [32, 80, 166, 242, 368, 415, 494, 572, 673, 686], (22, 4): [118, 230, 241, 750], (22, 8): [731], (23, 0): [124, 181, 237, 247, 277, 483, 538, 649], (23, 1): [112, 127, 153, 157, 173, 249, 450, 553, 574, 609, 650, 688, 767], (23, 2): [122, 328, 430, 451, 617, 632, 637, 679, 692, 709], (23, 3): [197, 234, 347], (23, 4): [73, 144, 535], (23, 6): [98], (24, 0): [109, 211, 213, 229, 297, 485, 531, 619, 631], (24, 1): [89, 103, 150, 258, 293, 325, 353, 380, 385, 534, 562, 600, 665, 718], (24, 2): [63, 79, 96, 252, 267, 454, 490, 591, 732], (24, 3): [110, 227, 514, 524, 527, 610, 710], (24, 4): [262, 442, 474, 641], (24, 5): [457], (24, 6): [121], (24, 7): [49], (25, 0): [45, 120, 253, 266, 291, 308, 407, 426, 445, 452, 467, 589, 677], (25, 1): [68, 383, 384, 411, 575, 607, 726], (25, 2): [172, 210, 257, 275, 301, 331, 373, 395, 497, 520, 593, 655, 685, 694], (25, 3): [108, 313, 321, 370, 398, 399, 551, 678, 752], (25, 4): [113, 543], (25, 5): [117, 189, 216], (26, 0): [78, 177, 226, 335, 428, 447, 449, 681, 753], (26, 1): [51, 125, 224, 420, 461, 599, 758], (26, 2): [87, 134, 315, 405, 700], (26, 3): [6, 40, 348, 521, 741], (26, 4): [198, 235, 288, 699], (26, 5): [71], (26, 6): [522, 613], (27, 0): [162, 239, 564, 608, 640], (27, 1): [106, 418, 651, 746], (27, 2): [38, 85, 104, 203, 251, 312, 653, 764], (27, 3): [20, 261, 541, 615, 644, 659], (27, 4): [69, 683, 704], (27, 5): [77, 183, 205, 391], (27, 6): [469, 581], (28, 0): [280, 561], (28, 1): [201, 356, 409, 446, 470, 554, 639, 751], (28, 2): [70, 269, 374, 620, 621], (28, 3): [31, 318, 389, 419, 501, 515], (28, 4): [482, 488, 547, 698, 735], (28, 5): [139, 303, 437, 652], (28, 6): [33, 295, 410, 601, 705], (29, 0): [138, 435, 481], (29, 1): [46, 287, 359, 532, 544, 687], (29, 2): [244, 296, 305, 433, 476], (29, 3): [169, 317], (29, 4): [168, 199, 233, 350, 625], (29, 5): [195, 360], (29, 6): [171, 366, 587], (29, 7): [276], (29, 9): [23], (29, 10): [7], (30, 0): [300], (30, 1): [326, 556, 602], (30, 2): [309, 645], (30, 3): [126, 132, 256, 316], (30, 4): [10, 351, 364, 444], (30, 5): [5, 52, 365, 496, 765], (30, 6): [616], (30, 10): [706], (31, 0): [16, 57, 484, 529], (31, 1): [1, 99], (31, 2): [135, 292], (31, 3): [696, 716], (31, 4): [228, 320, 394, 400, 425, 643], (31, 6): [439, 533, 675], (31, 7): [17, 48, 477], (31, 8): [188], (31, 10): [634], (32, 0): [164, 202], (32, 1): [19, 747], (32, 3): [539, 714], (32, 4): [378], (32, 5): [65, 218], (32, 6): [180, 217, 563], (32, 7): [15, 638], (32, 8): [2], (32, 9): [238], (33, 0): [4, 569], (33, 1): [18, 100, 187, 646], (33, 2): [174], (33, 4): [35, 130, 492], (33, 5): [289, 343], (33, 6): [243], (33, 8): [443], (33, 9): [131, 338, 762], (34, 2): [147], (34, 3): [260, 730], (34, 4): [91, 167, 720], (34, 5): [286], ...}
>>> grouped = df.groupby('Outcome')
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    grouped = df.groupby('Outcome')
NameError: name 'df' is not defined
>>> grouped = data.groupby('Outcome')
>>> grouped
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000026073EA18B0>
>>> grouped.get_group(0)
     Pregnancies  Glucose  ...  Age  Outcome
1              1       85  ...   31        0
3              1       89  ...   21        0
5              5      116  ...   30        0
7             10      115  ...   29        0
10             4      110  ...   30        0
..           ...      ...  ...  ...      ...
762            9       89  ...   33        0
763           10      101  ...   63        0
764            2      122  ...   27        0
765            5      121  ...   30        0
767            1       93  ...   23        0

[500 rows x 9 columns]
>>> grouped.get_group(0).to_string()

>>> grouped.get_group(0).head(30)
    Pregnancies  Glucose  BloodPressure  ...  DiabetesPedigreeFunction  Age  Outcome
1             1       85             66  ...                     0.351   31        0
3             1       89             66  ...                     0.167   21        0
5             5      116             74  ...                     0.201   30        0
7            10      115              0  ...                     0.134   29        0
10            4      110             92  ...                     0.191   30        0
12           10      139             80  ...                     1.441   57        0
18            1      103             30  ...                     0.183   33        0
20            3      126             88  ...                     0.704   27        0
21            8       99             84  ...                     0.388   50        0
27            1       97             66  ...                     0.487   22        0
28           13      145             82  ...                     0.245   57        0
29            5      117             92  ...                     0.337   38        0
30            5      109             75  ...                     0.546   60        0
32            3       88             58  ...                     0.267   22        0
33            6       92             92  ...                     0.188   28        0
34           10      122             78  ...                     0.512   45        0
35            4      103             60  ...                     0.966   33        0
36           11      138             76  ...                     0.420   35        0
40            3      180             64  ...                     0.271   26        0
41            7      133             84  ...                     0.696   37        0
42            7      106             92  ...                     0.235   48        0
44            7      159             64  ...                     0.294   40        0
46            1      146             56  ...                     0.564   29        0
47            2       71             70  ...                     0.586   22        0
49            7      105              0  ...                     0.305   24        0
50            1      103             80  ...                     0.491   22        0
51            1      101             50  ...                     0.526   26        0
52            5       88             66  ...                     0.342   30        0
54            7      150             66  ...                     0.718   42        0
55            1       73             50  ...                     0.248   21        0

[30 rows x 9 columns]
>>> g=data.groupby('Age')
>>> g.get_group(50).head(30)
     Pregnancies  Glucose  ...  Age  Outcome
0              6      148  ...   50        1
21             8       99  ...   50        0
473            7      136  ...   50        0
548            1      164  ...   50        0
614           11      138  ...   50        1
618            9      112  ...   50        1
642            6      147  ...   50        1
749            6      162  ...   50        1

[8 rows x 9 columns]
>>> g=data.groupby(['Age','Outcome'])
>>> g.get_group(50,0)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    g.get_group(50,0)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\groupby\groupby.py", line 751, in get_group
    inds = self._get_index(name)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\groupby\groupby.py", line 679, in _get_index
    return self._get_indices([name])[0]
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\groupby\groupby.py", line 652, in _get_indices
    raise ValueError(msg)
ValueError: must supply a tuple to get_group with multiple grouping keys
>>> g=data.groupby(['Age','Outcome']).groups
>>> g
{(21, 0): [3, 55, 60, 90, 94, 102, 105, 119, 136, 145, 156, 163, 182, 190, 196, 200, 208, 240, 268, 271, 273, 290, 307, 324, 354, 367, 371, 372, 382, 392, 413, 421, 422, 423, 438, 465, 486, 500, 507, 508, 511, 525, 526, 550, 566, 571, 597, 605, 623, 624, 626, 627, 629, 671, 713, 721, 736, 738], (21, 1): [220, 255, 414, 577, 580], (22, 0): [27, 32, 47, 50, 59, 74, 75, 80, 81, 83, 97, 101, 118, 137, 142, 149, 158, 166, 225, 232, 241, 279, 311, 334, 340, 342, 346, 368, 376, 377, 381, 412, 416, 432, 441, 466, 471, 472, 494, 513, 528, 530, 565, 572, 573, 585, 633, 654, 656, 673, 680, 682, 686, 697, 707, 727, 728, 729, 733, 742, 760], (22, 1): [230, 242, 397, 415, 448, 595, 606, 647, 661, 731, 750], (23, 0): [73, 98, 112, 122, 127, 144, 153, 157, 173, 181, 234, 247, 249, 277, 347, 430, 450, 483, 538, 553, 574, 609, 617, 632, 637, 649, 650, 679, 688, 692, 767], (23, 1): [124, 197, 237, 328, 451, 535, 709], (24, 0): [49, 63, 79, 89, 96, 103, 121, 150, 211, 229, 252, 258, 262, 267, 297, 325, 353, 380, 385, 442, 454, 457, 474, 490, 514, 524, 527, 531, 534, 562, 591, 600, 610, 631, 641, 665, 710, 718], (24, 1): [109, 110, 213, 227, 293, 485, 619, 732], (25, 0): [68, 108, 113, 117, 172, 210, 253, 257, 275, 313, 331, 373, 383, 384, 395, 398, 407, 411, 426, 452, 467, 497, 520, 543, 551, 575, 589, 593, 607, 677, 685, 694, 726, 752], (25, 1): [45, 120, 189, 216, 266, 291, 301, 308, 321, 370, 399, 445, 655, 678], (26, 0): [40, 51, 71, 87, 134, 224, 226, 288, 315, 335, 348, 405, 420, 428, 447, 449, 461, 521, 522, 599, 613, 699, 700, 741, 758], (26, 1): [6, 78, 125, 177, 198, 235, 681, 753], (27, 0): [20, 69, 77, 85, 104, 106, 162, 183, 203, 205, 239, 251, 418, 469, 564, 581, 608, 615, 640, 644, 651, 653, 704, 764], (27, 1): [38, 261, 312, 391, 541, 659, 683, 746], (28, 0): [33, 139, 201, 295, 318, 374, 389, 410, 437, 446, 470, 482, 488, 501, 547, 554, 601, 620, 621, 639, 652, 698, 705, 735, 751], (28, 1): [31, 70, 269, 280, 303, 356, 409, 419, 515, 561], (29, 0): [7, 46, 138, 168, 169, 233, 244, 305, 350, 433, 481, 532, 544, 587, 625, 687], (29, 1): [23, 171, 195, 199, 276, 287, 296, 317, 359, 360, 366, 435, 476], (30, 0): [5, 10, 52, 126, 256, 316, 351, 364, 365, 496, 556, 602, 616, 645, 765], (30, 1): [132, 300, 309, 326, 444, 706], (31, 0): [1, 57, 135, 228, 320, 439, 477, 529, 533, 634, 643], (31, 1): [16, 17, 48, 99, 188, 292, 394, 400, 425, 484, 675, 696, 716], (32, 0): [65, 180, 202, 217, 563, 714, 747], (32, 1): [2, 15, 19, 164, 218, 238, 378, 539, 638], (33, 0): [18, 35, 174, 289, 343, 492, 762], (33, 1): [4, 100, 130, 131, 187, 243, 338, 443, 569, 646], (34, 0): [91, 147, 167, 248, 260, 286, 464, 594, 690, 720], (34, 1): [11, 630, 715, 730], (35, 0): [36, 302, 379, 559, 576], (35, 1): [264, 386, 402, 480, 506], (36, 0): [62, 82, 160, 341, 434, 578], (36, 1): [155, 170, 175, 192, 214, 322, 424, 604, 611, 748], (37, 0): [41, 107, 151, 222, 282, 304, 327, 329, 393, 463, 549, 555, 568], (37, 1): [84, 179, 349, 417, 545, 755], (38, 0): [29, 141, 403, 431, 505, 725], (38, 1): [66, 116, 215, 270, 427, 455, 468, 598, 635, 712], (39, 0): [133, 281, 396, 462, 478, 499, 570, 744, 756], (39, 1): [61, 114, 408], (40, 0): [44, 95, 184, 191, 272, 504, 711], (40, 1): [128, 193, 612, 663, 664, 667], (41, 0): [76, 146, 246, 310, 436, 503, 518, 657, 703], (41, 1): [22, 25, 56, 165, 185, 209, 219, 332, 339, 404, 440, 502, 586], (42, 0): [54, 92, 176, 194, 250, 390, 491, 558, 583, 723, 737], (42, 1): [64, 72, 143, 152, 648, 722, 739], (43, 0): [265, 668], (43, 1): [26, 88, 154, 314, 323, 429, 540, 662, 693, 695, 761], (44, 0): [58, 333, 336], (44, 1): [254, 337, 357, 592, 691], (45, 0): [34, 86, 161, 622, 628, 669, 724], (45, 1): [369, 387, 493, 523, 590, 708, 743, 754], (46, 0): [330, 352, 536, 567, 596, 745], (46, 1): [37, 111, 231, 298, 406, 510, 689], (47, 0): [178, 672], (47, 1): [159, 283, 306, 766], (48, 0): [42, 358, 460, 636], (48, 1): [740], (49, 0): [345, 670], (49, 1): [245, 355, 701], (50, 0): [21, 473, 548], (50, 1): [0, 614, 618, 642, 749], (51, 0): [285, 517, 658], (51, 1): [14, 24, 236, 259, 458], (52, 0): [274], (52, 1): [207, 284, 584, 588, 702, 719, 757], (53, 0): [734], (53, 1): [8, 516, 546, 676], (54, 0): [67, 660], (54, 1): [9, 43, 560, 603], (55, 0): [140, 204, 401], (55, 1): [498], (56, 0): [717], (56, 1): [39, 542], (57, 0): [12, 28, 278, 344], (57, 1): [206], (58, 0): [299, 487, 512, 557], (58, 1): [53, 375, 388], (59, 0): [475], (59, 1): [13, 319], (60, 0): [30, 212, 519], (60, 1): [93, 186], (61, 0): [223], (61, 1): [115], (62, 0): [456, 582], (62, 1): [129, 579], (63, 0): [263, 361, 479, 763], (64, 0): [509], (65, 0): [148, 294, 362], (66, 0): [495, 552], (66, 1): [221, 759], (67, 0): [489, 537], (67, 1): [363], (68, 0): [674], (69, 0): [123, 684], (70, 1): [666], (72, 0): [453], (81, 0): [459]}
>>> g=data.groupby('Age')
>>> g.Age['Outcome']
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    g.Age['Outcome']
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\base.py", line 217, in __getitem__
    raise IndexError(f"Column(s) {self._selection} already selected")
IndexError: Column(s) Age already selected
>>> data.Age.max()
81
>>> data.Age.min()
21
>>> data.Age.mean()
33.240885416666664
>>> data.Age.median()
29.0
>>> data.shape
(768, 9)
>>> data.size
6912
>>> data.empty
False
>>> data.set_index()
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    data.set_index()
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\util\_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
TypeError: set_index() missing 1 required positional argument: 'keys'
>>> data.set_index('Outcome')
         Pregnancies  Glucose  ...  DiabetesPedigreeFunction  Age
Outcome                        ...                               
1                  6      148  ...                     0.627   50
0                  1       85  ...                     0.351   31
1                  8      183  ...                     0.672   32
0                  1       89  ...                     0.167   21
1                  0      137  ...                     2.288   33
...              ...      ...  ...                       ...  ...
0                 10      101  ...                     0.171   63
0                  2      122  ...                     0.340   27
0                  5      121  ...                     0.245   30
1                  1      126  ...                     0.349   47
0                  1       93  ...                     0.315   23

[768 rows x 8 columns]
>>> data
     Pregnancies  Glucose  ...  Age  Outcome
0              6      148  ...   50        1
1              1       85  ...   31        0
2              8      183  ...   32        1
3              1       89  ...   21        0
4              0      137  ...   33        1
..           ...      ...  ...  ...      ...
763           10      101  ...   63        0
764            2      122  ...   27        0
765            5      121  ...   30        0
766            1      126  ...   47        1
767            1       93  ...   23        0

[768 rows x 9 columns]
>>> d=data.set_index('Outcome',inplace=True)
>>> d
>>> data.set_index('Outcome',inplace=True)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    data.set_index('Outcome',inplace=True)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\util\_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 5446, in set_index
    raise KeyError(f"None of {missing} are in the columns")
KeyError: "None of ['Outcome'] are in the columns"
>>> data.set_index(['Outcome'],inplace=True)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    data.set_index(['Outcome'],inplace=True)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\util\_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 5446, in set_index
    raise KeyError(f"None of {missing} are in the columns")
KeyError: "None of ['Outcome'] are in the columns"
>>> 