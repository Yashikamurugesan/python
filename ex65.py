Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> df1=pd.DataFrame({"Name":['sathish','sivam','yasi','saara','shree','nithish','praveen'],"Age":[20,35,25,45,21,20,27]})
>>> df1
      Name  Age
0  sathish   20
1    sivam   35
2     yasi   25
3    saara   45
4    shree   21
5  nithish   20
6  praveen   27
>>> df2=pd.DataFrame({"Name":['sathish','sivam','yasi','saara','shree','nithish','praveen'],"Department":['CIVIL','ECE','IT','MECH','AUTOMOBILE','CSE','MBA']})
>>> df2
      Name  Department
0  sathish       CIVIL
1    sivam         ECE
2     yasi          IT
3    saara        MECH
4    shree  AUTOMOBILE
5  nithish         CSE
6  praveen         MBA
>>> df3=pd.merge(df1,df2)
>>> df3
      Name  Age  Department
0  sathish   20       CIVIL
1    sivam   35         ECE
2     yasi   25          IT
3    saara   45        MECH
4    shree   21  AUTOMOBILE
5  nithish   20         CSE
6  praveen   27         MBA
>>> df4=pd.DataFrame({"Name":['sathish','sivam','yasi','saara','shree','nithish','praveen'],"Busno":[101,102,103,104,105,106,107]})
>>> df4
      Name  Busno
0  sathish    101
1    sivam    102
2     yasi    103
3    saara    104
4    shree    105
5  nithish    106
6  praveen    107
>>> df3=pd.merge(df2,df4)
>>> df3
      Name  Department  Busno
0  sathish       CIVIL    101
1    sivam         ECE    102
2     yasi          IT    103
3    saara        MECH    104
4    shree  AUTOMOBILE    105
5  nithish         CSE    106
6  praveen         MBA    107
>>> df4=pd.DataFrame({"Age":[20,35,25,45,21,20,27],"JOY":[2014,2013,2019,2017,2012,2018,2021]})
>>> df4
   Age   JOY
