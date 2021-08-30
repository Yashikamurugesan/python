Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> data=pd.DataFrame({'Name':['Yashika','Ajay','Sivam','rupa'],'Age':[20,23,34,23],'City':['Mecheri','Mecheri','Salem','Salem']})
>>> data
      Name  Age     City
0  Yashika   20  Mecheri
1     Ajay   23  Mecheri
2    Sivam   34    Salem
3     rupa   23    Salem
>>> data.items()
<generator object DataFrame.items at 0x00000259279DB200>
>>> for i in data.items():
	print(i)

	
('Name', 0    Yashika
1       Ajay
2      Sivam
3       rupa
Name: Name, dtype: object)
('Age', 0    20
1    23
2    34
3    23
Name: Age, dtype: int64)
('City', 0    Mecheri
1    Mecheri
2      Salem
3      Salem
Name: City, dtype: object)
>>> for i in data.iteritems():
	print(i)

	
('Name', 0    Yashika
1       Ajay
2      Sivam
3       rupa
Name: Name, dtype: object)
('Age', 0    20
1    23
2    34
3    23
Name: Age, dtype: int64)
('City', 0    Mecheri
1    Mecheri
2      Salem
3      Salem
Name: City, dtype: object)
>>> for i in data.iterrows():
	print(i)

	
(0, Name    Yashika
Age          20
City    Mecheri
Name: 0, dtype: object)
(1, Name       Ajay
Age          23
City    Mecheri
Name: 1, dtype: object)
(2, Name    Sivam
Age        34
City    Salem
Name: 2, dtype: object)
(3, Name     rupa
Age        23
City    Salem
Name: 3, dtype: object)
>>> for i in data.itertuples():
	print(i)

	
Pandas(Index=0, Name='Yashika', Age=20, City='Mecheri')
Pandas(Index=1, Name='Ajay', Age=23, City='Mecheri')
Pandas(Index=2, Name='Sivam', Age=34, City='Salem')
Pandas(Index=3, Name='rupa', Age=23, City='Salem')
>>> for i in data.itertuples(index=False):
	print(i)

	
Pandas(Name='Yashika', Age=20, City='Mecheri')
Pandas(Name='Ajay', Age=23, City='Mecheri')
Pandas(Name='Sivam', Age=34, City='Salem')
Pandas(Name='rupa', Age=23, City='Salem')
>>> for i in data.iterrows(index=False):
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    for i in data.iterrows(index=False):
TypeError: iterrows() got an unexpected keyword argument 'index'
>>> for i,j in data.items():
	print(i)

	
Name
Age
City
>>> for i,j in data.items():
	print(j)

	
0    Yashika
1       Ajay
2      Sivam
3       rupa
Name: Name, dtype: object
0    20
1    23
2    34
3    23
Name: Age, dtype: int64
0    Mecheri
1    Mecheri
2      Salem
3      Salem
Name: City, dtype: object
>>> for i,j in data.items():
	print(i)
	print(j)

	
Name
0    Yashika
1       Ajay
2      Sivam
3       rupa
Name: Name, dtype: object
Age
0    20
1    23
2    34
3    23
Name: Age, dtype: int64
City
0    Mecheri
1    Mecheri
2      Salem
3      Salem
Name: City, dtype: object
>>> for i,j in data.items():
	print(j)
	print(i)

	
0    Yashika
1       Ajay
2      Sivam
3       rupa
Name: Name, dtype: object
Name
0    20
1    23
2    34
3    23
Name: Age, dtype: int64
Age
0    Mecheri
1    Mecheri
2      Salem
3      Salem
Name: City, dtype: object
City
>>> for i,j in data.iteritems():
	print(j)
	print(i)

	
0    Yashika
1       Ajay
2      Sivam
3       rupa
Name: Name, dtype: object
Name
0    20
1    23
2    34
3    23
Name: Age, dtype: int64
Age
0    Mecheri
1    Mecheri
2      Salem
3      Salem
Name: City, dtype: object
City
>>> for i,j in data.iteritems():
	print(i)

	
Name
Age
City
>>> for i,j in data.iterrows():
	print(i)

	
0
1
2
3
>>> for i,j in data.iterrows():
	print(j)

	
Name    Yashika
Age          20
City    Mecheri
Name: 0, dtype: object
Name       Ajay
Age          23
City    Mecheri
Name: 1, dtype: object
Name    Sivam
Age        34
City    Salem
Name: 2, dtype: object
Name     rupa
Age        23
City    Salem
Name: 3, dtype: object
>>> for i,j in data.iterrows():
	print(i,j)

	
