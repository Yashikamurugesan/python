Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> np.random.randint(100,size=(10,15))
array([[56,  9, 24, 68, 56, 22, 72, 91,  7, 44, 35, 13, 20, 35, 95],
       [67, 23, 36,  5, 53,  2, 67, 70,  1, 91, 93, 66, 29, 12, 12],
       [17, 46, 53, 74,  6, 91, 75, 30, 15, 75, 31, 84, 91, 19, 94],
       [92, 30, 21,  9, 73, 12, 13, 28, 54, 97,  2, 14, 82,  7, 27],
       [10, 83, 17, 90, 27, 41, 84, 74,  3, 50, 49, 78,  6,  5, 96],
       [71, 27, 71, 24, 56, 41, 98, 80,  4, 19, 56, 51, 38, 77, 19],
       [42, 59, 31, 36,  8, 66, 51, 29, 24, 18, 37, 53, 83, 59, 70],
       [51, 32,  0, 77, 15, 79, 31, 72,  1, 14, 73, 82, 32, 10, 50],
       [84, 78, 58, 97, 33, 82, 51, 58, 48, 69, 72, 58, 66, 47, 43],
       [28, 12, 93, 88, 69, 75, 92, 21, 36, 69, 47, 36, 97,  3, 98]])
>>> x=np.random.randint(100,size=(10,15))
>>> x
array([[79, 25, 76, 79, 75, 96, 57, 35, 34, 41, 37, 95, 34, 77, 56],
       [90, 24, 76, 31, 75, 78, 59, 77, 57, 76, 92, 21, 42, 87, 44],
       [96, 17, 25,  8, 54, 30, 61, 94, 57, 37, 16, 49, 78, 81, 39],
       [ 9, 51, 92, 30, 44, 22, 54, 91, 47, 62, 30,  8, 14, 22, 48],
       [ 4, 28, 48, 52, 10, 55, 41, 79, 90, 58,  9, 39, 44, 51, 42],
       [34,  3, 99, 43, 26, 59, 32, 44, 96, 63, 37, 42, 10, 37, 47],
       [42,  2, 32, 26, 71, 54, 68, 48, 37, 97, 93, 40, 67, 96, 29],
       [86, 77, 17, 57, 71, 45, 90, 89, 52, 60, 17, 41, 89, 91, 83],
       [39, 85, 12, 14, 13, 85, 25,  0, 81, 26, 75, 61, 28, 85, 26],
       [88,  2, 38, 29, 16, 46, 70, 71, 52, 29, 45, 95, 14, 10, 49]])
>>> np.sum(x)
7589
>>> x.sum()
7589
>>> sum(x)
array([567, 314, 515, 369, 455, 570, 557, 628, 603, 549, 451, 491, 420,
       637, 463])
>>> np.count_nonzero(x)
149
>>> np.count_nonzero(x==4))
SyntaxError: unmatched ')'
>>> np.count_nonzero(x==4)
1
>>> np.any(x<6)
True
>>> np.ravel(x)
array([79, 25, 76, 79, 75, 96, 57, 35, 34, 41, 37, 95, 34, 77, 56, 90, 24,
       76, 31, 75, 78, 59, 77, 57, 76, 92, 21, 42, 87, 44, 96, 17, 25,  8,
       54, 30, 61, 94, 57, 37, 16, 49, 78, 81, 39,  9, 51, 92, 30, 44, 22,
       54, 91, 47, 62, 30,  8, 14, 22, 48,  4, 28, 48, 52, 10, 55, 41, 79,
       90, 58,  9, 39, 44, 51, 42, 34,  3, 99, 43, 26, 59, 32, 44, 96, 63,
       37, 42, 10, 37, 47, 42,  2, 32, 26, 71, 54, 68, 48, 37, 97, 93, 40,
       67, 96, 29, 86, 77, 17, 57, 71, 45, 90, 89, 52, 60, 17, 41, 89, 91,
       83, 39, 85, 12, 14, 13, 85, 25,  0, 81, 26, 75, 61, 28, 85, 26, 88,
        2, 38, 29, 16, 46, 70, 71, 52, 29, 45, 95, 14, 10, 49])
