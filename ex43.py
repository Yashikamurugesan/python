Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> d=pd.read_csv("C:\Users\Asus\Downloads.csv")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> d=pd.read_csv("C:\Users\Asus\Downloads")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> d=pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
>>> data
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    data
NameError: name 'data' is not defined
>>> position=2
>>> label='Name'
>>> output=data.at[position,label]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    output=data.at[position,label]
NameError: name 'data' is not defined
>>> d=pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
>>> position=2
>>> label='Name'
>>> output=data.at[position,label]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    output=data.at[position,label]
NameError: name 'data' is not defined
>>> d=pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
>>> position=2
>>> label='Name'
>>> d
              Name            Team  ...            College     Salary
0    Avery Bradley  Boston Celtics  ...              Texas  7730337.0
1      Jae Crowder  Boston Celtics  ...          Marquette  6796117.0
2     John Holland  Boston Celtics  ...  Boston University        NaN
3      R.J. Hunter  Boston Celtics  ...      Georgia State  1148640.0
4    Jonas Jerebko  Boston Celtics  ...                NaN  5000000.0
..             ...             ...  ...                ...        ...
453   Shelvin Mack       Utah Jazz  ...             Butler  2433333.0
454      Raul Neto       Utah Jazz  ...                NaN   900000.0
455   Tibor Pleiss       Utah Jazz  ...                NaN  2900000.0
456    Jeff Withey       Utah Jazz  ...             Kansas   947276.0
457            NaN             NaN  ...                NaN        NaN

[458 rows x 9 columns]
>>> output=d.at[position,label]
>>> print(output)
John Holland
>>> d=pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
>>> d=pd.read_csv(["https://media.geeksforgeeks.org/wp-content/uploads/nba.csv"])
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    d=pd.read_csv(["https://media.geeksforgeeks.org/wp-content/uploads/nba.csv"])
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
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\io\common.py", line 395, in _get_filepath_or_buffer
    raise ValueError(msg)
ValueError: Invalid file path or buffer object type: <class 'list'>
>>> 