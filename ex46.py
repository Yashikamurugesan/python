Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> x= {'Name': ['Joe', 'Nat', 'Harry','Jack','Jose','Jill','Rose'],
                'Age': [20, 21, 19,17,18,19,17],
                'Marks': [85.10, 77.80, 91.54,72,87.9,90,72]}

>>> y= pd.DataFrame(x)
>>> z=y.head()
>>> print(z)
    Name  Age  Marks
0    Joe   20  85.10
1    Nat   21  77.80
2  Harry   19  91.54
3   Jack   17  72.00
4   Jose   18  87.90
>>> data=pd.read_html('f:\DATA SCIENCE NOTES\pandas2 (1).html')
>>> print(data)

>>> data=pd.read_excel('f:\DATA SCIENCE NOTES\KSRCE DB.xlsx')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    data=pd.read_excel('f:\DATA SCIENCE NOTES\KSRCE DB.xlsx')
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\util\_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\io\excel\_base.py", line 364, in read_excel
    io = ExcelFile(io, storage_options=storage_options, engine=engine)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\io\excel\_base.py", line 1233, in __init__
    self._reader = self._engines[engine](self._io, storage_options=storage_options)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\io\excel\_openpyxl.py", line 521, in __init__
    import_optional_dependency("openpyxl")
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\compat\_optional.py", line 118, in import_optional_dependency
    raise ImportError(msg) from None
ImportError: Missing optional dependency 'openpyxl'.  Use pip or conda to install openpyxl.
>>> data=pd.read_excel('f:\DATA SCIENCE NOTES\KSRCE DB.xlsx')
>>> data
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
>>> data=pd.read_excel('f:\DATA SCIENCE NOTES\KSRCE DB.xlsx',header=0)
>>> data
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
>>> data=pd.read_excel('f:\DATA SCIENCE NOTES\KSRCE DB.xlsx',header=1)
>>> data
     1  ...  16,KRISHNA SAMY STREET, MUNICIPAL COLONY,ERODE-638004