>>> np.vsplit(x)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    np.vsplit(x)
  File "<__array_function__ internals>", line 4, in vsplit
TypeError: _hvdsplit_dispatcher() missing 1 required positional argument: 'indices_or_sections'
>>> np.shape(x)
(10, 15)
>>> np.size(x)
150
>>> np.size(x)
150
>>> np.reshape(x,(5,20))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    np.reshape(x,(5,20))
  File "<__array_function__ internals>", line 5, in reshape
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\numpy\core\fromnumeric.py", line 298, in reshape
    return _wrapfunc(a, 'reshape', newshape, order=order)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\numpy\core\fromnumeric.py", line 57, in _wrapfunc
    return bound(*args, **kwds)
ValueError: cannot reshape array of size 150 into shape (5,20)
>>> np.reshape(x,(10,20))
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    np.reshape(x,(10,20))
  File "<__array_function__ internals>", line 5, in reshape
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\numpy\core\fromnumeric.py", line 298, in reshape
    return _wrapfunc(a, 'reshape', newshape, order=order)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\numpy\core\fromnumeric.py", line 57, in _wrapfunc
    return bound(*args, **kwds)
ValueError: cannot reshape array of size 150 into shape (10,20)
>>> np.reshape(x,(15,10))
array([[79, 25, 76, 79, 75, 96, 57, 35, 34, 41],
       [37, 95, 34, 77, 56, 90, 24, 76, 31, 75],
       [78, 59, 77, 57, 76, 92, 21, 42, 87, 44],
       [96, 17, 25,  8, 54, 30, 61, 94, 57, 37],
       [16, 49, 78, 81, 39,  9, 51, 92, 30, 44],
       [22, 54, 91, 47, 62, 30,  8, 14, 22, 48],
       [ 4, 28, 48, 52, 10, 55, 41, 79, 90, 58],
       [ 9, 39, 44, 51, 42, 34,  3, 99, 43, 26],
       [59, 32, 44, 96, 63, 37, 42, 10, 37, 47],
       [42,  2, 32, 26, 71, 54, 68, 48, 37, 97],
       [93, 40, 67, 96, 29, 86, 77, 17, 57, 71],
       [45, 90, 89, 52, 60, 17, 41, 89, 91, 83],
       [39, 85, 12, 14, 13, 85, 25,  0, 81, 26],
       [75, 61, 28, 85, 26, 88,  2, 38, 29, 16],
       [46, 70, 71, 52, 29, 45, 95, 14, 10, 49]])
>>> np.ravel(x)
array([79, 25, 76, 79, 75, 96, 57, 35, 34, 41, 37, 95, 34, 77, 56, 90, 24,
       76, 31, 75, 78, 59, 77, 57, 76, 92, 21, 42, 87, 44, 96, 17, 25,  8,
       54, 30, 61, 94, 57, 37, 16, 49, 78, 81, 39,  9, 51, 92, 30, 44, 22,
       54, 91, 47, 62, 30,  8, 14, 22, 48,  4, 28, 48, 52, 10, 55, 41, 79,
       90, 58,  9, 39, 44, 51, 42, 34,  3, 99, 43, 26, 59, 32, 44, 96, 63,
       37, 42, 10, 37, 47, 42,  2, 32, 26, 71, 54, 68, 48, 37, 97, 93, 40,
       67, 96, 29, 86, 77, 17, 57, 71, 45, 90, 89, 52, 60, 17, 41, 89, 91,
       83, 39, 85, 12, 14, 13, 85, 25,  0, 81, 26, 75, 61, 28, 85, 26, 88,
        2, 38, 29, 16, 46, 70, 71, 52, 29, 45, 95, 14, 10, 49])
>>> np.any(x)
True
>>> np.any(x==100)
False
>>> np.all(x)
False
>>> np.all(x<101)
True
>>> np.all(x>101)
False
>>> 
=============== RESTART: C:/Users/Asus/OneDrive/programs/snake game.py ===============
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/snake game.py", line 3, in <module>
    from freegames import square,vector
