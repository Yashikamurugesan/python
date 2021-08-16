Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32=========== RESTART: C:\Users\Asus\OneDrive\programs\ex23.py ===========
The filtered names are:
nave
rema
dhanu
>>> 
=========== RESTART: C:\Users\Asus\OneDrive\programs\ex23.py ===========
The filtered names are:
>>> 
=========== RESTART: C:\Users\Asus\OneDrive\programs\ex23.py ===========
The filtered names are:
nave
rema
dhanu
>>> 
=========== RESTART: C:\Users\Asus\OneDrive\programs\ex23.py ===========
The filtered names are:
nave
rema
dhanu
>>> list=['priya','riya','meenu','yasi','nave','rupa']
>>> mapobj=map(lambda x:x.replace('','').list)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    mapobj=map(lambda x:x.replace('','').list)
TypeError: map() must have at least two arguments.
>>> mapobj=map(lambda x:x.pop().list)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    mapobj=map(lambda x:x.pop().list)
TypeError: map() must have at least two arguments.
>>> mapobj=map(lambda x:x.pop().['priya','riya','meenu','yasi','nave','rupa'])
SyntaxError: invalid syntax
>>> mapobj=map(lambda x:x.pop(),['priya','riya','meenu','yasi','nave','rupa'])
>>> for i in mapobj:
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    for i in mapobj:
  File "<pyshell#4>", line 1, in <lambda>
    mapobj=map(lambda x:x.pop(),['priya','riya','meenu','yasi','nave','rupa'])
AttributeError: 'str' object has no attribute 'pop'
>>> for i in mapobj():
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    for i in mapobj():
TypeError: 'map' object is not callable
>>> mapobj=map(lambda x:x.pop(),['priya','riya','meenu','yasi','nave','rupa'])
>>> mapobj
<map object at 0x0000027483C1DE20>
>>> list=['priya','riya','meenu','yasi','nave','rupa']
>>> mapobj=map(lambda x:x.replace(' ',''),['priya','riya','meenu','yasi','nave','rupa'])
>>> mapobj
<map object at 0x0000027483C1DBE0>
>>> for i in mapobj:
	print(i)

	
priya
riya
meenu
yasi
nave
rupa
>>> mapobj=map(lambda x:x.replace('',' '),['priya','riya','meenu','yasi','nave','rupa'])
>>> for i in mapobj:
	print(i)

	
 p r i y a 
 r i y a 
 m e e n u 
 y a s i 
 n a v e 
 r u p a 
>>> mapobj=map(lambda x:x.replace('','#'),['priya','riya','meenu','yasi','nave','rupa'])
>>> 
>>> for i in mapobj:
	print(i)

	
#p#r#i#y#a#
#r#i#y#a#
#m#e#e#n#u#
#y#a#s#i#
#n#a#v#e#
#r#u#p#a#
>>> mapobj=map(lambda x:x.replace('p','r'),['priya','riya','meenu','yasi','nave','rupa'])
>>> 
>>> for i in mapobj:
	print(i)

	
rriya
riya
meenu
yasi
nave
rura
>>> mapobj=map(lambda x:x.insert(0,'mangai'),['priya','riya','meenu','yasi','nave','rupa'])
>>> for i in mapobj:
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    for i in mapobj:
  File "<pyshell#29>", line 1, in <lambda>
    mapobj=map(lambda x:x.insert(0,'mangai'),['priya','riya','meenu','yasi','nave','rupa'])
AttributeError: 'str' object has no attribute 'insert'
>>> mapobj=map(lambda x:x.insert(1,'mangai'),['priya','riya','meenu','yasi','nave','rupa'])
>>> mapobj
<map object at 0x0000027483C1D1C0>
>>> for i in mapobj:
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    for i in mapobj:
  File "<pyshell#32>", line 1, in <lambda>
    mapobj=map(lambda x:x.insert(1,'mangai'),['priya','riya','meenu','yasi','nave','rupa'])
