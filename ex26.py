def getdata(x):
    return x.upper()
string="yeah it's me yasi"
mapobj=map(getdata,string)
for i in mapobj:
    print(i,end=" ")






lis=['meenu','nave','priya','riya','rupa','kaviya']
mapobj=map(getdata,lis)
for i in mapobj:
    print(i)
