Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> d1=pd.DataFrame({"Name":['meenu','siva','divagar','jaanu','ashika','rishi','priya'],"Busno":[104,102,105,109,106,103,105]})
>>> d1
      Name  Busno
0    meenu    104
1     siva    102
2  divagar    105
3    jaanu    109
4   ashika    106
5    rishi    103
6    priya    105
>>> d1=pd.DataFrame({"Name":['riya','keerthi','sivam','prabhu','yashika','nithish','navetha','rekka','dhanu'],"Busno":[1,3,2,5,8,4,9,6,7]})
>>> d1=pd.DataFrame({"Name":['meenu','siva','divagar','jaanu','ashika','rishi','priya'],"Busno":[104,102,105,109,106,103,105]})
>>> d1
      Name  Busno
0    meenu    104
1     siva    102
2  divagar    105
3    jaanu    109
4   ashika    106
5    rishi    103
6    priya    105
>>> d2=pd.DataFrame({"Name":['riya','keerthi','sivam','prabhu','yashika','nithish','navetha','rekka','dhanu'],"Busno":[1,3,2,5,8,4,9,6,7]})
>>> d2
      Name  Busno
0     riya      1
1  keerthi      3
2    sivam      2
3   prabhu      5
4  yashika      8
5  nithish      4
6  navetha      9
7    rekka      6
8    dhanu      7
>>> d3=pd.merge(d1,d2)
>>> d3
Empty DataFrame
Columns: [Name, Busno]
Index: []
>>> product=pd.DataFrame({ 'Product_ID':[101,102,103,104,105,106,107], 'Product_name':['Watch','Bag','Shoes','Smartphone','Books','Oil','Laptop'], 'Category':['Fashion','Fashion','Fashion','Electronics','Study','Grocery','Electronics'],'Price':[299.0,1350.50,2999.0,14999.0,145.0,110.0,79999.0],'Seller_City':['Delhi','Mumbai','Chennai','Kolkata','Delhi','Chennai','Bengalore']})

>>> product
   Product_ID Product_name     Category    Price Seller_City
0         101        Watch      Fashion    299.0       Delhi
1         102          Bag      Fashion   1350.5      Mumbai
2         103        Shoes      Fashion   2999.0     Chennai
3         104   Smartphone  Electronics  14999.0     Kolkata
4         105        Books        Study    145.0       Delhi
5         106          Oil      Grocery    110.0     Chennai
6         107       Laptop  Electronics  79999.0   Bengalore
>>>  customer=pd.DataFrame({'id':[1,2,3,4,5,6,7,8,9],'name':['Olivia','Aditya','Cory','Isabell','Dominic','Tyler','Samuel','Daniel','Jeremy'],'age':[20,25,15,10,30,65,35,18,23],'Product_ID':[101,0,106,0,103,104,0,0,107],'Purchased_Product':['Watch','NA','Oil','NA','Shoes','Smartphone','NA','NA','Laptop'],'City':['Mumbai','Delhi','Bangalore','Chennai','Chennai','Delhi','Kolkata','Delhi','Mumbai']})
 
SyntaxError: unexpected indent
>>> customer=pd.DataFrame({'id':[1,2,3,4,5,6,7,8,9],'name':['Olivia','Aditya','Cory','Isabell','Dominic','Tyler','Samuel','Daniel','Jeremy'],'age':[20,25,15,10,30,65,35,18,23],'Product_ID':[101,0,106,0,103,104,0,0,107],'Purchased_Product':['Watch','NA','Oil','NA','Shoes','Smartphone','NA','NA','Laptop'],'City':['Mumbai','Delhi','Bangalore','Chennai','Chennai','Delhi','Kolkata','Delhi','Mumbai']})
>>> customer
   id     name  age  Product_ID Purchased_Product       City
