Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> d=pd.read_csv('f://DATA SCIENCE NOTES/nba.csv,index_col=0')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    d=pd.read_csv('f://DATA SCIENCE NOTES/nba.csv,index_col=0')
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\util\_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\io\parsers\readers.py", line 586, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\io\parsers\readers.py", line 482, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\io\parsers\readers.py", line 811, in __init__
    self._engine = self._make_engine(self.engine)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\io\parsers\readers.py", line 1040, in _make_engine
    return mapping[engine](self.f, **self.options)  # type: ignore[call-arg]
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\io\parsers\c_parser_wrapper.py", line 51, in __init__
    self._open_handles(src, kwds)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\io\parsers\base_parser.py", line 222, in _open_handles
    self.handles = get_handle(
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\io\common.py", line 608, in get_handle
    ioargs = _get_filepath_or_buffer(
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\io\common.py", line 336, in _get_filepath_or_buffer
    fsspec = import_optional_dependency("fsspec")
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\compat\_optional.py", line 118, in import_optional_dependency
    raise ImportError(msg) from None
ImportError: Missing optional dependency 'fsspec'.  Use pip or conda to install fsspec.
>>> d=pd.read_csv('f://DATA SCIENCE NOTES/nba.csv,index_col=0')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    d=pd.read_csv('f://DATA SCIENCE NOTES/nba.csv,index_col=0')
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\util\_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\io\parsers\readers.py", line 586, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\io\parsers\readers.py", line 482, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\io\parsers\readers.py", line 811, in __init__
    self._engine = self._make_engine(self.engine)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\io\parsers\readers.py", line 1040, in _make_engine
    return mapping[engine](self.f, **self.options)  # type: ignore[call-arg]
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\io\parsers\c_parser_wrapper.py", line 51, in __init__
    self._open_handles(src, kwds)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\io\parsers\base_parser.py", line 222, in _open_handles
    self.handles = get_handle(
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\io\common.py", line 608, in get_handle
    ioargs = _get_filepath_or_buffer(
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\io\common.py", line 357, in _get_filepath_or_buffer
    file_obj = fsspec.open(
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\fsspec\core.py", line 135, in open
    out = self.__enter__()
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\fsspec\core.py", line 102, in __enter__
    f = self.fs.open(self.path, mode=mode)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\fsspec\spec.py", line 976, in open
    f = self._open(
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\fsspec\implementations\local.py", line 145, in _open
    return LocalFileOpener(path, mode, fs=self, **kwargs)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\fsspec\implementations\local.py", line 236, in __init__
    self._open()
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\fsspec\implementations\local.py", line 241, in _open
    self.f = open(self.path, mode=self.mode)
FileNotFoundError: [Errno 2] No such file or directory: 'f:/DATA SCIENCE NOTES/nba.csv,index_col=0'
>>> self._open()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    self._open()
NameError: name 'self' is not defined
>>> d=pd.read_csv('f://DATA SCIENCE NOTES/nba.csv')
>>> d
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
>>> da=pd.read_excel('f:\DATA SCIENCE NOTES\KSRCE DB.xlsx')
>>> da
    S_No  ...                                    Contact_Address
0      1  ...  16,KRISHNA SAMY STREET, MUNICIPAL COLONY,ERODE...
1      2  ...  15/4, SYED JAFFER STREET, ARISIPALAYAM,SALEM-6...
2      3  ...  4/36, RAMANATHAPURAM, GOUNDAMPALAYAM(PO), KUMA...
3      4  ...  KARUKANSAVA(VILL),KAVERIPATTINAM(PO),KRISHNAGI...
4      5  ...  166 GOPAL SAMY KOVIL STREET NADUPALAYAM CHITHO...
5      6  ...  NO:51,MUMBAI SOUTHERN ROADWAYS PVT.LTD,OPP.JOH...
6      7  ...  25/1 THANGAM NAGAR,T.V PUDUR,PERUNDURAI-638052...
7      8  ...  4/494, IYNTHUPANAI, KADACHANALLUR(PO), KUMARAP...
8      9  ...  78/2, N. G. G. O COLONY, PUTHUMARIAMMAN KOVIL ...
9     10  ...  6/2 ,PALAMEDU ,PALAMEDU (PO),TIRUCHENGODE (T.K...
10    11  ...  3/112,DURAIRAMASAMY NAGAR,VALLIYARACHAL ROAD, ...
11    12  ...  6/39 BOOYER STREET RAMAGOUNDANUR ERUPPALI(PO) ...
12    13  ...  NEIKARAPATTI, CHINNATHAMBIPALAYAM (PO), TIRUCH...
13    14  ...  21/33 WEST STREET, OVIYAMPALAYAM, PARAMATHI VE...
14    15  ...      9,AMARAVATHY NAGAR ,RN PUDUR(PO),ERODE-638005
15    16  ...  58/73 NADUPALAYAM ,KANJI KOVIL ROAD,CHITHODE,E...
16    17  ...  136/P5,PANANKATTUPALAYAM, DEVANANKURICHI (PO),...
17    18  ...  2/488-15, VINAYAKAPURAM, KUTCHIPALAYAM (PO), T...
18    19  ...           61, THACHAMOZHI, SATHANKULAM, TUTICORIN.
19    20  ...  59-A JAGADESH CHETTY KADU,PRABATH BACK SIDE ,G...
20    21  ...   3/370 SAMBARAVALLI, PETHIKUTTAI (PO),COIMBATORE 
21    22  ...  NO:49/17,ELLAMAIYAKINAR KOIL STREET, CHIDHAMBA...
22    23  ...      121,Gandhi street, kuttipalayam, erode-638312
23    24  ...  Gokul Raj mariyappan,2/3-300,thuttampatty by-p...
24    25  ...  91,Vinobha nagar,Thalaivaipettai,Erode distric...
25    26  ...  Address: 12-Eswaran kovil street, Mecheri (pos...
26    27  ...     101/55a, vaikalpatrai, allikutai [po], salem-3
27    28  ...  9/3 ayyan nagar 2nd St. Parapalayam mangalam r...

[28 rows x 20 columns]
>>> da.DOB
0     2000-06-14 00:00:00
1     2001-07-30 00:00:00
2     2000-11-15 00:00:00
3     2000-12-22 00:00:00
4     2001-07-02 00:00:00
5     2000-12-20 00:00:00
6     2001-06-16 00:00:00
7     2001-07-12 00:00:00
8     2001-01-03 00:00:00
9     2000-12-26 00:00:00
10             01.11.2000
11    2000-07-07 00:00:00
12    1999-11-21 00:00:00
13    2001-03-22 00:00:00
14    2000-06-27 00:00:00
15    2001-09-25 00:00:00
16    2001-03-05 00:00:00
17    2000-11-10 00:00:00
18    1999-11-20 00:00:00
19    2001-01-10 00:00:00
20    2001-05-26 00:00:00
21    2000-08-19 00:00:00
22    2001-08-09 00:00:00
23    2000-07-02 00:00:00
24    2000-09-17 00:00:00
25    2000-12-16 00:00:00
26    2000-09-28 00:00:00
27             13.04.2000
Name: DOB, dtype: object
>>> da.Arrear_Count
0     NaN
1     NaN
2     NaN
3     NaN
4     NaN
5     NaN
6     NaN
7     NaN
8     NaN
9     NaN
10    NaN
11    1.0
12    NaN
13    0.0
14    0.0
15    0.0
16    0.0
17    0.0
18    0.0
19    0.0
20    0.0
21    0.0
22    0.0
23    0.0
24    0.0
25    0.0
26    0.0
27    0.0
Name: Arrear_Count, dtype: float64
>>> da.columns
Index(['S_No', 'Reg_No', 'Name', 'College', 'Degree', 'Branch', 'DOB',
       'Gender', '10th_Percentage', '10th_Year', '12th_Percentage', '12_Year',
       'Diploma_Percentage', 'Diploma_Year', 'UG_CGPA', 'Arrear_Status',
       'Arrear_Count', 'Mobile_NO', 'Email_ID', 'Contact_Address'],
      dtype='object')
>>> da.copy(y)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    da.copy(y)
NameError: name 'y' is not defined
>>> da.copy(depp:'bool_t'=True)
SyntaxError: invalid syntax
>>> da.copy(deep:'bool_t'=True)
SyntaxError: invalid syntax
>>> da.count(axis:0)
SyntaxError: invalid syntax
>>> da.count(axis=0)
S_No                  28
Reg_No                28
Name                  28
College               28
Degree                28
Branch                28
DOB                   28
Gender                28
10th_Percentage       28
10th_Year             28
12th_Percentage       26
12_Year               26
Diploma_Percentage     2
Diploma_Year           2
UG_CGPA               28
Arrear_Status         28
Arrear_Count          16
Mobile_NO             28
Email_ID              28
Contact_Address       28
dtype: int64
>>> da.drop("Name")
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    da.drop("Name")
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\util\_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 4901, in drop
    return super().drop(
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\generic.py", line 4147, in drop
    obj = obj._drop_axis(labels, axis, level=level, errors=errors)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\generic.py", line 4182, in _drop_axis
    new_axis = axis.drop(labels, errors=errors)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 6018, in drop
    raise KeyError(f"{labels[mask]} not found in axis")
KeyError: "['Name'] not found in axis"
>>> da.drop(['Reg_N0'])
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    da.drop(['Reg_N0'])
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\util\_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 4901, in drop
    return super().drop(
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\generic.py", line 4147, in drop
    obj = obj._drop_axis(labels, axis, level=level, errors=errors)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\generic.py", line 4182, in _drop_axis
    new_axis = axis.drop(labels, errors=errors)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 6018, in drop
    raise KeyError(f"{labels[mask]} not found in axis")
KeyError: "['Reg_N0'] not found in axis"
>>> da.drop['Reg_N0']
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    da.drop['Reg_N0']
TypeError: 'method' object is not subscriptable
>>> import matplotlib.pypplt as plt
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    import matplotlib.pypplt as plt
ModuleNotFoundError: No module named 'matplotlib.pypplt'
>>> import numpy as np
>>> a=np.array([0,1,2,3,4])
>>> b=np.array([0,1,2,3,4])
>>> A,B=np.meshgrid(a,b)
>>> A
array([[0, 1, 2, 3, 4],
       [0, 1, 2, 3, 4],
       [0, 1, 2, 3, 4],
       [0, 1, 2, 3, 4],
       [0, 1, 2, 3, 4]])
>>> B
array([[0, 0, 0, 0, 0],
       [1, 1, 1, 1, 1],
       [2, 2, 2, 2, 2],
       [3, 3, 3, 3, 3],
       [4, 4, 4, 4, 4]])
>>> print(A,B=np.meshgrid(a,b))
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(A,B=np.meshgrid(a,b))
TypeError: 'B' is an invalid keyword argument for print()
>>> from matplotlib import pyplot as plt
>>> import matplotlib.pyplot as plt
>>> plt.plot(A,B,'or')
[<matplotlib.lines.Line2D object at 0x0000024C865495B0>, <matplotlib.lines.Line2D object at 0x0000024C86549610>, <matplotlib.lines.Line2D object at 0x0000024C86549700>, <matplotlib.lines.Line2D object at 0x0000024C86549820>, <matplotlib.lines.Line2D object at 0x0000024C86549940>]
>>> plt.show()

========= RESTART: C:/Users/Asus/OneDrive/programs/ex48.py =========
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex48.py", line 3, in <module>
    a=np.array([0,1,2,3,4])
NameError: name 'np' is not defined
>>> 
========= RESTART: C:/Users/Asus/OneDrive/programs/ex48.py =========
A
B
>>> 
========= RESTART: C:/Users/Asus/OneDrive/programs/ex48.py =========
a
b

========= RESTART: C:/Users/Asus/OneDrive/programs/ex48.py =========
a
b
>>> 
========= RESTART: C:/Users/Asus/OneDrive/programs/ex48.py =========
[0 1 2 3 4]
[0 1 2 3 4]
[<matplotlib.lines.Line2D object at 0x000001A4F3F5CEE0>, <matplotlib.lines.Line2D object at 0x000001A4F3F5CF40>, <matplotlib.lines.Line2D object at 0x000001A4F3F72070>, <matplotlib.lines.Line2D object at 0x000001A4F3F72190>, <matplotlib.lines.Line2D object at 0x000001A4F3F722B0>]

========= RESTART: C:/Users/Asus/OneDrive/programs/ex48.py =========
[0 1 2 3 4]
[0 1 2 3 4]
[[0 1 2 3 4]
 [0 1 2 3 4]
 [0 1 2 3 4]
 [0 1 2 3 4]
 [0 1 2 3 4]]
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex48.py", line 10, in <module>
    PRINT(B)
NameError: name 'PRINT' is not defined
>>> 
========= RESTART: C:/Users/Asus/OneDrive/programs/ex48.py =========
[0 1 2 3 4]
[0 1 2 3 4]
[[0 1 2 3 4]
 [0 1 2 3 4]
 [0 1 2 3 4]
 [0 1 2 3 4]
 [0 1 2 3 4]]
[[0 0 0 0 0]
 [1 1 1 1 1]
 [2 2 2 2 2]
 [3 3 3 3 3]
 [4 4 4 4 4]]
[<matplotlib.lines.Line2D object at 0x00000243E3C3CEE0>, <matplotlib.lines.Line2D object at 0x00000243E3C3CF40>, <matplotlib.lines.Line2D object at 0x00000243E5C51070>, <matplotlib.lines.Line2D object at 0x00000243E5C51190>, <matplotlib.lines.Line2D object at 0x00000243E5C512B0>]

========= RESTART: C:/Users/Asus/OneDrive/programs/ex48.py =========
[0 1 2 3 4]
[0 1 2 3 4]
[[0 1 2 3 4]
 [0 1 2 3 4]
 [0 1 2 3 4]
 [0 1 2 3 4]
 [0 1 2 3 4]]
[[0 0 0 0 0]
 [1 1 1 1 1]
 [2 2 2 2 2]
 [3 3 3 3 3]
 [4 4 4 4 4]]

========= RESTART: C:/Users/Asus/OneDrive/programs/ex48.py =========
a.array [0 1 2 3 4]
b.array [0 1 2 3 4]
A [[0 1 2 3 4]
 [0 1 2 3 4]
 [0 1 2 3 4]
 [0 1 2 3 4]
 [0 1 2 3 4]]
B [[0 0 0 0 0]
 [1 1 1 1 1]
 [2 2 2 2 2]
 [3 3 3 3 3]
 [4 4 4 4 4]]

========= RESTART: C:/Users/Asus/OneDrive/programs/ex48.py =========
a.array :  [0 1 2 3 4]
b.array :  [0 1 2 3 4]
A [[0 1 2 3 4]
 [0 1 2 3 4]
 [0 1 2 3 4]
 [0 1 2 3 4]
 [0 1 2 3 4]]
B [[0 0 0 0 0]
 [1 1 1 1 1]
 [2 2 2 2 2]
 [3 3 3 3 3]
 [4 4 4 4 4]]
>>> np.mgrid
<numpy.lib.index_tricks.MGridClass object at 0x000001FB7717D0A0>
>>> 
========= RESTART: C:/Users/Asus/OneDrive/programs/ex48.py =========
a.array :  [0 1 2 3 4]
b.array :  [0 1 2 3 4]
A [[0 1 2 3 4]
 [0 1 2 3 4]
 [0 1 2 3 4]
 [0 1 2 3 4]
 [0 1 2 3 4]]
B [[0 0 0 0 0]
 [1 1 1 1 1]
 [2 2 2 2 2]
 [3 3 3 3 3]
 [4 4 4 4 4]]
