Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> np.array([1,2,3,4,5,6,7,8,9,10])
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
>>> l=[ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10]
>>> np.array(l)
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
>>> np.array(1,None,*,True,'K',False,0,None)
SyntaxError: iterable argument unpacking follows keyword argument unpacking
>>> a=np.array([1,2,3],[4,5,6],[7,8,9])
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a=np.array([1,2,3],[4,5,6],[7,8,9])
TypeError: array() takes from 1 to 2 positional arguments but 3 were given
>>> a=np.array([[1,2,3],[4,5,6],[7,8,9]])
>>> a
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> dtype(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dtype(a)
NameError: name 'dtype' is not defined
>>> type(a)
<class 'numpy.ndarray'>
>>> a.dtype
dtype('int32')
>>> print("Array is :",a)
Array is : [[1 2 3]
 [4 5 6]
 [7 8 9]]
>>> print ("Dimensions of a are:", a.ndim)

Dimensions of a are: 2
>>> print ("Dimensions of a are:", a.ndim)
Dimensions of a are: 2
>>> print ("Shape of a is", a.shape)

Shape of a is (3, 3)
>>> 
KeyboardInterrupt
>>> print ("Size of a is", a.size)


Size of a is 9
>>> print ("Size of a is", a.data)
Size of a is <memory at 0x000002052EF38110>
>>> print ("Size of a is", a.item(*args))
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print ("Size of a is", a.item(*args))
NameError: name 'args' is not defined
>>> print ("Size of a is", a.item())
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print ("Size of a is", a.item())
ValueError: can only convert an array of size 1 to a Python scalar
>>> print ("Size of a is", a.itemsize)
Size of a is 4
>>> print ("Size of a is", a.nbytes)
Size of a is 36
>>> print ("Size of a is", a.reshape(8))
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print ("Size of a is", a.reshape(8))
ValueError: cannot reshape array of size 9 into shape (8,)
>>> print ("Size of a is", a.reshape(10,'c'))
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print ("Size of a is", a.reshape(10,'c'))
TypeError: 'str' object cannot be interpreted as an integer
>>> print ("Size of a is", a.reshape(10,c))
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    print ("Size of a is", a.reshape(10,c))
NameError: name 'c' is not defined
>>> print ("Size of a is", a.reshape(10,C))
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    print ("Size of a is", a.reshape(10,C))
NameError: name 'C' is not defined
>>> a=np.empty([2,2],dtype=int)
>>> print(a)
[[ -565312707  1819006733]
 [ 1724040469 -1802978454]]
>>> x=np.empty([2,2],dtype=int)
>>> print(x)
[[ -565312707  1819006733]
 [ 1724040469 -1802978454]]
>>> x=np.empty([2,2],dtype=float)
>>> print(x)
[[5.e-324 4.e-323]
 [2.e-323 2.e-323]]
>>> a=np.zeros([2,2],dtype=int)
>>> 
>>> print(a)
[[0 0]
 [0 0]]
>>> a=np.zeros([2,2],dtype=float)
>>> print(a)
[[0. 0.]
 [0. 0.]]
>>> a=np.zeros_like
>>> print(a)
<function zeros_like at 0x000002052F2980D0>
>>> for i in a:
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    for i in a:
TypeError: 'function' object is not iterable
>>> for i in np.zeros_like(a):
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    for i in np.zeros_like(a):
TypeError: iteration over a 0-d array
>>> for i in np.zeros_like(a,dtype=0):
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    for i in np.zeros_like(a,dtype=0):
  File "<__array_function__ internals>", line 5, in zeros_like
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\numpy\core\numeric.py", line 138, in zeros_like
    res = empty_like(a, dtype=dtype, order=order, subok=subok, shape=shape)
  File "<__array_function__ internals>", line 5, in empty_like
TypeError: Cannot interpret '0' as a data type
>>> for i in np.zeros_like(a,dtype=1):
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    for i in np.zeros_like(a,dtype=1):
  File "<__array_function__ internals>", line 5, in zeros_like
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\numpy\core\numeric.py", line 138, in zeros_like
    res = empty_like(a, dtype=dtype, order=order, subok=subok, shape=shape)
  File "<__array_function__ internals>", line 5, in empty_like
TypeError: Cannot interpret '1' as a data type
>>> a=np.zeros([2,2],dtype=int)
>>> print(a)
[[0 0]
 [0 0]]
>>> b=np.ones([2,2],dtype=int)
>>> print(c)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    print(c)
NameError: name 'c' is not defined
>>> print(b)

[[1 1]
 [1 1]]
>>> np.copyto(a,b)
>>> print(a)
[[1 1]
 [1 1]]
>>> a=np.array([[1,2],[3,4]])
>>> print(a)
[[1 2]
 [3 4]]
>>> print(np.reshape(a,4))
[1 2 3 4]
>>> print(np.reshape(a,5))
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    print(np.reshape(a,5))
  File "<__array_function__ internals>", line 5, in reshape
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\numpy\core\fromnumeric.py", line 298, in reshape
    return _wrapfunc(a, 'reshape', newshape, order=order)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\numpy\core\fromnumeric.py", line 57, in _wrapfunc
    return bound(*args, **kwds)
ValueError: cannot reshape array of size 4 into shape (5,)
>>> a=np.array([[1,2],[3,4],[2]])

Warning (from warnings module):
  File "<pyshell#80>", line visibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray.
>>> a=np.array([[1,2],[3,4],[5,6]])
>>> print(np.reshape(a,6))
[1 2 3 4 5 6]
>>> a=np.array([[1,2],[3,4]])
>>> print(a)
[[1 2]
 [3 4]]
>>> print(a.T)
[[1 3]
 [2 4]]
>>> np.moveaxis(a,b,a)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    np.moveaxis(a,b,a)
  File "<__array_function__ internals>", line 5, in moveaxis
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\numpy\core\numeric.py", line 1454, in moveaxis
    source = normalize_axis_tuple(source, a.ndim, 'source')
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\numpy\core\numeric.py", line 1385, in normalize_axis_tuple
    axis = tuple([normalize_axis_index(ax, ndim, argname) for ax in axis])
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\numpy\core\numeric.py", line 1385, in <listcomp>
    axis = tuple([normalize_axis_index(ax, ndim, argname) for ax in axis])
TypeError: only integer scalar arrays can be converted to a scalar index
>>> np.rollaxis(a,0)
array([[1, 2],
       [3, 4]])
>>> np.rollaxis(a,1)
array([[1, 3],
       [2, 4]])
>>> np.rollaxis(a,2)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    np.rollaxis(a,2)
  File "<__array_function__ internals>", line 5, in rollaxis
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\numpy\core\numeric.py", line 1318, in rollaxis
    axis = normalize_axis_index(axis, n)
numpy.AxisError: axis 2 is out of bounds for array of dimension 2
>>> a = np.array([[1, 2], [3, 4]])

>>> b = np.array([[5, 6]])
>>> print ("concatenated array vertically:", np.concatenate((a, b), axis=0))
concatenated array vertically: [[1 2]
 [3 4]
 [5 6]]
>>> print ("concatenated array horizontally:", np.concatenate((a, b), axis=None))
concatenated array horizontally: [1 2 3 4 5 6]
>>> print ("concatenated array vertically:", np.concatenate((a, b), axis=1))
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    print ("concatenated array vertically:", np.concatenate((a, b), axis=1))
  File "<__array_function__ internals>", line 5, in concatenate
ValueError: all the input array dimensions for the concatenation axis must match exactly, but along dimension 0, the array at index 0 has size 2 and the array at index 1 has size 1
>>> a = np.arange(8)
>>> print(a)
[0 1 2 3 4 5 6 7]
>>> print(np.split(a,4))
[array([0, 1]), array([2, 3]), array([4, 5]), array([6, 7])]
>>> a = np.arange(10)
>>> print(a)
[0 1 2 3 4 5 6 7 8 9]
>>> print(np.split(a,5))
[array([0, 1]), array([2, 3]), array([4, 5]), array([6, 7]), array([8, 9])]
>>> print(np.split(a,2))
[array([0, 1, 2, 3, 4]), array([5, 6, 7, 8, 9])]
>>> a = np.array([[1,2,3],[1,2,3]])
>>> print ("array a is :", a)
array a is : [[1 2 3]
 [1 2 3]]
>>> print (np.insert(a,1,5, axis = 1))
[[1 5 2 3]
 [1 5 2 3]]
>>> a = np.array([[1,2,3],[1,2,3]])
>>> print (a)
[[1 2 3]
 [1 2 3]]
>>> print (np.insert(a,1,5, axis = 1))
[[1 5 2 3]
 [1 5 2 3]]
>>> print (np.insert(a,2,5,axis=1))
[[1 2 5 3]
 [1 2 5 3]]
>>> a = np.array([[1,2,3],[0.1,2,4]])
>>> print (np.insert(a,2,5,axis=1))
[[1.  2.  5.  3. ]
 [0.1 2.  5.  4. ]]
>>> a = np.array([[1,2,3],[0,1,2,4]])
>>> print (np.insert(a,2,5,axis=1))
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    print (np.insert(a,2,5,axis=1))
  File "<__array_function__ internals>", line 5, in insert
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\numpy\lib\function_base.py", line 4673, in insert
    axis = normalize_axis_index(axis, ndim)
numpy.AxisError: axis 1 is out of bounds for array of dimension 1
>>> a = np.array([[1,2,3,5],[0,1,2,4]])
>>> print (np.insert(a,2,5,axis=1))
[[1 2 5 3 5]
 [0 1 5 2 4]]
>>> a = np.array([[1,2,3],[4,5,6]])
>>> print(a)
[[1 2 3]
 [4 5 6]]
>>> 
KeyboardInterrupt
>>> print( np.delete(a,[1,2,3],0))
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    print( np.delete(a,[1,2,3],0))
  File "<__array_function__ internals>", line 5, in delete
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\numpy\lib\function_base.py", line 4552, in delete
    keep[obj,] = False
IndexError: index 2 is out of bounds for axis 0 with size 2
>>> print( np.delete(a,[1,2,3],axis=0))
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    print( np.delete(a,[1,2,3],axis=0))
  File "<__array_function__ internals>", line 5, in delete
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\numpy\lib\function_base.py", line 4552, in delete
    keep[obj,] = False
IndexError: index 2 is out of bounds for axis 0 with size 2
>>> print( np.delete(a,[1,2,3],axis=1))
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    print( np.delete(a,[1,2,3],axis=1))
  File "<__array_function__ internals>", line 5, in delete
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\numpy\lib\function_base.py", line 4552, in delete
    keep[obj,] = False
IndexError: index 3 is out of bounds for axis 0 with size 3
>>> print( np.delete(a,[1,2,3],axis=0))
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    print( np.delete(a,[1,2,3],axis=0))
  File "<__array_function__ internals>", line 5, in delete
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\numpy\lib\function_base.py", line 4552, in delete
    keep[obj,] = False
IndexError: index 2 is out of bounds for axis 0 with size 2
>>> a = np.array([[1,2,3],[1,2,3]])

>>> print ("array a after deletion :", np.delete(a,[1,2,3], axis = 0))


Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    print ("array a after deletion :", np.delete(a,[1,2,3], axis = 0))
  File "<__array_function__ internals>", line 5, in delete
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\numpy\lib\function_base.py", line 4552, in delete
    keep[obj,] = False
IndexError: index 2 is out of bounds for axis 0 with size 2
>>> print (np.delete(a,[1,2,3], axis = 0))
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    print (np.delete(a,[1,2,3], axis = 0))
  File "<__array_function__ internals>", line 5, in delete
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\numpy\lib\function_base.py", line 4552, in delete
    keep[obj,] = False
IndexError: index 2 is out of bounds for axis 0 with size 2
>>> np.delete(a,obj([1,2,3]),axis=0))
SyntaxError: unmatched ')'
>>> np.delete(a,obj([1,2,3]),axis=0)
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    np.delete(a,obj([1,2,3]),axis=0)
NameError: name 'obj' is not defined
>>> np.delete(a,[1,2,3],axis=0)
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    np.delete(a,[1,2,3],axis=0)
  File "<__array_function__ internals>", line 5, in delete
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\numpy\lib\function_base.py", line 4552, in delete
    keep[obj,] = False