ModuleNotFoundError: No module named 'freegames'
>>> 
=============== RESTART: C:/Users/Asus/OneDrive/programs/snake game.py ===============
>>> 
>>> 

=============== RESTART: C:/Users/Asus/OneDrive/programs/snake game.py ===============
>>> 
>>> change(10,10)
>>> 
= RESTART: C:/Users/Asus/OneDrive/programs/snake game.py
>>> move()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    move()
  File "C:/Users/Asus/OneDrive/programs/snake game.py", line 24, in move
    snake.append()
TypeError: list.append() takes exactly one argument (0 given)
>>> 
= RESTART: C:/Users/Asus/OneDrive/programs/snake grame 2.py
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/snake grame 2.py", line 4, in <module>
    wn=turtle.screen()
AttributeError: module 'turtle' has no attribute 'screen'
>>> 
= RESTART: C:/Users/Asus/OneDrive/programs/snake game.py
>>> change(10,10)
>>> inside(head)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    inside(head)
NameError: name 'head' is not defined
>>> move()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    move()
  File "C:/Users/Asus/OneDrive/programs/snake game.py", line 39, in move
    ontime(move,100)
NameError: name 'ontime' is not defined
>>> 
= RESTART: C:/Users/Asus/OneDrive/programs/snake game.py
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/snake game.py", line 51, in <module>
    onti
NameError: name 'onti' is not defined
>>> 
= RESTART: C:/Users/Asus/OneDrive/programs/snake game.py
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/snake game.py", line 52, in <module>
    onti
NameError: name 'onti' is not defined
>>> 
= RESTART: C:/Users/Asus/OneDrive/programs/snake game.py
>>> move()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    move()
  File "C:/Users/Asus/OneDrive/programs/snake game.py", line 47, in move
    onkey(lambda:change(0,10),'UP')
  File "<string>", line 8, in onkey
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1395, in onkey
    self._onkeyrelease(fun, key)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 686, in _onkeyrelease
    self.cv.bind("<KeyRelease-%s>" % key, eventfun)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 417, in bind
    self._canvas.bind(*args, **kwargs)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1392, in bind
    return self._bind(('bind', self._w), sequence, func, add)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1346, in _bind
    self.tk.call(what + (sequence, cmd))
_tkinter.TclError: bad event type or keysym "UP"
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1892, in __call__
    return self.func(*args)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 814, in callit
    func(*args)
  File "C:/Users/Asus/OneDrive/programs/snake game.py", line 47, in move
    onkey(lambda:change(0,10),'UP')
  File "<string>", line 8, in onkey
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1395, in onkey
    self._onkeyrelease(fun, key)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 686, in _onkeyrelease
    self.cv.bind("<KeyRelease-%s>" % key, eventfun)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 417, in bind
    self._canvas.bind(*args, **kwargs)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1392, in bind
    return self._bind(('bind', self._w), sequence, func, add)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1346, in _bind
    self.tk.call(what + (sequence, cmd))
_tkinter.TclError: bad event type or keysym "UP"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1892, in __call__
    return self.func(*args)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 814, in callit
    func(*args)
  File "C:/Users/Asus/OneDrive/programs/snake game.py", line 47, in move
    onkey(lambda:change(0,10),'UP')
  File "<string>", line 8, in onkey
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1395, in onkey
    self._onkeyrelease(fun, key)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 686, in _onkeyrelease
    self.cv.bind("<KeyRelease-%s>" % key, eventfun)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 417, in bind
    self._canvas.bind(*args, **kwargs)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1392, in bind
    return self._bind(('bind', self._w), sequence, func, add)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1346, in _bind
    self.tk.call(what + (sequence, cmd))
_tkinter.TclError: bad event type or keysym "UP"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1892, in __call__
    return self.func(*args)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 814, in callit
    func(*args)
  File "C:/Users/Asus/OneDrive/programs/snake game.py", line 47, in move
    onkey(lambda:change(0,10),'UP')
  File "<string>", line 8, in onkey
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1395, in onkey
    self._onkeyrelease(fun, key)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 686, in _onkeyrelease
    self.cv.bind("<KeyRelease-%s>" % key, eventfun)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 417, in bind
    self._canvas.bind(*args, **kwargs)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1392, in bind
    return self._bind(('bind', self._w), sequence, func, add)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1346, in _bind
    self.tk.call(what + (sequence, cmd))
