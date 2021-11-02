Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> str="hi i'm yasi"
>>> def getupper(str):
	return str.upper(i)

>>> getupper("hi i'm yasi")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    getupper("hi i'm yasi")
  File "<pyshell#3>", line 2, in getupper
    return str.upper(i)
NameError: name 'i' is not defined
>>> str="hi i'm yasi"
>>> def getupper(str):
	return str.upper()

>>> getupper("hi i'm yasi")
"HI I'M YASI"
>>> str="yeah it's yasi"
>>> def getlower(str)
SyntaxError: invalid syntax
>>> str="yeah it's yasi"
>>> def getlower(str):
	return str.lower()

>>> getlower("yeah it's yasi")
"yeah it's yasi"
>>> def getlower(str):
	return str.center(10,' ')

>>> getlower("yeah it's yashika")
"yeah it's yashika"
>>> def getcenter(str):
	return str.center(10,'*')

>>> getcenter("yeah it's yashika")
"yeah it's yashika"
>>> def getcenter(str):
	return str.center(40,'$')

>>> getcenter("yeah it's yashika")
"$$$$$$$$$$$yeah it's yashika$$$$$$$$$$$$"
>>> def getcenter(str):
	return str.center(40,' ')

>>> getcenter("yeah it's yashika")
"           yeah it's yashika            "
>>> def getcenter(str):
	return str.center(40,' ')

>>> getcenter('yeah its yashika')
'            yeah its yashika            '
>>> get=getcenter
>>> get('hi')
'                   hi                   '
>>> get=getcenter
>>> get.upper()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    get.upper()
AttributeError: 'function' object has no attribute 'upper'
>>> def get(str):
	return str.upper()

>>> get("hi")
'HI'
>>> def getcenter(str):
	return str.center(40,' ')
getcenter('yeah its yashika')
SyntaxError: invalid syntax
>>> def getcenter(str):
	return str.center(40,' ')

>>> getcenter('yeah its yashika')
'            yeah its yashika            '
>>> get=getcenter
>>> get('hi')
'                   hi                   '
>>> get=getcenter
>>> def get(str):
	return str.upper()

>>> get("hi")
'HI'
>>> x=['yasi','nave','rema','abi','dhanu']
>>> for i in x:
	print(i)

	
yasi
nave
rema
abi
dhanu
>>> for i in x:
	return (i)
SyntaxError: 'return' outside function
>>> for i in x:return (i)
SyntaxError: 'return' outside function
>>> for i in x:
	return (i)
SyntaxError: 'return' outside function
>>> for i in x:
return (i)
SyntaxError: expected an indented block
>>> for i in x:return (i)
SyntaxError: 'return' outside function
>>> for i in x:
	return i
SyntaxError: 'return' outside function
>>> for i in x:
	print i
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(i)?
>>> 
>>> for i in x:
	print (i)

	
yasi
nave
rema
abi
dhanu
>>> for i in x:
	if x[1]=='a'
	
SyntaxError: invalid syntax
>>> for i in x:
	if x[1]=='a':
		print(i)

		
>>> for i in x:
	if i[1]=='a':
		print(i)

		
yasi
nave
>>> for i in x:
	if i[3]=='a':
		print(i)

		
rema
Traceback (most recent call last):
  File "<pyshell#73>", line 2, in <module>
    if i[3]=='a':
IndexError: string index out of range
>>> for i in x:
	if i[0]=='y':
		print(i)

		
yasi
>>> for i in x:
	if i[0]=='y':
		i.upper()
		print(i)

		
'YASI'
yasi
>>> for i in x:
	if i[0]=='y':
		x.upper()
		print(i)

		
Traceback (most recent call last):
  File "<pyshell#79>", line 3, in <module>
    x.upper()
AttributeError: 'list' object has no attribute 'upper'
>>> for i in x:
	if i[1]=='a':
		i.upper()
		print(i)

		
'YASI'
yasi
'NAVE'
nave
>>> for i in x:
	if i[1]=='a':
		x.upper()
		print(x)

		
Traceback (most recent call last):
  File "<pyshell#83>", line 3, in <module>
    x.upper()
AttributeError: 'list' object has no attribute 'upper'
>>> for i in x:
	if x[1]=='a':
		x.upper()
		print(x)

		
>>> for i in x:
	if i[1]=='a':
		i.upper()
		print(x)

		
'YASI'
['yasi', 'nave', 'rema', 'abi', 'dhanu']
'NAVE'
['yasi', 'nave', 'rema', 'abi', 'dhanu']
>>> for i in x:
	if i[1]=='a':
		print(x)
		i.upper()

		
