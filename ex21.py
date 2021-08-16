
def getupper(str): 
    return str.upper() 
    
def getlower(str): 
    return str.lower() 
    
def greet(func): 
    greeting = func("Hi, I am created by a function \passed as an argument.") 
    print(greeting)  
    
greet(getupper) 
greet(getlower)