_tkinter.TclError: bad event type or keysym "UP"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1892, in __call__
    return self.func(*args)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 814, in callit
    func(*args)
  File "C:/Users/Asus/OneDrive/programs/snake game.py", line 47, in move
    onkey(lambda:change(0,10),'UP')
  File "<string>", line 8, in onkey
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1395, in onkey
    self._onkeyrelease(fun, key)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 686, in _onkeyrelease
    self.cv.bind("<KeyRelease-%s>" % key, eventfun)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 417, in bind
    self._canvas.bind(*args, **kwargs)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1392, in bind
    return self._bind(('bind', self._w), sequence, func, add)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1346, in _bind
    self.tk.call(what + (sequence, cmd))
_tkinter.TclError: bad event type or keysym "UP"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1892, in __call__
    return self.func(*args)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 814, in callit
    func(*args)
  File "C:/Users/Asus/OneDrive/programs/snake game.py", line 47, in move
    onkey(lambda:change(0,10),'UP')
  File "<string>", line 8, in onkey
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1395, in onkey
    self._onkeyrelease(fun, key)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 686, in _onkeyrelease
    self.cv.bind("<KeyRelease-%s>" % key, eventfun)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 417, in bind
    self._canvas.bind(*args, **kwargs)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1392, in bind
    return self._bind(('bind', self._w), sequence, func, add)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1346, in _bind
    self.tk.call(what + (sequence, cmd))
_tkinter.TclError: bad event type or keysym "UP"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1892, in __call__
    return self.func(*args)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 814, in callit
    func(*args)
  File "C:/Users/Asus/OneDrive/programs/snake game.py", line 47, in move
    onkey(lambda:change(0,10),'UP')
  File "<string>", line 8, in onkey
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1395, in onkey
    self._onkeyrelease(fun, key)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 686, in _onkeyrelease
    self.cv.bind("<KeyRelease-%s>" % key, eventfun)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 417, in bind
    self._canvas.bind(*args, **kwargs)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1392, in bind
    return self._bind(('bind', self._w), sequence, func, add)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1346, in _bind
    self.tk.call(what + (sequence, cmd))
_tkinter.TclError: bad event type or keysym "UP"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1892, in __call__
    return self.func(*args)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 814, in callit
    func(*args)
  File "C:/Users/Asus/OneDrive/programs/snake game.py", line 47, in move
    onkey(lambda:change(0,10),'UP')
  File "<string>", line 8, in onkey
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1395, in onkey
    self._onkeyrelease(fun, key)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 686, in _onkeyrelease
    self.cv.bind("<KeyRelease-%s>" % key, eventfun)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 417, in bind
    self._canvas.bind(*args, **kwargs)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1392, in bind
    return self._bind(('bind', self._w), sequence, func, add)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1346, in _bind
    self.tk.call(what + (sequence, cmd))
_tkinter.TclError: bad event type or keysym "UP"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1892, in __call__
    return self.func(*args)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 814, in callit
    func(*args)
  File "C:/Users/Asus/OneDrive/programs/snake game.py", line 47, in move
    onkey(lambda:change(0,10),'UP')
  File "<string>", line 8, in onkey
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1395, in onkey
    self._onkeyrelease(fun, key)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 686, in _onkeyrelease
    self.cv.bind("<KeyRelease-%s>" % key, eventfun)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 417, in bind
    self._canvas.bind(*args, **kwargs)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1392, in bind
    return self._bind(('bind', self._w), sequence, func, add)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1346, in _bind
    self.tk.call(what + (sequence, cmd))