0   1   Olivia   20         101             Watch     Mumbai
1   2   Aditya   25           0                NA      Delhi
2   3     Cory   15         106               Oil  Bangalore
3   4  Isabell   10           0                NA    Chennai
4   5  Dominic   30         103             Shoes    Chennai
5   6    Tyler   65         104        Smartphone      Delhi
6   7   Samuel   35           0                NA    Kolkata
7   8   Daniel   18           0                NA      Delhi
8   9   Jeremy   23         107            Laptop     Mumbai
>>> df4=pd.merge(product,customer)
>>> df4
   Product_ID Product_name     Category  ...  age Purchased_Product       City
0         101        Watch      Fashion  ...   20             Watch     Mumbai
1         103        Shoes      Fashion  ...   30             Shoes    Chennai
2         104   Smartphone  Electronics  ...   65        Smartphone      Delhi
3         106          Oil      Grocery  ...   15               Oil  Bangalore
4         107       Laptop  Electronics  ...   23            Laptop     Mumbai

[5 rows x 10 columns]
>>> df4=pd.merge(product,customer).to_string()
>>> df4
'   Product_ID Product_name     Category    Price Seller_City  id     name  age Purchased_Product       City\n0         101        Watch      Fashion    299.0       Delhi   1   Olivia   20             Watch     Mumbai\n1         103        Shoes      Fashion   2999.0     Chennai   5  Dominic   30             Shoes    Chennai\n2         104   Smartphone  Electronics  14999.0     Kolkata   6    Tyler   65        Smartphone      Delhi\n3         106          Oil      Grocery    110.0     Chennai   3     Cory   15               Oil  Bangalore\n4         107       Laptop  Electronics  79999.0   Bengalore   9   Jeremy   23            Laptop     Mumbai'
>>> print(df4=pd.merge(product,customer).to_string())
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print(df4=pd.merge(product,customer).to_string())
TypeError: 'df4' is an invalid keyword argument for print()
>>> print(pd.merge(product,customer).to_string())
   Product_ID Product_name     Category    Price Seller_City  id     name  age Purchased_Product       City
0         101        Watch      Fashion    299.0       Delhi   1   Olivia   20             Watch     Mumbai
1         103        Shoes      Fashion   2999.0     Chennai   5  Dominic   30             Shoes    Chennai
2         104   Smartphone  Electronics  14999.0     Kolkata   6    Tyler   65        Smartphone      Delhi
3         106          Oil      Grocery    110.0     Chennai   3     Cory   15               Oil  Bangalore
4         107       Laptop  Electronics  79999.0   Bengalore   9   Jeremy   23            Laptop     Mumbai
>>> pd.merge(product,customer,left_on=['Product_ID','Seller_City'],right_on=['Product_ID','City'])
   Product_ID Product_name Category  ...  age Purchased_Product     City
0         103        Shoes  Fashion  ...   30             Shoes  Chennai

[1 rows x 10 columns]
>>> pd.merge(product,customer,left_on=['Product_ID','Seller_City'],right_on=['Product_ID','City']).to_string()
'   Product_ID Product_name Category   Price Seller_City  id     name  age Purchased_Product     City\n0         103        Shoes  Fashion  2999.0     Chennai   5  Dominic   30             Shoes  Chennai'
>>> pd.merge(product,customer,how='inner'left_on=['Product_ID','Seller_City'],right_on=['Product_ID','City']).to_string()
SyntaxError: invalid syntax
>>> pd.merge(product,customer,how='inner',left_on=['Product_ID','Seller_City'],right_on=['Product_ID','City'])
   Product_ID Product_name Category  ...  age Purchased_Product     City
0         103        Shoes  Fashion  ...   30             Shoes  Chennai

[1 rows x 10 columns]
>>> pd.merge(product,customer,how="outer",left_on="Product_ID",right_on="ProductID",indicator=True)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    pd.merge(product,customer,how="outer",left_on="Product_ID",right_on="ProductID",indicator=True)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\reshape\merge.py", line 107, in merge
    op = _MergeOperation(
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\reshape\merge.py", line 700, in __init__
    ) = self._get_merge_keys()
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\reshape\merge.py", line 1092, in _get_merge_keys
    right_keys.append(right._get_label_or_level_values(rk))
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\generic.py", line 1776, in _get_label_or_level_values
    raise KeyError(key)
