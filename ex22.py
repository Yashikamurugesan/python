
def get(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False
    
x=['g','a','i','o', 'j', 'k', 's', 'p', 'r']

filtered = filter(get, x)
  
print('The filtered letters are:')
for i in filtered:
    print(i)
