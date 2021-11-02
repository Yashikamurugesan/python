def getdata(str):
    return str.replace("kaviya","kavi")
lis=['meenu','nave','priya','riya','rupa','kaviya']
mapobj=map(getdata,lis)
print(mapobj)
for i in mapobj:
    print(i)

def putdata(var):
    return var.replace("","")    
liss=['meenu','nave',' priya','riya','rupa','kaviya']
obj=map(putdata,liss)
print(obj)
for j in obj:
    print(tuple(j))




