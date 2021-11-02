Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> x=[1,2,3]
>>> np.array(x)
array([1, 2, 3])
>>> y=np.arange(0,5)
>>> y
array([0, 1, 2, 3, 4])
>>> y=np.arange((0,5),dtype=float)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    y=np.arange((0,5),dtype=float)
TypeError: arange: scalar arguments expected instead of a tuple.
>>> np.diff(x)
array([1, 1])
>>> x=np.random.randint(12,size=(3,3))
>>> x
array([[ 2,  7,  4],
       [ 6,  6, 10],
       [ 3,  8,  9]])
>>> x+y
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    x+y
ValueError: operands could not be broadcast together with shapes (3,3) (5,) 
>>> from PIL import image
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    from PIL import image
ImportError: cannot import name 'image' from 'PIL' (C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\PIL\__init__.py)
>>> from PIL import image
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    from PIL import image
ImportError: cannot import name 'image' from 'PIL' (C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\PIL\__init__.py)
>>> import image
>>> from PIL
SyntaxError: invalid syntax
>>> from PIL:
	
SyntaxError: invalid syntax
>>> from PIL import image
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    from PIL import image
ImportError: cannot import name 'image' from 'PIL' (C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\PIL\__init__.py)
>>> from PIL import Image
>>> import numpy as np
>>> image=image.open("F:\kid.JPG")
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    image=image.open("F:\kid.JPG")
AttributeError: module 'image' has no attribute 'open'
>>> image=image.open("f:\Users\Asus\anaconda3")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> image=image.open("F:\")
		 
SyntaxError: EOL while scanning string literal
>>> image=image.open("F:\IT'S MY PERSONAL ITEAMS")
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    image=image.open("F:\IT'S MY PERSONAL ITEAMS")
AttributeError: module 'image' has no attribute 'open'
>>> image=image.open("F:\kid.JPG")
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    image=image.open("F:\kid.JPG")
AttributeError: module 'image' has no attribute 'open'
>>> image=image.open("F:\pic image.jpeg")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    image=image.open("F:\pic image.jpeg")
AttributeError: module 'image' has no attribute 'open'
>>> image=Image.open("F:\pic image.jpeg")
>>> image
<PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=992x1271 at 0x28A3DB0F760>
>>> image.format
'JPEG'
>>> image.size
(992, 1271)
>>> image.mode
'RGB'
>>> numimage=np.asarray(image)
>>> numimage
array([[[203, 225, 236],
        [203, 225, 236],
        [203, 225, 236],
        ...,
        [209, 227, 237],
        [209, 227, 237],
        [209, 227, 237]],

       [[203, 225, 236],
        [203, 225, 236],
        [203, 225, 236],
        ...,
        [209, 227, 237],
        [209, 227, 237],
        [209, 227, 237]],

       [[203, 225, 236],
        [203, 225, 236],
        [203, 225, 236],
        ...,
        [209, 227, 237],
        [209, 227, 237],
        [209, 227, 237]],

       ...,

       [[182, 200, 210],
        [182, 200, 210],
        [182, 200, 210],
        ...,
        [201, 219, 229],
        [201, 219, 229],
        [201, 219, 229]],

       [[181, 199, 209],
        [182, 200, 210],
        [182, 200, 210],
        ...,
        [201, 219, 229],
        [201, 219, 229],
        [201, 219, 229]],

       [[181, 199, 209],
        [181, 199, 209],
        [182, 200, 210],
        ...,
        [201, 219, 229],
        [201, 219, 229],
        [201, 219, 229]]], dtype=uint8)
>>> numimage.size
3782496
>>> numimage.shape
(1271, 992, 3)
>>> numimage.ndim
3
>>> numimage.nbytes
3782496
>>> image.show()
>>> image.filter()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    image.filter()
TypeError: filter() missing 1 required positional argument: 'filter'
>>> image.show()
>>> image.crop()
<PIL.Image.Image image mode=RGB size=992x1271 at 0x28A3DA29D30>
>>> PIL.ImageFile
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    PIL.ImageFile
NameError: name 'PIL' is not defined
>>> PIL.Image
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    PIL.Image
NameError: name 'PIL' is not defined
>>> PIL.Image("f:\pic image.jpeg")
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    PIL.Image("f:\pic image.jpeg")
NameError: name 'PIL' is not defined
>>> numimage+2
array([[[205, 227, 238],
        [205, 227, 238],
        [205, 227, 238],
        ...,
        [211, 229, 239],
        [211, 229, 239],
        [211, 229, 239]],

       [[205, 227, 238],
        [205, 227, 238],
        [205, 227, 238],
        ...,
        [211, 229, 239],
        [211, 229, 239],
        [211, 229, 239]],

       [[205, 227, 238],
        [205, 227, 238],
        [205, 227, 238],
        ...,
        [211, 229, 239],
        [211, 229, 239],
        [211, 229, 239]],

       ...,

       [[184, 202, 212],
        [184, 202, 212],
        [184, 202, 212],
        ...,
        [203, 221, 231],
        [203, 221, 231],
        [203, 221, 231]],

       [[183, 201, 211],
        [184, 202, 212],
        [184, 202, 212],
        ...,
        [203, 221, 231],
        [203, 221, 231],
        [203, 221, 231]],

       [[183, 201, 211],
        [183, 201, 211],
        [184, 202, 212],
        ...,
        [203, 221, 231],
        [203, 221, 231],
        [203, 221, 231]]], dtype=uint8)
>>> s=numimage+200
>>> image.show(s)
>>> s=numimage+2000.
>>> s=numimage+2000
>>> image.show(s)
>>> import matplotlib.pyplot as plt
>>> plt.show(s)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    plt.show(s)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\matplotlib\pyplot.py", line 378, in show
    return _backend_mod.show(*args, **kwargs)
TypeError: show() takes 1 positional argument but 2 were given
>>> plt.show()
>>> numimage=2
>>> numimage+2
4
>>> numimage+200
202
>>> s=numimage+200
>>> s
202
>>> numimage+2
4
>>> plt.show()
>>> plt.matshow()
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    plt.matshow()
TypeError: matshow() missing 1 required positional argument: 'A'
>>> plt.matshow(s)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    plt.matshow(s)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\matplotlib\pyplot.py", line 2460, in matshow
    fig = figure(fignum, figsize=figaspect(A))
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\matplotlib\figure.py", line 3218, in figaspect
    nr, nc = arg.shape[:2]
ValueError: not enough values to unpack (expected 2, got 0)
>>> numimage.size
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    numimage.size
AttributeError: 'int' object has no attribute 'size'
>>> image=Image.open("F:\pic image.jpeg")
>>> image.size
(992, 1271)
>>> image.show()
>>> image.mode
'RGB'
>>> num=np.asarray(image)
>>> num
array([[[203, 225, 236],
        [203, 225, 236],
        [203, 225, 236],
        ...,
        [209, 227, 237],
        [209, 227, 237],
        [209, 227, 237]],

       [[203, 225, 236],
        [203, 225, 236],
        [203, 225, 236],
        ...,
        [209, 227, 237],
        [209, 227, 237],
        [209, 227, 237]],

       [[203, 225, 236],
        [203, 225, 236],
        [203, 225, 236],
        ...,
        [209, 227, 237],
        [209, 227, 237],
        [209, 227, 237]],

       ...,

       [[182, 200, 210],
        [182, 200, 210],
        [182, 200, 210],
        ...,
        [201, 219, 229],
        [201, 219, 229],
        [201, 219, 229]],

       [[181, 199, 209],
        [182, 200, 210],
        [182, 200, 210],
        ...,
        [201, 219, 229],
        [201, 219, 229],
        [201, 219, 229]],

       [[181, 199, 209],
        [181, 199, 209],
        [182, 200, 210],
        ...,
        [201, 219, 229],
        [201, 219, 229],
        [201, 219, 229]]], dtype=uint8)
>>> num.size
3782496
>>> num.ndim
3
>>> num.nbytes
3782496
>>> num.shape
(1271, 992, 3)
>>>  import matplotlib.pyplot as plt
 
SyntaxError: unexpected indent
>>> import matplotlib.pyplot as plt
>>> 
========= RESTART: C:/Users/Asus/OneDrive/programs/ex38.py ========
<class 'numpy.ndarray'>
(737280,)
(1024, 720)
[[  0   1   2 ... 205 206 207]
 [208 209 210 ... 157 158 159]
 [160 161 162 ... 109 110 111]
 ...
 [144 145 146 ...  93  94  95]
 [ 96  97  98 ...  45  46  47]
 [ 48  49  50 ... 253 254 255]]
>>> 