IndexError: index 2 is out of bounds for axis 0 with size 2
>>> a = np.array([[1,2,3],[1,2,3]])
>>> print (np.delete(a,[1,2,3], axis = 0))
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    print (np.delete(a,[1,2,3], axis = 0))
  File "<__array_function__ internals>", line 5, in delete
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\numpy\lib\function_base.py", line 4552, in delete
    keep[obj,] = False
IndexError: index 2 is out of bounds for axis 0 with size 2
>>> a = np.array([[1,2],[3,4]])

>>> print (np.rot90(a,1,(1,0)))
[[3 1]
 [4 2]]
>>> print (np.rot90(a,1,(0,1)))
[[2 4]
 [1 3]]
>>> a = np.array([[1,2],[3,4]])
>>> print (np.rot90(a,1,(0,1)))
[[2 4]
 [1 3]]
>>> print (np.rot90(a,1,(0,1)))
[[2 4]
 [1 3]]
>>> a = np.array([[1,2],[3,4]])
>>> x=np.array([1,2,3,4,5])
>>> x
array([1, 2, 3, 4, 5])
>>> print(x)
[1 2 3 4 5]
>>> x[0]
1
>>> for i in x:
	print(i)

	
1
2
3
4
5
>>> for i in x:
	print(type(i))

	
<class 'numpy.int32'>
<class 'numpy.int32'>
<class 'numpy.int32'>
<class 'numpy.int32'>
<class 'numpy.int32'>
>>> for i in x:
	print(dtype(i))

	
Traceback (most recent call last):
  File "<pyshell#155>", line 2, in <module>
    print(dtype(i))
NameError: name 'dtype' is not defined
>>> x.size
5
>>> x.itemsize
4
>>> x.nbytes
20
>>> x.dtype
dtype('int32')
>>> x=np.zeros(0)\\
SyntaxError: unexpected character after line continuation character
>>> x=np.zeros(0)
>>> x
array([], dtype=float64)
>>> help
