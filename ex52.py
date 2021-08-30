Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import arrow
>>> x=arrow.now()
>>> x
<Arrow [2021-08-27T14:27:18.816802+05:30]>
>>> arrow.utcnow()
<Arrow [2021-08-27T08:57:44.377216+00:00]>
>>> arrow.__version__
'1.1.1'
>>> arrow.get()
<Arrow [2021-08-27T08:58:19.965742+00:00]>
>>>
