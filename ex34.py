from functools import reduce
def getdata(a,b):
    return a+b
num=[2,3,4,5,6,7]
s=reduce(getdata,num)
print(s)
