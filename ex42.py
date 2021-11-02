Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import numpy as np
>>> import calendar
>>> cal=calendar.calendar(0)
>>> import pandas as pd
>>> import numpy as np
>>> import calendar
>>> cal=calendar.Calendar(0)
>>> data=pd.DataFrame([{i for i in cal.itermonthdays3(2021,8)]})
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> data=pd.DataFrame([{i for i in cal.itermonthdays3(2021,8)}])
>>> data
              0              1   ...            40             41
0  (2021, 8, 10)  (2021, 8, 16)  ...  (2021, 8, 7)  (2021, 8, 13)

[1 rows x 42 columns]
>>> print(data)
              0              1   ...            40             41
0  (2021, 8, 10)  (2021, 8, 16)  ...  (2021, 8, 7)  (2021, 8, 13)

[1 rows x 42 columns]
>>> data=pd.DataFrame({"Date":[i for i in cal.itermonthdays3(2021,8)]})
>>> data
             Date
0   (2021, 7, 26)
1   (2021, 7, 27)
2   (2021, 7, 28)
3   (2021, 7, 29)
4   (2021, 7, 30)
5   (2021, 7, 31)
6    (2021, 8, 1)
7    (2021, 8, 2)
8    (2021, 8, 3)
9    (2021, 8, 4)
10   (2021, 8, 5)
11   (2021, 8, 6)
12   (2021, 8, 7)
13   (2021, 8, 8)
14   (2021, 8, 9)
15  (2021, 8, 10)
16  (2021, 8, 11)
17  (2021, 8, 12)
18  (2021, 8, 13)
19  (2021, 8, 14)
20  (2021, 8, 15)
21  (2021, 8, 16)
22  (2021, 8, 17)
23  (2021, 8, 18)
24  (2021, 8, 19)
25  (2021, 8, 20)
26  (2021, 8, 21)
27  (2021, 8, 22)
28  (2021, 8, 23)
29  (2021, 8, 24)
30  (2021, 8, 25)
31  (2021, 8, 26)
32  (2021, 8, 27)
33  (2021, 8, 28)
34  (2021, 8, 29)
35  (2021, 8, 30)
36  (2021, 8, 31)
37   (2021, 9, 1)
38   (2021, 9, 2)
39   (2021, 9, 3)
40   (2021, 9, 4)
41   (2021, 9, 5)
>>> data=pd.DataFrame({[i for i in cal.itermonthdays3(2021,8)]})
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    data=pd.DataFrame({[i for i in cal.itermonthdays3(2021,8)]})
TypeError: unhashable type: 'list'
>>> data=pd.DataFrame({"Date":[i for i in cal.itermonthdays3(2021,8)]})
>>> data
             Date
0   (2021, 7, 26)
1   (2021, 7, 27)
2   (2021, 7, 28)
3   (2021, 7, 29)
4   (2021, 7, 30)
5   (2021, 7, 31)
6    (2021, 8, 1)
7    (2021, 8, 2)
8    (2021, 8, 3)
9    (2021, 8, 4)
10   (2021, 8, 5)
11   (2021, 8, 6)
12   (2021, 8, 7)
13   (2021, 8, 8)
14   (2021, 8, 9)
15  (2021, 8, 10)
16  (2021, 8, 11)
17  (2021, 8, 12)
18  (2021, 8, 13)
19  (2021, 8, 14)
20  (2021, 8, 15)
21  (2021, 8, 16)
22  (2021, 8, 17)
23  (2021, 8, 18)
24  (2021, 8, 19)
25  (2021, 8, 20)
26  (2021, 8, 21)
27  (2021, 8, 22)
28  (2021, 8, 23)
29  (2021, 8, 24)
30  (2021, 8, 25)
31  (2021, 8, 26)
32  (2021, 8, 27)
33  (2021, 8, 28)
34  (2021, 8, 29)
35  (2021, 8, 30)
36  (2021, 8, 31)
37   (2021, 9, 1)
38   (2021, 9, 2)
39   (2021, 9, 3)
40   (2021, 9, 4)
41   (2021, 9, 5)
>>> data=pd.DataFrame([[i for i in cal.itermonthdays3(2021,8)]])
>>> 
>>> data
              0              1   ...            40            41
0  (2021, 7, 26)  (2021, 7, 27)  ...  (2021, 9, 4)  (2021, 9, 5)