_tkinter.TclError: bad event type or keysym "UP"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1892, in __call__
    return self.func(*args)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 814, in callit
    func(*args)
  File "C:/Users/Asus/OneDrive/programs/snake game.py", line 47, in move
    onkey(lambda:change(0,10),'UP')
  File "<string>", line 8, in onkey
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1395, in onkey
    self._onkeyrelease(fun, key)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 686, in _onkeyrelease
    self.cv.bind("<KeyRelease-%s>" % key, eventfun)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 417, in bind
    self._canvas.bind(*args, **kwargs)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1392, in bind
    return self._bind(('bind', self._w), sequence, func, add)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1346, in _bind
    self.tk.call(what + (sequence, cmd))
_tkinter.TclError: bad event type or keysym "UP"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1892, in __call__
    return self.func(*args)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 814, in callit
    func(*args)
  File "C:/Users/Asus/OneDrive/programs/snake game.py", line 47, in move
    onkey(lambda:change(0,10),'UP')
  File "<string>", line 8, in onkey
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1395, in onkey
    self._onkeyrelease(fun, key)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 686, in _onkeyrelease
    self.cv.bind("<KeyRelease-%s>" % key, eventfun)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 417, in bind
    self._canvas.bind(*args, **kwargs)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1392, in bind
    return self._bind(('bind', self._w), sequence, func, add)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1346, in _bind
    self.tk.call(what + (sequence, cmd))
_tkinter.TclError: bad event type or keysym "UP"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1892, in __call__
    return self.func(*args)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 814, in callit
    func(*args)
  File "C:/Users/Asus/OneDrive/programs/snake game.py", line 47, in move
    onkey(lambda:change(0,10),'UP')
  File "<string>", line 8, in onkey
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1395, in onkey
    self._onkeyrelease(fun, key)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 686, in _onkeyrelease
    self.cv.bind("<KeyRelease-%s>" % key, eventfun)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 417, in bind
    self._canvas.bind(*args, **kwargs)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1392, in bind
    return self._bind(('bind', self._w), sequence, func, add)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1346, in _bind
    self.tk.call(what + (sequence, cmd))
_tkinter.TclError: bad event type or keysym "UP"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1892, in __call__
    return self.func(*args)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 814, in callit
    func(*args)
  File "C:/Users/Asus/OneDrive/programs/snake game.py", line 47, in move
    onkey(lambda:change(0,10),'UP')
  File "<string>", line 8, in onkey
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1395, in onkey
    self._onkeyrelease(fun, key)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 686, in _onkeyrelease
    self.cv.bind("<KeyRelease-%s>" % key, eventfun)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 417, in bind
    self._canvas.bind(*args, **kwargs)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1392, in bind
    return self._bind(('bind', self._w), sequence, func, add)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1346, in _bind
    self.tk.call(what + (sequence, cmd))
_tkinter.TclError: bad event type or keysym "UP"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1892, in __call__
    return self.func(*args)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 814, in callit
    func(*args)
  File "C:/Users/Asus/OneDrive/programs/snake game.py", line 47, in move
    onkey(lambda:change(0,10),'UP')
  File "<string>", line 8, in onkey
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1395, in onkey
    self._onkeyrelease(fun, key)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 686, in _onkeyrelease
    self.cv.bind("<KeyRelease-%s>" % key, eventfun)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 417, in bind
    self._canvas.bind(*args, **kwargs)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1392, in bind
    return self._bind(('bind', self._w), sequence, func, add)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1346, in _bind
    self.tk.call(what + (sequence, cmd))
_tkinter.TclError: bad event type or keysym "UP"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1892, in __call__
    return self.func(*args)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 814, in callit
    func(*args)
  File "C:/Users/Asus/OneDrive/programs/snake game.py", line 47, in move
    onkey(lambda:change(0,10),'UP')
  File "<string>", line 8, in onkey
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1395, in onkey
    self._onkeyrelease(fun, key)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 686, in _onkeyrelease
    self.cv.bind("<KeyRelease-%s>" % key, eventfun)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 417, in bind
    self._canvas.bind(*args, **kwargs)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1392, in bind
    return self._bind(('bind', self._w), sequence, func, add)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1346, in _bind
    self.tk.call(what + (sequence, cmd))