0    2  ...  15/4, SYED JAFFER STREET, ARISIPALAYAM,SALEM-6...    
1    3  ...  4/36, RAMANATHAPURAM, GOUNDAMPALAYAM(PO), KUMA...    
2    4  ...  KARUKANSAVA(VILL),KAVERIPATTINAM(PO),KRISHNAGI...    
3    5  ...  166 GOPAL SAMY KOVIL STREET NADUPALAYAM CHITHO...    
4    6  ...  NO:51,MUMBAI SOUTHERN ROADWAYS PVT.LTD,OPP.JOH...    
5    7  ...  25/1 THANGAM NAGAR,T.V PUDUR,PERUNDURAI-638052...    
6    8  ...  4/494, IYNTHUPANAI, KADACHANALLUR(PO), KUMARAP...    
7    9  ...  78/2, N. G. G. O COLONY, PUTHUMARIAMMAN KOVIL ...    
8   10  ...  6/2 ,PALAMEDU ,PALAMEDU (PO),TIRUCHENGODE (T.K...    
9   11  ...  3/112,DURAIRAMASAMY NAGAR,VALLIYARACHAL ROAD, ...    
10  12  ...  6/39 BOOYER STREET RAMAGOUNDANUR ERUPPALI(PO) ...    
11  13  ...  NEIKARAPATTI, CHINNATHAMBIPALAYAM (PO), TIRUCH...    
12  14  ...  21/33 WEST STREET, OVIYAMPALAYAM, PARAMATHI VE...    
13  15  ...      9,AMARAVATHY NAGAR ,RN PUDUR(PO),ERODE-638005    
14  16  ...  58/73 NADUPALAYAM ,KANJI KOVIL ROAD,CHITHODE,E...    
15  17  ...  136/P5,PANANKATTUPALAYAM, DEVANANKURICHI (PO),...    
16  18  ...  2/488-15, VINAYAKAPURAM, KUTCHIPALAYAM (PO), T...    
17  19  ...           61, THACHAMOZHI, SATHANKULAM, TUTICORIN.    
18  20  ...  59-A JAGADESH CHETTY KADU,PRABATH BACK SIDE ,G...    
19  21  ...   3/370 SAMBARAVALLI, PETHIKUTTAI (PO),COIMBATORE     
20  22  ...  NO:49/17,ELLAMAIYAKINAR KOIL STREET, CHIDHAMBA...    
21  23  ...      121,Gandhi street, kuttipalayam, erode-638312    
22  24  ...  Gokul Raj mariyappan,2/3-300,thuttampatty by-p...    
23  25  ...  91,Vinobha nagar,Thalaivaipettai,Erode distric...    
24  26  ...  Address: 12-Eswaran kovil street, Mecheri (pos...    
25  27  ...     101/55a, vaikalpatrai, allikutai [po], salem-3    
26  28  ...  9/3 ayyan nagar 2nd St. Parapalayam mangalam r...    

[27 rows x 20 columns]
>>> data.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 27 entries, 0 to 26
Data columns (total 20 columns):
 #   Column                                                 Non-Null Count  Dtype  
---  ------                                                 --------------  -----  
 0   1                                                      27 non-null     int64  
 1   1813006                                                27 non-null     int64  
 2   BALAMURUGAN C                                          27 non-null     object 
 3   KSRCE                                                  27 non-null     object 
 4   B.E                                                    27 non-null     object 
 5   CSE                                                    27 non-null     object 
 6   2000-06-14 00:00:00                                    27 non-null     object 
 7   MALE                                                   27 non-null     object 
 8   94.6                                                   27 non-null     float64
 9   2016                                                   27 non-null     int64  
 10  87.41                                                  25 non-null     float64
 11  2018                                                   25 non-null     float64
 12  NA                                                     2 non-null      float64
 13  NA.1                                                   2 non-null      float64
 14  8.68                                                   27 non-null     float64
 15  NHA                                                    27 non-null     object 
 16  NA.2                                                   16 non-null     float64
 17  7305207408                                             27 non-null     int64  
 18  cbalamurugan2k@gmail.com                               27 non-null     object 
 19  16,KRISHNA SAMY STREET, MUNICIPAL COLONY,ERODE-638004  27 non-null     object 
dtypes: float64(7), int64(4), object(9)
memory usage: 4.3+ KB
>>> data
     1  ...  16,KRISHNA SAMY STREET, MUNICIPAL COLONY,ERODE-638004
0    2  ...  15/4, SYED JAFFER STREET, ARISIPALAYAM,SALEM-6...    
1    3  ...  4/36, RAMANATHAPURAM, GOUNDAMPALAYAM(PO), KUMA...    
2    4  ...  KARUKANSAVA(VILL),KAVERIPATTINAM(PO),KRISHNAGI...    
3    5  ...  166 GOPAL SAMY KOVIL STREET NADUPALAYAM CHITHO...    
4    6  ...  NO:51,MUMBAI SOUTHERN ROADWAYS PVT.LTD,OPP.JOH...    
5    7  ...  25/1 THANGAM NAGAR,T.V PUDUR,PERUNDURAI-638052...    
6    8  ...  4/494, IYNTHUPANAI, KADACHANALLUR(PO), KUMARAP...    
7    9  ...  78/2, N. G. G. O COLONY, PUTHUMARIAMMAN KOVIL ...    
8   10  ...  6/2 ,PALAMEDU ,PALAMEDU (PO),TIRUCHENGODE (T.K...    
9   11  ...  3/112,DURAIRAMASAMY NAGAR,VALLIYARACHAL ROAD, ...    
10  12  ...  6/39 BOOYER STREET RAMAGOUNDANUR ERUPPALI(PO) ...    
11  13  ...  NEIKARAPATTI, CHINNATHAMBIPALAYAM (PO), TIRUCH...    
12  14  ...  21/33 WEST STREET, OVIYAMPALAYAM, PARAMATHI VE...    
13  15  ...      9,AMARAVATHY NAGAR ,RN PUDUR(PO),ERODE-638005    
14  16  ...  58/73 NADUPALAYAM ,KANJI KOVIL ROAD,CHITHODE,E...    
15  17  ...  136/P5,PANANKATTUPALAYAM, DEVANANKURICHI (PO),...    
16  18  ...  2/488-15, VINAYAKAPURAM, KUTCHIPALAYAM (PO), T...    
17  19  ...           61, THACHAMOZHI, SATHANKULAM, TUTICORIN.    
18  20  ...  59-A JAGADESH CHETTY KADU,PRABATH BACK SIDE ,G...    
19  21  ...   3/370 SAMBARAVALLI, PETHIKUTTAI (PO),COIMBATORE     
20  22  ...  NO:49/17,ELLAMAIYAKINAR KOIL STREET, CHIDHAMBA...    
21  23  ...      121,Gandhi street, kuttipalayam, erode-638312    
22  24  ...  Gokul Raj mariyappan,2/3-300,thuttampatty by-p...    
23  25  ...  91,Vinobha nagar,Thalaivaipettai,Erode distric...    
24  26  ...  Address: 12-Eswaran kovil street, Mecheri (pos...    
25  27  ...     101/55a, vaikalpatrai, allikutai [po], salem-3    
26  28  ...  9/3 ayyan nagar 2nd St. Parapalayam mangalam r...    

[27 rows x 20 columns]
>>> data.CSE
0     CSE
1     CSE
2     CSE
3     CSE
4     CSE
5     CSE
6     CSE
7     CSE
8     CSE
9     CSE
10    CSE
11    CSE
12    CSE
13    CSE
14    CSE
15    CSE
16    CSE
17    CSE
18    ECE
19    ECE
20    ECE
21    ECE
22     IT
23     IT
24     IT
25     IT
26     IT
Name: CSE, dtype: object
>>> data.head(0)
Empty DataFrame
Columns: [1, 1813006, BALAMURUGAN C, KSRCE, B.E, CSE, 2000-06-14 00:00:00, MALE, 94.6, 2016, 87.41, 2018, NA, NA.1, 8.68, NHA, NA.2, 7305207408, cbalamurugan2k@gmail.com, 16,KRISHNA SAMY STREET, MUNICIPAL COLONY,ERODE-638004]
Index: []
>>> data.head([0:6])
SyntaxError: invalid syntax
>>> data.head(1)
   1  ...  16,KRISHNA SAMY STREET, MUNICIPAL COLONY,ERODE-638004
0  2  ...  15/4, SYED JAFFER STREET, ARISIPALAYAM,SALEM-6...    

[1 rows x 20 columns]
>>> x=pd.read_csv('f:\DATA SCIENCE NOTES\nba.csv')
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    x=pd.read_csv('f:\DATA SCIENCE NOTES\nba.csv')
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
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\io\common.py", line 701, in get_handle
    handle = open(
OSError: [Errno 22] Invalid argument: 'f:\\DATA SCIENCE NOTES\nba.csv'
>>> x=pd.read_csv('f:\\DATA SCIENCE NOTES\nba.csv')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    x=pd.read_csv('f:\\DATA SCIENCE NOTES\nba.csv')
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
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\io\common.py", line 701, in get_handle
    handle = open(
OSError: [Errno 22] Invalid argument: 'f:\\DATA SCIENCE NOTES\nba.csv'
>>> x=pd.read_csv('f:/DATA SCIENCE NOTES/nba.csv')
>>> x
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
>>> x.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 457 entries, 0 to 456
Data columns (total 9 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   Name      457 non-null    object 
 1   Team      457 non-null    object 
 2   Number    457 non-null    int64  
 3   Position  457 non-null    object 
 4   Age       457 non-null    int64  
 5   Height    457 non-null    object 
 6   Weight    457 non-null    int64  
 7   College   373 non-null    object 
 8   Salary    446 non-null    float64
dtypes: float64(1), int64(3), object(5)
memory usage: 32.3+ KB
>>> x.Age
0      25
1      25
2      27
3      22
4      29
       ..
452    20
453    26
454    24
455    26
456    26
Name: Age, Length: 457, dtype: int64
>>> x.head()
            Name            Team  Number  ... Weight            College     Salary
0  Avery Bradley  Boston Celtics       0  ...    180              Texas  7730337.0
1    Jae Crowder  Boston Celtics      99  ...    235          Marquette  6796117.0
2   John Holland  Boston Celtics      30  ...    205  Boston University        NaN
3    R.J. Hunter  Boston Celtics      28  ...    185      Georgia State  1148640.0
4  Jonas Jerebko  Boston Celtics       8  ...    231                NaN  5000000.0

[5 rows x 9 columns]
>>> x.tail()
             Name       Team  Number  ... Weight   College     Salary
452    Trey Lyles  Utah Jazz      41  ...    234  Kentucky  2239800.0
453  Shelvin Mack  Utah Jazz       8  ...    203    Butler  2433333.0
454     Raul Neto  Utah Jazz      25  ...    179       NaN   900000.0
455  Tibor Pleiss  Utah Jazz      21  ...    256       NaN  2900000.0
456   Jeff Withey  Utah Jazz      24  ...    231    Kansas   947276.0

[5 rows x 9 columns]
>>> x.College
0                  Texas
1              Marquette
2      Boston University
3          Georgia State
4                    NaN
             ...        
452             Kentucky
453               Butler
454                  NaN
455                  NaN
456               Kansas
Name: College, Length: 457, dtype: object
>>> x.College.head()
0                Texas
1            Marquette
2    Boston University
3        Georgia State
4                  NaN
Name: College, dtype: object
>>> x.head().Name.tail()
0    Avery Bradley
1      Jae Crowder
2     John Holland
3      R.J. Hunter
4    Jonas Jerebko
Name: Name, dtype: object
>>> x=pd.read_csv('f:/DATA SCIENCE NOTES/nba.csv',header(0))
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    x=pd.read_csv('f:/DATA SCIENCE NOTES/nba.csv',header(0))
NameError: name 'header' is not defined
>>> x=pd.read_csv('f:/DATA SCIENCE NOTES/nba.csv',header(1))
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    x=pd.read_csv('f:/DATA SCIENCE NOTES/nba.csv',header(1))
NameError: name 'header' is not defined
>>> x=pd.read_csv('f:/DATA SCIENCE NOTES/nba.csv',header=1)
>>> x
     Avery Bradley  Boston Celtics   0  ...  180              Texas     7730337
0      Jae Crowder  Boston Celtics  99  ...  235          Marquette   6796117.0
1     John Holland  Boston Celtics  30  ...  205  Boston University         NaN
2      R.J. Hunter  Boston Celtics  28  ...  185      Georgia State   1148640.0
3    Jonas Jerebko  Boston Celtics   8  ...  231                NaN   5000000.0
4     Amir Johnson  Boston Celtics  90  ...  240                NaN  12000000.0
..             ...             ...  ..  ...  ...                ...         ...
451     Trey Lyles       Utah Jazz  41  ...  234           Kentucky   2239800.0
452   Shelvin Mack       Utah Jazz   8  ...  203             Butler   2433333.0
453      Raul Neto       Utah Jazz  25  ...  179                NaN    900000.0
454   Tibor Pleiss       Utah Jazz  21  ...  256                NaN   2900000.0
455    Jeff Withey       Utah Jazz  24  ...  231             Kansas    947276.0

[456 rows x 9 columns]
>>> x=pd.read_csv('f:/DATA SCIENCE NOTES/nba.csv')
>>> x
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
>>> x['Name','College','Salary']
Traceback (most recent call last):
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 3361, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas\_libs\index.pyx", line 76, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 5198, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 5206, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: ('Name', 'College', 'Salary')

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    x['Name','College','Salary']
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 3455, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\indexes\base.py", line 3363, in get_loc
    raise KeyError(key) from err
KeyError: ('Name', 'College', 'Salary')
>>> x('Name','College','Salary')
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    x('Name','College','Salary')
TypeError: 'DataFrame' object is not callable
>>> 