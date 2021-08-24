Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> data=pd.read_csv("F:\DATA SCIENCE NOTES\nba.csv")
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    data=pd.read_csv("F:\DATA SCIENCE NOTES\nba.csv")
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
OSError: [Errno 22] Invalid argument: 'F:\\DATA SCIENCE NOTES\nba.csv'
>>> data=pd.read_excel("F:\DATA SCIENCE NOTES\KSRCE DeltaX DB - 2022 ( count -28 ).xlsx")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    data=pd.read_excel("F:\DATA SCIENCE NOTES\KSRCE DeltaX DB - 2022 ( count -28 ).xlsx")
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
>>> data=pd.read_excel('F:\DATA SCIENCE NOTES\KSRCE DB.xlsx')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    data=pd.read_excel('F:\DATA SCIENCE NOTES\KSRCE DB.xlsx')
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
>>> data=pd.read_excel('F:\\DATA SCIENCE NOTES\KSRCE DB.xlsx')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    data=pd.read_excel('F:\\DATA SCIENCE NOTES\KSRCE DB.xlsx')
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
>>> data=pd.read_excel('F:\DATA SCIENCE NOTES\\KSRCE DB.xlsx')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    data=pd.read_excel('F:\DATA SCIENCE NOTES\\KSRCE DB.xlsx')
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
>>> data=pd.read_excel('KSRCE DB.xlsx')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    data=pd.read_excel('KSRCE DB.xlsx')
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\util\_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\io\excel\_base.py", line 364, in read_excel
    io = ExcelFile(io, storage_options=storage_options, engine=engine)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\io\excel\_base.py", line 1191, in __init__
    ext = inspect_excel_format(
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\io\excel\_base.py", line 1070, in inspect_excel_format
    with get_handle(
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\io\common.py", line 710, in get_handle
    handle = open(handle, ioargs.mode)
FileNotFoundError: [Errno 2] No such file or directory: 'KSRCE DB.xlsx'
>>> pd.read_csv("f:\DATA SCIENCE NOTES\nba.csv")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    pd.read_csv("f:\DATA SCIENCE NOTES\nba.csv")
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
>>> pd.read_html('f:\DATA SCIENCE NOTES\pandas2 (1).html')

>>> pd.read_excel('f:\DATA SCIENCE NOTES\~$KSRCE DB.xlsx')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    pd.read_excel('f:\DATA SCIENCE NOTES\~$KSRCE DB.xlsx')
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\util\_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\io\excel\_base.py", line 364, in read_excel
    io = ExcelFile(io, storage_options=storage_options, engine=engine)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\io\excel\_base.py", line 1191, in __init__
    ext = inspect_excel_format(
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\io\excel\_base.py", line 1070, in inspect_excel_format
    with get_handle(
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\io\common.py", line 710, in get_handle
    handle = open(handle, ioargs.mode)
PermissionError: [Errno 13] Permission denied: 'f:\\DATA SCIENCE NOTES\\~$KSRCE DB.xlsx'
>>> pd.read_html('f:\DATA SCIENCE NOTES\pandas2 (1).html',header(0))
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    pd.read_html('f:\DATA SCIENCE NOTES\pandas2 (1).html',header(0))
NameError: name 'header' is not defined
>>> x=pd.read_html('f:\DATA SCIENCE NOTES\pandas2 (1).html')
>>> x.header(0)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    x.header(0)
AttributeError: 'list' object has no attribute 'header'
>>> header(x)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    header(x)
NameError: name 'header' is not defined
>>> head(x)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    head(x)
NameError: name 'head' is not defined
>>> pd.header(x)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    pd.header(x)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\__init__.py", line 244, in __getattr__
    raise AttributeError(f"module 'pandas' has no attribute '{name}'")
AttributeError: module 'pandas' has no attribute 'header'
>>> tail(x)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    tail(x)
NameError: name 'tail' is not defined
>>> import pandas as pd

>>> x= {'Name': ['Joe', 'Nat', 'Harry'], 'Age': [20, 21, 19], 
                'Marks': [85.10, 77.80, 91.54]}
>>> 
>>> y== pd.DataFrame(student_dict)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    y== pd.DataFrame(student_dict)
NameError: name 'y' is not defined
>>> y== pd.DataFrame(x)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    y== pd.DataFrame(x)
NameError: name 'y' is not defined
>>> y=pd.DataFrame(x)
>>> print(y.iat[1,2])
77.8
>>> x= {'Name': ['Joe', 'Nat', 'Harry','Jack','Jose','Jill','Rose'],
                'Age': [20, 21, 19,17,18,19,17],
                'Marks': [85.10, 77.80, 91.54,72,87.9,90,72]}

>>> y= pd.DataFrame(x)
>>> topRows =y.head()

>>> topRows
    Name  Age  Marks
0    Joe   20  85.10
1    Nat   21  77.80
2  Harry   19  91.54
3   Jack   17  72.00
4   Jose   18  87.90
>>> 