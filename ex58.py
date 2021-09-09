Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd

>>> import numpy as np
>>> url=pd.read_csv("f://DATA SCIENCE NOTES/nba.csv")
>>> url
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
>>> import pandas as pd
>>> import numpy as np
>>> url=pd.read_csv("f://DATA SCIENCE NOTES/nba.csv")
>>> url
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
>>> data['Time']=pd.to_datetime(data.Time)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    data['Time']=pd.to_datetime(data.Time)
NameError: name 'data' is not defined
>>> url['Time']=pd.to_datetime(url.Time)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    url['Time']=pd.to_datetime(url.Time)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\generic.py", line 5478, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'Time'
>>> df = pd.read_csv(url)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    df = pd.read_csv(url)
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
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\io\common.py", line 584, in get_handle
    if _is_binary_mode(path_or_buf, mode) and "b" not in mode:
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\io\common.py", line 953, in _is_binary_mode
    return isinstance(handle, binary_classes) or "b" in getattr(handle, "mode", mode)
TypeError: argument of type 'method' is not iterable
>>> 
===== RESTART: C:/Users/Asus/OneDrive/programs/ex57.py ====
>>> 
===== RESTART: C:/Users/Asus/OneDrive/programs/ex57.py ====
                           Name                    Team  Number Position  Age  Height  Weight                College      Salary
0  0               Avery Bradley          Boston ...                                                                            
1  1                 Jae Crowder          Boston ...                                                                            
2  2                John Holland          Boston ...                                                                            
3  3                 R.J. Hunter          Boston ...                                                                            
4  4               Jonas Jerebko          Boston ...                                                                            
>>> 
===== RESTART: C:/Users/Asus/OneDrive/programs/ex57.py ====
                           Name                    Team  Number Position  Age  Height  Weight                College      Salary
0  0               Avery Bradley          Boston ...                                                                            
1  1                 Jae Crowder          Boston ...                                                                            
2  2                John Holland          Boston ...                                                                            
3  3                 R.J. Hunter          Boston ...                                                                            
4  4               Jonas Jerebko          Boston ...                                                                            
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex57.py", line 8, in <module>
    df['Time'] = pd.to_datetime(df.Time)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\generic.py", line 5478, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'Time'
>>> 
===== RESTART: C:/Users/Asus/OneDrive/programs/ex57.py ====
                           Name                    Team  Number Position  Age  Height  Weight                College      Salary
0  0               Avery Bradley          Boston ...                                                                            
1  1                 Jae Crowder          Boston ...                                                                            
2  2                John Holland          Boston ...                                                                            
3  3                 R.J. Hunter          Boston ...                                                                            
4  4               Jonas Jerebko          Boston ...                                                                            
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex57.py", line 8, in <module>
    df['Time'] = pd.to_datetime(df.Time)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\generic.py", line 5478, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'Time'
>>> dmy = pd.date_range('2017-06-04', periods=5, freq='S')
>>> dmy
DatetimeIndex(['2017-06-04 00:00:00', '2017-06-04 00:00:01',
               '2017-06-04 00:00:02', '2017-06-04 00:00:03',
               '2017-06-04 00:00:04'],
              dtype='datetime64[ns]', freq='S')
>>> dmy = pd.date_range('2017-06-04', periods=456, freq='S')
>>> dmy
DatetimeIndex(['2017-06-04 00:00:00', '2017-06-04 00:00:01',
               '2017-06-04 00:00:02', '2017-06-04 00:00:03',
               '2017-06-04 00:00:04', '2017-06-04 00:00:05',
               '2017-06-04 00:00:06', '2017-06-04 00:00:07',
               '2017-06-04 00:00:08', '2017-06-04 00:00:09',
               ...
               '2017-06-04 00:07:26', '2017-06-04 00:07:27',
               '2017-06-04 00:07:28', '2017-06-04 00:07:29',
               '2017-06-04 00:07:30', '2017-06-04 00:07:31',
               '2017-06-04 00:07:32', '2017-06-04 00:07:33',
               '2017-06-04 00:07:34', '2017-06-04 00:07:35'],
              dtype='datetime64[ns]', length=456, freq='S')
>>> d=url+dmy
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    d=url+dmy
TypeError: can only concatenate str (not "DatetimeIndex") to str
>>> d=pd.read_csv(url+dmy)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    d=pd.read_csv(url+dmy)
TypeError: can only concatenate str (not "DatetimeIndex") to str
>>> d=pd.read_csv('url+dmy')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    d=pd.read_csv('url+dmy')
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
FileNotFoundError: [Errno 2] No such file or directory: 'url+dmy'
>>> d=pd.DataFrame([[url],[dmy]])
>>> d
                                                   0
0                     f://DATA SCIENCE NOTES/nba.csv
1  DatetimeIndex(['2017-06-04 00:00:00', '2017-06...
>>> print(d)
                                                   0
0                     f://DATA SCIENCE NOTES/nba.csv
1  DatetimeIndex(['2017-06-04 00:00:00', '2017-06...
>>> d.to_string()
"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   0\n0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     f://DATA SCIENCE NOTES/nba.csv\n1  DatetimeIndex(['2017-06-04 00:00:00', '2017-06-04 00:00:01',\n               '2017-06-04 00:00:02', '2017-06-04 00:00:03',\n               '2017-06-04 00:00:04', '2017-06-04 00:00:05',\n               '2017-06-04 00:00:06', '2017-06-04 00:00:07',\n               '2017-06-04 00:00:08', '2017-06-04 00:00:09',\n               ...\n               '2017-06-04 00:07:26', '2017-06-04 00:07:27',\n               '2017-06-04 00:07:28', '2017-06-04 00:07:29',\n               '2017-06-04 00:07:30', '2017-06-04 00:07:31',\n               '2017-06-04 00:07:32', '2017-06-04 00:07:33',\n               '2017-06-04 00:07:34', '2017-06-04 00:07:35'],\n              dtype='datetime64[ns]', length=456, freq='S')"
>>> print(d.to_string())
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   0
0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     f://DATA SCIENCE NOTES/nba.csv
1  DatetimeIndex(['2017-06-04 00:00:00', '2017-06-04 00:00:01',
               '2017-06-04 00:00:02', '2017-06-04 00:00:03',
               '2017-06-04 00:00:04', '2017-06-04 00:00:05',
               '2017-06-04 00:00:06', '2017-06-04 00:00:07',
               '2017-06-04 00:00:08', '2017-06-04 00:00:09',
               ...
               '2017-06-04 00:07:26', '2017-06-04 00:07:27',
               '2017-06-04 00:07:28', '2017-06-04 00:07:29',
               '2017-06-04 00:07:30', '2017-06-04 00:07:31',
               '2017-06-04 00:07:32', '2017-06-04 00:07:33',
               '2017-06-04 00:07:34', '2017-06-04 00:07:35'],
              dtype='datetime64[ns]', length=456, freq='S')
>>>
