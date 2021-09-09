Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> data=pd.DataFrame({'Name':['Yashika','Ajay','Sivam','rupa'],'Age':[20,23,34,23],'City':['Mecheri','Mecheri','Salem','Salem']})
>>> data
      Name  Age     City
0  Yashika   20  Mecheri
1     Ajay   23  Mecheri
2    Sivam   34    Salem
3     rupa   23    Salem
>>> s = pd.Series(['A', 'B', 'C'])
>>> for i,j in s.items():
	print(i)
	ptint(j)

	
0
Traceback (most recent call last):
  File "<pyshell#7>", line 3, in <module>
    ptint(j)
NameError: name 'ptint' is not defined
>>> for i,j in s.items():
	print(i)
	print(j)

	
0
A
1
B
2
C
>>> for i,j in s.items():
	print(i)

	
0
1
2
>>> for i,j in s.items():
	print(j)

	
A
B
C
>>> for i,j in 
	print(j)s = pd.Series(['A', 'B', 'C'],['D','E','F'])
	
SyntaxError: invalid syntax
>>> s = pd.Series(['A', 'B', 'C'],['D','E','F']):
	
SyntaxError: invalid syntax
>>> s = pd.Series(['A', 'B', 'C'],['D','E','F'])
>>> s
D    A
E    B
F    C
dtype: object
>>> for i,j in s.item():
	print(i)
	print(j)

	
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    for i,j in s.item():
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\base.py", line 331, in item
    raise ValueError("can only convert an array of size 1 to a Python scalar")
ValueError: can only convert an array of size 1 to a Python scalar
>>> for i,j in s.item():
	print(i)

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    for i,j in s.item():
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\base.py", line 331, in item
    raise ValueError("can only convert an array of size 1 to a Python scalar")
ValueError: can only convert an array of size 1 to a Python scalar
>>> for i in s.item():
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    for i in s.item():
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\base.py", line 331, in item
    raise ValueError("can only convert an array of size 1 to a Python scalar")
ValueError: can only convert an array of size 1 to a Python scalar
>>> s = pd.Series(['A', 'B', 'C'],['D','E','F'])
>>> print(s)
D    A
E    B
F    C
dtype: object
>>> 
>>> s.item()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    s.item()
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\base.py", line 331, in item
    raise ValueError("can only convert an array of size 1 to a Python scalar")
ValueError: can only convert an array of size 1 to a Python scalar
>>> s.items()
<zip object at 0x000001898AC5E180>
>>> for i in s.items():
	print(i)
	print(j)

	
('D', 'A')
C
('E', 'B')
C
('F', 'C')
C
>>> for i in s.items():
	print(j)

	
C
C
C
>>> import pandas as pd
>>> s = pd.Series(['A', 'B', 'C'],['D','E','F'])
>>> s
D    A
E    B
F    C
dtype: object
>>> for i in s.items():
	print(i)

	
('D', 'A')
('E', 'B')
('F', 'C')
>>> for i,j in s.items():
	print(i)
	print(j)

	
D
A
E
B
F
C
>>> for i,j in s.iteritems():
	print(i)
	print(j)

	
D
A
E
B
F
C
>>> for i,j in s.iteritems():
	print(i,j[0])

	
D A
E B
F C
>>> for i,j in s.iteritems():
	print(i,j[1])

	
Traceback (most recent call last):
  File "<pyshell#49>", line 2, in <module>
    print(i,j[1])
IndexError: string index out of range
>>> 