_tkinter.TclError: bad event type or keysym "UP"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1892, in __call__
    return self.func(*args)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 814, in callit
    func(*args)
  File "C:/Users/Asus/OneDrive/programs/snake game.py", line 47, in move
    onkey(lambda:change(0,10),'UP')
  File "<string>", line 8, in onkey
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1395, in onkey
    self._onkeyrelease(fun, key)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 686, in _onkeyrelease
    self.cv.bind("<KeyRelease-%s>" % key, eventfun)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 417, in bind
    self._canvas.bind(*args, **kwargs)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1392, in bind
    return self._bind(('bind', self._w), sequence, func, add)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1346, in _bind
    self.tk.call(what + (sequence, cmd))
_tkinter.TclError: bad event type or keysym "UP"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1892, in __call__
    return self.func(*args)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 814, in callit
    func(*args)
  File "C:/Users/Asus/OneDrive/programs/snake game.py", line 47, in move
    onkey(lambda:change(0,10),'UP')
  File "<string>", line 8, in onkey
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1395, in onkey
    self._onkeyrelease(fun, key)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 686, in _onkeyrelease
    self.cv.bind("<KeyRelease-%s>" % key, eventfun)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 417, in bind
    self._canvas.bind(*args, **kwargs)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1392, in bind
    return self._bind(('bind', self._w), sequence, func, add)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1346, in _bind
    self.tk.call(what + (sequence, cmd))
_tkinter.TclError: bad event type or keysym "UP"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1892, in __call__
    return self.func(*args)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 814, in callit
    func(*args)
  File "C:/Users/Asus/OneDrive/programs/snake game.py", line 47, in move
    onkey(lambda:change(0,10),'UP')
  File "<string>", line 8, in onkey
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1395, in onkey
    self._onkeyrelease(fun, key)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 686, in _onkeyrelease
    self.cv.bind("<KeyRelease-%s>" % key, eventfun)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 417, in bind
    self._canvas.bind(*args, **kwargs)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1392, in bind
    return self._bind(('bind', self._w), sequence, func, add)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1346, in _bind
    self.tk.call(what + (sequence, cmd))
_tkinter.TclError: bad event type or keysym "UP"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1892, in __call__
    return self.func(*args)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 814, in callit
    func(*args)
  File "C:/Users/Asus/OneDrive/programs/snake game.py", line 47, in move
    onkey(lambda:change(0,10),'UP')
  File "<string>", line 8, in onkey
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1395, in onkey
    self._onkeyrelease(fun, key)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 686, in _onkeyrelease
    self.cv.bind("<KeyRelease-%s>" % key, eventfun)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 417, in bind
    self._canvas.bind(*args, **kwargs)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1392, in bind
    return self._bind(('bind', self._w), sequence, func, add)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1346, in _bind
    self.tk.call(what + (sequence, cmd))
_tkinter.TclError: bad event type or keysym "UP"
_tkinter.TclError: bad event type or keysym "UP"
SyntaxError: invalid syntax
>>> import turtle
>>> wn=turtle.Screen()
>>> wn.setup(width=600,height=600)
>>> wn.mainloop()

= RESTART: C:/Users/Asus/OneDrive/programs/snake game 3.py

= RESTART: C:/Users/Asus/OneDrive/programs/snake game 3.py
>>> 
= RESTART: C:/Users/Asus/OneDrive/programs/snake game 3.py

= RESTART: C:/Users/Asus/OneDrive/programs/snake game 3.py

= RESTART: C:/Users/Asus/OneDrive/programs/snake game 3.py

= RESTART: C:/Users/Asus/OneDrive/programs/snake game 3.py
>>> 
= RESTART: C:/Users/Asus/OneDrive/programs/snake game 3.py
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/snake game 3.py", line 17, in <module>
    wn.update()
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1304, in update
    t._update_data()
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 2647, in _update_data
    self.screen._incrementudc()
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1293, in _incrementudc
    raise Terminator
turtle.Terminator
>>> 
= RESTART: C:/Users/Asus/OneDrive/programs/snake game 3.py