AttributeError: 'str' object has no attribute 'insert'
>>> mapobj=map(lambda x:x.insert(1,'mangai'),list)
>>> for i in mapobj:
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    for i in mapobj:
  File "<pyshell#37>", line 1, in <lambda>
    mapobj=map(lambda x:x.insert(1,'mangai'),list)
AttributeError: 'str' object has no attribute 'insert'
>>> mapobj=map(lambda x:x.insert(1,'mangai'),list)
>>> 
>>> mapobj=map(lambda x:x.insert(2,'kavi'),['priya','riya','meenu','yasi','nave','rupa'])
>>> mapobj
<map object at 0x0000027483C1DF70>
>>> print(mapobj)
<map object at 0x0000027483C1DF70>
>>> for i in mapobj:
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    for i in mapobj:
  File "<pyshell#43>", line 1, in <lambda>
    mapobj=map(lambda x:x.insert(2,'kavi'),['priya','riya','meenu','yasi','nave','rupa'])
AttributeError: 'str' object has no attribute 'insert'
>>> mapobj=map(lambda x:x.pop() ,['priya','riya','meenu','yasi','nave','rupa'])
>>> for i in mapobj:
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    for i in mapobj:
  File "<pyshell#49>", line 1, in <lambda>
    mapobj=map(lambda x:x.pop() ,['priya','riya','meenu','yasi','nave','rupa'])
AttributeError: 'str' object has no attribute 'pop'
>>> mapobj=map(lambda x:x.pop() ,['priya','riya','meenu','yasi','nave','rupa'])
>>> 
=========== RESTART: C:/Users/Asus/OneDrive/programs/ex25.py ===========
 priya
 riya
 meenu
 yasi
 nave
 rupa
>>> 
=========== RESTART: C:/Users/Asus/OneDrive/programs/ex25.py ===========
priya
riya
meenu
yasi
nave
rupa
>>> 
=========== RESTART: C:/Users/Asus/OneDrive/programs/ex25.py ===========
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex25.py", line 4, in <module>
    for i in mapobj:
  File "C:/Users/Asus/OneDrive/programs/ex25.py", line 3, in <lambda>
    mapobj=map(lambda x:x.insert(2,'kavi') ,[' priya',' riya',' meenu',' yasi',' nave',' rupa'])
AttributeError: 'str' object has no attribute 'insert'
>>> 
=========== RESTART: C:/Users/Asus/OneDrive/programs/ex26.py ===========
<map object at 0x0000016DCA379DC0>
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex26.py", line 6, in <module>
    for i in mapobj:
TypeError: getdata() takes 0 positional arguments but 1 was given
>>> 
=========== RESTART: C:/Users/Asus/OneDrive/programs/ex26.py ===========
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex26.py", line 5, in <module>
    for i in mapobj:
TypeError: getdata() takes 0 positional arguments but 1 was given
>>> 
=========== RESTART: C:/Users/Asus/OneDrive/programs/ex26.py ===========
Y
E
A
H
 
I
T
'
S
 
M
E
 
Y
A
S
I
>>> 
=========== RESTART: C:/Users/Asus/OneDrive/programs/ex26.py ===========
Y
E
A
H
 
I
T
'
S
 
M
E
 
Y
A
S
I
MEENU
NAVE
PRIYA
RIYA
RUPA
KAVIYA
>>> 
=========== RESTART: C:/Users/Asus/OneDrive/programs/ex26.py ===========
Y
E
A
H
 
I
T
'
S
 
M
E
 
Y
A
S
I
MEENU
NAVE
PRIYA
RIYA
RUPA
KAVIYA
>>> 
=========== RESTART: C:/Users/Asus/OneDrive/programs/ex28.py ===========
KAVIYA
MEENU
PRIYA
NAVE
RUPA
RIYA
>>> 
=========== RESTART: C:/Users/Asus/OneDrive/programs/ex28.py ===========
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex28.py", line 5, in <module>
    for i in mapobj:
  File "C:/Users/Asus/OneDrive/programs/ex28.py", line 2, in getdata
    return x.insert(1,'kavi')