KeyError: 'ProductID'
>>> pd.merge(product,customer,how="outer",left_on="Product_ID",right_on="Product_ID",indicator=True)
    Product_ID Product_name  ...       City      _merge
0          101        Watch  ...     Mumbai        both
1          102          Bag  ...        NaN   left_only
2          103        Shoes  ...    Chennai        both
3          104   Smartphone  ...      Delhi        both
4          105        Books  ...        NaN   left_only
5          106          Oil  ...  Bangalore        both
6          107       Laptop  ...     Mumbai        both
7            0          NaN  ...      Delhi  right_only
8            0          NaN  ...    Chennai  right_only
9            0          NaN  ...    Kolkata  right_only
10           0          NaN  ...      Delhi  right_only

[11 rows x 11 columns]
>>> pd.merge(product,customer,how="outer",left_on="Product_ID",right_on="Product_ID",indicator=True).to_string()
'    Product_ID Product_name     Category    Price Seller_City   id     name   age Purchased_Product       City      _merge\n0          101        Watch      Fashion    299.0       Delhi  1.0   Olivia  20.0             Watch     Mumbai        both\n1          102          Bag      Fashion   1350.5      Mumbai  NaN      NaN   NaN               NaN        NaN   left_only\n2          103        Shoes      Fashion   2999.0     Chennai  5.0  Dominic  30.0             Shoes    Chennai        both\n3          104   Smartphone  Electronics  14999.0     Kolkata  6.0    Tyler  65.0        Smartphone      Delhi        both\n4          105        Books        Study    145.0       Delhi  NaN      NaN   NaN               NaN        NaN   left_only\n5          106          Oil      Grocery    110.0     Chennai  3.0     Cory  15.0               Oil  Bangalore        both\n6          107       Laptop  Electronics  79999.0   Bengalore  9.0   Jeremy  23.0            Laptop     Mumbai        both\n7            0          NaN          NaN      NaN         NaN  2.0   Aditya  25.0                NA      Delhi  right_only\n8            0          NaN          NaN      NaN         NaN  4.0  Isabell  10.0                NA    Chennai  right_only\n9            0          NaN          NaN      NaN         NaN  7.0   Samuel  35.0                NA    Kolkata  right_only\n10           0          NaN          NaN      NaN         NaN  8.0   Daniel  18.0                NA      Delhi  right_only'
>>> print(pd.merge(product,customer,how="outer",left_on="Product_ID",right_on="Product_ID",indicator=True).to_string())
    Product_ID Product_name     Category    Price Seller_City   id     name   age Purchased_Product       City      _merge
0          101        Watch      Fashion    299.0       Delhi  1.0   Olivia  20.0             Watch     Mumbai        both
1          102          Bag      Fashion   1350.5      Mumbai  NaN      NaN   NaN               NaN        NaN   left_only
2          103        Shoes      Fashion   2999.0     Chennai  5.0  Dominic  30.0             Shoes    Chennai        both
3          104   Smartphone  Electronics  14999.0     Kolkata  6.0    Tyler  65.0        Smartphone      Delhi        both
4          105        Books        Study    145.0       Delhi  NaN      NaN   NaN               NaN        NaN   left_only
5          106          Oil      Grocery    110.0     Chennai  3.0     Cory  15.0               Oil  Bangalore        both
6          107       Laptop  Electronics  79999.0   Bengalore  9.0   Jeremy  23.0            Laptop     Mumbai        both
7            0          NaN          NaN      NaN         NaN  2.0   Aditya  25.0                NA      Delhi  right_only
8            0          NaN          NaN      NaN         NaN  4.0  Isabell  10.0                NA    Chennai  right_only
9            0          NaN          NaN      NaN         NaN  7.0   Samuel  35.0                NA    Kolkata  right_only
10           0          NaN          NaN      NaN         NaN  8.0   Daniel  18.0                NA      Delhi  right_only
>>> print(pd.merge(product,customer,left_on="Product_ID",right_on="Product_ID",indicator=True).to_string())
   Product_ID Product_name     Category    Price Seller_City  id     name  age Purchased_Product       City _merge