= RESTART: C:/Users/Asus/OneDrive/programs/snake game 3.py
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/snake game 3.py", line 22, in <module>
    wn.update()
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1304, in update
    t._update_data()
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 2647, in _update_data
    self.screen._incrementudc()
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1293, in _incrementudc
    raise Terminator
turtle.Terminator
>>> 
= RESTART: C:/Users/Asus/OneDrive/programs/snake game 3.py
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/snake game 3.py", line 24, in <module>
    wn.update()
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1304, in update
    t._update_data()
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 2647, in _update_data
    self.screen._incrementudc()
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1293, in _incrementudc
    raise Terminator
turtle.Terminator
>>> 
= RESTART: C:/Users/Asus/OneDrive/programs/snake game 3.py
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/snake game 3.py", line 39, in <module>
    wn.update()
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1304, in update
    t._update_data()
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 2647, in _update_data
    self.screen._incrementudc()
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1293, in _incrementudc
    raise Terminator
turtle.Terminator
>>> 
= RESTART: C:/Users/Asus/OneDrive/programs/snake game 3.py

= RESTART: C:/Users/Asus/OneDrive/programs/snake game 3.py

= RESTART: C:/Users/Asus/OneDrive/programs/snake game 3.py

= RESTART: C:/Users/Asus/OneDrive/programs/snake game 3.py
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/snake game 3.py", line 51, in <module>
    wn.onkeypress(go_rightp,'d')
NameError: name 'go_rightp' is not defined
>>> 
= RESTART: C:/Users/Asus/OneDrive/programs/snake game 3.py
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/snake game 3.py", line 57, in <module>
    move()
  File "C:/Users/Asus/OneDrive/programs/snake game 3.py", line 40, in move
    head.setx(x-20)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1809, in setx
    self._goto(Vec2D(x, self._position[1]))
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 3159, in _goto
    screen._pointlist(self.currentLineItem),
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 754, in _pointlist
    cl = self.cv.coords(item)
  File "<string>", line 1, in coords
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 2766, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"
>>> 
= RESTART: C:/Users/Asus/OneDrive/programs/snake game 3.py
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/snake game 3.py", line 57, in <module>
    move()
  File "C:/Users/Asus/OneDrive/programs/snake game 3.py", line 44, in move
    head.setx(x+20)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1809, in setx
    self._goto(Vec2D(x, self._position[1]))
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 3159, in _goto
    screen._pointlist(self.currentLineItem),
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 754, in _pointlist
    cl = self.cv.coords(item)
  File "<string>", line 1, in coords
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 2766, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"
>>> 
= RESTART: C:/Users/Asus/OneDrive/programs/snake game 3.py
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/snake game 3.py", line 57, in <module>
    move()
  File "C:/Users/Asus/OneDrive/programs/snake game 3.py", line 44, in move
    head.setx(x+20)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1809, in setx
    self._goto(Vec2D(x, self._position[1]))
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 3159, in _goto
    screen._pointlist(self.currentLineItem),
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 754, in _pointlist
    cl = self.cv.coords(item)
  File "<string>", line 1, in coords
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 2766, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"
>>> 
= RESTART: C:/Users/Asus/OneDrive/programs/snake game 3.py
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/snake game 3.py", line 57, in <module>
    move()
  File "C:/Users/Asus/OneDrive/programs/snake game 3.py", line 36, in move
    head.sety(y-20)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1827, in sety
    self._goto(Vec2D(self._position[0], y))
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 3159, in _goto
    screen._pointlist(self.currentLineItem),
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 754, in _pointlist
    cl = self.cv.coords(item)
  File "<string>", line 1, in coords
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 2766, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"
>>> 
= RESTART: C:/Users/Asus/OneDrive/programs/snake game 3.py
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/snake game 3.py", line 66, in <module>
    move()
  File "C:/Users/Asus/OneDrive/programs/snake game 3.py", line 45, in move
    head.sety(y-20)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1827, in sety
    self._goto(Vec2D(self._position[0], y))
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 3159, in _goto
    screen._pointlist(self.currentLineItem),
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 754, in _pointlist
    cl = self.cv.coords(item)
  File "<string>", line 1, in coords
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 2766, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"
>>> 
= RESTART: C:/Users/Asus/OneDrive/programs/snake game 3.py
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/snake game 3.py", line 66, in <module>
    x=random.randint(-290,290)