AttributeError: 'str' object has no attribute 'insert'
>>> 
=========== RESTART: C:/Users/Asus/OneDrive/programs/ex28.py ===========
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex28.py", line 5, in <module>
    for i in mapobj:
  File "C:/Users/Asus/OneDrive/programs/ex28.py", line 2, in getdata
    return x.insert([1,'kavi'])
AttributeError: 'str' object has no attribute 'insert'
>>> 
=========== RESTART: C:/Users/Asus/OneDrive/programs/ex28.py ===========
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex28.py", line 5, in <module>
    for i in mapobj:
  File "C:/Users/Asus/OneDrive/programs/ex28.py", line 2, in getdata
    return x.insert([1,'kavi'])
AttributeError: 'str' object has no attribute 'insert'
>>> 
=========== RESTART: C:/Users/Asus/OneDrive/programs/ex28.py ===========
<map object at 0x000001E518349D90>
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex28.py", line 6, in <module>
    for i in mapobj:
  File "C:/Users/Asus/OneDrive/programs/ex28.py", line 2, in getdata
    return x.insert([1,'kavi'])
AttributeError: 'str' object has no attribute 'insert'
>>> 
=========== RESTART: C:/Users/Asus/OneDrive/programs/ex28.py ===========
<map object at 0x000002C474F79D90>
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex28.py", line 6, in <module>
    for i in mapobj:
  File "C:/Users/Asus/OneDrive/programs/ex28.py", line 2, in getdata
    return x.insert([1,'kavi'])
AttributeError: 'str' object has no attribute 'insert'
>>> 
=========== RESTART: C:/Users/Asus/OneDrive/programs/ex28.py ===========
<map object at 0x00000175877B9D90>
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex28.py", line 6, in <module>
    for i in mapobj:
  File "C:/Users/Asus/OneDrive/programs/ex28.py", line 2, in getdata
    return x.insert([1,'kavi'])
AttributeError: 'str' object has no attribute 'insert'
>>> 
=========== RESTART: C:/Users/Asus/OneDrive/programs/ex28.py ===========
<map object at 0x0000024D634C9D90>
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex28.py", line 6, in <module>
    for i in mapobj:
  File "C:/Users/Asus/OneDrive/programs/ex28.py", line 2, in getdata
    return x.insert(1,'kavi')
AttributeError: 'str' object has no attribute 'insert'
>>> 
=========== RESTART: C:/Users/Asus/OneDrive/programs/ex28.py ===========
<map object at 0x000001B5764B9D90>
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex28.py", line 6, in <module>
    for i in mapobj:
  File "C:/Users/Asus/OneDrive/programs/ex28.py", line 2, in getdata
    return x.insert(1,'kavi')
AttributeError: 'str' object has no attribute 'insert'
>>> 
=========== RESTART: C:/Users/Asus/OneDrive/programs/ex28.py ===========
<map object at 0x000002112C4F9D90>
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex28.py", line 6, in <module>
    for i in mapobj:
  File "C:/Users/Asus/OneDrive/programs/ex28.py", line 2, in getdata
    return x.replace(1,'kavi')