0         101        Watch      Fashion    299.0       Delhi   1   Olivia   20             Watch     Mumbai   both
1         103        Shoes      Fashion   2999.0     Chennai   5  Dominic   30             Shoes    Chennai   both
2         104   Smartphone  Electronics  14999.0     Kolkata   6    Tyler   65        Smartphone      Delhi   both
3         106          Oil      Grocery    110.0     Chennai   3     Cory   15               Oil  Bangalore   both
4         107       Laptop  Electronics  79999.0   Bengalore   9   Jeremy   23            Laptop     Mumbai   both
>>> print(pd.merge(product,customer,how='right',left_on="Product_ID",right_on="Product_ID",indicator=True).to_string())
   Product_ID Product_name     Category    Price Seller_City  id     name  age Purchased_Product       City      _merge
0         101        Watch      Fashion    299.0       Delhi   1   Olivia   20             Watch     Mumbai        both
1           0          NaN          NaN      NaN         NaN   2   Aditya   25                NA      Delhi  right_only
2         106          Oil      Grocery    110.0     Chennai   3     Cory   15               Oil  Bangalore        both
3           0          NaN          NaN      NaN         NaN   4  Isabell   10                NA    Chennai  right_only
4         103        Shoes      Fashion   2999.0     Chennai   5  Dominic   30             Shoes    Chennai        both
5         104   Smartphone  Electronics  14999.0     Kolkata   6    Tyler   65        Smartphone      Delhi        both
6           0          NaN          NaN      NaN         NaN   7   Samuel   35                NA    Kolkata  right_only
7           0          NaN          NaN      NaN         NaN   8   Daniel   18                NA      Delhi  right_only
8         107       Laptop  Electronics  79999.0   Bengalore   9   Jeremy   23            Laptop     Mumbai        both
>>> print(pd.merge(product,customer,how='right',left_on="P7roduct_ID",right_on="Product_ID").to_string())
   Product_ID Product_name     Category    Price Seller_City  id     name  age Purchased_Product       City
0         101        Watch      Fashion    299.0       Delhi   1   Olivia   20             Watch     Mumbai
1           0          NaN          NaN      NaN         NaN   2   Aditya   25                NA      Delhi
2         106          Oil      Grocery    110.0     Chennai   3     Cory   15               Oil  Bangalore
3           0          NaN          NaN      NaN         NaN   4  Isabell   10                NA    Chennai
4         103        Shoes      Fashion   2999.0     Chennai   5  Dominic   30             Shoes    Chennai
5         104   Smartphone  Electronics  14999.0     Kolkata   6    Tyler   65        Smartphone      Delhi
6           0          NaN          NaN      NaN         NaN   7   Samuel   35                NA    Kolkata
7           0          NaN          NaN      NaN         NaN   8   Daniel   18                NA      Delhi
8         107       Laptop  Electronics  79999.0   Bengalore   9   Jeremy   23            Laptop     Mumbai
>>> print(pd.merge(product,customer,how='left',left_on="Product_ID",right_on="Product_ID").to_string())
   Product_ID Product_name     Category    Price Seller_City   id     name   age Purchased_Product       City
0         101        Watch      Fashion    299.0       Delhi  1.0   Olivia  20.0             Watch     Mumbai
1         102          Bag      Fashion   1350.5      Mumbai  NaN      NaN   NaN               NaN        NaN
2         103        Shoes      Fashion   2999.0     Chennai  5.0  Dominic  30.0             Shoes    Chennai
3         104   Smartphone  Electronics  14999.0     Kolkata  6.0    Tyler  65.0        Smartphone      Delhi
4         105        Books        Study    145.0       Delhi  NaN      NaN   NaN               NaN        NaN
5         106          Oil      Grocery    110.0     Chennai  3.0     Cory  15.0               Oil  Bangalore
6         107       Laptop  Electronics  79999.0   Bengalore  9.0   Jeremy  23.0            Laptop     Mumbai
>>> 