0 Name    Yashika
Age          20
City    Mecheri
Name: 0, dtype: object
1 Name       Ajay
Age          23
City    Mecheri
Name: 1, dtype: object
2 Name    Sivam
Age        34
City    Salem
Name: 2, dtype: object
3 Name     rupa
Age        23
City    Salem
Name: 3, dtype: object
>>> for i in data.iterrows():
	print (i)

	
(0, Name    Yashika
Age          20
City    Mecheri
Name: 0, dtype: object)
(1, Name       Ajay
Age          23
City    Mecheri
Name: 1, dtype: object)
(2, Name    Sivam
Age        34
City    Salem
Name: 2, dtype: object)
(3, Name     rupa
Age        23
City    Salem
Name: 3, dtype: object)
>>> for i in data.itertuples():
	print (i)

	
Pandas(Index=0, Name='Yashika', Age=20, City='Mecheri')
Pandas(Index=1, Name='Ajay', Age=23, City='Mecheri')
Pandas(Index=2, Name='Sivam', Age=34, City='Salem')
Pandas(Index=3, Name='rupa', Age=23, City='Salem')
>>> for i,j in data.itertuples():
	print (i)

	
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    for i,j in data.itertuples():
ValueError: too many values to unpack (expected 2)
>>> for i,j in data.itertuples():
	print (i,j)

	
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    for i,j in data.itertuples():
ValueError: too many values to unpack (expected 2)
>>> for i,j in data.itertuples():
	print (i)
	print(j)

	
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    for i,j in data.itertuples():
ValueError: too many values to unpack (expected 2)
>>> data
      Name  Age     City
0  Yashika   20  Mecheri
1     Ajay   23  Mecheri
2    Sivam   34    Salem
3     rupa   23    Salem
>>> for i in data.iterrows():
	print (i)

	
(0, Name    Yashika
Age          20
City    Mecheri
Name: 0, dtype: object)
(1, Name       Ajay
Age          23
City    Mecheri
Name: 1, dtype: object)
(2, Name    Sivam
Age        34
City    Salem
Name: 2, dtype: object)
(3, Name     rupa
Age        23
City    Salem
Name: 3, dtype: object)
>>> rows=next(data.iterrows())
>>> print(rows)
(0, Name    Yashika
Age          20
City    Mecheri
Name: 0, dtype: object)
>>> rows=next(data.iterrows())[1]
>>> print(rows)
Name    Yashika
Age          20
City    Mecheri
Name: 0, dtype: object
>>> rows=next(data.iterrows())[2]
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    rows=next(data.iterrows())[2]
IndexError: tuple index out of range
>>> rows=next(data.iterrows())[0]
>>> print(rows)
0
>>> print(rows=next(data.iterrows())[1])
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    print(rows=next(data.iterrows())[1])
TypeError: 'rows' is an invalid keyword argument for print()
>>> print(next(data.iterrows())[1])
Name    Yashika
Age          20
City    Mecheri
Name: 0, dtype: object
>>> print(next(data.iterrows()))
(0, Name    Yashika
Age          20
City    Mecheri
Name: 0, dtype: object)
>>> 
>>> data
      Name  Age     City
0  Yashika   20  Mecheri
1     Ajay   23  Mecheri
2    Sivam   34    Salem
3     rupa   23    Salem
>>> for i,j in data.iterrows():
	print (i,j[0])

	
0 Yashika
1 Ajay
2 Sivam
3 rupa
>>> for i,j in data.iterrows():
	print (i,j[1])

	
0 20
1 23
2 34
3 23
>>> for i,j in data.iteritems():
	print (i,j)

	
Name 0    Yashika
1       Ajay
2      Sivam
3       rupa
Name: Name, dtype: object
Age 0    20
1    23
2    34
3    23
Name: Age, dtype: int64
City 0    Mecheri
1    Mecheri
2      Salem
3      Salem
Name: City, dtype: object
>>> for i,j in data.iteritems():
	print (i,j[0])

	
Name Yashika
Age 20
City Mecheri
>>> for i,j in data.iteritems():
	print (i,j[1])

	
Name Ajay
Age 23
City Mecheri
>>> for i,j in data.iteritems():
	print (i,j[2])

	
Name Sivam
Age 34
City Salem
>>> 