TypeError: replace() argument 1 must be str, not int
>>> 
=========== RESTART: C:/Users/Asus/OneDrive/programs/ex28.py ===========
<map object at 0x0000014F4DAA9D90>
[' ', 'm', ' ', 'e', ' ', 'e', ' ', 'n', ' ', 'u', ' ']
[' ', 'n', ' ', 'a', ' ', 'v', ' ', 'e', ' ']
[' ', 'p', ' ', 'r', ' ', 'i', ' ', 'y', ' ', 'a', ' ']
[' ', 'r', ' ', 'i', ' ', 'y', ' ', 'a', ' ']
[' ', 'r', ' ', 'u', ' ', 'p', ' ', 'a', ' ']
[' ', 'k', ' ', 'a', ' ', 'v', ' ', 'i', ' ', 'y', ' ', 'a', ' ']
>>> 
=========== RESTART: C:/Users/Asus/OneDrive/programs/ex28.py ===========
<map object at 0x0000025A61CC9D90>
['m', 'e', 'e', 'n', 'u']
['n', 'a', 'v', 'e']
['p', 'r', 'i', 'y', 'a']
['r', 'i', 'y', 'a']
['r', 'u', 'p', 'a']
['k', 'a', 'v', 'i', 'y', 'a']
>>> 
=========== RESTART: C:/Users/Asus/OneDrive/programs/ex28.py ===========
<map object at 0x000001C846929D90>
meenu
nave
priya
riya
rupa
kaviya
>>> 
=========== RESTART: C:/Users/Asus/OneDrive/programs/ex28.py ===========
<map object at 0x00000268EF789D90>
meenu
nave
priya
riya
rupa
kaviya
>>> x['a','s']
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    x['a','s']
NameError: name 'x' is not defined
>>> x=['a','s']
>>> x.count('d')
0
>>> x
['a', 's']
>>> x=['a','s']
>>> x.count('s')
1
>>> 
=========== RESTART: C:/Users/Asus/OneDrive/programs/ex28.py ===========
<map object at 0x0000019EBCEF9D90>
0
0
1
1
0
0
>>> 
=========== RESTART: C:/Users/Asus/OneDrive/programs/ex29.py ===========
>>> from ex29 import get
>>> get.display()
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    get.display()
TypeError: display() missing 1 required positional argument: 'self'
>>> x=get()
>>> get.display
<function get.display at 0x0000026CBB8C2F70>
>>> 

=========== RESTART: C:/Users/Asus/OneDrive/programs/ex29.py ===========
>>> 
>>> 
=========== RESTART: C:/Users/Asus/OneDrive/programs/ex29.py ===========
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/ex29.py", line 1, in <module>
    class get(s):
NameError: name 's' is not defined
>>> 
=========== RESTART: C:/Users/Asus/OneDrive/programs/ex29.py ===========
>>> x=get()
>>> x.display()
hi
>>> x.showme()
i'm yasi
>>> from ex29 import get
>>> get()
<ex29.get object at 0x0000023404E270D0>
>>> get().display()
hi
>>> get().showme()
i'm yasi
>>> 
=========== RESTART: C:/Users/Asus/OneDrive/programs/ex29.py ===========
>>> from ex29 import get
>>> get()
<ex29.get object at 0x000001DB276470D0>
>>> get().display()
hi
>>> i'm yasi

>>> 
=========== RESTART: C:/Users/Asus/OneDrive/programs/ex28.py ====================== RESTART: C:\Users\Asus\OneDrive\programs\ex28.py ===========
<map object at 0x0000023405429D90>
0
0
1
1
0
0
>>> 
=========== RESTART: C:\Users\Asus\OneDrive\programs\ex28.py ===========
<map object at 0x0000015A22769D90>
1
0
0
0
0
0
>>> 
=========== RESTART: C:\Users\Asus\OneDrive\programs\ex28.py ===========
<map object at 0x00000286E77E9D90>
Traceback (most recent call last):
  File "C:\Users\Asus\OneDrive\programs\ex28.py", line 6, in <module>
    for i in mapobj:
  File "C:\Users\Asus\OneDrive\programs\ex28.py", line 2, in getdata
    return x.count(1)
TypeError: must be str, not int
>>> 
=========== RESTART: C:\Users\Asus\OneDrive\programs\ex28.py ===========
<map object at 0x000001F6CB869D90>
1
0
0
0
0
0
>>> mapobj=map(lambda x:x.replace('p','r'),['priya','riya','meenu','yasi','nave','rupa'])
>>> for i in mapobj:
	print(i)

	
