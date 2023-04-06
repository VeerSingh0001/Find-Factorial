# Program for finding Factorial of number in python.
import sys
sys.set_int_max_str_digits(999999999)
def fact(val):
    firstval = 1
    secondval = 2
    if val <= 0:
        print('Please enter the value greater than 0!')
    elif val == 1:
        print(firstval)
    else:
        for i in range(1, val+1):
            firstval = firstval * i
        print(firstval)

num = int(input("Enter the value you want to find the factorial of: "))
fact(num)
