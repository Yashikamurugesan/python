
x=['a','d','y','n','v','n','m']
def filtered(data):
    
    if data=='n':
        return True
    else:
        return False
ans=filter(filtered,x)
print (list(ans))


