def getdata():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))

    if operation == '+':
        print("{} + {} = ".format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print("{} - {} = ".format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print("{} * {} = ".format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print("{} / {} = ".format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print("You have not typed a valid operator, please run the program again:")

    get()

def get():
    calc_get = input('''
Do you want to getdata again?
Please type Y for YES or N for NO.
''')

    if calc_get.upper() == 'Y':
        getdata()
    elif calc_get.upper() == 'N':
        print("See you later.")
    else:
        get()
getdata()
            
            
