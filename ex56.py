Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import numpy as np
>>> data=pd.DataFrame({"Name":['meenu','yashika','riya','janu','pooja'],"Age":[23,24,21,20,26],"City":["chennai","salem","chennai","salem","salem"]})
>>> data
      Name  Age     City
0    meenu   23  chennai
1  yashika   24    salem
2     riya   21  chennai
3     janu   20    salem
4    pooja   26    salem
>>> data.index
RangeIndex(start=0, stop=5, step=1)
>>> data.set_index("City")
            Name  Age
City                 
chennai    meenu   23
salem    yashika   24
chennai     riya   21
salem       janu   20
salem      pooja   26
>>> data.xs("salem")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    data.xs("salem")
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\generic.py", line 3773, in xs
    loc = index.get_loc(key)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\range.py", line 388, in get_loc
    raise KeyError(key)
KeyError: 'salem'
>>> data=pd.DataFrame({"Name":['gowtham','meenu','yashika','riya','janu','rishi','pooja'],"Age":[23,27,22,24,21,20,26],"City":["chennai","salem","chennai","salem","chennai","salem","salem"],"Gender":['male','female','female','female','female',,'male','female',]})
SyntaxError: invalid syntax
>>> 
>>> data=pd.DataFrame({"Name":['gowtham','meenu','yashika','riya','janu','rishi','pooja'],"Age":[23,27,22,24,21,20,26],"City":["chennai","salem","chennai","salem","chennai","salem","salem"],"Gender":['male','female','female','female','female','male','female',]})
>>> data
      Name  Age     City  Gender
0  gowtham   23  chennai    male
1    meenu   27    salem  female
2  yashika   22  chennai  female
3     riya   24    salem  female
4     janu   21  chennai  female
5    rishi   20    salem    male
6    pooja   26    salem  female
>>> data.index
RangeIndex(start=0, stop=7, step=1)
>>> data.set_index("Gender")
           Name  Age     City
Gender                       
male    gowtham   23  chennai
female    meenu   27    salem
female  yashika   22  chennai
female     riya   24    salem
female     janu   21  chennai
male      rishi   20    salem
female    pooja   26    salem
>>> data.xs("female")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    data.xs("female")
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\generic.py", line 3773, in xs
    loc = index.get_loc(key)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\range.py", line 388, in get_loc
    raise KeyError(key)
KeyError: 'female'
>>> data.xs('female')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    data.xs('female')
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\generic.py", line 3773, in xs
    loc = index.get_loc(key)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\range.py", line 388, in get_loc
    raise KeyError(key)
KeyError: 'female'
>>> import  numpy as n
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
>>> data.to_string
<bound method DataFrame.to_string of               Name            Team  ...            College     Salary
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

[457 rows x 9 columns]>
>>> data.to_string("f://DATA SCIENCE NOTES/nba.csv")
>>> d=data.to_string("f://DATA SCIENCE NOTES/nba.csv")
>>> d
>>> d
>>> print(d)
None
>>> data=pd.to_timedelta(np.arange(457),'D')
>>> data
TimedeltaIndex([  '0 days',   '1 days',   '2 days',   '3 days',   '4 days',
                  '5 days',   '6 days',   '7 days',   '8 days',   '9 days',
                ...
                '447 days', '448 days', '449 days', '450 days', '451 days',
                '452 days', '453 days', '454 days', '455 days', '456 days'],
               dtype='timedelta64[ns]', length=457, freq=None)
>>> d1=pd.read_csv("f://DATA SCIENCE NOTES/nba.csv")
>>> d1
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
>>> d2=pd.to_timedelta(np.arange(457),'D')
>>> d2
TimedeltaIndex([  '0 days',   '1 days',   '2 days',   '3 days',   '4 days',
                  '5 days',   '6 days',   '7 days',   '8 days',   '9 days',
                ...
                '447 days', '448 days', '449 days', '450 days', '451 days',
                '452 days', '453 days', '454 days', '455 days', '456 days'],
               dtype='timedelta64[ns]', length=457, freq=None)