['yasi', 'nave', 'rema', 'abi', 'dhanu']
'YASI'
['yasi', 'nave', 'rema', 'abi', 'dhanu']
'NAVE'
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex21.py =======
HI, I AM CREATED BY A FUNCTION \PASSED AS AN ARGUMENT.
hi, i am created by a function \passed as an argument.
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex21.py =======
HI, I AM CREATED BY A FUNCTION \PASSED AS AN ARGUMENT.
hi, i am created by a function \passed as an argument.
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex21.py =======
HI, I AM CREATED BY A FUNCTION \PASSED AS AN ARGUMENT.
hi, i am created by a function \passed as an argument.
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex21.py =======
HI, I AM CREATED BY A FUNCTION \PASSED AS AN ARGUMENT.
hi, i am created by a function \passed as an argument.
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex21.py", line 19, in <module>
    for i in x:
NameError: name 'x' is not defined
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex21.py =======
HI, I AM CREATED BY A FUNCTION \PASSED AS AN ARGUMENT.
hi, i am created by a function \passed as an argument.
['yasi', 'nave', 'rema', 'abi', 'dhanu']
['yasi', 'nave', 'rema', 'abi', 'dhanu']
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex21.py =======
HI, I AM CREATED BY A FUNCTION \PASSED AS AN ARGUMENT.
hi, i am created by a function \passed as an argument.
['yasi', 'nave', 'rema', 'abi', 'dhanu']
['yasi', 'nave', 'rema', 'abi', 'dhanu']
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex21.py =======
['yasi', 'nave', 'rema', 'abi', 'dhanu']
['yasi', 'nave', 'rema', 'abi', 'dhanu']
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex21.py =======
['yasi', 'nave', 'rema', 'abi', 'dhanu']
['yasi', 'nave', 'rema', 'abi', 'dhanu']
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex21.py =======
['yasi', 'nave', 'rema', 'abi', 'dhanu']
['yasi', 'nave', 'rema', 'abi', 'dhanu']
>>> for i in x:
	if i[1]=='a':
		print(x)
		i.upper()

		
['yasi', 'nave', 'rema', 'abi', 'dhanu']
'YASI'
['yasi', 'nave', 'rema', 'abi', 'dhanu']
'NAVE'
>>> def createadd(x):
	def adder(y):
		return x+y
	return adder
add=createadder
SyntaxError: invalid syntax
>>> def createadd(x):
	def adder(y):
		return x+y
	return adder
add=createadder
SyntaxError: invalid syntax
>>> 
>>> def createadd(x):
	def adder(y):
		return x+y
	return adder

>>> 
>>> add=createadder
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    add=createadder
NameError: name 'createadder' is not defined
>>> def createadd(x):
	def adder(y):
		return x+y
	return adder

>>> add=createadder(10)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    add=createadder(10)
NameError: name 'createadder' is not defined
>>> def createadd(x):
	def adder(y):
		return x+y
	return adder

>>> add=createadd(10)
>>> print(add(10))
20
>>> def createadd(x):
	def adder(y):
		return x+y
	return adder
add=createadd(15)
SyntaxError: invalid syntax
>>> def createadd(x):
	def adder(y):
		return x+y
	return adder

>>> def createadd(x):
	def adder(y):
		return x+y
	return adder
add=createadd(15)
SyntaxError: invalid syntax
>>> def createadd(x):
	def adder(y):
		return x+y
	return adder

>>> add=createadd(10)
>>> print(add(10))
20
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex21.py =======
HI, I AM CREATED BY A FUNCTION \PASSED AS AN ARGUMENT.
hi, i am created by a function \passed as an argument.
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex22.py =======
The filtered letters are:
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex22.py =======
The filtered letters are:
e
e
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex22.py =======
The filtered letters are:
e
e
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex22.py =======
The filtered letters are:
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex22.py =======
The filtered letters are:
a
i
o
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex23.py =======
The filtered letters are:
nave
rema
dhanu
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex23.py =======
The filtered letters are:
nave
rema
dhanu
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex23.py =======
The filtered names are:
nave
rema
dhanu
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex23.py =======
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex23.py", line 6, in <module>
    filtered = filter(get, x)
NameError: name 'x' is not defined
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex23.py =======
The filtered names are:
nave
rema
dhanu
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex23.py =======
The filtered names are:
riya
janu
nave
priya
rema
dhanu
kavi
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex23.py =======
The filtered names are:
nave
rema
dhanu
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex23.py =======
The filtered names are:
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex23.py =======
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex23.py", line 10, in <module>
    filtered = filter(get, x)
NameError: name 'x' is not defined
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex23.py =======
The filtered names are:
nave
rema
dhanu
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex23.py =======
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex23.py", line 10, in <module>
    filtered = filter( x)
TypeError: filter expected 2 arguments, got 1
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex23.py =======
The filtered names are:
nave
rema
dhanu
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex23.py =======
The filtered names are:
nave
rema
dhanu
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
>>> get('g')
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    get('g')
  File "C:/Users/Asus/OneDrive/programs/ex24.py", line 4, in get
    for i in filter(get,x):
  File "C:/Users/Asus/OneDrive/programs/ex24.py", line 4, in get
    for i in filter(get,x):
  File "C:/Users/Asus/OneDrive/programs/ex24.py", line 4, in get
    for i in filter(get,x):
  [Previous line repeated 1022 more times]
