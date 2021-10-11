Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> df=pd.concat(map['f://DATA SCIENCE NOTES/one.csv','f://DATA SCIENCE NOTES/to one.csv'])
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    df=pd.concat(map['f://DATA SCIENCE NOTES/one.csv','f://DATA SCIENCE NOTES/to one.csv'])
TypeError: 'type' object is not subscriptable
>>> df=pd.concat(map(pd.read_csv,['f://DATA SCIENCE NOTES/one.csv','f://DATA SCIENCE NOTES/to one.csv']),ignore_index=True)
>>> df
             User Name First Name Last Name Department     JOY
0    chris@contoso.com      meenu         V         IT     NaN
1      ben@contoso.com       yasi         G        CSE     NaN
2    david@contoso.com      sivam         I      CIVIL     NaN
3  cynthia@contoso.com    nithish         Y         IT     NaN
4  melissa@contoso.com       riya         K        ECE     NaN
5    chris@contoso.com      meenu         V         IT  2017.0
6      ben@contoso.com       yasi         G        CSE  2016.0
7    david@contoso.com      sivam         I      CIVIL  2018.0
8  cynthia@contoso.com    nithish         Y         IT  2017.0
9  melissa@contoso.com       riya         K        ECE  2016.0
>>> df=pd.concat(map(pd.read_csv,['f://DATA SCIENCE NOTES/one.csv','f://DATA SCIENCE NOTES/to one.csv']))
>>> df
             User Name First Name Last Name Department     JOY
0    chris@contoso.com      meenu         V         IT     NaN
1      ben@contoso.com       yasi         G        CSE     NaN
2    david@contoso.com      sivam         I      CIVIL     NaN
3  cynthia@contoso.com    nithish         Y         IT     NaN
4  melissa@contoso.com       riya         K        ECE     NaN
0    chris@contoso.com      meenu         V         IT  2017.0
1      ben@contoso.com       yasi         G        CSE  2016.0
2    david@contoso.com      sivam         I      CIVIL  2018.0
3  cynthia@contoso.com    nithish         Y         IT  2017.0
4  melissa@contoso.com       riya         K        ECE  2016.0
>>> df=pd.concat(map(pd.read_csv,['f://DATA SCIENCE NOTES/one.csv','f://DATA SCIENCE NOTES/to one.csv']),ignore_index=True)
>>> df
             User Name First Name Last Name Department     JOY
0    chris@contoso.com      meenu         V         IT     NaN
1      ben@contoso.com       yasi         G        CSE     NaN
2    david@contoso.com      sivam         I      CIVIL     NaN
3  cynthia@contoso.com    nithish         Y         IT     NaN
4  melissa@contoso.com       riya         K        ECE     NaN
5    chris@contoso.com      meenu         V         IT  2017.0
6      ben@contoso.com       yasi         G        CSE  2016.0
7    david@contoso.com      sivam         I      CIVIL  2018.0
8  cynthia@contoso.com    nithish         Y         IT  2017.0
9  melissa@contoso.com       riya         K        ECE  2016.0
>>> df=map(pd.read_csv,['f://DATA SCIENCE NOTES/one.csv','f://DATA SCIENCE NOTES/to one.csv']),ignore_index=True
SyntaxError: cannot assign to function call
>>> df=pd.concat(map(pd.read_csv,['f://DATA SCIENCE NOTES/one.csv','f://DATA SCIENCE NOTES/to one.csv']),ignore_index=True)
>>> df
             User Name First Name Last Name Department     JOY
0    chris@contoso.com      meenu         V         IT     NaN
1      ben@contoso.com       yasi         G        CSE     NaN
2    david@contoso.com      sivam         I      CIVIL     NaN
3  cynthia@contoso.com    nithish         Y         IT     NaN
4  melissa@contoso.com       riya         K        ECE     NaN
5    chris@contoso.com      meenu         V         IT  2017.0
6      ben@contoso.com       yasi         G        CSE  2016.0
7    david@contoso.com      sivam         I      CIVIL  2018.0
8  cynthia@contoso.com    nithish         Y         IT  2017.0
9  melissa@contoso.com       riya         K        ECE  2016.0
>>> import glob
>>> import os
>>> joined_list=os.path.join('f://DATA SCIENCE NOTES/one.csv','f://DATA SCIENCE NOTES/to many.csv')
>>> j=os.path.join('f://DATA SCIENCE NOTES/one.csv','f://DATA SCIENCE NOTES/to many.csv')
>>> j
'f://DATA SCIENCE NOTES/to many.csv'
>>> j_l=glob.glob(j)
>>> j_l
['f://DATA SCIENCE NOTES/to many.csv']
>>> df1=pd.concat(pd.read_csv,j_l),ignore_index=True)
SyntaxError: cannot assign to function call
>>> df1=pd.concat(map(pd.read_csv,j_l),ignore_index=True)
>>> df1
             User Name First Name Last Name  ...   JOY  Busno              Skill
0    chris@contoso.com      meenu         V  ...  2017    101                 CV
1      ben@contoso.com       yasi         G  ...  2016    103        programming
2    david@contoso.com      sivam         I  ...  2018    105           Embedded
3  cynthia@contoso.com    nithish         Y  ...  2017    106  ThermoEngineering
4  melissa@contoso.com       riya         K  ...  2016    101               Data

[5 rows x 7 columns]
>>> print(df1)
             User Name First Name Last Name  ...   JOY  Busno              Skill
