def get(variable):
    names = ['yasi', 'nave', 'rema', 'abi', 'dhanu']
    if (variable in names):
        return True
    else:
        return False
    
x=['riya','janu','nave','priya','rema','dhanu','kavi','meenu','sasi']
filtered = filter(get, x)
print('The filtered names are:')

for i in filtered:
    print(i)