>>> d=d1+d2
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    d=d1+d2
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\ops\common.py", line 69, in new_method
    return method(self, other)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\arraylike.py", line 92, in __add__
    return self._arith_method(other, operator.add)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 6859, in _arith_method
    self, other = ops.align_method_FRAME(self, other, axis, flex=True, level=None)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\ops\__init__.py", line 281, in align_method_FRAME
    right = to_series(right)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\ops\__init__.py", line 238, in to_series
    raise ValueError(
ValueError: Unable to coerce to Series, length must be 1: given 457
>>> d=pd.DataFrame([d1],[d2])
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    d=pd.DataFrame([d1],[d2])
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 711, in __init__
    mgr = ndarray_to_mgr(
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\internals\construction.py", line 302, in ndarray_to_mgr
    values = _prep_ndarray(values, copy=copy)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\internals\construction.py", line 553, in _prep_ndarray
    raise ValueError(f"Must pass 2-d input. shape={values.shape}")
ValueError: Must pass 2-d input. shape=(1, 457, 1)
>>> d=pd.DataFrame({[d1],[d2]})
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    d=pd.DataFrame({[d1],[d2]})
TypeError: unhashable type: 'list'
>>> d=pd.DataFrame([[d1],[d2]])
>>> d
                                                   0
0                               Name             ...
1  TimedeltaIndex([  '0 days',   '1 days',   '2 d...
>>> d.to_period(457)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    d.to_period(457)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 10427, in to_period
    raise TypeError(f"unsupported Type {type(old_ax).__name__}")
TypeError: unsupported Type RangeIndex
>>> d
                                                   0
0                               Name             ...
1  TimedeltaIndex([  '0 days',   '1 days',   '2 d...
>>> d.to_string()
"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         0\n0                                Name                    Team  Number Position  Age  Height  Weight                College      Salary\n0    0               Avery Bradley          Boston Celtics       0       PG   25  06-Feb     180                  Texas   7730337.0\n1    1                 Jae Crowder          Boston Celtics      99       SF   25  06-Jun     235              Marquette   6796117.0\n2    2                John Holland          Boston Celtics      30       SG   27  06-May     205      Boston University         NaN\n3    3                 R.J. Hunter          Boston Celtics      28       SG   22  06-May     185          Georgia State   1148640.0\n4    4               Jonas Jerebko          Boston Celtics       8       PF   29  06-Oct     231                    NaN   5000000.0\n..                                                                                                                              ...\n452  452                Trey Lyles               Utah Jazz      41       PF   20  06-Oct     234               Kentucky   2239800.0\n453  453              Shelvin Mack               Utah Jazz       8       PG   26  06-Mar     203                 Butler   2433333.0\n454  454                 Raul Neto               Utah Jazz      25       PG   24  06-Jan     179                    NaN    900000.0\n455  455              Tibor Pleiss               Utah Jazz      21        C   26  07-Mar     256                    NaN   2900000.0\n456  456               Jeff Withey               Utah Jazz      24        C   26  Jul-00     231                 Kansas    947276.0\n\n[457 rows x 1 columns]\n1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      TimedeltaIndex([  '0 days',   '1 days',   '2 days',   '3 days',   '4 days',\n                  '5 days',   '6 days',   '7 days',   '8 days',   '9 days',\n                ...\n                '447 days', '448 days', '449 days', '450 days', '451 days',\n                '452 days', '453 days', '454 days', '455 days', '456 days'],\n               dtype='timedelta64[ns]', length=457, freq=None)"
>>> print(d.to_string())
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         0
0                                Name                    Team  Number Position  Age  Height  Weight                College      Salary
0    0               Avery Bradley          Boston Celtics       0       PG   25  06-Feb     180                  Texas   7730337.0
1    1                 Jae Crowder          Boston Celtics      99       SF   25  06-Jun     235              Marquette   6796117.0
2    2                John Holland          Boston Celtics      30       SG   27  06-May     205      Boston University         NaN
3    3                 R.J. Hunter          Boston Celtics      28       SG   22  06-May     185          Georgia State   1148640.0
4    4               Jonas Jerebko          Boston Celtics       8       PF   29  06-Oct     231                    NaN   5000000.0
..                                                                                                                              ...
452  452                Trey Lyles               Utah Jazz      41       PF   20  06-Oct     234               Kentucky   2239800.0
453  453              Shelvin Mack               Utah Jazz       8       PG   26  06-Mar     203                 Butler   2433333.0
454  454                 Raul Neto               Utah Jazz      25       PG   24  06-Jan     179                    NaN    900000.0
455  455              Tibor Pleiss               Utah Jazz      21        C   26  07-Mar     256                    NaN   2900000.0
456  456               Jeff Withey               Utah Jazz      24        C   26  Jul-00     231                 Kansas    947276.0

[457 rows x 1 columns]
1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      TimedeltaIndex([  '0 days',   '1 days',   '2 days',   '3 days',   '4 days',
                  '5 days',   '6 days',   '7 days',   '8 days',   '9 days',
                ...
                '447 days', '448 days', '449 days', '450 days', '451 days',
                '452 days', '453 days', '454 days', '455 days', '456 days'],
               dtype='timedelta64[ns]', length=457, freq=None)
>>> d=pd.DataFrame([[d1],"date":[d2]])
SyntaxError: invalid syntax
>>> d=pd.DataFrame([[d1],[d2]])
>>> 