rriya
riya
meenu
yasi
nave
rura
>>> mapobj=map(lambda x:x.replace(' ',''),[' priya',' riya',' meenu','yasi','nave','rupa'])
>>> for i in mapobj:
	print(i)

	
priya
riya
meenu
yasi
nave
rupa
>>> mapobj=map(lambda x:x.upper(),[' priya',' riya',' meenu','yasi','nave','rupa'])
>>> for i in mapobj:
	print(i)

	
 PRIYA
 RIYA
 MEENU
YASI
NAVE
RUPA
>>> mapobj=map(lambda x:x.upper(),['priya','riya','meenu','yasi','nave','rupa'])
>>> for i in mapobj:
	print(i)

	
PRIYA
RIYA
MEENU
YASI
NAVE
RUPA
>>> mapobj=map(lambda x:x.insert(1,'kavi'),['priya','riya','meenu','yasi','nave','rupa'])
>>> for i in mapobj:
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    for i in mapobj:
  File "<pyshell#90>", line 1, in <lambda>
    mapobj=map(lambda x:x.insert(1,'kavi'),['priya','riya','meenu','yasi','nave','rupa'])
AttributeError: 'str' object has no attribute 'insert'
>>> x=1
>>> y=9
>>> lambda x,y:x+y
<function <lambda> at 0x000001F6CB8773A0>
>>> z=lambda x,y:x+y
>>> x=lambda a,b:a+b
>>> print(x(1,9))
10
>>> import array
>>> import list
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    import list
ModuleNotFoundError: No module named 'list'
>>> list=['yashika']
>>> print(list)
['yashika']
>>> import numpy
d
>>> import numpy
>>> import pandas
>>> import pandas
>>> 
=========== RESTART: C:/Users/Asus/OneDrive/programs/ex26.py ===========
Y
E
A
H
 
I
T
'

S
 
M
E
 
Y
A
S
I
MEENU
NAVE
PRIYA
RIYA
RUPA
KAVIYA
>>> 
=========== RESTART: C:/Users/Asus/OneDrive/programs/ex26.py ===========
YEAH IT'S ME YASIMEENU
NAVE
PRIYA
RIYA
RUPA
KAVIYA
>>> 
=========== RESTART: C:/Users/Asus/OneDrive/programs/ex26.py ===========
Y/nE/nA/nH/n /nI/nT/n'/nS/n /nM/nE/n /nY/nA/nS/nI/nMEENU
NAVE
PRIYA
RIYA
RUPA
KAVIYA
>>> 
=========== RESTART: C:/Users/Asus/OneDrive/programs/ex26.py ===========
Y/n 
E/n 
A/n 
H/n 
 /n 
I/n 
T/n 
'/n 
S/n 
 /n 
M/n 
E/n 
 /n 
Y/n 
A/n 
S/n 
I/n 
MEENU
NAVE
PRIYA
RIYA
RUPA
KAVIYA
>>> 
=========== RESTART: C:/Users/Asus/OneDrive/programs/ex26.py ===========
Y
 
E
 
A
 
H
 
 
 
I
 
T
 
'
 
S
 
 
 
M
 
E
 
 
 
Y
 
A
 
S
 
I
 
MEENU
NAVE
PRIYA
RIYA
RUPA
KAVIYA
>>> 
=========== RESTART: C:/Users/Asus/OneDrive/programs/ex26.py ===========
Y

E

A

H

 

I

T

'

S

 

M

E

 

Y

A

S

I

MEENU
NAVE
PRIYA
RIYA
RUPA
KAVIYA
>>> 
=========== RESTART: C:/Users/Asus/OneDrive/programs/ex26.py ===========
Y E A H   I T ' S   M E   Y A S I MEENU
NAVE
PRIYA
RIYA
RUPA
KAVIYA
>>> 

=========== RESTART: C:\Users\Asus\OneDrive\programs\ex28.py ===========
>>> 
<map object at 0x000001F06B1DDB80>
1
0
0
0
0
0
>>> 