0    chris@contoso.com      meenu         V  ...  2017    101                 CV
1      ben@contoso.com       yasi         G  ...  2016    103        programming
2    david@contoso.com      sivam         I  ...  2018    105           Embedded
3  cynthia@contoso.com    nithish         Y  ...  2017    106  ThermoEngineering
4  melissa@contoso.com       riya         K  ...  2016    101               Data

[5 rows x 7 columns]
>>> df1.to_string()
'             User Name First Name Last Name Department   JOY  Busno              Skill\n0    chris@contoso.com      meenu         V         IT  2017    101                 CV\n1      ben@contoso.com       yasi         G        CSE  2016    103        programming\n2    david@contoso.com      sivam         I      CIVIL  2018    105           Embedded\n3  cynthia@contoso.com    nithish         Y         IT  2017    106  ThermoEngineering\n4  melissa@contoso.com       riya         K        ECE  2016    101               Data'
>>> print(df1.to_string())
             User Name First Name Last Name Department   JOY  Busno              Skill
0    chris@contoso.com      meenu         V         IT  2017    101                 CV
1      ben@contoso.com       yasi         G        CSE  2016    103        programming
2    david@contoso.com      sivam         I      CIVIL  2018    105           Embedded
3  cynthia@contoso.com    nithish         Y         IT  2017    106  ThermoEngineering
4  melissa@contoso.com       riya         K        ECE  2016    101               Data
>>> j=os.path.join('f://DATA SCIENCE NOTES/one.csv','f://DATA SCIENCE NOTES/to one.csv')
>>> j_l=glob.glob(j)
>>> df1=pd.concat(map(pd.read_csv,j_l),ignore_index=True)
>>> print(df1.to_string())
             User Name First Name Last Name Department   JOY
0    chris@contoso.com      meenu         V         IT  2017
1      ben@contoso.com       yasi         G        CSE  2016
2    david@contoso.com      sivam         I      CIVIL  2018
3  cynthia@contoso.com    nithish         Y         IT  2017
4  melissa@contoso.com       riya         K        ECE  2016
>>> df=pd.read_csv("f://DATA SCIENCE NOTES/one.csv")
>>> df1=pd.read_csv("f://DATA SCIENCE NOTES/to one.csv")
>>> m=pd.merge(df,df1))
SyntaxError: unmatched ')'
>>> m=pd.merge(df,df1)
>>> m
             User Name First Name Last Name Department   JOY
0    chris@contoso.com      meenu         V         IT  2017
1      ben@contoso.com       yasi         G        CSE  2016
2    david@contoso.com      sivam         I      CIVIL  2018
3  cynthia@contoso.com    nithish         Y         IT  2017
4  melissa@contoso.com       riya         K        ECE  2016
>>> import pandas as pd
>>> import glob
>>> import os
>>> df=pd.concat(map(pd.read_csv,['f://DATA SCIENCE NOTES/one.csv','f://DATA SCIENCE NOTES/to one.csv']),ignore_index=True)
>>> df
             User Name First Name Last Name Department     JOY
0    chris@contoso.com      meenu         V         IT     NaN
1      ben@contoso.com       yasi         G        CSE     NaN
2    david@contoso.com      sivam         I      CIVIL     NaN
3  cynthia@contoso.com    nithish         Y         IT     NaN
4  melissa@contoso.com       riya         K        ECE     NaN
5    chris@contoso.com      meenu         V         IT  2017.0
6      ben@contoso.com       yasi         G        CSE  2016.0
7    david@contoso.com      sivam         I      CIVIL  2018.0
8  cynthia@contoso.com    nithish         Y         IT  2017.0
9  melissa@contoso.com       riya         K        ECE  2016.0
>>> j=os.path.join('f://DATA SCIENCE NOTES/one.csv','f://DATA SCIENCE NOTES/to many.csv')
>>> j_l=glob.glob(pd.read_csv,j)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    j_l=glob.glob(pd.read_csv,j)
TypeError: glob() takes 1 positional argument but 2 were given
>>> j_l=glob.glob(j)
>>> df1=pd.concat(map(pd.read_csv,j_l),ignore_index=True)
>>> df1.to_string
<bound method DataFrame.to_string of              User Name First Name Last Name  ...   JOY  Busno              Skill
0    chris@contoso.com      meenu         V  ...  2017    101                 CV
1      ben@contoso.com       yasi         G  ...  2016    103        programming
2    david@contoso.com      sivam         I  ...  2018    105           Embedded
3  cynthia@contoso.com    nithish         Y  ...  2017    106  ThermoEngineering
4  melissa@contoso.com       riya         K  ...  2016    101               Data

[5 rows x 7 columns]>
>>> print(df1.to_string)
<bound method DataFrame.to_string of              User Name First Name Last Name  ...   JOY  Busno              Skill
0    chris@contoso.com      meenu         V  ...  2017    101                 CV
1      ben@contoso.com       yasi         G  ...  2016    103        programming
2    david@contoso.com      sivam         I  ...  2018    105           Embedded
3  cynthia@contoso.com    nithish         Y  ...  2017    106  ThermoEngineering
4  melissa@contoso.com       riya         K  ...  2016    101               Data

[5 rows x 7 columns]>
>>> print(df1.to_string())
             User Name First Name Last Name Department   JOY  Busno              Skill
0    chris@contoso.com      meenu         V         IT  2017    101                 CV
1      ben@contoso.com       yasi         G        CSE  2016    103        programming
2    david@contoso.com      sivam         I      CIVIL  2018    105           Embedded
3  cynthia@contoso.com    nithish         Y         IT  2017    106  ThermoEngineering
4  melissa@contoso.com       riya         K        ECE  2016    101               Data
>>> 