RecursionError: maximum recursion depth exceeded while calling a Python object
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
>>> get()
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    get()
  File "C:/Users/Asus/OneDrive/programs/ex24.py", line 4, in get
    for i in filter(get,x):
TypeError: get() takes 0 positional arguments but 1 was given
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
>>> get()
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    get()
TypeError: get() missing 1 required positional argument: 'self'
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
>>> get("a")
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    get("a")
TypeError: get() missing 1 required positional argument: 'letters'
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
>>> get("y")
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    get("y")
TypeError: get() missing 1 required positional argument: 'letters'
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
>>> get(1)
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    get(1)
  File "C:/Users/Asus/OneDrive/programs/ex24.py", line 3, in get
    for i in filter(get,names):
  File "C:/Users/Asus/OneDrive/programs/ex24.py", line 3, in get
    for i in filter(get,names):
  File "C:/Users/Asus/OneDrive/programs/ex24.py", line 3, in get
    for i in filter(get,names):
  [Previous line repeated 1022 more times]
RecursionError: maximum recursion depth exceeded while calling a Python object
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex24.py", line 2, in <module>
    for i in filter(get,names):
NameError: name 'get' is not defined
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex24.py", line 2, in <module>
    for i in filter(names):
TypeError: filter expected 2 arguments, got 1
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex24.py", line 2, in <module>
    for i in filter(names):
TypeError: filter expected 2 arguments, got 1

>>> 
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex24.py", line 2, in <module>
    for i in filter(names):
TypeError: filter expected 2 arguments, got 1
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex24.py", line 4, in <module>
    for i in filter(get,names):
NameError: name 'get' is not defined
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex24.py", line 4, in <module>
    for i in filter(getdata,names):
NameError: name 'names' is not defined
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex24.py", line 5, in <module>
    for i in filter(getdata,names):
NameError: name 'names' is not defined
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex24.py", line 5, in <module>
    for i in filter(get,names):
NameError: name 'names' is not defined
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
yeah it's crt
yeah it's crt
yeah it's crt
yeah it's crt
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
>>> get("yeah it's crt")
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
>>> get("y")
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    get("y")
  File "C:/Users/Asus/OneDrive/programs/ex24.py", line 3, in get
    for i in filter(get,names):
  File "C:/Users/Asus/OneDrive/programs/ex24.py", line 3, in get
    for i in filter(get,names):
  File "C:/Users/Asus/OneDrive/programs/ex24.py", line 3, in get
    for i in filter(get,names):
  [Previous line repeated 1022 more times]
RecursionError: maximum recursion depth exceeded while calling a Python object
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
>>> get()
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    get()
TypeError: get() missing 1 required positional argument: 'object'
>>> get('a')
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    get('a')
  File "C:/Users/Asus/OneDrive/programs/ex24.py", line 3, in get
    for i in names():
TypeError: 'list' object is not callable
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex24.py", line 2, in <module>
    for i in names():
TypeError: 'list' object is not callable
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
y
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
>>> get()
y
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
>>> get()
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    get()
  File "C:/Users/Asus/OneDrive/programs/ex24.py", line 3, in get
    for i in filter(get,x):
TypeError: get() takes 0 positional arguments but 1 was given
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
>>> get()
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    get()
  File "C:/Users/Asus/OneDrive/programs/ex24.py", line 4, in get
    for i in filter(get,x):
TypeError: get() takes 0 positional arguments but 1 was given
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
>>> get()
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    get()
  File "C:/Users/Asus/OneDrive/programs/ex24.py", line 4, in get
    for i in filter(get,z):
TypeError: get() takes 0 positional arguments but 1 was given
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex24.py", line 9, in <module>
    filtered=filter(is_filtererd,x)
NameError: name 'is_filtererd' is not defined
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex24.py", line 9, in <module>
    ans=filter(filtererd,x)
NameError: name 'filtererd' is not defined
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex24.py", line 10, in <module>
    print(list(ans))
  File "C:/Users/Asus/OneDrive/programs/ex24.py", line 4, in filtered
    if data % 2 ==0:
TypeError: not all arguments converted during string formatting
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
[2, 4, 6, 8, 10]
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
['y']
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
<filter object at 0x000001ED43279FD0>
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex24.py", line 10, in <module>
    print (dic(ans))
NameError: name 'dic' is not defined
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex24.py", line 10, in <module>
    print (dict(ans))
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
['y']
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
[]
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
['y']
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
['y', 'y']
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
['y', 'y']
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
['n']
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex24.py =======
['n', 'n']
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex23.py =======
The filtered names are:
['n', 'a', 'v', 'e']
['r', 'e', 'm', 'a']
['d', 'h', 'a', 'n', 'u']
>>> 
======= RESTART: C:/Users/Asus/OneDrive/programs/ex23.py =======
The filtered names are:
nave
rema
dhanu
>>> 