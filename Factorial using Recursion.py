import sys
sys.setrecursionlimit(999999999)


def fact(val):
    if val == 0:
        return 1

    return val * fact(val-1)


num = int(input("Enter the value you want to find the factorial of: "))
print(fact(num))