[1 rows x 42 columns]
>>> data=pd.DataFrame(["Date":{i for i in cal.itermonthdays3(2021,8)}])
SyntaxError: invalid syntax
>>> data=pd.DataFrame("Date":i for i in cal.itermonthdays3(2021,8))
SyntaxError: invalid syntax
>>> data=pd.DataFrame("Date":[i for i in cal.itermonthdays3(2021,8)])
SyntaxError: invalid syntax
>>> data=pd.DataFrame("Date":{i for i in cal.itermonthdays3(2021,8)})
SyntaxError: invalid syntax
>>> data=pd.DataFrame([i for i in cal.itermonthdays3(2021,8)],[],[])
Traceback (most recent call last):
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\internals\construction.py", line 886, in _finalize_columns_and_data
    columns = _validate_or_indexify_columns(contents, columns)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\internals\construction.py", line 934, in _validate_or_indexify_columns
    raise AssertionError(
AssertionError: 0 columns passed, passed data had 3 columns

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    data=pd.DataFrame([i for i in cal.itermonthdays3(2021,8)],[],[])
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 694, in __init__
    arrays, columns, index = nested_data_to_arrays(
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\internals\construction.py", line 481, in nested_data_to_arrays
    arrays, columns = to_arrays(data, columns, dtype=dtype)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\internals\construction.py", line 787, in to_arrays
    content, columns = _finalize_columns_and_data(arr, columns, dtype)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\internals\construction.py", line 889, in _finalize_columns_and_data
    raise ValueError(err) from err
ValueError: 0 columns passed, passed data had 3 columns
>>> data=pd.DataFrame([i for i in cal.itermonthdays3(2021,8)])
>>> data
       0  1   2
0   2021  7  26
1   2021  7  27
2   2021  7  28
3   2021  7  29
4   2021  7  30
5   2021  7  31
6   2021  8   1
7   2021  8   2
8   2021  8   3
9   2021  8   4
10  2021  8   5
11  2021  8   6
12  2021  8   7
13  2021  8   8
14  2021  8   9
15  2021  8  10
16  2021  8  11
17  2021  8  12
18  2021  8  13
19  2021  8  14
20  2021  8  15
21  2021  8  16
22  2021  8  17
23  2021  8  18
24  2021  8  19
25  2021  8  20
26  2021  8  21
27  2021  8  22
28  2021  8  23
29  2021  8  24
30  2021  8  25
31  2021  8  26
32  2021  8  27
33  2021  8  28
34  2021  8  29
35  2021  8  30
36  2021  8  31
37  2021  9   1
38  2021  9   2
39  2021  9   3
40  2021  9   4
41  2021  9   5
>>> import pandas as pd
>>> import calendar
>>> cal=calendar.Calendar(0)
>>> data=pd.DataFrame([i for i in cal.itermonthdays3(2021,8)])
>>> print(i)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    print(i)
NameError: name 'i' is not defined
>>> import pandas as pd
>>> import calendar
>>> cal=calendar.Calendar(0)
>>> data=pd.DataFrame([i for i in cal.itermonthdays3(2021,8)])
>>> print(data)
       0  1   2
0   2021  7  26
1   2021  7  27
2   2021  7  28
3   2021  7  29
4   2021  7  30
5   2021  7  31
6   2021  8   1
7   2021  8   2
8   2021  8   3
9   2021  8   4
10  2021  8   5
11  2021  8   6
12  2021  8   7
13  2021  8   8
14  2021  8   9
15  2021  8  10
16  2021  8  11
17  2021  8  12
18  2021  8  13
19  2021  8  14
20  2021  8  15
21  2021  8  16
22  2021  8  17
23  2021  8  18
24  2021  8  19
25  2021  8  20
26  2021  8  21
27  2021  8  22
28  2021  8  23
29  2021  8  24
30  2021  8  25
31  2021  8  26
32  2021  8  27
33  2021  8  28
34  2021  8  29
35  2021  8  30
36  2021  8  31
37  2021  9   1
38  2021  9   2
39  2021  9   3
40  2021  9   4
41  2021  9   5
>>> data=pd.DataFrame({"date":[i for i in cal.itermonthdays3(2021,8)]})
>>> print(data)
             date
0   (2021, 7, 26)
1   (2021, 7, 27)
2   (2021, 7, 28)
3   (2021, 7, 29)
4   (2021, 7, 30)
5   (2021, 7, 31)
6    (2021, 8, 1)
7    (2021, 8, 2)
8    (2021, 8, 3)
9    (2021, 8, 4)
10   (2021, 8, 5)
11   (2021, 8, 6)
12   (2021, 8, 7)
13   (2021, 8, 8)
14   (2021, 8, 9)
15  (2021, 8, 10)
16  (2021, 8, 11)
17  (2021, 8, 12)
18  (2021, 8, 13)
19  (2021, 8, 14)
20  (2021, 8, 15)
21  (2021, 8, 16)
22  (2021, 8, 17)
23  (2021, 8, 18)
24  (2021, 8, 19)
25  (2021, 8, 20)
26  (2021, 8, 21)
27  (2021, 8, 22)
28  (2021, 8, 23)
29  (2021, 8, 24)
30  (2021, 8, 25)
31  (2021, 8, 26)
32  (2021, 8, 27)
33  (2021, 8, 28)
34  (2021, 8, 29)
35  (2021, 8, 30)
36  (2021, 8, 31)
37   (2021, 9, 1)
38   (2021, 9, 2)
39   (2021, 9, 3)
40   (2021, 9, 4)
41   (2021, 9, 5)
>>> data=pd.DataFrame(["date":{[i for i in cal.itermonthdays3(2021,8)}])
		  
SyntaxError: invalid syntax
>>> data=pd.DataFrame(["date"{[i for i in cal.itermonthdays3(2021,8)}])
		  
SyntaxError: invalid syntax
>>> data=pd.DataFrame(["date"{[i for i in cal.itermonthdays3(2021,8)}])
		  
SyntaxError: invalid syntax
data=pd.DataFrame(["date"{[i for i in cal.itermonthdays3(2021,8)}])
>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> data=pd.DataFrame({"date":i for i in cal.itermonthdays3(2021,8)})
>>> print(data)
   date
0  2021
1     9
2     5
>>> data=pd.DataFrame({"date":[i for i in cal.itermonthdays3(2021,8)]})
>>> print(data)
             date
0   (2021, 7, 26)
1   (2021, 7, 27)
2   (2021, 7, 28)
3   (2021, 7, 29)
4   (2021, 7, 30)
5   (2021, 7, 31)
6    (2021, 8, 1)
7    (2021, 8, 2)
8    (2021, 8, 3)
9    (2021, 8, 4)
10   (2021, 8, 5)
11   (2021, 8, 6)
12   (2021, 8, 7)
13   (2021, 8, 8)
14   (2021, 8, 9)
15  (2021, 8, 10)
16  (2021, 8, 11)
17  (2021, 8, 12)
18  (2021, 8, 13)
19  (2021, 8, 14)
20  (2021, 8, 15)
21  (2021, 8, 16)
22  (2021, 8, 17)
23  (2021, 8, 18)
24  (2021, 8, 19)
25  (2021, 8, 20)
26  (2021, 8, 21)
27  (2021, 8, 22)
28  (2021, 8, 23)
29  (2021, 8, 24)
30  (2021, 8, 25)
31  (2021, 8, 26)
32  (2021, 8, 27)
33  (2021, 8, 28)
34  (2021, 8, 29)
35  (2021, 8, 30)
36  (2021, 8, 31)
37   (2021, 9, 1)
38   (2021, 9, 2)
39   (2021, 9, 3)
40   (2021, 9, 4)
41   (2021, 9, 5)
>>> data=pd.DataFrame({"date":pd.Series(i for i in cal.itermonthdays3(2021,8))})
>>> print(data)
             date
0   (2021, 7, 26)
1   (2021, 7, 27)
2   (2021, 7, 28)
3   (2021, 7, 29)
4   (2021, 7, 30)
5   (2021, 7, 31)
6    (2021, 8, 1)
7    (2021, 8, 2)
8    (2021, 8, 3)
9    (2021, 8, 4)
10   (2021, 8, 5)
11   (2021, 8, 6)
12   (2021, 8, 7)
13   (2021, 8, 8)
14   (2021, 8, 9)
15  (2021, 8, 10)
16  (2021, 8, 11)
17  (2021, 8, 12)
18  (2021, 8, 13)
19  (2021, 8, 14)
20  (2021, 8, 15)
21  (2021, 8, 16)
22  (2021, 8, 17)
23  (2021, 8, 18)
24  (2021, 8, 19)
25  (2021, 8, 20)
26  (2021, 8, 21)
27  (2021, 8, 22)
28  (2021, 8, 23)
29  (2021, 8, 24)
30  (2021, 8, 25)
31  (2021, 8, 26)
32  (2021, 8, 27)
33  (2021, 8, 28)
34  (2021, 8, 29)
35  (2021, 8, 30)
36  (2021, 8, 31)
37   (2021, 9, 1)
38   (2021, 9, 2)
39   (2021, 9, 3)
40   (2021, 9, 4)
41   (2021, 9, 5)
>>> data=pd.DataFrame(columns=['YEAR','MONTH','DATE'],[i for i in cal.itermonthdays3(2021,8)])
SyntaxError: positional argument follows keyword argument
>>> data=pd.DataFrame([i for i in cal.itermonthdays3(2021,8)])
>>> data
       0  1   2
0   2021  7  26
1   2021  7  27
2   2021  7  28
3   2021  7  29
4   2021  7  30
5   2021  7  31
6   2021  8   1
7   2021  8   2
8   2021  8   3
9   2021  8   4
10  2021  8   5
11  2021  8   6
12  2021  8   7
13  2021  8   8
14  2021  8   9
15  2021  8  10
16  2021  8  11
17  2021  8  12
18  2021  8  13
19  2021  8  14
20  2021  8  15
21  2021  8  16
22  2021  8  17
23  2021  8  18
24  2021  8  19
25  2021  8  20
26  2021  8  21
27  2021  8  22
28  2021  8  23
29  2021  8  24
30  2021  8  25
31  2021  8  26
32  2021  8  27
33  2021  8  28
34  2021  8  29
35  2021  8  30
36  2021  8  31
37  2021  9   1
38  2021  9   2
39  2021  9   3
40  2021  9   4
41  2021  9   5
>>> data=pd.DataFrame([i for i in cal.itermonthdays3(2021,8)],columns=['YEAR','MONTH','DATE'])
>>> data
    YEAR  MONTH  DATE
0   2021      7    26
1   2021      7    27
2   2021      7    28
3   2021      7    29
4   2021      7    30
5   2021      7    31
6   2021      8     1
7   2021      8     2
8   2021      8     3
9   2021      8     4
10  2021      8     5
11  2021      8     6
12  2021      8     7
13  2021      8     8
14  2021      8     9
15  2021      8    10
16  2021      8    11
17  2021      8    12
18  2021      8    13
19  2021      8    14
20  2021      8    15
21  2021      8    16
22  2021      8    17
23  2021      8    18
24  2021      8    19
25  2021      8    20
26  2021      8    21
27  2021      8    22
28  2021      8    23
29  2021      8    24
30  2021      8    25
31  2021      8    26
32  2021      8    27
33  2021      8    28
34  2021      8    29
35  2021      8    30
36  2021      8    31
37  2021      9     1
38  2021      9     2
39  2021      9     3
40  2021      9     4
41  2021      9     5
>>> data=pd.DataFrame([i for i in cal.itermonthdays3(2021,8)],columns=['YEAR','MONTH','DATE','EMPTY'])
Traceback (most recent call last):
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\internals\construction.py", line 886, in _finalize_columns_and_data
    columns = _validate_or_indexify_columns(contents, columns)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\internals\construction.py", line 934, in _validate_or_indexify_columns
    raise AssertionError(
AssertionError: 4 columns passed, passed data had 3 columns

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    data=pd.DataFrame([i for i in cal.itermonthdays3(2021,8)],columns=['YEAR','MONTH','DATE','EMPTY'])
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 694, in __init__
    arrays, columns, index = nested_data_to_arrays(
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\internals\construction.py", line 481, in nested_data_to_arrays
    arrays, columns = to_arrays(data, columns, dtype=dtype)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\internals\construction.py", line 787, in to_arrays
    content, columns = _finalize_columns_and_data(arr, columns, dtype)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\internals\construction.py", line 889, in _finalize_columns_and_data
    raise ValueError(err) from err
ValueError: 4 columns passed, passed data had 3 columns
>>> data=pd.DataFrame([i for i in cal.itermonthdays3(2021,8)],columns=['YEAR','MONTH'])
Traceback (most recent call last):
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\internals\construction.py", line 886, in _finalize_columns_and_data
    columns = _validate_or_indexify_columns(contents, columns)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\internals\construction.py", line 934, in _validate_or_indexify_columns
    raise AssertionError(
AssertionError: 2 columns passed, passed data had 3 columns

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    data=pd.DataFrame([i for i in cal.itermonthdays3(2021,8)],columns=['YEAR','MONTH'])
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\frame.py", line 694, in __init__
    arrays, columns, index = nested_data_to_arrays(
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\internals\construction.py", line 481, in nested_data_to_arrays
    arrays, columns = to_arrays(data, columns, dtype=dtype)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\internals\construction.py", line 787, in to_arrays
    content, columns = _finalize_columns_and_data(arr, columns, dtype)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\internals\construction.py", line 889, in _finalize_columns_and_data
    raise ValueError(err) from err
ValueError: 2 columns passed, passed data had 3 columns
>>> 