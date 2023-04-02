# Program for finding Factorial of number in python.

def fact(val):
    firstval = 1
    secondval = 2
    if val <= 0:
        print('Please enter the value greater than 0!')
    elif val == 1:
        print(firstval)
    else:
        for i in range(1, val):
            result = firstval * secondval
            firstval = result 
            secondval += 1
        print(result)

num = int(input("Enter the value you want to find the factorial of: "))
fact(num)