NameError: name 'random' is not defined
>>> 
= RESTART: C:/Users/Asus/OneDrive/programs/snake game 3.py
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/snake game 3.py", line 70, in <module>
    food.goto(random.randint(x,y))
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1775, in goto
    self._goto(Vec2D(*x))
TypeError: turtle.Vec2D() argument after * must be an iterable, not int
>>> 
= RESTART: C:/Users/Asus/OneDrive/programs/snake game 3.py
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/snake game 3.py", line 72, in <module>
    move()
  File "C:/Users/Asus/OneDrive/programs/snake game 3.py", line 46, in move
    head.sety(y-20)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1827, in sety
    self._goto(Vec2D(self._position[0], y))
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 3159, in _goto
    screen._pointlist(self.currentLineItem),
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 754, in _pointlist
    cl = self.cv.coords(item)
  File "<string>", line 1, in coords
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 2766, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"
>>> 
= RESTART: C:/Users/Asus/OneDrive/programs/snake game 3.py

= RESTART: C:/Users/Asus/OneDrive/programs/snake game 3.py

= RESTART: C:/Users/Asus/OneDrive/programs/snake game 3.py
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/snake game 3.py", line 72, in <module>
    move()
  File "C:/Users/Asus/OneDrive/programs/snake game 3.py", line 46, in move
    head.sety(y-20)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1827, in sety
    self._goto(Vec2D(self._position[0], y))
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 3159, in _goto
    screen._pointlist(self.currentLineItem),
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 754, in _pointlist
    cl = self.cv.coords(item)
  File "<string>", line 1, in coords
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 2766, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"
>>> 
= RESTART: C:/Users/Asus/OneDrive/programs/snake game 3.py
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/snake game 3.py", line 72, in <module>
    move()
  File "C:/Users/Asus/OneDrive/programs/snake game 3.py", line 42, in move
    head.sety(y+20)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1827, in sety
    self._goto(Vec2D(self._position[0], y))
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 3159, in _goto
    screen._pointlist(self.currentLineItem),
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 754, in _pointlist
    cl = self.cv.coords(item)
  File "<string>", line 1, in coords
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 2766, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"
>>> 
= RESTART: C:/Users/Asus/OneDrive/programs/snake game 3.py
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/snake game 3.py", line 68, in <module>
    wn.update()
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1304, in update
    t._update_data()
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 2647, in _update_data
    self.screen._incrementudc()
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1293, in _incrementudc
    raise Terminator
turtle.Terminator
>>> 
= RESTART: C:/Users/Asus/OneDrive/programs/snake game 3.py
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/snake game 3.py", line 68, in <module>
    wn.update()
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1304, in update
    t._update_data()
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 2647, in _update_data
    self.screen._incrementudc()
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1293, in _incrementudc
    raise Terminator
turtle.Terminator
>>> 
= RESTART: C:/Users/Asus/OneDrive/programs/snake game 3.py
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/snake game 3.py", line 68, in <module>
    wn.update()
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1304, in update
    t._update_data()
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 2647, in _update_data
    self.screen._incrementudc()
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1293, in _incrementudc
    raise Terminator
turtle.Terminator
>>> 
= RESTART: C:/Users/Asus/OneDrive/programs/snake game 3.py
Traceback (most recent call last):
  File "C:/Users/Asus/OneDrive/programs/snake game 3.py", line 75, in <module>
    move()
  File "C:/Users/Asus/OneDrive/programs/snake game 3.py", line 49, in move
    head.sety(y-20)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1827, in sety
    self._goto(Vec2D(self._position[0], y))
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 3159, in _goto
    screen._pointlist(self.currentLineItem),
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 754, in _pointlist
    cl = self.cv.coords(item)
  File "<string>", line 1, in coords
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.1520.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 2766, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"
>>> 