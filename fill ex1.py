Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import numpy as np
>>> data=pd.read_csv("F://DATA SCIENCE NOTES/wther.csv")
>>> data.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 9 entries, 0 to 8
Data columns (total 4 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   day          9 non-null      object 
 1   temperature  5 non-null      float64
 2   windspeed    5 non-null      float64
 3   event        7 non-null      object 
dtypes: float64(2), object(2)
memory usage: 416.0+ bytes
>>> #data=pd.read_csv("F://DATA SCIENCE NOTES/wther.csv",parse_dates=False)
>>> data=pd.read_csv("F://DATA SCIENCE NOTES/wther.csv",parse_dates=False)
>>> data
          day  temperature  windspeed   event
0  01-01-2017         32.0        6.0    Rain
1  01-04-2017          NaN        9.0   Sunny
2  01-05-2017         28.0        NaN    Snow
3  01-06-2017          NaN        7.0     NaN
4  01-07-2017         32.0        NaN    Rain
5  01-08-2017          NaN        NaN   Sunny
6  01-09-2017          NaN        NaN     NaN
7  01-10-2017         34.0        8.0  Cloudy
8  01-11-2017         40.0       12.0   Sunny
>>> data.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 9 entries, 0 to 8
Data columns (total 4 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   day          9 non-null      object 
 1   temperature  5 non-null      float64
 2   windspeed    5 non-null      float64
 3   event        7 non-null      object 
dtypes: float64(2), object(2)
memory usage: 416.0+ bytes
>>> data=pd.read_csv("F://DATA SCIENCE NOTES/wther.csv",parse_dates=True)
>>> data.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 9 entries, 0 to 8
Data columns (total 4 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   day          9 non-null      object 
 1   temperature  5 non-null      float64
 2   windspeed    5 non-null      float64
 3   event        7 non-null      object 
dtypes: float64(2), object(2)
memory usage: 416.0+ bytes
>>> data=pd.read_csv("F://DATA SCIENCE NOTES/wther.csv",parse_dates=day)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    data=pd.read_csv("F://DATA SCIENCE NOTES/wther.csv",parse_dates=day)
NameError: name 'day' is not defined
>>> data=pd.read_csv("F://DATA SCIENCE NOTES/wther.csv",parse_dates='day')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    data=pd.read_csv("F://DATA SCIENCE NOTES/wther.csv",parse_dates='day')
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
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\io\parsers\c_parser_wrapper.py", line 37, in __init__
    ParserBase.__init__(self, kwds)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\io\parsers\base_parser.py", line 137, in __init__
    self.parse_dates = _validate_parse_dates_arg(kwds.pop("parse_dates", False))
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\io\parsers\base_parser.py", line 1225, in _validate_parse_dates_arg
    raise TypeError(msg)
TypeError: Only booleans, lists, and dictionaries are accepted for the 'parse_dates' parameter
>>> data=pd.read_csv("F://DATA SCIENCE NOTES/wther.csv",[parse_dates='day'])
SyntaxError: invalid syntax
>>> #data=pd.read_csv("F://DATA SCIENCE NOTES/wther.csv",[parse_dates='day'])
>>> data=pd.read_csv("F://DATA SCIENCE NOTES/wther.csv",index_col=0, parse_dates=True)
>>> data.info()
<class 'pandas.core.frame.DataFrame'>
DatetimeIndex: 9 entries, 2017-01-01 to 2017-01-11
Data columns (total 3 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   temperature  5 non-null      float64
 1   windspeed    5 non-null      float64
 2   event        7 non-null      object 
dtypes: float64(2), object(1)
memory usage: 288.0+ bytes
>>> data
            temperature  windspeed   event
day                                       
2017-01-01         32.0        6.0    Rain
2017-01-04          NaN        9.0   Sunny
2017-01-05         28.0        NaN    Snow
2017-01-06          NaN        7.0     NaN
2017-01-07         32.0        NaN    Rain
2017-01-08          NaN        NaN   Sunny
2017-01-09          NaN        NaN     NaN
2017-01-10         34.0        8.0  Cloudy
2017-01-11         40.0       12.0   Sunny
>>> data=pd.read_csv("F://DATA SCIENCE NOTES/wther.csv",parse_dates=True)
>>> data
          day  temperature  windspeed   event
0  01-01-2017         32.0        6.0    Rain
1  01-04-2017          NaN        9.0   Sunny
2  01-05-2017         28.0        NaN    Snow
3  01-06-2017          NaN        7.0     NaN
4  01-07-2017         32.0        NaN    Rain
5  01-08-2017          NaN        NaN   Sunny
6  01-09-2017          NaN        NaN     NaN
7  01-10-2017         34.0        8.0  Cloudy
8  01-11-2017         40.0       12.0   Sunny
>>> data.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 9 entries, 0 to 8
Data columns (total 4 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   day          9 non-null      object 
 1   temperature  5 non-null      float64
 2   windspeed    5 non-null      float64
 3   event        7 non-null      object 
dtypes: float64(2), object(2)
memory usage: 416.0+ bytes
>>> data=pd.read_csv("F://DATA SCIENCE NOTES/wther.csv",parse_dates=['day'])
>>> data
         day  temperature  windspeed   event
0 2017-01-01         32.0        6.0    Rain
1 2017-01-04          NaN        9.0   Sunny
2 2017-01-05         28.0        NaN    Snow
3 2017-01-06          NaN        7.0     NaN
4 2017-01-07         32.0        NaN    Rain
5 2017-01-08          NaN        NaN   Sunny
6 2017-01-09          NaN        NaN     NaN
7 2017-01-10         34.0        8.0  Cloudy
8 2017-01-11         40.0       12.0   Sunny
>>> data.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 9 entries, 0 to 8
Data columns (total 4 columns):
 #   Column       Non-Null Count  Dtype         
---  ------       --------------  -----         
 0   day          9 non-null      datetime64[ns]
 1   temperature  5 non-null      float64       
 2   windspeed    5 non-null      float64       
 3   event        7 non-null      object        
dtypes: datetime64[ns](1), float64(2), object(1)
memory usage: 416.0+ bytes
>>> 