0   20  2014
1   35  2013
2   25  2019
3   45  2017
4   21  2012
5   20  2018
6   27  2021
>>> df4=pd.DataFrame({"Age":[20,35,25,45,21,27],"JOY":[2014,2013,2019,2017,2012,2018,2021]})
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    df4=pd.DataFrame({"Age":[20,35,25,45,21,27],"JOY":[2014,2013,2019,2017,2012,2018,2021]})
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 614, in __init__
    mgr = dict_to_mgr(data, index, columns, dtype=dtype, copy=copy, typ=manager)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\internals\construction.py", line 462, in dict_to_mgr
    return arrays_to_mgr(
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\internals\construction.py", line 117, in arrays_to_mgr
    index = _extract_index(arrays)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\internals\construction.py", line 623, in _extract_index
    raise ValueError("All arrays must be of the same length")
ValueError: All arrays must be of the same length
>>> df4=pd.DataFrame({"Age":[20,35,25,45,21,27],"JOY":[2014,2013,2019,2017,2012,2021]})
>>> df4
   Age   JOY
0   20  2014
1   35  2013
2   25  2019
3   45  2017
4   21  2012
5   27  2021
>>> df5=pd.merge(df3,df4)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    df5=pd.merge(df3,df4)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\reshape\merge.py", line 107, in merge
    op = _MergeOperation(
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\reshape\merge.py", line 682, in __init__
    self._validate_specification()
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\reshape\merge.py", line 1342, in _validate_specification
    raise MergeError(
pandas.errors.MergeError: No common columns to perform merge on. Merge options: left_on=None, right_on=None, left_index=False, right_index=False
>>> df3
      Name  Department  Busno
0  sathish       CIVIL    101
1    sivam         ECE    102
2     yasi          IT    103
3    saara        MECH    104
4    shree  AUTOMOBILE    105
5  nithish         CSE    106
6  praveen         MBA    107
>>> df2
      Name  Department
0  sathish       CIVIL
1    sivam         ECE
2     yasi          IT
3    saara        MECH
4    shree  AUTOMOBILE
5  nithish         CSE
6  praveen         MBA
>>> df1
      Name  Age
0  sathish   20
1    sivam   35
2     yasi   25
3    saara   45
4    shree   21
5  nithish   20
6  praveen   27
>>> 
>>> df5=pd.merge(df1,df4)
>>> df5
      Name  Age   JOY
0  sathish   20  2014
1  nithish   20  2014
2    sivam   35  2013
3     yasi   25  2019
4    saara   45  2017
5    shree   21  2012
6  praveen   27  2021
>>> df1=pd.read_csv("f://DATA SCIENCE NOTES/one.csv")
>>> df1
             User Name First Name Last Name Department
0    chris@contoso.com      meenu         V         IT
1      ben@contoso.com       yasi         G        CSE
2    david@contoso.com      sivam         I      CIVIL
3  cynthia@contoso.com    nithish         Y         IT
4  melissa@contoso.com       riya         K        ECE
>>> df2=pd.read_csv("f://DATA SCIENCE NOTES/to one.csvone.csv")
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    df2=pd.read_csv("f://DATA SCIENCE NOTES/to one.csvone.csv")
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
FileNotFoundError: [Errno 2] No such file or directory: 'f:/DATA SCIENCE NOTES/to one.csvone.csv'
>>> df2=pd.read_csv("f://DATA SCIENCE NOTES/to one.csv")
>>> df2
             User Name First Name Last Name Department   JOY
0    chris@contoso.com      meenu         V         IT  2017
1      ben@contoso.com       yasi         G        CSE  2016
2    david@contoso.com      sivam         I      CIVIL  2018
3  cynthia@contoso.com    nithish         Y         IT  2017
4  melissa@contoso.com       riya         K        ECE  2016
>>> df3=pd.merge(df1,df2)
>>> df3
             User Name First Name Last Name Department   JOY
0    chris@contoso.com      meenu         V         IT  2017
1      ben@contoso.com       yasi         G        CSE  2016
2    david@contoso.com      sivam         I      CIVIL  2018
3  cynthia@contoso.com    nithish         Y         IT  2017
4  melissa@contoso.com       riya         K        ECE  2016
>>> df4=pd.read_csv("f://DATA SCIENCE NOTES/many.csv")
>>> df4
             User Name First Name Last Name Department   JOY  Busno
0    chris@contoso.com      meenu         V         IT  2017    101
1      ben@contoso.com       yasi         G        CSE  2016    103
2    david@contoso.com      sivam         I      CIVIL  2018    105
3  cynthia@contoso.com    nithish         Y         IT  2017    106
4  melissa@contoso.com       riya         K        ECE  2016    101
>>> df5=pd.merge(df3,df4)
>>> df5
             User Name First Name Last Name Department   JOY  Busno
0    chris@contoso.com      meenu         V         IT  2017    101
1      ben@contoso.com       yasi         G        CSE  2016    103
2    david@contoso.com      sivam         I      CIVIL  2018    105
3  cynthia@contoso.com    nithish         Y         IT  2017    106
4  melissa@contoso.com       riya         K        ECE  2016    101
>>> df6=pd.read_csv("f://DATA SCIENCE NOTES/to many.csv")
>>> df6
             User Name First Name Last Name  ...   JOY  Busno              Skill
0    chris@contoso.com      meenu         V  ...  2017    101                 CV
1      ben@contoso.com       yasi         G  ...  2016    103        programming
2    david@contoso.com      sivam         I  ...  2018    105           Embedded
3  cynthia@contoso.com    nithish         Y  ...  2017    106  ThermoEngineering
4  melissa@contoso.com       riya         K  ...  2016    101               Data

[5 rows x 7 columns]
>>> df6=pd.read_csv("f://DATA SCIENCE NOTES/tomany.csv")
>>> df6
   Unnamed: 0  Unnamed: 1  Unnamed: 2  ...   JOY  Unnamed: 5              Skill
0         NaN         NaN         NaN  ...  2017         NaN                 CV
1         NaN         NaN         NaN  ...  2016         NaN        programming
2         NaN         NaN         NaN  ...  2018         NaN           Embedded
3         NaN         NaN         NaN  ...  2017         NaN  ThermoEngineering
4         NaN         NaN         NaN  ...  2016         NaN               Data

[5 rows x 7 columns]
>>> df6=pd.read_csv("f://DATA SCIENCE NOTES/to  many.csv")
>>> df6
    JOY              Skill
0  2017                 CV
1  2016        programming
2  2018           Embedded
3  2017  ThermoEngineering
4  2016               Data
>>> df7=pd.merge(df1,df6)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    df7=pd.merge(df1,df6)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\reshape\merge.py", line 107, in merge
    op = _MergeOperation(
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\reshape\merge.py", line 682, in __init__
    self._validate_specification()
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\reshape\merge.py", line 1342, in _validate_specification
    raise MergeError(
pandas.errors.MergeError: No common columns to perform merge on. Merge options: left_on=None, right_on=None, left_index=False, right_index=False
>>> df5=pd.merge(df3,df4)
>>> df7=pd.merge(df5,df6)
>>> df7
             User Name First Name Last Name  ...   JOY  Busno              Skill
0    chris@contoso.com      meenu         V  ...  2017    101                 CV
1    chris@contoso.com      meenu         V  ...  2017    101  ThermoEngineering
2  cynthia@contoso.com    nithish         Y  ...  2017    106                 CV
3  cynthia@contoso.com    nithish         Y  ...  2017    106  ThermoEngineering
4      ben@contoso.com       yasi         G  ...  2016    103        programming
5      ben@contoso.com       yasi         G  ...  2016    103               Data
6  melissa@contoso.com       riya         K  ...  2016    101        programming
7  melissa@contoso.com       riya         K  ...  2016    101               Data
8    david@contoso.com      sivam         I  ...  2018    105           Embedded

[9 rows x 7 columns]
>>> 